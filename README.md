# mindfluence

> **Persuasion engineered through psychology, not manipulation.**

An AI prompt-skill that turns 20 cognitive biases into high-converting marketing copy — for any language, any platform, any audience.

---

## What is this?

**mindfluence** is a system prompt (skill) for LLMs — GPT-4, Claude, Gemini, or any capable model. It transforms the AI into a marketing strategist who understands *why* humans click, read, and buy — not just *what* to write.

It's built on decades of research in behavioral economics and evolutionary psychology: Kahneman's two systems, Cialdini's principles, Munger's psychological misjudgments, Festinger's cognitive dissonance — distilled into actionable copywriting instructions.

## How it works

1. **Load `SKILL.md`** as a system prompt into any LLM.
2. **Give a task:** "Write a LinkedIn post about..." / "Create a landing page for..." / "Audit this ad for cognitive biases."
3. **Get output** with every bias labeled, every decision explained, every word psychologically justified.

**Two modes:**
- **Quick Mode** (default) — minimal input, immediate output. The AI picks the best biases automatically.
- **Deep Mode** — the AI asks clarifying questions about audience, platform, tone, and desired action before generating.

## What's inside

```
mindfluence/
├── SKILL.md                    ← Main instruction. 20 biases, methodology, tone-of-voice, ethics, output format.
├── decision-matrix.md          ← Audience × product × platform → bias priority map. Eliminates guesswork.
├── anti-patterns.md            ← 12 common AI copywriting failures + concrete fixes + audit checklist.
├── scenarios/                  ← Task-specific playbooks (11 scenarios)
│   ├── product-launch.md       ← Pre-launch → launch day → post-launch bias sequences
│   ├── social-media-post.md    ← X, LinkedIn, Instagram, Telegram, TikTok patterns
│   ├── landing-page.md         ← Full page bias map — hero to footer, section by section
│   ├── email-sequence.md       ← Welcome, nurture, cart abandonment, re-engagement
│   ├── webinar-warmup.md       ← Registration → live event (minute-by-minute) → post-webinar
│   ├── ad-campaign.md          ← Video, search, social, retargeting + A/B testing framework
│   ├── sales-page.md           ← Long-form sales page — 12-section psychological arc for high-ticket
│   ├── case-study.md           ← 6-part success story structure (situation → result → CTA)
│   ├── pricing-page.md         ← Anchoring architecture, decoy engineering, localization psychology
│   ├── cold-outreach.md        ← 5-line rule for cold email/DM — no trust, no social proof
│   └── crisis-response.md      ← 6-part apology structure — defensive bias engineering
├── examples/                   ← Annotated outputs showing the skill in action
│   ├── social-post.md          ← LinkedIn post for freelancers (7 biases dissected)
│   ├── landing-hero.md         ← Hero section for premium meal delivery
│   ├── ad-script.md            ← 30s video ad for language app
│   ├── email-welcome.md        ← SaaS welcome email
│   └── longform-article.md     ← Article intro with full bias analysis
└── README.md
```

## The 20 Cognitive Biases

| # | Bias | Category | Marketing Use |
|---|------|----------|---------------|
| 1 | **Social Proof / Bandwagon** | Social | "Join 10,000+ who already..." |
| 2 | **Anchoring** | Optimizer | Show expensive option first; everything else seems cheap |
| 3 | **Framing** | Filter | Same fact, opposite reaction — depending on wording |
| 4 | **Appeal to Authority** | Social | Cite Harvard, Forbes, domain experts |
| 5 | **Fear / Loss Aversion** | Filter + Social | "You're losing $X/day. Here's the fix." |
| 6 | **Availability Heuristic** | Optimizer | Vivid stories beat statistics every time |
| 7 | **Confirmation Bias** | Filter | Tell people they were right; they'll love you |
| 8 | **Cognitive Dissonance** | Filter + Optimizer | Surface contradictions → offer resolution through your product |
| 9 | **Survivorship Bias** | Optimizer | Show winners; acknowledge they're the best outcomes |
| 10 | **Endowment Effect** | Optimizer | Free trials = they already "own" it = cancelling hurts |
| 11 | **Fundamental Attribution Error** | Social | Blame the system, not the customer |
| 12 | **Sunk Cost Fallacy** | Optimizer | "You've already read 3,000 words. Last step." |
| 13 | **Status Quo Bias** | Filter | "Works with what you already have. No migration needed." |
| 14 | **False Consensus Effect** | Social | "Everyone secretly thinks this. We say it out loud." |
| 15 | **In-Group Favoritism** | Social | "For people like us..." — instant belonging |
| 16 | **Halo Effect** | Optimizer | Beautiful design = trustworthy product |
| 17 | **Hindsight Bias** | Optimizer | "We predicted this in 2022. Here we are." |
| 18 | **Backfire Effect** | Filter | Never correct — reframe. "Yes, AND..." |
| 19 | **Bias Blind Spot** | Filter | "Smart people know biases apply to THEM too." |
| 20 | **Group Polarization** | Social | Communities don't moderate — they amplify. Build one. |

## Tone-of-Voice Switcher

Every output is tagged with one of 5 styles (or a hybrid):

| Style | Voice | Best for |
|-------|-------|----------|
| `bold-sell` | Aggressive, urgent, punchy | Flash sales, DTC, launches |
| `expert-calm` | Intellectual, measured, data-rich | B2B, SaaS, consulting |
| `rebel-edgy` | Disruptive, contrarian | Youth brands, challengers, creators |
| `warm-human` | Empathetic, story-driven | Health, coaching, community |
| `luxe-minimal` | Polished, sparse, high-status | Premium, luxury, design |

## Bias Combinations

Some biases multiply when combined:

| Combo | Biases | Use for |
|-------|--------|---------|
| **Trust Spiral** | Authority → Social Proof → Confirmation → Endowment | Landing pages, sales pages |
| **Urgency Engine** | Fear → Loss Aversion → Social Proof → Scarcity | Flash sales, launches |
| **Loyalty Loop** | Confirmation → In-Group → Sunk Cost → Status Quo | Retention, upsells |
| **Conversion Chain** | Availability → Framing → Anchoring → Social Proof → Risk Reversal | Ads, free-to-paid |

## Decision Matrix

The skill doesn't guess which biases to use. `decision-matrix.md` provides a lookup table:

- **Audience temperature** (cold / warm / hot / lapsed / skeptical) → bias priority
- **Product type** (low-B2C, high-B2C, B2B SaaS, info-products, health, community) → dominant biases
- **Platform constraint** (Twitter, LinkedIn, Instagram, email, landing page, webinar) → allowed & forbidden biases
- **Step-by-step flow:** audience → product → platform → combine → validate
- **Quick-lookup table** for 18 common tasks with pre-computed bias stacks

## Anti-Patterns

`anti-patterns.md` catches the 12 most common ways AI gets cognitive-bias copy wrong — each with the failing output, the psychological reason it fails, the concrete fix, and a rule to follow:

| # | Anti-Pattern | Example Failure |
|---|-------------|-----------------|
| 1 | Vague Social Proof | "Thousands of satisfied customers" |
| 2 | Fear Without an Exit | Threat with no immediate solution |
| 3 | Framing Without Anchoring | "This is a revolution" — no reference point |
| 4 | Authority Without Proof | "Studies show..." — no source, no year |
| 5 | Transactional Reciprocity | "Free ebook! Now buy." — gift and pitch in same breath |
| 6 | Fake Scarcity | Countdown timers that reset on reload |
| 7 | Premature Sunk Cost | "You've come this far" — in the first paragraph |
| 8 | Empty In-Group | "Like-minded people" — no shared identity |
| 9 | Wrong-Source Halo | "As seen on Forbes" — audience doesn't respect Forbes |
| 10 | Insulting Confirmation | "Most people are wrong" — makes reader defensive |
| 11 | Abstract Availability | "Imagine struggling" — no concrete sensory details |
| 12 | Blaming Dissonance | "You say X but do Y" — blames the reader, not the system |

Includes an **audit checklist** — scan any output in 30 seconds before delivering.

## Example

**Request:** "Write a LinkedIn post about why freelancers undercharge."

**Output:** *(annotated with `[TONE]`, `[BIASES ENGAGED]`, `[TARGET ACTION]`, and `[RATIONALE]`)*

> `[TONE: warm-human × expert-calm]`
>
> I lost $23,000 before I understood this.
>
> For 3 years, I charged clients based on what "felt right"...

*→ [full example in `examples/social-post.md`]*

## Ethical Boundaries

**Always:**
- Use biases to get attention for genuinely valuable products
- Be transparent about what your product does and doesn't do
- Use factual, verifiable social proof

**Never:**
- Create false scarcity
- Fabricate testimonials or reviews
- Exploit fear to sell solutions that don't solve the fear
- Reinforce harmful beliefs
- Target vulnerable populations

**The line:** Would the customer, with full information and time to reflect, still choose your product? *Yes* = persuasion. *No* = manipulation.

## Getting Started

### Quick start (any LLM)

1. Copy the contents of `SKILL.md`
2. Paste as a system prompt / custom instructions
3. Type: *"Write a post about [topic] for [audience] on [platform]"*

### With OpenCode (native)

Place the `mindfluence/` folder into `.opencode/skills/` (project) or `~/.config/opencode/skills/` (global). OpenCode auto-discovers `SKILL.md` via its frontmatter — no extra config needed. The skill activates when you ask for marketing copy, ads, landing pages, emails, or launch content.

### With Claude Code

Copy `SKILL.md` into your project as `CLAUDE.md`, or place the full `mindfluence/` folder under `~/.claude/skills/`.

### As a Custom GPT / Claude Project

Upload `SKILL.md` as the system prompt. Add `decision-matrix.md`, `anti-patterns.md`, and files from `scenarios/` and `examples/` to the knowledge section for full context.

### With any other LLM agent (Cursor, Windsurf, Copilot, Cline, Aider, etc.)

Copy the contents of `SKILL.md` into that agent's instruction file (`.cursorrules`, `.windsurfrules`, `.github/copilot-instructions.md`, `.clinerules`, `CONVENTIONS.md`, etc.). The prompt content is platform-agnostic — only the file name changes.

## Requirements

- Any LLM with a system prompt / custom instructions field (GPT-4, Claude 3+, Gemini, local models via Ollama/LM Studio)
- For full skill functionality (decision matrix, anti-patterns, scenarios, examples): a skill system that loads files from a folder (OpenCode, Claude Code). For other agents, copy `SKILL.md` as a standalone prompt — it contains the complete core methodology.
- No API keys, no tools, no dependencies — pure prompt engineering
- Works in any language; adapts cultural references to the target market

## Why "mindfluence"?

**mind** (the brain — cognitive biases live here) + **influence** (what persuasion actually does — shapes decisions without force).

---

## License

MIT — use freely in commercial and non-commercial projects.

---

## GitHub Description

```
An AI prompt-skill that turns 20 cognitive biases into high-converting marketing copy. Includes playbooks for ads, landing pages, email sequences, social posts, webinars, launches, sales pages, case studies, pricing pages, cold outreach, and crisis response. Language-agnostic. Works with any LLM.
```

## GitHub Tags

`prompt-engineering` `cognitive-biases` `marketing` `copywriting` `behavioral-economics` `psychology` `ai-prompts` `llm-skills` `persuasion` `neuromarketing` `conversion-optimization` `content-strategy` `system-prompt` `gpt` `claude`
