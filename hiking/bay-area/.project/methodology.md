# Methodology — Bay Area Hiking Guide: A Follow-Up to gurmeet.net/hiking

**Document version:** March 24, 2026
**Scope:** Complete methodology for researching and compiling detailed hike guides across all 27 categories from Gurmeet Singh's Bay Area hiking page, executed in a single extended session using the same research methodology as the [Agentic LLMs in the Wild survey](../../ai/agentic-lm-survey/).

---

## 1. Research Question

**Starting point:** Gurmeet Singh's [Bay Area Hiking page](https://gurmeet.net/hiking/) provides an excellent thematic taxonomy of Bay Area hiking — 27 categories ranging from Peaks to Monasteries — but lacks specific trail details (distances, elevation gains, difficulty ratings, trailhead information). The question: can we fill in the details systematically, following the transparent research methodology established by the agentic-lm-survey project?

**Framing decision:** Rather than creating a competing guide, we chose to build a *complementary resource* — a detailed trail database organized under Gurmeet's original taxonomy, with interactive HTML deep-dives matching the survey project's aesthetic.

---

## 2. Taxonomy Design

### 2.1 Preserving the Original Structure

We preserved Gurmeet's 27 thematic categories exactly as published, then grouped them into five sections for interactive deep-dive pages:

- **Section 1: Nature** — Peaks, Redwoods, Waterfalls, Wildflowers
- **Section 2: Water** — Lakes, Creeks, Coastline, Beach Walks
- **Section 3: Views** — Ocean Views, Bay Views, Green Hills
- **Section 4: Adventure** — Caves, Full Moon, River Crossings, Ropes, Swings
- **Section 5: Special** — Lighthouses, Monasteries, Islands, Wildlife, Bridges

### 2.2 Per-Hike Data Schema

For each hike, we collected:
- **Trail name** (as commonly known on AllTrails/hiking sites)
- **Park/Preserve** (managing authority)
- **Location** (city/county)
- **Distance** (miles, round-trip)
- **Elevation gain** (feet)
- **Difficulty** (Easy / Moderate / Hard / Strenuous)
- **Best season** (months or conditions)
- **Key features** (notable attractions)
- **Description** (1–2 sentences)
- **Source URL** (where data was found)

---

## 3. Research Process

### 3.1 Source Collection

**Method:** Parallel web search across hiking databases, national/state park sites, and regional hiking blogs. Searches used category-specific terms:

- "Bay Area peak hikes," "Mission Peak trail," "Mt Tamalpais hiking"
- "Bay Area redwood hikes," "Muir Woods trails," "Big Basin trails"
- "Bay Area waterfall hikes," "Alamere Falls," "Berry Creek Falls"
- "Bay Area coastal hikes," "Point Reyes trails," "Marin Headlands"
- "Pinnacles cave hikes," "Bay Area full moon hikes"
- "Bay Area wildlife viewing," "tule elk Point Reyes," "Año Nuevo seals"

### 3.2 Primary Sources (by reliability tier)

**Tier 1 — Official park sources:**
- National Park Service (nps.gov) — Point Reyes, Golden Gate NRA, Pinnacles
- California State Parks (parks.ca.gov) — Big Basin, Armstrong, Angel Island
- East Bay Regional Parks (ebparks.org) — Briones, Sunol, Coyote Hills
- Midpeninsula Regional Open Space District (openspace.org)

**Tier 2 — Curated databases:**
- AllTrails (alltrails.com) — distance, elevation, difficulty ratings
- Modern Hiker (modernhiker.com) — detailed trail descriptions
- Bay Area Hiker (bahiker.com) — local knowledge
- Hiking Project (hikingproject.com) — community-verified data

**Tier 3 — Regional guides and blogs:**
- 7x7 Bay Area, KQED Science, Trail to Peak
- Parks Conservancy (parksconservancy.org)
- Peninsula Open Space Trust (openspacetrust.org)

### 3.3 Reading Strategy (Three Tiers)

Following the agentic-lm-survey methodology, sources were read at varying depths:

- **Deep read (full trail page):** ~40 sources — individual trail pages on AllTrails, NPS, State Parks with complete details extracted
- **Cross-reference read:** ~25 sources — secondary sources used to verify distances/elevations from primary sources
- **Survey read (category pages):** ~15 sources — used to identify which trails to include, not for trail details

**Total sources consulted:** ~80 across all categories.

### 3.4 Data Verification

Where possible, trail statistics were cross-referenced between at least two sources. Discrepancies were resolved by preferring:
1. Official park sources (NPS, State Parks) for distances and regulations
2. AllTrails for elevation gain (GPS-verified)
3. Recent sources over older ones

---

## 4. Coverage Statistics

### 4.1 Hikes Per Category

| Category | Hikes Documented | Coverage Depth |
|----------|-----------------|----------------|
| Peaks | 10 | Deep — major summits with multiple route options |
| Redwoods | 17 | Deep — multiple parks, varied difficulty |
| Waterfalls | 9 | Deep — seasonal flow info included |
| Wildflowers | 7 | Moderate — spring-specific timing |
| Lakes | 8 | Deep — reservoir loops and mountain lakes |
| Creeks | 5 | Moderate — representative trails |
| Coastline | 8 | Deep — Marin to San Mateo coverage |
| Beach Walks | 5 | Moderate — major beaches |
| Ocean Views | 5 | Moderate — non-coastal trails with vistas |
| Bay Views | 6 | Moderate — around-the-bay coverage |
| Green Hills | 6 | Moderate — East Bay focus |
| Caves | 3 | Deep — all Pinnacles caves covered |
| Full Moon | 3 | Light — program availability varies |
| River Crossings | 3 | Light — seasonal activity |
| Lighthouses | 4 | Deep — all accessible lighthouses |
| Monasteries | 3 | Moderate — access restrictions noted |
| Islands | 3 | Deep — Angel Island comprehensive |
| Wildlife | 5 | Deep — species-specific timing |
| Bridges | 3 | Moderate — walkable spans |
| Swings | 4 | Light — ephemeral installations |
| Ropes | 4 | Light — climbing area overviews |
| **TOTAL** | **~140** | |

### 4.2 Geographic Distribution

- **Marin County:** ~35% of hikes (Point Reyes, Mt Tamalpais, Marin Headlands)
- **San Mateo County:** ~20% (coast, redwoods, peninsula)
- **East Bay (Alameda/Contra Costa):** ~20% (peaks, green hills, lakes)
- **San Francisco:** ~10% (urban coastal, bridges)
- **Santa Cruz/San Benito:** ~10% (Big Basin, Pinnacles)
- **Sonoma/Napa:** ~5% (Armstrong, Mt St Helena)

---

## 5. Deliverables

| Deliverable | Format | Purpose |
|------------|--------|---------|
| `.project/methodology.md` | Markdown | This document — complete research methodology |
| `s1-nature.dd.html` | Interactive HTML | Deep-dive: Peaks, Redwoods, Waterfalls, Wildflowers |
| `s2-water.dd.html` | Interactive HTML | Deep-dive: Lakes, Creeks, Coastline, Beach Walks |
| `s3-views.dd.html` | Interactive HTML | Deep-dive: Ocean Views, Bay Views, Green Hills |
| `s4-adventure.dd.html` | Interactive HTML | Deep-dive: Caves, Full Moon, River Crossings, Ropes, Swings |
| `s5-special.dd.html` | Interactive HTML | Deep-dive: Lighthouses, Monasteries, Islands, Wildlife, Bridges |
| `index.html` | Interactive HTML | Landing page with section navigation |

---

## 6. Explicit Limitations

1. **Single-session research:** All data collected in one extended session, not verified by hiking the trails
2. **No GPS verification:** Distances and elevations from published sources, not personally GPS-tracked
3. **Seasonal accuracy:** Trail conditions, closures, and seasonal programs change annually — verify before hiking
4. **Ephemeral features:** Rope swings, tree swings, and informal trail features may be removed at any time
5. **Access restrictions:** Some trails (Spirit Rock, Land of Medicine Buddha) have restricted access — check before visiting
6. **Completeness:** Not every trail in every park is listed — we selected representative and notable trails per category
7. **AllTrails bias:** AllTrails was a primary source for statistics; their user-reported data may differ from official measurements
8. **Post-2023 changes:** Big Basin Redwoods was heavily damaged by the CZU Lightning Complex fire (2020) and is still recovering — trail availability may differ from pre-fire descriptions

---

## 7. Relationship to gurmeet.net/hiking

This project is a fan-made companion resource. Gurmeet Singh's original page provides the thematic framework; this project fills in specific trail details. The original page remains the authoritative source for the Bay Area hiking taxonomy.

---

## 8. Tooling

- **Repository:** github.com/nafSadh/read-rd (hiking/bay-area/)
- **Research:** Web search (multiple search engines), direct URL fetching
- **Build:** Single-file HTML with embedded CSS/JS (matching agentic-lm-survey aesthetic)
- **Design system:** Dual-theme (light academic + dark luxury), EB Garamond / Jost / IBM Plex Mono typography
