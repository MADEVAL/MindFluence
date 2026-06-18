# Example: Audit Mode Output

**Context:** User submits a Facebook ad for audit.
**Request:** "Audit this ad for cognitive biases."

**Ad being audited:**
> "Tired of expensive software? Our platform is used by thousands of happy customers. Studies show our method is the most effective. Try it now - only 3 spots left at this price!"

---

[BIASES FOUND]
- **Social Proof (#1)** - "Thousands of happy customers" detected.
- **Appeal to Authority (#4)** - "Studies show" detected.
- **Scarcity (technique, mapped to #5)** - "Only 3 spots left" detected.

[ANTI-PATTERNS FOUND]
- **Anti-pattern #1 (Vague Social Proof):** "Thousands of happy customers" - no specific number, no name, no face, no measurable result. See Bias #1 for correct application.
- **Anti-pattern #4 (Authority Without Proof):** "Studies show" - no source, no year, no specific finding. See Bias #4 for correct application.
- **Anti-pattern #6 (Fake Scarcity):** "Only 3 spots left at this price" - no explanation of WHY it's limited. Is it a cohort cap? A launch discount ending? An artificial timer? Unexplained scarcity reads as fake. See Scarcity technique rules.

[ANALYSIS per bias]

**Social Proof (#1):** Present but fatally underpowered. A vague claim ("thousands") has near-zero psychological impact. The brain dismisses unquantified social proof as noise. Needs: a specific number ("4,827 customers"), at least one identifiable person (name + role + result), or a recognizable metric (rating, review count from a trusted platform).

**Appeal to Authority (#4):** Formally present but non-functional. "Studies show" without attribution is the most credibility-destroying phrase in copywriting. Readers have been burned by this too many times. Needs: named source + year + specific finding. Example: "A 2024 RCT in the Journal of Marketing (N=2,400) found teams using [approach] ship 23% faster."

**Scarcity (technique):** Present but structurally unsound. Unexplained, unqualified scarcity is indistinguishable from the countless fake-countdown ads consumers have trained themselves to ignore. Needs: a genuine constraint, EXPLAINED. "Cohort capped at 50 because our team of 3 gives individual feedback." The "why" transforms scarcity from manipulative to credible.

**Missing biases this ad should have:**
- **Framing (#3):** "Tired of expensive software?" is a price frame, but it doesn't establish what "expensive" means. No anchor. The reader doesn't know if "expensive" = $30/mo or $3,000/mo.
- **Loss Aversion (#5):** No quantification of what the reader is losing by not acting. No cost-of-inaction frame.

[RECOMMENDATIONS]

**Fix 1 - REWRITE the social proof:**
> "4,827 teams switched this year. Sarah Chen, Ops Director at Merge: 'We cut reporting from 11 hours to 17 minutes a week.'"
→ Replaces vague claim with specific number + named person + measurable outcome.

**Fix 2 - REWRITE the authority claim:**
> "A 2024 meta-analysis in the Journal of Applied Psychology (12,000 participants) found [specific mechanism] improves output by 31%."
→ Replaces "studies show" with named, dated, quantified authority.

**Fix 3 - REWRITE the scarcity:**
> "We cap each cohort at 50 founders - our team of 3 reviews every submission personally. Current cohort: 47/50. Registration closes Friday midnight PT."
→ Replaces unexplained scarcity with genuine constraint + specific deadline + current status.

**Fix 4 - ADD framing with anchor:**
> "Most project management tools cost $12–25/user/month and take weeks to configure. Our platform: $7/user, runs in your browser in 30 seconds."
→ Adds price anchor + time anchor, creating a frame where the offer looks favorable.

**Fix 5 - ADD loss aversion:**
> "Every month you wait, that's $200–600 in per-seat costs and 15–30 hours of configuration time you're spending on outdated tools."
→ Quantifies the cost of inaction. Concrete loss > abstract benefit.

**Revised ad (applying all fixes):**
> "Most project tools cost $12–25/user/month and take weeks to set up. Ours runs in your browser in 30 seconds - $7/user. A 2024 meta-analysis (12,000 participants) found our approach improves team output by 31%. Sarah Chen, Ops Director at Merge: 'We cut reporting from 11 hours to 17 minutes a week.' 4,827 teams switched this year. Cohort 12: 47 of 50 spots filled. Registration closes Friday midnight. Start your free trial - no credit card, cancel anytime."
