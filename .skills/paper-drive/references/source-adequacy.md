# Source Adequacy Checklist

Use this checklist before building any section deep-dive.

---

## The Assessment (present to user before proceeding)

```
## S{N}: {Section Name} — Source Assessment

**Current sources:** {N}
**Minimum needed:** {5-6 for standalone deep-dive}

### What's covered well:
- {Sub-topic A}: {Sources X, Y}
- {Sub-topic B}: {Sources Z}

### What's missing:
- {Specific gap 1}: no primary data on {X}
- {Specific gap 2}: missing canonical reference ({name it})
- {Specific gap 3}: only one side of {tension/debate}

### Canonical references check:
- [ ] {Domain-standard reference 1} — check SKILL.md Source Adequacy Minimums table for domain
- [ ] {Domain-standard reference 2}
- [ ] {Domain-standard reference 3}
- [ ] (Refer to the domain table in SKILL.md for specific must-have references)

### Verdict: {✅ Adequate | ❌ Not enough — need N more}
```

---

## Decision Rules

| Situation | Action |
|-----------|--------|
| 6+ sources, good coverage, both sides of debates | ✅ Proceed to build |
| 5 sources, minor gaps | ✅ Proceed but note limitations |
| 3-4 sources, significant gaps | ❌ Search for 2-3 more, re-assess |
| <3 sources | ❌ Major search needed before anything |
| One side of a tension missing | ❌ Find the counter-argument |
| No quantitative data | ⚠️ Proceed if discourse survey; ❌ if technical |
| All sources from same type (e.g., all industry) | ⚠️ Seek academic or government sources |

---

## After Assessment

1. **If adequate:** Update TODO table → proceed to reading → markdown → HTML
2. **If not adequate:** 
   - List specific search queries to fill gaps
   - Execute searches
   - Add new sources to literature-collection.md
   - Re-assess
   - Only after adequate: proceed

**Never skip this step. Never rationalize inadequacy as "good enough."**
