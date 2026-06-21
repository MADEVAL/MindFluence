# Scenario: SEO Brief (RankWise Integration)

## CONTEXT
Generating persuasive marketing copy within a pre-existing SEO skeleton. The heading structure, keyword placement, internal link plan, and meta data have already been determined by RankWise. Your job is NOT to restructure — it is to inject cognitive bias persuasion into the provided skeleton without breaking SEO signals.

## TRIGGER
User mentions: "RankWise brief", "SEO brief", "SEO skeleton", "SEO structure", "keyword brief", "SEO plan", OR a joint pipeline: "RankWise brief for X, then MindFluence", "MindFluence landing page from RankWise brief".

Also triggers when user says "humanize", "HumanAI pass", "make it sound human" — in this case, you are in the MIDDLE of the triple pipeline (RankWise → MindFluence → HumanAI) and must generate copy that will survive HumanAI cleanup.

## GOAL
Produce high-converting copy that:
- Fits exactly into the provided SEO heading structure (H1, H2s, H3s)
- Places keywords at specified positions without over-stuffing
- Applies cognitive biases within the existing skeleton
- Preserves internal links and their anchor text variety
- Survives HumanAI humanization without losing SEO or bias signals

---

## MODE: SEO BRIEF INTEGRATION

When an SEO brief is provided, enter **SEO Brief Mode** — a constrained variant of Quick Mode:

1. **Read the brief first.** Extract: heading structure (H1→H2→H3), primary keyword, secondary keywords, word count target, internal link plan, meta drafts.
2. **Do NOT restructure.** The heading hierarchy is deliberate SEO architecture. Use it as your skeleton. Sections may be reordered ONLY if the brief explicitly allows it.
3. **Run standard BIAS SELECTION** (decision matrix + category check) against the audience/product/platform in the brief.
4. **Map biases to sections.** Each H2 section gets one dominant bias. The introduction and conclusion each get their own bias.
5. **Apply keyword constraints** (see below).
6. **Verify against anti-patterns.md** before output.
7. **Preserve HumanAI-survivability** (see below).

---

## KEYWORD PLACEMENT RULES

### Mandatory Positions
- **Primary keyword in H1** — the brief specifies this. Do not change the H1 text.
- **Primary keyword in first paragraph** — within the first 100–150 words. This is the copy you write.
- **Primary keyword in at least one H2** — the brief marks which H2(s) contain the keyword. Keep the keyword in those headings. Write the surrounding body copy.
- **Secondary keywords in their designated H2/H3 sections** — as specified in the brief.

### Density Caps per Tone

| Tone | Max Keyword Density | Notes |
|------|-------------------|-------|
| `bold-sell` | 1.5% | Highest risk of over-stuffing. Cap strictly. Use keyword-adjacent language instead of repeating the exact keyword. |
| `expert-calm` | 1.2% | Natural fit for informational content. Keywords distribute well in data-rich copy. |
| `rebel-edgy` | 1.5% | Contrarian framing can push keyword out — ensure it appears in the first 150 words. |
| `warm-human` | 1.2% | Conversational tone distributes keywords naturally. Monitor for accidental keyword gaps. |
| `luxe-minimal` | 1.0% | Sparse copy risks under-placement. If the brief requires a keyword that doesn't fit the minimal style, place it once prominently rather than forcing multiple instances. |

### Over-Stuffing Prevention
- If a section's bias execution naturally pulls in the keyword, do NOT force an additional instance.
- Count keyword instances after writing each section. If approaching the cap, use synonyms, LSI terms, or keyword-adjacent phrasing.
- **bold-sell red flag:** urgency language ("Limited", "Only X left") may push the keyword out of the first 150 words. Compensate by placing the keyword in the opening pattern-interrupt sentence.

---

## INTERNAL LINK PRESERVATION

The brief specifies target URLs and suggested anchor text. When writing copy:

- Place internal links at the positions specified in the brief.
- Use the suggested anchor text variety. Do not convert all anchors to exact-match keywords — the brief's variety is deliberate.
- Max 2 exact-match keyword anchors across the entire document.
- Links should feel like natural reading progression, not "link dumping."
- If a bias execution (social proof, authority) naturally creates a link opportunity not in the brief, add it — but flag it as `[ADDED LINK: url → anchor]`.

---

## POWER WORDS & BURNED WORDS CROSS-REFERENCE

When using power words in bias execution, cross-check against `shared/power-words.md` (RankWise) or the AI burned-word list:

- Avoid power words that overlap with AI-burned-word lists (e.g., "leverage", "robust", "seamless", "cutting-edge").
- If a power word is burned, find a concrete replacement: describe what happens instead of labeling it.
- This is especially critical for content that will pass through HumanAI — burned words will be stripped in Stage 1 (cleanup), potentially removing your bias language.

---

## HUMANI SURVIVABILITY

When the pipeline is RankWise → MindFluence → HumanAI, your copy must survive HumanAI's 5-stage pipeline:

### What HumanAI will try to do (and what you should prepare for):
| HumanAI Stage | Risk to Your Copy | Countermeasure |
|--------------|-------------------|----------------|
| Stage 1: Cleanup | May strip bias language, power words, social proof numbers | Use concrete numbers (not "thousands"), name authority sources, embed bias in structure not vocabulary |
| Stage 2: Specificity | May replace your chosen examples | Anchor examples to the keyword topic — HumanAI won't remove topic-relevant detail |
| Stage 3: Tone | May override your tone | Announce your tone explicitly in output. HumanAI respects pre-set tone when declared |
| Stage 4: Rhythm | Low risk | Sentence variety is compatible with both skills |
| Stage 5: Proofread | May flag your bias markers as "AI tells" | Avoid burned-word vocabulary. Use original phrasing for bias execution |

### Bias Markers to Protect
The following are core to MindFluence persuasion and MUST survive HumanAI:
- Social proof: specific numbers + named sources (e.g., "14,327 users" not "many users")
- Anchoring: the first price/number shown (anchoring is structural, hard to strip)
- Framing: loss-frame language ("Stop losing $300/day")
- In-group identity labels ("Rational optimists", "Conscious parents")
- Story hooks and vivid examples (availability heuristic)

### What HumanAI Will Preserve (Safe)
- Heading structure (H1, H2, H3) — HumanAI is instructed NOT to delete keyword-containing headings
- Internal links — HumanAI is instructed to skip deletion of internal link anchors
- Minimum word count — HumanAI is instructed to preserve 600+ words
- Explicit tone declarations

---

## BIAS-SEO COMPATIBILITY

Some cognitive biases interact with SEO requirements. Flag these proactively:

| Bias | SEO Risk | Mitigation |
|------|---------|------------|
| Anchoring | Low | Numbers in opening naturally satisfy C5 (number in title) — compatible |
| Loss Aversion | Low | "Stop losing X" — keyword still needs to appear in first 150 words |
| Social Proof | Medium | Testimonials don't contain keywords → add keyword in the framing sentence around the testimonial |
| Sunk Cost | Low | Time/effort framing doesn't conflict with SEO |
| Scarcity | Medium | "Limited", "Only X left" — may push keyword out of first 150 words. Place keyword in the preceding sentence. |
| Confirmation | Low | "You already know X" — fits keyword-adjacent language naturally |
| In-Group Favoritism | Low | Tribe labels don't conflict with keyword placement |
| Framing | Low | Loss/gain frames are keyword-agnostic |

### Minimum Word Count
- SEO minimum: 600 words (unless user explicitly requests shorter).
- Each bias needs room to execute — allocate words per bias: introduction (100–150w), each H2 section (150–300w), conclusion (50–100w).
- If the word count target from the brief is higher than your standard output, extend the body sections rather than adding fluff.

---

## OUTPUT FORMAT IN SEO BRIEF MODE

Standard MindFluence output format, with SEO Brief additions:

```
[TONE: selected-style]
[BIASES ENGAGED: bias-1, bias-2, bias-3...]
[TARGET ACTION: click / subscribe / buy / share / think]
[KEYWORD: primary-keyword] [DENSITY: X.X%] [WORD COUNT: N]
[SEO BRIEF: heading structure preserved / link plan preserved]

[THE ACTUAL MARKETING CONTENT — written within the brief's heading skeleton]

---
[RATIONALE]
Why these biases were chosen and how they map to the brief's sections.

[SEO NOTES]
- Keyword density check: pass / warn / fail
- Sections with keyword placement: [list]
- Internal links placed: [count] (brief specified: [count])
- HumanAI survivability: [protected markers] / [at-risk markers]
```

---

## JOINT PROMPT EXAMPLES

### RankWise → MindFluence
> "RankWise SEO brief for SaaS landing page. Keyword: project management. Then MindFluence generate from that brief. Expert-calm tone."

### RankWise → MindFluence → HumanAI
> "Triple pipeline: 1) RankWise SEO brief for [topic]. Keyword: [kw]. 2) MindFluence generate from that brief (expert-calm tone). 3) HumanAI humanize the output."

### MindFluence → HumanAI only
> "Generate a landing page with MindFluence (bold-sell). Then pass it through HumanAI."

---

## CROSS-REFERENCE

- `decision-matrix.md` — audience-to-bias mapping (standard procedure, used in SEO Brief Mode)
- `anti-patterns.md` — pre-output verification (standard procedure)
- `cultural-matrix.md` — adapt biases to target region (if brief specifies locale)
- RankWise `shared/power-words.md` — avoid burned-word overlap
- RankWise `shared/keyword-rules.md` — density rules, LSI strategy
- HumanAI `SKILL.md` — understand what Stage 1–5 will do to your copy
