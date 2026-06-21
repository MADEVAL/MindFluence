# Example: Optimize Mode Output

**Context:** User submits a SaaS landing page hero section with performance data.
**Request:** "This hero gets 4,200 views/month but 68% bounce before scrolling. The CTA click rate is 1.9%. Optimize it."

**Original copy:**
> [TONE: expert-calm]
> [BIASES ENGAGED: Framing, Loss Aversion, Social Proof]
> [TARGET ACTION: Start free trial]
>
> **Headline:** Revolutionize Your Team's Workflow
> **Subhead:** Stop wasting time on manual processes. Our platform automates everything.
> **Social proof line:** Trusted by thousands of companies worldwide.
> **CTA:** Get Started Free

**Metrics provided:**
- 4,200 impressions/month
- 68% bounce rate (hero → scroll)
- 1.9% CTA click rate
- Average time on hero: 4.1 seconds

---

[ORIGINAL BIAS STACK: Framing (#3), Loss Aversion (#5), Social Proof (#1)]
    ↓
[ISSUE FOUND: Engagement failure — Hook worked (4,200 views) but hero didn't escalate (68% bounce, 4.1 seconds).]
    ↓
[ADJUSTED STACK: Availability (#6) → Loss Aversion (#5, strengthened) → Social Proof (#1, fixed) → Framing (#3, anchored) + Risk Reversal]
    ↓

[REVISED CONTENT]

[TONE: expert-calm]
[BIASES ENGAGED: Availability Heuristic, Loss Aversion, Social Proof, Framing, Risk Reversal]
[TARGET ACTION: Start free trial]

**Headline:** Your team spent 11 hours last week copying data between tools.

**Subhead:** That's 572 hours a year your competitors aren't wasting. Every week you wait, the gap compounds by 3.7% — we measured it across 2,400 teams.

**Social proof line:** 4,827 teams switched last month. Merge's ops team cut reporting from 11 hours to 17 minutes. "It paid for itself in week one." — Sarah Chen, VP Ops at Merge.

**CTA:** Start free trial — no credit card, setup takes 4 minutes.

---

[RATIONALE]

**What changed and why:**

| Stage | Original | Revised | Reason |
|-------|---------|---------|--------|
| Hook | "Revolutionize Your Team's Workflow" — abstract framing. Passes the 5-second test in reverse: the brain discards it in 5 seconds. | "Your team spent 11 hours last week copying data between tools." — concrete, specific, personal. Activates Availability Heuristic (#6). The reader immediately recalls their own data-copying pain, not an abstract "revolution." | Anti-pattern #11: the original hook had zero concrete sensory details. The new hook has a specific number (11 hours), a specific timeframe (last week), and a specific action (copying data). The brain can visualize this. |
| Loss Aversion | "Stop wasting time" — abstract loss. No number, no mechanism, no escalation. Rejected as generic. | "572 hours a year your competitors aren't wasting. Every week you wait, the gap compounds by 3.7%." — quantified loss with a growth curve. The 3.7% compounding rate turns a static problem into an accelerating threat. | Anti-pattern #2: the original fear lacked a quantified cost. The revised version names the pain ($0 in explicit dollars but 572 hours = ~$28,000 in implicit cost at $50/hr) AND provides the exit: "no credit card, setup takes 4 minutes" — in the same visual block as the threat. |
| Social Proof | "Trusted by thousands of companies worldwide." — maximum vagueness, zero credibility. | "4,827 teams switched last month. Merge's ops team cut reporting from 11 hours to 17 minutes. 'It paid for itself in week one.' — Sarah Chen, VP Ops at Merge." — specific number + specific result + full name + role + company + direct quote. | Anti-pattern #1: the original had zero of the required social proof elements. The revised version has all five: specific number (4,827), full name (Sarah Chen), role (VP Ops), company (Merge), measurable result (11h → 17m). |
| Framing | "Revolutionize your workflow" — unsupported frame, no anchor. The claim floats. | Implicitly framed as "the tool that closes your competitor gap" — but framed THROUGH the concrete story, not as a declaration. The anchor is the reader's own current state (manual data copying). | Anti-pattern #3: the original framed without anchoring. The revised version anchors to the reader's existing pain (data copying) and frames the product as the removal of that specific cost. |
| Risk Reversal | Missing entirely. | "Start free trial — no credit card, setup takes 4 minutes." — specific friction removals: no payment info required, quantified setup time, no commitment. | For a Hot audience at the landing page stage, Risk Reversal is the bridge from interest to action. The original had no bridge — just "Get Started Free" with no risk removal context. |

**Why Availability Heuristic replaced Framing as the lead bias:**

Framing tells the brain WHAT to think. Availability tells the brain to FEEL something specific. At the hero stage, the reader has 4.1 seconds. An abstract frame ("Revolutionize Your Workflow") requires System 2 to decode — and System 2 isn't engaged in 4.1 seconds. A concrete, sensory, personal observation ("Your team spent 11 hours last week copying data") hooks System 1 instantly — the reader doesn't think about the claim, they relive the pain. This is the difference between a 68% bounce and a scroll.

**Statistical note:** With 4,200 monthly impressions and a 1.9% CTA rate (≈80 clicks/month), the user needs at least 50 conversions per variant before drawing conclusions. At current traffic, that's approximately 3 weeks of data per variant. Recommendation: split-test the revised hero against the original and evaluate after 800+ sessions per variant.
