#!/usr/bin/env python3
"""Generate audio narrations from .dd.html deep-dive files using Gemini TTS.

Audio files are placed alongside their HTML sources as MP3:
  physics/block-universe.dd.html → physics/block-universe.mp3
"""

import argparse
import os
import re
import sys
import wave
import html
import time
import struct
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# ---------------------------------------------------------------------------
# Text extraction from .dd.html files
# ---------------------------------------------------------------------------

def extract_js_array(html_src: str, var_name: str) -> list[str]:
    """Extract a JS array of template-literal strings from HTML source."""
    pattern = rf'const\s+{var_name}\s*=\s*\[(.*?)\];'
    m = re.search(pattern, html_src, re.DOTALL)
    if not m:
        return []
    block = m.group(1)
    items = re.findall(r'`(.*?)`', block, re.DOTALL)
    return items


def strip_html_tags(text: str) -> str:
    """Remove HTML/SVG tags and decode entities, keeping only prose."""
    text = re.sub(r'<svg[\s\S]*?</svg>', '', text)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = html.unescape(text)
    # Replace unicode symbols with spoken equivalents
    text = text.replace('→', ' to ')
    text = text.replace('←', ' from ')
    text = text.replace('↔', ' between ')
    text = text.replace('≈', ' approximately ')
    text = text.replace('≠', ' not equal to ')
    text = text.replace('≥', ' greater than or equal to ')
    text = text.replace('≤', ' less than or equal to ')
    text = text.replace('×', ' times ')
    text = text.replace('÷', ' divided by ')
    text = text.replace('±', ' plus or minus ')
    text = text.replace('∞', ' infinity ')
    text = text.replace('—', ', ')
    text = text.replace('–', ' to ')
    text = text.replace('"', '"').replace('"', '"')
    text = text.replace(''', "'").replace(''', "'")
    text = text.replace('…', '...')
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_title(html_src: str) -> str:
    """Extract the page <title>."""
    m = re.search(r'<title>(.*?)</title>', html_src)
    if not m:
        return ''
    return m.group(1).replace(' — Deep Dive', '').replace(' — Slides', '').strip()


def extract_section_titles(html_src: str) -> list[str]:
    """Extract section titles from const sections = [...]."""
    pattern = r"const\s+sections\s*=\s*\[(.*?)\];"
    m = re.search(pattern, html_src, re.DOTALL)
    if not m:
        return []
    block = m.group(1)
    titles = []
    for item in re.finditer(r"\{(.*?)\}", block, re.DOTALL):
        inner = item.group(1)
        title_m = re.search(r"title\s*:\s*['\"](.+?)['\"]", inner) or \
                  re.search(r"title\s*:\s*'(.*?)'", inner)
        if title_m:
            titles.append(strip_html_tags(title_m.group(1)))
    return titles


def extract_narration_text(html_path: Path) -> str:
    """Extract readable narration text from a .dd.html file."""
    src = html_path.read_text(encoding='utf-8')
    title = extract_title(src)
    section_titles = extract_section_titles(src)
    summaries = extract_js_array(src, 'summaries')
    details = extract_js_array(src, 'details')

    parts = []
    if title:
        parts.append(f"{title}.")

    # Summaries = main panel content (primary narration)
    for i, summary in enumerate(summaries):
        sec_title = section_titles[i] if i < len(section_titles) else None
        text = strip_html_tags(summary)
        if not text or text.lower().startswith('references and sources'):
            continue
        if sec_title and 'source' not in sec_title.lower():
            parts.append(f"\n{sec_title}.\n")
        parts.append(text)

    # Details = right-panel deep content (supplementary)
    for i, detail in enumerate(details):
        sec_title = section_titles[i] if i < len(section_titles) else None
        if sec_title and 'source' in sec_title.lower():
            continue
        text = strip_html_tags(detail)
        if text and len(text) > 100:
            parts.append(text)

    return '\n\n'.join(parts)


# ---------------------------------------------------------------------------
# Gemini TTS
# ---------------------------------------------------------------------------

def get_gemini_client():
    """Create Gemini client with API key from env or .env file."""
    api_key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    if not api_key:
        env_path = Path(__file__).parent / '.env'
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                if line.startswith('GEMINI_API_KEY='):
                    api_key = line.split('=', 1)[1].strip().strip('"').strip("'")
                    break
    if not api_key:
        print("Error: Set GEMINI_API_KEY in environment or .env file", file=sys.stderr)
        sys.exit(1)
    from google import genai
    return genai.Client(api_key=api_key)


def text_to_speech(client, text: str, voice: str = 'Enceladus',
                   model: str = 'gemini-2.5-flash-preview-tts',
                   style_prompt: str = '') -> bytes:
    """Convert text to PCM audio via Gemini TTS. Returns raw PCM bytes."""
    from google.genai import types

    prompt = f"{style_prompt}\n\n{text}" if style_prompt else text

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=voice,
                    )
                )
            ),
        )
    )
    return response.candidates[0].content.parts[0].inline_data.data


def chunk_text(text: str, max_chars: int = 6000) -> list[str]:
    """Split text into chunks at paragraph boundaries."""
    paragraphs = text.split('\n\n')
    chunks, current, current_len = [], [], 0
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if current_len + len(para) > max_chars and current:
            chunks.append('\n\n'.join(current))
            current, current_len = [para], len(para)
        else:
            current.append(para)
            current_len += len(para)
    if current:
        chunks.append('\n\n'.join(current))
    return chunks


def pcm_to_mp3(pcm_data: bytes, channels=1, rate=24000, sample_width=2,
               bitrate=128) -> bytes:
    """Encode raw PCM data to MP3 using lameenc."""
    import lameenc
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(bitrate)
    encoder.set_in_sample_rate(rate)
    encoder.set_channels(channels)
    encoder.set_quality(2)  # 2 = high quality
    mp3_data = encoder.encode(pcm_data)
    mp3_data += encoder.flush()
    return mp3_data


def write_wav(filename: str, pcm_data: bytes, channels=1, rate=24000, sample_width=2):
    """Write PCM data to a WAV file."""
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm_data)


def write_mp3(filename: str, pcm_data: bytes, channels=1, rate=24000,
              sample_width=2, bitrate=48):
    """Write PCM data as MP3."""
    mp3_data = pcm_to_mp3(pcm_data, channels, rate, sample_width, bitrate)
    Path(filename).write_bytes(mp3_data)


def output_path_for(html_path: Path) -> Path:
    """Get the MP3 output path alongside the HTML file."""
    stem = html_path.stem
    for suffix in ['.dd', '.slides', '.guide']:
        if stem.endswith(suffix):
            stem = stem[:-len(suffix)]
            break
    return html_path.parent / f"{stem}.mp3"


def extract_markdown_text(md_path: Path) -> str:
    """Extract narration text from a markdown paper file."""
    src = md_path.read_text(encoding='utf-8')
    # Remove YAML frontmatter if present
    if src.startswith('---'):
        end = src.find('---', 3)
        if end > 0:
            src = src[end+3:]
    # Strip markdown formatting for speech
    # Remove horizontal rules
    src = re.sub(r'^---+$', '', src, flags=re.MULTILINE)
    # Convert headers to spoken section breaks
    src = re.sub(r'^#{1,6}\s+(.+)$', r'\n\1.\n', src, flags=re.MULTILINE)
    # Remove bold/italic markers
    src = re.sub(r'\*{1,3}(.+?)\*{1,3}', r'\1', src)
    # Remove links, keep text
    src = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', src)
    # Remove inline code
    src = re.sub(r'`([^`]+)`', r'\1', src)
    # Clean up unicode
    src = src.replace('\u2014', ', ').replace('\u2013', ' to ')
    src = src.replace('\u201c', '"').replace('\u201d', '"')
    src = src.replace('\u2018', "'").replace('\u2019', "'")
    src = src.replace('\u2026', '...')
    src = src.replace('\u2192', ' to ')
    # Collapse whitespace
    src = re.sub(r'\n{3,}', '\n\n', src)
    return src.strip()


def find_markdown_source(html_path: Path) -> Path | None:
    """Find a markdown paper file that corresponds to an HTML file."""
    # Check for paper files in the same directory or parent
    parent = html_path.parent
    stem = html_path.stem.replace('.dd', '').replace('.slides', '').replace('.guide', '')

    # Direct match
    candidates = [
        parent / f"{stem}.md",
        parent / f"{stem}-paper.md",
        parent / "survey-paper.md",
        parent / "geometry-of-feeling.md",
    ]
    for c in candidates:
        if c.exists():
            return c

    # For overview files, check for synthesis
    if 'overview' in html_path.name:
        synth = parent / "notes" / "00-synthesis.md"
        if synth.exists():
            return synth

    return None


def generate_audio_for_file(client, html_path: Path, voice: str,
                            style_prompt: str, dry_run: bool = False) -> Path | None:
    """Generate audio for a single file. Prefers markdown source, falls back to HTML."""
    # Try markdown source first
    md_source = find_markdown_source(html_path)
    if md_source:
        text = extract_markdown_text(md_source)
        source_label = f"(from {md_source.name})"
    else:
        text = extract_narration_text(html_path)
        source_label = "(from HTML)"

    if not text or len(text) < 200:
        print(f"  Skip {html_path.name}: too little text ({len(text)} chars)")
        return None

    out_path = output_path_for(html_path)

    # Skip if already generated
    if out_path.exists() and out_path.stat().st_size > 1000:
        print(f"  Already exists: {out_path.name}")
        return out_path

    chunks = chunk_text(text)

    if dry_run:
        print(f"  {html_path.name} {source_label} → {out_path.name}  ({len(text)} chars, {len(chunks)} chunks)")
        return out_path

    print(f"  {html_path.name} {source_label}: {len(text)} chars, {len(chunks)} chunks", flush=True)

    all_pcm = b''
    for i, chunk in enumerate(chunks):
        try:
            pcm = text_to_speech(client, chunk, voice=voice, style_prompt=style_prompt)
            all_pcm += pcm
            print(f"    {html_path.name} chunk {i+1}/{len(chunks)} OK ({len(pcm)//1024}KB)", flush=True)
        except Exception as e:
            print(f"    {html_path.name} chunk {i+1}/{len(chunks)} ERROR: {e}", flush=True)
            time.sleep(2)
            continue

    if not all_pcm:
        print(f"  FAILED: {html_path.name}", flush=True)
        return None

    write_mp3(str(out_path), all_pcm)
    size_kb = out_path.stat().st_size // 1024
    print(f"  DONE: {out_path.name} ({size_kb}KB)", flush=True)
    return out_path


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------

def find_dd_files(root: Path, filter_path: str = None) -> list[Path]:
    """Find all .dd.html / .slides.html / .guide.html files."""
    patterns = ['**/*.dd.html', '**/*.slides.html', '**/*.guide.html']
    files = []
    for pat in patterns:
        files.extend(root.glob(pat))
    skip = ['.project', 'node_modules', 'courses', 'digests', 'hiking']
    files = [f for f in files if not any(s in str(f).replace('\\', '/') for s in skip)]
    if filter_path:
        files = [f for f in files
                 if str(f.relative_to(root)).replace('\\', '/').startswith(filter_path.replace('\\', '/'))]
    files.sort()
    return files


# ---------------------------------------------------------------------------
# Voice sampling mode
# ---------------------------------------------------------------------------

BRITISH_STYLE = "Read in a clear, measured British accent, as if narrating a BBC documentary. Articulate and thoughtful."

# Structured style prompts per topic (Audio Profile + Scene + Director's Notes)
STYLE_MAP = {
    'physics': (
        "Audio Profile: A thoughtful British physicist-narrator, mid-40s, "
        "reminiscent of a BBC Horizon presenter. Warm but intellectually precise.\n"
        "Scene: A quiet university study, late evening. The tone is contemplative.\n"
        "Director's Notes:\n"
        "- Style: Measured, wonder-filled, occasionally reverent when discussing deep concepts\n"
        "- Accent: Educated British (RP), clear enunciation of technical terms\n"
        "- Pacing: Moderate, slowing for key insights, brief pauses between sections"
    ),
    'philosophy': (
        "Audio Profile: An authoritative British lecturer, experienced in philosophy "
        "and social science. Confident, engaging, with dry wit.\n"
        "Scene: A well-attended lecture hall. The audience is attentive.\n"
        "Director's Notes:\n"
        "- Style: Authoritative but accessible, occasionally provocative\n"
        "- Accent: British RP, strong and clear\n"
        "- Pacing: Steady, with deliberate emphasis on key arguments"
    ),
    'self': (
        "Audio Profile: A warm, empathetic British narrator. Gentle but clear, "
        "like a trusted friend explaining something personal.\n"
        "Scene: A comfortable living room, one-on-one conversation.\n"
        "Director's Notes:\n"
        "- Style: Compassionate, reflective, occasionally vulnerable\n"
        "- Accent: Soft British, approachable\n"
        "- Pacing: Unhurried, with space for emotional weight"
    ),
    'neuro': (
        "Audio Profile: A precise British neuroscience communicator, clinical "
        "but accessible. Thinks carefully before speaking.\n"
        "Scene: A research seminar, collegial atmosphere.\n"
        "Director's Notes:\n"
        "- Style: Clear, methodical, grounded in evidence\n"
        "- Accent: British RP, measured articulation of medical terms\n"
        "- Pacing: Even and steady, technical sections slightly slower"
    ),
    'ai': (
        "Audio Profile: A knowledgeable British technology journalist, well-versed "
        "in AI research. Energetic but grounded.\n"
        "Scene: A podcast studio, explaining cutting-edge research to a smart audience.\n"
        "Director's Notes:\n"
        "- Style: Informed, forward-looking, with occasional excitement about breakthroughs\n"
        "- Accent: Modern British, professional\n"
        "- Pacing: Moderate to brisk, slowing for complex architectures"
    ),
    'craft': (
        "Audio Profile: A literate British narrator with deep appreciation for "
        "language, craft, and creative work. Articulate and warm.\n"
        "Scene: A book-lined study, sharing discoveries about art and literature.\n"
        "Director's Notes:\n"
        "- Style: Appreciative, knowledgeable, savouring language\n"
        "- Accent: Educated British, with natural rhythm\n"
        "- Pacing: Moderate, lingering on beautiful passages"
    ),
    'cog-sci': (
        "Audio Profile: A clear-headed British cognitive scientist, precise but "
        "engaging. Explains complex research with natural clarity.\n"
        "Scene: An interdisciplinary seminar bridging psychology and neuroscience.\n"
        "Director's Notes:\n"
        "- Style: Lucid, analytical, connecting theory to real experience\n"
        "- Accent: British RP, crisp\n"
        "- Pacing: Measured, with emphasis on key findings"
    ),
    'anthro': (
        "Audio Profile: An authoritative British anthropologist and historian. "
        "Worldly, respectful of cultural nuance.\n"
        "Scene: A documentary narration, richly illustrated with examples.\n"
        "Director's Notes:\n"
        "- Style: Authoritative, culturally sensitive, narrative-driven\n"
        "- Accent: British RP, documentary style\n"
        "- Pacing: Moderate, storytelling cadence"
    ),
    'courses': (
        "Audio Profile: A patient, clear British university lecturer. "
        "Expert at breaking down mathematical and technical concepts.\n"
        "Scene: A small tutorial room, working through material step by step.\n"
        "Director's Notes:\n"
        "- Style: Pedagogical, encouraging, precise with definitions\n"
        "- Accent: British RP, professorial\n"
        "- Pacing: Measured, slower for equations and derivations"
    ),
    'hiking': (
        "Audio Profile: An enthusiastic British outdoors guide. "
        "Loves nature, knows the trails intimately.\n"
        "Scene: Standing at a trailhead, briefing hikers before setting off.\n"
        "Director's Notes:\n"
        "- Style: Enthusiastic, descriptive, practical\n"
        "- Accent: Warm British, conversational\n"
        "- Pacing: Relaxed, picking up energy for exciting features"
    ),
}


def style_for_file(html_path: Path, root: Path) -> str:
    """Pick a style prompt based on the file's topic directory."""
    rel = str(html_path.relative_to(root)).replace('\\', '/')
    for prefix, style in STYLE_MAP.items():
        if rel.startswith(prefix + '/'):
            return style
    return BRITISH_STYLE  # fallback

VOICE_SAMPLES = {
    'Enceladus': 'Breathy, measured',
    'Charon': 'Informative, authoritative',
    'Algieba': 'Smooth, composed',
    'Schedar': 'Even, steady',
    'Gacrux': 'Mature',
    'Sadaltager': 'Knowledgeable, clear',
    'Iapetus': 'Clear, precise',
}

# Voice assignment by topic directory
VOICE_MAP = {
    'physics':     'Enceladus',   # breathy, measured — suits deep physics
    'philosophy':  'Charon',      # authoritative — suits psychology/philosophy
    'self':        'Algieba',     # smooth, composed — suits personal topics
    'neuro':       'Schedar',     # even, steady — suits neuroscience
    'ai':          'Gacrux',      # mature — suits AI/tech
    'craft':       'Sadaltager',  # knowledgeable — suits literature/craft
    'cog-sci':     'Iapetus',     # clear, precise — suits cognitive science
    'anthro':      'Charon',      # authoritative — suits anthropology
    'courses':     'Schedar',     # even, steady — suits coursework
    'hiking':      'Algieba',     # smooth — suits trail guides
}


def voice_for_file(html_path: Path, root: Path) -> str:
    """Pick a voice based on the file's topic directory."""
    rel = str(html_path.relative_to(root)).replace('\\', '/')
    for prefix, voice in VOICE_MAP.items():
        if rel.startswith(prefix + '/'):
            return voice
    return 'Enceladus'  # fallback

VOICE_SAMPLE_PAIRS = [
    ('Enceladus',  'physics/block-universe.dd.html'),
    ('Charon',     'philosophy/dark-psychology.dd.html'),
    ('Algieba',    'self/audhd.dd.html'),
    ('Schedar',    'neuro/brain-energy/s1-metabolic-theory.dd.html'),
    ('Gacrux',     'ai/trending-ai.dd.html'),
    ('Sadaltager', 'craft/project-hail-mary.dd.html'),
    ('Iapetus',    'cog-sci/attachment-theory/overview.dd.html'),
]


def generate_voice_samples(client, root: Path):
    """Generate one sample per voice, each from a different .dd.html file."""
    sample_dir = root / '_voice-samples'
    sample_dir.mkdir(parents=True, exist_ok=True)

    for voice, sf in VOICE_SAMPLE_PAIRS:
        html_path = root / sf
        if not html_path.exists():
            print(f"  Not found: {sf}")
            continue

        text = extract_narration_text(html_path)
        if not text:
            continue

        # ~1500 char sample, cut at sentence boundary
        sample_text = text[:1500]
        cut = sample_text.rfind('.')
        if cut > 500:
            sample_text = sample_text[:cut+1]

        stem = html_path.stem.replace('.dd', '').replace('.slides', '')
        out_path = sample_dir / f"{stem}_{voice.lower()}.wav"
        if out_path.exists():
            print(f"  Already exists: {out_path.name}")
            continue

        desc = VOICE_SAMPLES.get(voice, '')
        print(f"  {voice} ({desc}) × {stem}...", end='', flush=True)
        try:
            pcm = text_to_speech(client, sample_text, voice=voice,
                                 style_prompt=BRITISH_STYLE)
            write_wav(str(out_path), pcm)
            print(f" OK → {out_path.name}")
        except Exception as e:
            print(f" ERROR: {e}")
        time.sleep(1)

    print(f"\nDone! Samples in {sample_dir}/")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Generate audio from .dd.html files')
    parser.add_argument('path', nargs='?', default=None,
                        help='Filter by path prefix (e.g., physics/ or physics/block-universe.dd.html)')
    parser.add_argument('--voice', default='auto',
                        help='Voice name, or "auto" to pick per topic (default: auto)')
    parser.add_argument('--style', default=BRITISH_STYLE, help='Style prompt for narration')
    parser.add_argument('--dry-run', action='store_true', help='Preview without generating')
    parser.add_argument('--samples', action='store_true', help='Generate voice comparison samples')
    parser.add_argument('--list-voices', action='store_true', help='List available voices')
    parser.add_argument('--overviews-only', action='store_true',
                        help='Only process overview.dd.html and standalone (non-section) files')
    parser.add_argument('--workers', type=int, default=4,
                        help='Number of parallel workers (default: 4)')

    args = parser.parse_args()

    if args.list_voices:
        print("Recommended voices for narration:")
        for v, d in VOICE_SAMPLES.items():
            print(f"  {v:20s} — {d}")
        print("\nAll 30: Zephyr, Puck, Charon, Kore, Fenrir, Leda, Orus, Aoede,")
        print("  Callirrhoe, Autonoe, Enceladus, Iapetus, Umbriel, Algieba, Despina,")
        print("  Erinome, Algenib, Rasalgethi, Laomedeia, Achernar, Alnilam, Schedar,")
        print("  Gacrux, Pulcherrima, Achird, Zubenelgenubi, Vindemiatrix, Sadachbia,")
        print("  Sadaltager, Sulafat")
        return

    root = Path(__file__).parent

    if args.samples:
        client = get_gemini_client()
        print("Generating voice samples (3 files × 7 voices)...")
        generate_voice_samples(client, root)
        return

    files = find_dd_files(root, args.path)
    if not files:
        print(f"No .dd.html files found" + (f" matching '{args.path}'" if args.path else ""))
        return

    if args.overviews_only:
        def is_overview_or_standalone(f: Path) -> bool:
            name = f.name
            rel = str(f.relative_to(root)).replace('\\', '/')
            # overview files in paper-drive projects
            if 'overview' in name or name.startswith('genai-2026-overview'):
                return True
            # standalone files (not in a project subdir with sections)
            # standalone = file is directly in a topic dir, not in a sub-project
            parts = rel.split('/')
            if len(parts) == 2:  # e.g. "physics/block-universe.dd.html"
                return True
            # Named project overviews like flag-history.dd.html
            if not name.startswith('s') or not name[1:2].isdigit():
                # Not a section file (s1-, s2-, etc.)
                if 'overview' not in name and len(parts) == 3:
                    # Could be a named overview like flag-history/flag-history.dd.html
                    parent_name = parts[-2]
                    stem = f.stem.replace('.dd', '').replace('.slides', '').replace('.guide', '')
                    if stem == parent_name or stem.startswith('0'):
                        return True
            return False

        files = [f for f in files if is_overview_or_standalone(f)]

    print(f"Found {len(files)} files")

    auto_voice = args.voice == 'auto'
    auto_style = args.style == BRITISH_STYLE  # use per-topic styles when default

    if args.dry_run:
        total_chars = 0
        total_chunks = 0
        for f in files:
            text = extract_narration_text(f)
            if len(text) < 200:
                continue
            chunks = chunk_text(text)
            total_chars += len(text)
            total_chunks += len(chunks)
            rel = str(f.relative_to(root)).replace('\\', '/')
            v = voice_for_file(f, root) if auto_voice else args.voice
            print(f"  {rel}: {len(text)} chars, {len(chunks)} chunks, voice={v} → {output_path_for(f).name}")
        print(f"\nTotal: {total_chars:,} chars, {total_chunks} API calls")
        return

    client = get_gemini_client()
    print_lock = threading.Lock()
    generated = []
    failed = []

    def process_file(idx_f):
        idx, f = idx_f
        rel = str(f.relative_to(root)).replace('\\', '/')
        v = voice_for_file(f, root) if auto_voice else args.voice
        s = style_for_file(f, root) if auto_style else args.style
        with print_lock:
            print(f"\n[{idx+1}/{len(files)}] {rel} (voice={v})")
        out = generate_audio_for_file(client, f, v, s)
        return (rel, out)

    workers = min(args.workers, len(files))
    print(f"Using {workers} parallel workers")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(process_file, (i, f)): f
                   for i, f in enumerate(files)}
        for future in as_completed(futures):
            rel, out = future.result()
            if out:
                generated.append(out)
            else:
                failed.append(rel)

    print(f"\n{'='*60}")
    print(f"Generated {len(generated)}/{len(files)} audio files")
    if failed:
        print(f"Failed: {', '.join(failed)}")


if __name__ == '__main__':
    main()
