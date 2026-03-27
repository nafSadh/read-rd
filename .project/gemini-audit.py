#!/usr/bin/env python3
"""
Gemini paper auditor — read-rd NPOV & scholastic rigor review.

For each paper file, calls Gemini Flash to audit for:
  - POV injection (first/second person, personal opinions as fact)
  - Logical consistency (contradictions, non-sequiturs)
  - Scholastic rigor (unsupported claims, missing attributions, overstatements)
  - Tone (editorial flourishes, informal register, advocacy language)

Writes gemini-npov-rvw.md next to each paper file.
Does NOT edit files — Claude reads the review and applies fixes.

Usage:
  GEMINI_API_KEY=... python3 .project/gemini-audit.py
  GEMINI_API_KEY=... python3 .project/gemini-audit.py --dry-run
  GEMINI_API_KEY=... python3 .project/gemini-audit.py --file path/to/paper.html
"""

import os
import sys
import argparse
import textwrap
from pathlib import Path
from datetime import datetime

import google.genai as genai

# Load .env from repo root if present
_env_file = Path(__file__).parent.parent / ".env"
if _env_file.exists():
    for _line in _env_file.read_text().splitlines():
        if "=" in _line and not _line.startswith("#"):
            _k, _v = _line.split("=", 1)
            os.environ.setdefault(_k.strip(), _v.strip())

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

MODEL = "gemini-3-flash-preview"

REPO_ROOT = Path(__file__).parent.parent

# Paper files to audit — only top-level paper outputs, not deep-dives
PAPER_GLOBS = [
    "**/survey-paper.html",
    "**/tensions-paper.html",
    "**/scenarios-paper.html",
    "**/synthesis-paper.html",
    "**/position-paper.html",
]

EXCLUDE_DIRS = {".claude", "node_modules", ".git"}

AUDIT_PROMPT = textwrap.dedent("""\
You are an expert academic editor performing a neutral-point-of-view (NPOV) and
scholastic rigor audit on a research paper written as HTML.

The paper was originally produced in a conversational AI session with personal
user context, which may have caused personal opinions, preferences, and
first/second-person address to leak into what should be objective scholarly prose.

Review the paper carefully and produce a structured audit report with these sections:

## Summary
One paragraph overview of the paper's topic and overall quality.

## POV Issues
List every instance of:
- First-person ("I", "we", "our", "my") used as authorial voice rather than
  attributed quotation or standard academic "we"
- Second-person ("you", "your") in expository or analytical prose
- Personal opinions stated as fact without attribution
- Enthusiast/fan framing (disproportionate positive coverage of specific tools,
  people, or viewpoints the author seems to prefer)

For each: quote the offending text, explain the issue, suggest a fix.

## Logical Consistency Issues
List any:
- Internal contradictions (claim A in one section contradicts claim B elsewhere)
- Conclusions that don't follow from the premises presented
- Circular reasoning
- Equivocation (same term used with different meanings)

For each: quote the relevant passages, explain the inconsistency.

## Scholastic Rigor Issues
List any:
- Factual claims presented without citation or attribution
- Statistics, percentages, or figures stated without sourcing
- Superlatives ("most important", "best", "only") that are unverified
- Overstatements that go beyond what the cited evidence supports
- Teleological language (e.g., "evolution designed X to Y")
- Causal claims where only correlation is established

For each: quote the claim, explain the issue, suggest hedging language.

## Tone Issues
List any:
- Editorial flourishes ("fascinating", "remarkable", "stunning", "genius")
- Informal/colloquial language inappropriate for scholarly prose
- Advocacy or cheerleading for a position beyond what the evidence warrants
- Rhetorical questions used persuasively rather than analytically
- Snarky or dismissive characterizations of opposing views

For each: quote the text, explain the issue, suggest neutral replacement.

## Priority Fixes
List the 3-5 most important fixes, ranked by severity.

## Overall Assessment
Letter grade (A/B/C/D) with brief justification.

---
HTML PAPER CONTENT FOLLOWS:
""")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def find_papers(root: Path) -> list[Path]:
    papers = []
    for glob in PAPER_GLOBS:
        for p in root.glob(glob):
            # skip worktrees and excluded dirs
            parts = set(p.parts)
            if any(ex in parts for ex in EXCLUDE_DIRS):
                continue
            papers.append(p)
    return sorted(set(papers))


def review_path(paper: Path) -> Path:
    return paper.parent / "gemini-npov-rvw.md"


def already_reviewed(paper: Path) -> bool:
    rv = review_path(paper)
    if not rv.exists():
        return False
    # check it was written for this exact paper
    content = rv.read_text(encoding="utf-8")
    return f"**File:** `{paper.name}`" in content


def audit_paper(client, paper: Path, dry_run: bool = False) -> str:
    html = paper.read_text(encoding="utf-8", errors="replace")

    # Truncate very large files to stay within token limits
    # Gemini 2.5 Flash has 1M context but we keep prompts reasonable
    MAX_CHARS = 400_000
    truncated = False
    if len(html) > MAX_CHARS:
        html = html[:MAX_CHARS]
        truncated = True

    if dry_run:
        return f"[DRY RUN — would audit {paper.name} ({len(html):,} chars)]"

    prompt = AUDIT_PROMPT + html
    if truncated:
        prompt += "\n\n[NOTE: file was truncated to 400k chars for length]"

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )
    return response.text


def write_review(paper: Path, audit_text: str) -> None:
    out = review_path(paper)
    header = textwrap.dedent(f"""\
        # Gemini NPOV Audit — `{paper.name}`

        **File:** `{paper.name}`
        **Path:** `{paper.relative_to(REPO_ROOT)}`
        **Model:** `{MODEL}`
        **Date:** {datetime.now().strftime("%Y-%m-%d")}

        ---

    """)
    out.write_text(header + audit_text, encoding="utf-8")
    print(f"  >> wrote {out.relative_to(REPO_ROOT)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Gemini NPOV audit for read-rd papers")
    parser.add_argument("--dry-run", action="store_true", help="List files without calling API")
    parser.add_argument("--file", help="Audit a single file")
    parser.add_argument("--force", action="store_true", help="Re-audit already-reviewed files")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key and not args.dry_run:
        print("ERROR: Set GEMINI_API_KEY environment variable", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key or "dry-run")

    if args.file:
        papers = [Path(args.file).resolve()]
    else:
        papers = find_papers(REPO_ROOT)

    print(f"Found {len(papers)} paper(s) to audit\n")

    ok, skipped, failed = 0, 0, 0

    for paper in papers:
        rel = paper.relative_to(REPO_ROOT)
        if not args.force and already_reviewed(paper):
            print(f"SKIP {rel}  (already reviewed)")
            skipped += 1
            continue

        print(f"AUDIT {rel}")
        try:
            audit = audit_paper(client, paper, dry_run=args.dry_run)
            if not args.dry_run:
                write_review(paper, audit)
            ok += 1
        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            failed += 1

    print(f"\nDone: {ok} audited, {skipped} skipped, {failed} failed")


if __name__ == "__main__":
    main()
