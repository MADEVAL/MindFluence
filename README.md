# MindFluence

[![Version](https://img.shields.io/badge/version-2.5.0-blue)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Compatibility](https://img.shields.io/badge/compatibility-plain%20markdown-purple)](#requirements)
[![CI](https://github.com/MADEVAL/MindFluence/actions/workflows/ci.yml/badge.svg)](https://github.com/MADEVAL/MindFluence/actions/workflows/ci.yml)
[![skills.sh](https://img.shields.io/badge/skills.sh-listed-2ea44f)](https://www.skills.sh/madeval/mindfluence)

\[ **English** | [Русский](README.ru.md) \]

> **Persuasion engineered through psychology, not manipulation.**

An AI prompt-skill that turns 20 cognitive biases into high-converting marketing copy - for any language, any platform, any audience. **Skill class:** orchestrator - self-contained `SKILL.md` plus on-demand references. **v2.3: self-contained core with narrative depth and provenance.** All tables, 13 anti-patterns with detection rules, cultural data, and few-shot examples are inlined into SKILL.md. A mandatory PROVENANCE / TRUTH GATE prevents invented numbers, names, and sources. Narrative depth supports two compliant modes: real-data Named Person Story Arc (NPSA) or a labeled `[illustrative]` fallback. No external file reads required for core operation.

---

## What is this?

**MindFluence** is a system prompt (skill) for LLMs - GPT, Claude, Gemini, DeepSeek or any capable model. It transforms the AI into a marketing strategist who understands *why* humans click, read, and buy - not just *what* to write.

It's built on decades of research in behavioral economics and evolutionary psychology: Kahneman's two systems, Cialdini's principles, Munger's psychological misjudgments, Festinger's cognitive dissonance - distilled into actionable copywriting instructions.

## How it works

1. **Load `SKILL.md`** as a system prompt into any LLM. That's it - the file is self-contained for core operation.
2. **Give a task:** "Write a LinkedIn post about..." / "Create a landing page for..." / "Audit this ad for cognitive biases."
3. **Get output** with every bias labeled, every decision explained, every word psychologically justified.

**The LLM uses a single-table Bias Selection Router** (audience × product × platform → instant bias stack) instead of a 10-step procedure. After generating, it runs a **mechanical Post-Generation Verification** - 7 checks (numbers, names, fear exit, scarcity explanation, system-blame, human narrative, provenance) - and a mandatory **narrative depth** requirement: real-data NPSA or a labeled `[illustrative]` fallback.

**Four modes:**
- **Quick Mode** (default) - data provenance audit → router lookup → scenario override → category check → compose → 7-point verify. Fast for user, fast for LLM.
- **Deep Mode** - the AI asks 5 clarifying questions at once, then routes through the same lookup.
- **Audit Mode** - analyzes existing copy for biases and anti-patterns using mechanical detection rules (13 anti-patterns including Statistical-Only Fallacy).
- **Optimize Mode** - iterates on underperforming copy using funnel-to-bias mapping. Generates A/B variants with statistical confidence thresholds. Also handles qualitative rewrites without metrics: tone shifts, bias injection/removal, anti-pattern fixes, audience/platform adaptation (7 rewrite intents).

## The 20 Cognitive Biases

| # | Bias | Category | Marketing Use |
|---|------|----------|---------------|
| 1  | **Social Proof / Bandwagon**     | Social              | Used by teams at Google, Airbnb, and 10,000+ startups |
| 2  | **Anchoring**                     | Optimizer           | Enterprise: $499/mo → Pro: $99/mo |
| 3  | **Framing**                       | Filter              | "90% success rate" vs "Only 10% fail" |
| 4  | **Appeal to Authority**           | Social              | The same method taught at Harvard Business School |
| 5  | **Fear / Loss Aversion**          | Filter + Social     | Every day without X costs you $200 in missed revenue |
| 6  | **Availability Heuristic**        | Optimizer           | "Sarah tripled her revenue in 3 months. Here's the exact playbook." |
| 7  | **Confirmation Bias**             | Filter              | "You already know newsletters are broken. Here's the data that proves your instinct right." |
| 8  | **Cognitive Dissonance**          | Filter + Optimizer  | "You care about health but skip breakfast. Our 2-minute shake fixes the gap." |
| 9  | **Survivorship Bias**             | Optimizer           | "The 23% who succeeded all followed this pattern. The 77% did not." |
| 10 | **Endowment Effect**              | Optimizer           | Your workspace is already set up. Cancelling means losing everything you built. |
| 11 | **Fundamental Attribution Error** | Social              | "It's not that you're bad at networking. Conferences are designed to exclude introverts." |
| 12 | **Sunk Cost Fallacy**             | Optimizer           | You've put 6 months into learning this skill. The next module is where it clicks. |
| 13 | **Status Quo Bias**               | Filter              | Works inside Slack. Your team won't even notice the switch. |
| 14 | **False Consensus Effect**        | Social              | "Most designers hate this tool. They just pretend they don't." |
| 15 | **In-Group Favoritism**           | Social              | The newsletter for founders who build in public - not sell courses. |
| 16 | **Halo Effect**                   | Optimizer           | Designed by the same studio behind Apple's award-winning UI. |
| 17 | **Hindsight Bias**                | Optimizer           | "In 2022, we said no-code would eat SaaS. 3 years later - here's the data." |
| 18 | **Backfire Effect**               | Filter              | "You're right - cold email IS broken. That's exactly why we rebuilt the approach." |
| 19 | **Bias Blind Spot**               | Filter              | "If you're skeptical about these claims -- great. Let's look at the data." |
| 20 | **Group Polarization**            | Social              | Join 5,000 founders who are quitting the 9-to-5 this year. |

## Tone-of-Voice Switcher

Every output is tagged with one of 7 styles (or a hybrid with formula: 70% primary cadence + 30% secondary lexical markers). Each tone has a mandatory narrative minimum - e.g., warm-human requires a Named Person Story Arc or a labeled `[illustrative]` narrative in the first 3 sentences; luxe-minimal requires a sensory-physical anchor.

| Style | Voice | Best for |
|-------|-------|----------|
| `bold-sell` | Direct, urgent, high-energy | Flash sales, DTC, launches |
| `expert-calm` | Measured, analytical, data-rich | B2B, SaaS, consulting |
| `rebel-edgy` | Contrarian, disruptive, provocative | Youth brands, challengers, creators |
| `warm-human` | Empathetic, story-driven, vulnerable | Health, coaching, community |
| `luxe-minimal` | Sparse, polished, high-status | Premium, luxury, design |
| `community-build` | Inclusive, tribal, «we»-language | Community launches, membership |
| `data-vivid` | Numbers-driven, visual, concrete | Case studies, ROI pages, B2B decks |

## Bias Combinations (14 pre-built stacks)

Some biases multiply when combined. The skill provides 14 ready-to-use combos with conflict detection:

| Combo | Biases | Use for |
|-------|--------|---------|
| **Trust Spiral** | Authority → Social Proof → Confirmation → Endowment | Landing pages, sales pages |
| **Urgency Engine** | Loss Aversion → Social Proof → Scarcity | Flash sales, launches |
| **Loyalty Loop** | Confirmation → In-Group → Sunk Cost → Status Quo | Retention, upsells |
| **Conversion Chain** | Availability → Framing → Anchoring → Social Proof → Risk Reversal | Ads, free-to-paid |
| **Cold-to-Warm Bridge** | Availability → Framing → Authority → Social Proof | Cold audience → consideration |
| **Trust-Repair Sequence** | BBS(rev) → FAE(rev) → CogDiss → SQ(rev) → Reciprocity | Crisis, apology |
| **Desire Escalator** | Fear → Availability → Survivorship → Loss Aversion | Problem → solution |
| **Objection Destroyer** | Backfire → Anchoring → CogDiss → Risk Reversal | FAQ, skeptical audiences |
| **Community Builder** | In-Group → Group Polarization → False Consensus → Social Proof | Community launch |
| **Premium Positioning** | Halo → Anchoring → Authority → In-Group | Luxury, high-ticket |
| **Launch Day Stack** | Framing → Anchoring → Social Proof → Scarcity → Risk Reversal | Launch day |
| **Lead Magnet Funnel** | Reciprocity → Endowment → Authority → Sunk Cost | Freebie → nurture |
| **Re-engagement Hook** | Availability → Sunk Cost → In-Group → Loss Aversion | Lapsed customers |
| **Micro-Content Burst** | Framing + False Consensus + Social Proof (parallel) | Twitter/X, push notifications |

## Bias Selection Router

The skill doesn't guess which biases to use. `SKILL.md` contains an inlined **Bias Selection Router** - a single master table (38 rows) that maps audience × product × platform directly to a bias stack. Three steps: lookup → scenario override → category check. No multi-step decision-matrix traversal.

- **Audience temperature** (cold / warm / hot / lapsed / skeptical / stranger / defensive) ×
- **Product type** (low-B2C, mid-B2C, high-B2C, SaaS B2B, info-product, health, community) ×
- **Platform** (Twitter/X, LinkedIn, Instagram, TikTok, email, landing page, webinar, search ads)
- **= Instant bias stack** (3-5 biases, pre-validated for complementarity)
- **Scenario Override** - if user request matches a trigger (e.g., "launch", "apology"), biases are swapped per the Scenario Quick-Reference table.

Also includes a **Bias Conflict Detector** - 6 known bias conflicts with resolution strategies (e.g., Loss Aversion + Confirmation compete → sequence them: Fear first, Confirmation after solution).

## Anti-Patterns (with Mechanical Detection Rules)

`SKILL.md` contains 13 anti-patterns inlined - each with a **detection rule** the LLM runs mechanically (grep-style) on its output before delivering:

| # | Anti-Pattern | Detection Rule | Example Failure |
|---|-------------|----------------|-----------------|
| 1 | Vague Social Proof | Search for "thousands","many" near customer claims → FAIL | "Thousands of satisfied customers" |
| 2 | Fear Without an Exit | Fear language without solution in same paragraph → FAIL | Threat with no immediate solution |
| 3 | Framing Without Anchoring | "Not X, but Y" without quantified old-way → FAIL | "This is a revolution" - no reference point |
| 4 | Authority Without Proof | "Studies show" without named source+year → FAIL | "Studies show..." - no source, no year |
| 5 | Transactional Reciprocity | Free value + pitch in same communication → FAIL | "Free ebook! Now buy." |
| 6 | Fake Scarcity | "Only X left" without explaining WHY → FAIL | Countdown timers that reset on reload |
| 7 | Premature Sunk Cost | "You've come this far" in first contact → FAIL | Sunk cost language in first paragraph |
| 8 | Empty In-Group | "Like-minded" without named identity → FAIL | "People like you" - no shared identity |
| 9 | Wrong-Source Halo | "Featured in [pub]" audience doesn't respect → FAIL | "As seen on Forbes" - audience doesn't respect Forbes |
| 10 | Insulting Confirmation | "Most people are wrong" → reader in "wrong" group → FAIL | Makes reader defensive, not engaged |
| 11 | Abstract Availability | "Imagine [scenario]" with <3 concrete sensory details → FAIL | No smells, sounds, times, names |
| 12 | Blaming Dissonance | "You say X but do Y" → blames reader, not system → FAIL | Shame → withdrawal, not action |
| 13 | Statistical-Only Fallacy | All social proof / authority claims are aggregate stats with zero named-person narrative → FAIL | Informs System 2, never activates System 1. Data without story = processed but not felt. |

**Post-Generation Verification:** After writing, the LLM runs a mandatory 7-point mechanical checklist before delivering any output - checking for specific numbers, named sources, fear exits, scarcity explanations, system-blame, human narrative depth (NPSA or `[illustrative]`), and **provenance** (every fact traceable to input, a verified source, or an explicit placeholder).

## What's inside

```
MindFluence/
├── skills/mindfluence/          ← runtime skill package
│   ├── SKILL.md                 ← Main instruction. Self-contained core v2.5.0.
│   │                              Inlined: Bias Selection Router (38 rows), Scenario Quick-Reference,
│   │                              Cultural Quick-Reference, 13 Anti-Patterns with detection rules
│   │                              (incl. Statistical-Only Fallacy), Narrative Depth Requirements
│   │                              (Mode A NPSA / Mode B [illustrative] + Conversational Direct Address + Unexpected Detail),
│   │                              14 Power Combinations, Bias Conflict Detector,
│   │                              Post-Generation Verification (7 checks including HUMAN/NARRATIVE and PROVENANCE),
│   │                              7 tones + hybrid formula with narrative minimums, 3-tier output format,
│   │                              5 inlined few-shot examples (Mode A/B), Quality Rubric,
│   │                              Rewrite Without Metrics (7 intents: full rewrite, tone shift, bias inject/remove,
│   │                              anti-pattern fix, audience/platform adaptation),
│   │                              External Reference Files table with relative paths.
│   ├── references/
│   │   ├── decision-matrix.md   ← Detailed audience×product×platform mapping. For deeper bias selection.
│   │   ├── anti-patterns.md     ← 13 AI copywriting failures + detailed fixes + 30-sec audit checklist.
│   │   └── cultural-matrix.md   ← Full bias-by-bias cultural adaptation across 4 cultural dimensions (Hofstede + Hall).
│   ├── scenarios/               ← Task-specific playbooks (13 scenarios) - authoritative for complex tasks
│   │   ├── product-launch.md    ← Pre-launch → launch day → post-launch bias sequences
│   │   ├── social-media-post.md ← X, LinkedIn, Instagram, Telegram, TikTok patterns
│   │   ├── landing-page.md      ← Full page bias map - hero to footer, section by section
│   │   ├── email-sequence.md    ← Welcome, nurture, cart abandonment, re-engagement
│   │   ├── webinar-warmup.md    ← Registration → live event (minute-by-minute) → post-webinar
│   │   ├── ad-campaign.md       ← Video, search, social, retargeting + A/B testing
│   │   ├── sales-page.md        ← 12-section psychological arc for high-ticket
│   │   ├── case-study.md        ← 6-part success story structure
│   │   ├── pricing-page.md      ← Anchoring architecture, decoy engineering
│   │   ├── cold-outreach.md     ← 5-line rule - no trust, no social proof
│   │   ├── crisis-response.md   ← 6-part apology structure - defensive bias engineering
│   │   ├── seo-brief.md         ← SEO brief integration, keyword density, humanization survivability
│   │   └── push-notifications.md ← Push & SMS - lock screen psychology, 6 push types
│   ├── examples/                ← Annotated outputs (7 examples)
│   │   ├── social-post.md       ← LinkedIn post for freelancers (7 biases dissected)
│   │   ├── landing-hero.md      ← Hero section for premium meal delivery
│   │   ├── ad-script.md         ← 30s video ad for language app
│   │   ├── email-welcome.md     ← SaaS welcome email
│   │   ├── longform-article.md  ← Article intro with full bias analysis
│   │   ├── audit-example.md     ← Audit Mode - ad analyzed for biases + anti-patterns + fixes
│   │   └── optimize-hero.md     ← Optimize Mode - hero iterated from metrics
│   └── agents/openai.yaml       ← OpenAI agent manifest
├── install.py                   ← Installer for Claude Code, OpenCode, Codex, .agents
├── .claude-plugin/plugin.json
├── .cursor-plugin/plugin.json
├── CHANGELOG.md                 ← Version history and release notes.
├── SECURITY.md                  ← Vulnerability reporting and security scope.
└── README.md / README.ru.md
```

## Example

**Request:** "Write a LinkedIn post about why freelancers undercharge."

**Output:** *(illustrative example; annotated with `[TONE]`, `[BIASES ENGAGED]`, `[TARGET ACTION]`, and `[RATIONALE]`)*

> `[TONE: warm-human × expert-calm]`
>
> I lost $23,000 before I understood this.
>
> For 3 years, I charged clients based on what "felt right"...

*→ [full example in `skills/mindfluence/examples/social-post.md`]*

## Ethical Boundaries

**Always:**
- Use biases to get attention for genuinely valuable products
- Be transparent about what your product does and doesn't do
- Use factual, verifiable social proof

**Never:**
- Create false scarcity
- Fabricate testimonials, reviews, numbers, names, quotes, or sources
- Exploit fear to sell solutions that don't solve the fear
- Reinforce harmful beliefs
- Target vulnerable populations

**The line:** Would the customer, with full information and time to reflect, still choose your product? *Yes* = persuasion. *No* = manipulation.

## Integration

MindFluence is designed for bi-directional integration with [RankWise](https://github.com/MADEVAL/RankWise) (SEO Content Engine) and [human-ai](https://github.com/MADEVAL/HumanAI) (Text Humanization Engine). The three skills form a complete content production pipeline: SEO structure → persuasive copy → human voice.

### With RankWise (SEO Content Engine)

**Pipeline:** RankWise provides the SEO skeleton → MindFluence injects cognitive bias persuasion into it.

**What MindFluence does:**
- Uses the brief's heading structure (H1, H2, H3) as its skeleton - does not restructure
- Places the primary keyword in: H1, first paragraph, and at least one H2 (as specified in the brief)
- Keeps keyword density within the tone-specific cap (see table below)
- Preserves the brief's internal link plan (target URLs and suggested anchor text)
- Cross-references power words - avoids words that overlap with AI-burned-word lists

**Keyword density caps by tone:**

| MindFluence Tone | Max Density | Notes |
|-----------------|-------------|-------|
| `bold-sell` | 1.5% | Highest risk of over-stuffing. Cap strictly. |
| `expert-calm` | 1.2% | Natural fit for informational content. |
| `warm-human` | 1.2% | Conversational tone distributes keywords well. |
| `rebel-edgy` | 1.5% | Contrarian framing may push keyword out - ensure first-150-word placement. |
| `luxe-minimal` | 1.0% | Sparse copy - place keyword once prominently rather than forcing multiple instances. |

**Joint prompts:**
- "RankWise SEO brief for [topic]. Keyword: [kw]. Then MindFluence from that brief. Expert-calm tone."
- "RankWise SEO brief for SaaS landing page. Then MindFluence landing page from that brief."

### With human-ai (Text Humanization)

**Pipeline:** MindFluence generates persuasive copy → human-ai humanizes it without breaking the bias structure.

**Tone mapping:**
| MindFluence Tone | human-ai Tone |
|-----------------|--------------|
| `warm-human` | `human` |
| `expert-calm` | `expert` |
| `bold-sell` | `landing` |
| `rebel-edgy` | `social` |
| `luxe-minimal` | `expert` |

**To preserve bias structure during humanization:** use `PIPELINE: cleanup → specificity → tone(skipped) → rhythm → proofread` - this tells human-ai to skip Stage 3 (tone) and keep the MindFluence voice.

**Joint prompts:**
- "Generate MindFluence copy (bold-sell tone), then human-ai humanize it. EN."
- "MindFluence landing page for [product]. Then pass through human-ai."

### Bias-SEO Compatibility

Some cognitive biases have specific SEO interactions. See `skills/mindfluence/scenarios/seo-brief.md` for the full table.

| Bias | SEO Risk | Mitigation |
|------|---------|------------|
| Anchoring | Low | Numbers in opening satisfy C5 (number in title) |
| Loss Aversion | Low | "Stop losing X" - ensure keyword appears in first 150 words |
| Social Proof | Medium | Testimonials lack keywords → add keyword in framing sentences |
| Sunk Cost | Low | Time/effort framing doesn't conflict with SEO |
| Scarcity | Medium | "Limited", "Only X left" may push keyword out of first 150 words |
| Confirmation | Low | "You already know X" - fits keyword-adjacent language |

### Triple Pipeline (RankWise → MindFluence → human-ai)

The complete production pipeline:

1. **RankWise** outputs a complete SEO brief with keyword plan, heading structure, meta drafts, internal link plan, and word count target.
2. **MindFluence** generates persuasive copy within the SEO skeleton, applying cognitive biases section by section.
3. **human-ai** humanizes the copy, respecting: no deletion of keyword-containing headings, no deletion of internal link anchors, no cleanup of bias markers (social proof numbers, anchoring numbers), minimum word count preservation.
4. **RankWise Audit** performs final verification of the 49 SEO factors.

**Joint triple prompt:**
```
Triple pipeline:
1) RankWise SEO brief for [topic]. Keyword: [kw]. Language: [xx].
2) MindFluence generate from that brief. Tone: [expert-calm/warm-human/bold-sell].
3) human-ai humanize the MindFluence output. Preserve SEO structure + bias markers.
4) RankWise audit the final result.
```

### File Locations

| Skill | Expected Location (OpenCode) | Expected Location (Claude Code) |
|-------|------------------------------|--------------------------------|
| RankWise | `.opencode/skills/rankwise/` | `~/.claude/skills/rankwise/` |
| MindFluence | `.opencode/skills/mindfluence/` | `~/.claude/skills/mindfluence/` |
| human-ai | `.opencode/skills/human-ai/` | `~/.claude/skills/human-ai/` |

---

## Getting Started

### Installer

```bash
python install.py --target all
python install.py --target opencode
python install.py --target claude
python install.py --list
python install.py --check
```

`--target all` installs to Claude Code, OpenCode, Codex, and the portable `~/.agents/skills`; `--target project` writes to the current project's `.opencode/skills/`. Add `--dry-run` to preview.

### Quick start (any LLM)

1. Copy the contents of [`skills/mindfluence/SKILL.md`](https://github.com/MADEVAL/MindFluence/blob/main/skills/mindfluence/SKILL.md)
2. Paste as a system prompt / custom instructions
3. Type: *"Write a post about [topic] for [audience] on [platform]"*
4. For deeper context: read the supplementary files in `skills/mindfluence/references/`, `skills/mindfluence/scenarios/`, and `skills/mindfluence/examples/`

**The file is self-contained for core operation.** No additional files needed for standard tasks. Bias Selection Router, Anti-Patterns with detection rules, Cultural Quick-Reference, few-shot examples - everything needed for core operation is inlined. If the LLM you're using can fetch external files, `SKILL.md` contains a full External Reference Files table with relative paths for all supplementary files (`references/decision-matrix.md`, `references/anti-patterns.md`, `references/cultural-matrix.md`, `scenarios/`, `examples/`).

### With OpenCode (native)

Place the `skills/mindfluence/` folder into `.opencode/skills/mindfluence/` (project) or `~/.config/opencode/skills/mindfluence/` (global), or run `python install.py --target opencode`. OpenCode discovers `SKILL.md` by its path - no extra config needed. The folder name becomes the skill ID; keep it lowercase kebab-case (`mindfluence`) for portability.

### With Claude Code

Run `python install.py --target claude`, or copy `skills/mindfluence/` to `~/.claude/skills/mindfluence/`. To use the skill as a project instruction file, copy `skills/mindfluence/SKILL.md` into your project as `CLAUDE.md`.

### As a Custom GPT / Claude Project

Upload `skills/mindfluence/SKILL.md` as the system prompt. For deeper context, add files from `skills/mindfluence/references/`, `skills/mindfluence/scenarios/`, and `skills/mindfluence/examples/` to the knowledge section. The file is self-contained for core operation, but the external files provide richer decision-matrix logic, detailed anti-pattern examples, and full scenario playbooks.

### With any other LLM agent (Cursor, Windsurf, Copilot, Cline, Aider, etc.)

Copy the contents of `skills/mindfluence/SKILL.md` into that agent's instruction file (`.cursorrules`, `.windsurfrules`, `.github/copilot-instructions.md`, `.clinerules`, `CONVENTIONS.md`, etc.). The prompt content is platform-agnostic.

## Requirements

- Any capable LLM with a system prompt / custom instructions field (GPT, Claude, Gemini, DeepSeek, open-source models)
- **Self-contained core:** `skills/mindfluence/SKILL.md`. All tables, detection rules, cultural data, and examples needed for standard tasks are inlined.
- Context window: 32K minimum for COMPACT/STANDARD; 64K+ recommended for EXTENDED and external references.
- For deeper context: external files (`references/decision-matrix.md`, `references/anti-patterns.md`, `references/cultural-matrix.md`, `skills/mindfluence/scenarios/`) preserved in the repo - relative paths in SKILL.md's External Reference Files section so LLMs working with one file can guide users to the rest of the package.
- No API keys, no tools, no dependencies - pure prompt engineering
- Works in any language; adapts cultural references to the target market

## Why "mindfluence"?

**mind** (the brain - cognitive biases live here) + **influence** (what persuasion actually does - shapes decisions without force).

---

## Security

Report vulnerabilities privately via GitHub Security Advisories. See [SECURITY.md](SECURITY.md) for scope and supported versions.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

---

## License

MIT

---

## GitHub Description

```
AI prompt-skill v2.5.0: 20 cognitive biases → high-converting marketing copy with a provenance-first narrative engine. Self-contained core with a 38-row Bias Selection Router (audience×product×platform→instant bias stack), 13 anti-patterns with mechanical detection rules (incl. Statistical-Only Fallacy), Narrative Depth Requirements (real-data NPSA or labeled [illustrative] fallback + Conversational Direct Address + Unexpected Detail), 14 power bias combinations, 7 tone styles + hybrid formula with narrative minimums, 3-tier output format (compact/standard/extended), 7-point post-generation verification (incl. PROVENANCE/TRUTH GATE and HUMAN narrative check), 12-region cultural quick-reference, Rewrite Without Metrics (7 rewrite intents), and 5 inlined few-shot examples. Covers ads, landing pages, email sequences, social posts, webinars, launches, sales pages, case studies, pricing pages, cold outreach, push notifications, crisis response, and SEO brief integration.
```

## GitHub Tags

`prompt-engineering` `cognitive-biases` `marketing` `copywriting` `behavioral-economics` `psychology` `ai-prompts` `llm-skills` `persuasion` `neuromarketing` `conversion-optimization` `content-strategy` `system-prompt` `gpt` `claude` `self-contained` `bias-detection` `marketing-automation` `narrative-engineering` `human-quality`

Skills.sh: https://www.skills.sh/madeval/mindfluence
