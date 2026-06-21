# MindFluence

[ **English** | [Русский](README.ru.md) ]

> **Persuasion engineered through psychology, not manipulation.**

An AI prompt-skill that turns 20 cognitive biases into high-converting marketing copy - for any language, any platform, any audience.

---

## What is this?

**MindFluence** is a system prompt (skill) for LLMs - GPT, Claude, Gemini, DeepSeek or any capable model. It transforms the AI into a marketing strategist who understands *why* humans click, read, and buy - not just *what* to write.

It's built on decades of research in behavioral economics and evolutionary psychology: Kahneman's two systems, Cialdini's principles, Munger's psychological misjudgments, Festinger's cognitive dissonance - distilled into actionable copywriting instructions.

## How it works

1. **Load `SKILL.md`** as a system prompt into any LLM.
2. **Give a task:** "Write a LinkedIn post about..." / "Create a landing page for..." / "Audit this ad for cognitive biases."
3. **Get output** with every bias labeled, every decision explained, every word psychologically justified.

**Two modes:**
- **Quick Mode** (default) - minimal input, immediate output. The AI picks the best biases automatically.
- **Deep Mode** - the AI asks clarifying questions about audience, platform, tone, and desired action before generating.
- **Audit Mode** - analyzes existing copy for cognitive biases and anti-patterns. Doesn't create — dissects.
- **Optimize Mode** - iterates on underperforming copy using metrics (CTR, conversion, open rate). Maps funnel stages to specific biases, swaps failing biases, generates A/B variants.

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
| 19 | **Bias Blind Spot**               | Filter              | "You're too smart to fall for this. Which is precisely why it'll work on you." |
| 20 | **Group Polarization**            | Social              | Join 5,000 founders who are quitting the 9-to-5 this year. |

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

`anti-patterns.md` catches the 12 most common ways AI gets cognitive-bias copy wrong - each with the failing output, the psychological reason it fails, the concrete fix, and a rule to follow:

| # | Anti-Pattern | Example Failure |
|---|-------------|-----------------|
| 1 | Vague Social Proof | "Thousands of satisfied customers" |
| 2 | Fear Without an Exit | Threat with no immediate solution |
| 3 | Framing Without Anchoring | "This is a revolution" - no reference point |
| 4 | Authority Without Proof | "Studies show..." - no source, no year |
| 5 | Transactional Reciprocity | "Free ebook! Now buy." - gift and pitch in same breath |
| 6 | Fake Scarcity | Countdown timers that reset on reload |
| 7 | Premature Sunk Cost | "You've come this far" - in the first paragraph |
| 8 | Empty In-Group | "Like-minded people" - no shared identity |
| 9 | Wrong-Source Halo | "As seen on Forbes" - audience doesn't respect Forbes |
| 10 | Insulting Confirmation | "Most people are wrong" - makes reader defensive |
| 11 | Abstract Availability | "Imagine struggling" - no concrete sensory details |
| 12 | Blaming Dissonance | "You say X but do Y" - blames the reader, not the system |

Includes an **audit checklist** - scan any output in 30 seconds before delivering.

## What's inside

```
mindfluence/
├── SKILL.md                    ← Main instruction. 20 biases, methodology, tone-of-voice, ethics, output format.
├── decision-matrix.md          ← Audience × product × platform → bias priority map. Eliminates guesswork.
├── anti-patterns.md            ← 12 common AI copywriting failures + concrete fixes + audit checklist.
├── cultural-matrix.md          ← Bias adaptation across 4 cultural dimensions + 12 region profiles.
├── scenarios/                  ← Task-specific playbooks (12 scenarios)
│   ├── product-launch.md       ← Pre-launch → launch day → post-launch bias sequences
│   ├── social-media-post.md    ← X, LinkedIn, Instagram, Telegram, TikTok patterns
│   ├── landing-page.md         ← Full page bias map - hero to footer, section by section
│   ├── email-sequence.md       ← Welcome, nurture, cart abandonment, re-engagement
│   ├── webinar-warmup.md       ← Registration → live event (minute-by-minute) → post-webinar
│   ├── ad-campaign.md          ← Video, search, social, retargeting + A/B testing framework
│   ├── sales-page.md           ← Long-form sales page - 12-section psychological arc for high-ticket
│   ├── case-study.md           ← 6-part success story structure (situation → result → CTA)
│   ├── pricing-page.md         ← Anchoring architecture, decoy engineering, localization psychology
│   ├── cold-outreach.md        ← 5-line rule for cold email/DM - no trust, no social proof
│   ├── crisis-response.md      ← 6-part apology structure - defensive bias engineering
│   └── push-notifications.md   ← Push & SMS - lock screen psychology, 6 push types, frequency caps
├── examples/                   ← Annotated outputs showing the skill in action (7 examples)
│   ├── social-post.md          ← LinkedIn post for freelancers (7 biases dissected)
│   ├── landing-hero.md         ← Hero section for premium meal delivery
│   ├── ad-script.md            ← 30s video ad for language app
│   ├── email-welcome.md        ← SaaS welcome email
│   ├── longform-article.md     ← Article intro with full bias analysis
│   ├── audit-example.md        ← Audit Mode — ad analyzed for biases + anti-patterns + fixes
│   └── optimize-hero.md        ← Optimize Mode — hero iterated from metrics with full rationale
└── README.md
```

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

Place the `mindfluence/` folder into `.opencode/skills/` (project) or `~/.config/opencode/skills/` (global). OpenCode auto-discovers `SKILL.md` via its frontmatter - no extra config needed. The skill activates when you ask for marketing copy, ads, landing pages, emails, or launch content.

### With Claude Code

Copy `SKILL.md` into your project as `CLAUDE.md`, or place the full `mindfluence/` folder under `~/.claude/skills/`.

### As a Custom GPT / Claude Project

Upload `SKILL.md` as the system prompt. Add `decision-matrix.md`, `anti-patterns.md`, and files from `scenarios/` and `examples/` to the knowledge section for full context.

### With any other LLM agent (Cursor, Windsurf, Copilot, Cline, Aider, etc.)

Copy the contents of `SKILL.md` into that agent's instruction file (`.cursorrules`, `.windsurfrules`, `.github/copilot-instructions.md`, `.clinerules`, `CONVENTIONS.md`, etc.). The prompt content is platform-agnostic - only the file name changes.

## Requirements

- Any capable LLM with a system prompt / custom instructions field (GPT, Claude, Gemini, DeepSeek, open-source models)
- For full skill functionality (decision matrix, anti-patterns, scenarios, examples): a skill system that loads files from a folder (OpenCode, Claude Code). For other agents, copy `SKILL.md` as a standalone prompt - it contains the complete core methodology.
- No API keys, no tools, no dependencies - pure prompt engineering
- Works in any language; adapts cultural references to the target market

## Why "mindfluence"?

**mind** (the brain - cognitive biases live here) + **influence** (what persuasion actually does - shapes decisions without force).

---

## License

MIT

---

## GitHub Description

```
An AI prompt-skill that turns 20 cognitive biases into high-converting marketing copy — for any language, any platform, any audience. Includes playbooks for ads, landing pages, email sequences, social posts, webinars, launches, sales pages, case studies, pricing pages, cold outreach, push notifications, and crisis response. Features a decision matrix (audience × product × platform), 12 anti-patterns with fixes, 20 bias cultural adaptations across 12 regions, and a measurement loop with statistical confidence thresholds.
```

## GitHub Tags

`prompt-engineering` `cognitive-biases` `marketing` `copywriting` `behavioral-economics` `psychology` `ai-prompts` `llm-skills` `persuasion` `neuromarketing` `conversion-optimization` `content-strategy` `system-prompt` `gpt` `claude`
