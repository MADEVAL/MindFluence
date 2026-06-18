# Scenario: Pricing Page

## CONTEXT
A dedicated page presenting your pricing - or the pricing section of a larger page. Pricing is the highest-leverage, highest-anxiety moment in the buyer journey. Done right, it converts. Done wrong, it leaks.

## GOAL
Engineer the pricing presentation so the prospect perceives maximum value, selects the option you want them to select, and feels smart about their choice.

---

## THE PSYCHOLOGY OF PRICING

Pricing is not about numbers. It's about **reference points.** The brain doesn't evaluate price in absolute terms - it evaluates price relative to the nearest available anchor. Your job: control every anchor on the page.

---

## 1. ANCHORING ARCHITECTURE

### The Three-Tier Rule
Always present 3 options. Not 2 (binary choice = anxiety). Not 4+ (choice overload = paralysis). Three is the Goldilocks number.

| Tier | Purpose | Price | Psychology |
|------|---------|-------|------------|
| **Enterprise / Premium** | Anchor. Makes everything else look affordable. | Highest | Almost nobody buys it. That's fine. Its job is to make the middle tier feel like 50% off. |
| **Most Popular** | Target. The one you WANT them to buy. | Middle | Visually highlighted. "Most Popular" badge. Different background color. Slightly larger card. |
| **Starter / Basic** | Entry. Makes the middle feel aspirational. | Lowest | Limited features. Creates "I'd outgrow this" anxiety. |

### Anchoring Techniques

**Technique 1: Show most expensive FIRST (left-to-right or top-to-bottom on mobile).**
The first price the eye sees becomes the anchor. Everything after is "cheap by comparison."
```
Enterprise: $299/mo → Professional: $99/mo → Starter: $29/mo
```
The brain: "$99 is way less than $299. Reasonable."

**Technique 2: Annual-vs-Monthly framing.**
Show annual price as the hero. Show monthly as the comparison anchor.
```
$16/mo (billed annually) ← highlighted
$20/mo (billed monthly) ← anchor
```
Instead of "Save 20% with annual," show the monthly as the reference and annual as the "discounted" version. Loss frame: "$20/mo → $16/mo."

**Technique 3: Pre-price anchoring.**
Before any price appears on the page, establish a value anchor:
> "Companies typically spend $50,000–150,000 building custom solutions for this. Our platform: starting at $99/mo."

The anchor doesn't need to be a competitor - it can be the cost of NOT using your product.

---

## 2. DECOY ENGINEERING

A decoy is an option you don't expect anyone to buy - it exists solely to make another option look better.

**The Classic Decoy (Asymmetric Dominance):**
```
Option A: Print only - $59
Option B: Print + Digital - $125 ← target
Option C: Digital only - $125 ← decoy
```
Option C is dominated by Option B (same price, fewer products). B looks like a bargain. Nobody buys C. They don't need to - C did its job just by existing.

**Modern SaaS Decoy:**
```
Starter: 5 users, 10 projects - $29/mo
Professional: 15 users, unlimited projects - $99/mo ← target
Enterprise: 50 users, unlimited projects, dedicated support - $299/mo ← anchor + decoy
```
Enterprise makes Professional look cheap (anchor). Starter makes Professional look capable (decoy - too limited for serious use).

---

## 3. PRICE PRESENTATION PSYCHOLOGY

### Charm Pricing ($99 vs $100)
- $99 signals "discount." Use for B2C, low-ticket, impulse purchases.
- $100 signals "quality." Use for B2B, high-ticket, premium positioning.
- $997 works better than $1,000 for info-products (both charm and anchor at the same time).
- Round numbers for luxury. $5,000 > $4,999 for a premium course. Odd numbers signal "discount store."

### Price Is Just a Number - Until You Contextualize It
- "Just $3/day" (reframes annual as daily - daily = negligible)
- "Less than your team's weekly coffee budget" (reframes relative to trivial expense)
- "Pays for itself in 2 client calls" (ROI reframe)

### The Left-Digit Effect
$3.99 feels significantly cheaper than $4.00 - because the brain anchors on the leftmost digit. Use for impulse purchases. Avoid for premium.

---

## 4. FEATURE TIERING PSYCHOLOGY

### The "Not Available" Anxiety
Features missing from lower tiers should create FOMO, not price resistance.
- Starter: "Up to 5 projects" → "I'd need more than that soon."
- Professional: "Unlimited projects" → "This is the one."

### The "Contact Us" Enterprise Move
"Call for pricing" on the top tier: creates exclusivity. But ONLY if your target market expects it (enterprise B2B). For consumer products, hidden pricing = distrust signal.

### Feature Bundling
Don't list 20 features. Group them into 3–4 capability bundles:
- "Collaboration: shared workspaces, comments, version history"
- "Analytics: custom dashboards, exports, scheduled reports"
- "Security: SSO, 2FA, audit logs"

Bundling reduces cognitive load. The brain sees 3 bundles, not 15 features.

---

## 5. THE FREE TIER DILEMMA

**If you offer Free:**
- Position it as a lead generation tool, not a real option. Make limitations clear.
- The primary CTA for free users should lead to upgrade, not to free signup.
- Use "Free forever" only if you mean it. "Free trial" is different.

**If you DON'T offer Free:**
- Offer a guarantee or trial INSTEAD. "Start your 14-day trial. No credit card."
- The guarantee IS your free tier - risk-free entry.

---

## 6. FAQ: PRICING OBJECTIONS

Address these ON the pricing page, below the tiers:

| Objection | Response Pattern |
|-----------|-----------------|
| "Why is this worth $X?" | ROI math. "$X saves you $Y/month in [cost/time]. Pays for itself in [timeframe]." |
| "Can I switch from [competitor]?" | Status Quo reassurance. "Import your data in 5 minutes. We handle the migration." |
| "What if I need to cancel?" | Risk reversal. "Cancel anytime. No questions. Pro-rated refunds." |
| "Do you offer discounts?" | "We offer annual billing at 20% off." (redirect to your preferred option) |
| "What's the difference between tiers?" | One-sentence comparison per tier. Not a feature matrix (save that for a comparison page). |

---

## 7. LOCALIZATION PSYCHOLOGY

Pricing that works in one market fails in another:

| Market | Price Expectation | Tactic |
|--------|-------------------|--------|
| US / Western | Round-ish ($97, $197, $497) | Charm for B2C, round for B2B |
| Japan | Precise (¥3,980, ¥9,800) | Exact numbers signal careful calculation |
| India | Round (₹499, ₹999) | Charm ending in 9, but round-ish |
| Germany | Round (€99, €199) | Precision signals quality. Odd numbers signal discount. |
| Brazil | Parcelamento (12× R$97) | Installments > total price. Show both. |

**Rule:** Never auto-convert prices. $99 → €89 is not a pricing strategy. Localize based on purchasing power, market expectations, and cultural price psychology.

---

## BIAS SEQUENCE FOR PRICING PAGE
```
Anchoring (pre-price value anchor)
 → Anchoring (three-tier: expensive first)
   → Halo Effect (visual differentiation of target tier)
     → Loss Aversion (annual savings framed as "don't overpay")
       → Status Quo (FAQ: migration is easy)
         → Risk Reversal (guarantee/trial)
           → Scarcity (if genuine: limited-time pricing, cohort capacity)
```

## PRICING PAGE AUDIT CHECKLIST
- [ ] Three tiers? (not 2, not 4+)
- [ ] Most expensive tier shown first?
- [ ] Target tier visually distinct (color, badge, size)?
- [ ] Annual savings shown as loss frame ("Don't pay $20 when you can pay $16")?
- [ ] Pre-price value anchor above the fold?
- [ ] ROI reframe somewhere on the page?
- [ ] FAQ addresses the top 3 objections?
- [ ] Guarantee specific (timeframe + how to claim)?
- [ ] No fake scarcity?
