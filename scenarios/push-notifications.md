# Scenario: Push Notifications & SMS

## CONTEXT
Mobile push notifications and SMS messages — the highest-interruption marketing format. The user didn't open your app or website. You're appearing on their lock screen, competing with messages from friends, family, and work.

## GOAL
Earn the open without triggering the "mute notifications" reflex. Push is permission-based by nature — the user opted in. Break that trust once, and you're muted forever.

---

## THE PUSH PARADOX

Push notifications have the highest open rates (30–60%) and the highest unsubscribe rates of any channel. Every message is a withdrawal from a trust account. The deposit was made at opt-in. Every irrelevant notification is an overdraft.

**The rule:** Each push must pass the "lock screen test" — if the user saw ONLY your notification among 12 others, would they feel glad they allowed it, or would they swipe to mute?

---

## STRUCTURE (50–120 characters visible, 3 lines max on lock screen)

```
Line 1: TITLE — the hook. Fits in one lock-screen line (~35 chars). Not truncated.
Line 2: BODY — the value. What they get by tapping. One sentence.
Line 3: (Hidden — visible on 3D Touch / long press, or in notification center)
```

SMS has more room (160 characters) but the same psychological constraints apply. No images, no formatting, no links that auto-preview. Pure text in an intimate channel.

---

## BIAS MAP BY PUSH TYPE

### 1. Transactional Push ("Your order shipped")

```
[STATUS QUO] Reinforce that everything is as expected.
[ENDOWMENT] "Your [item] is on the way." — it's already theirs.
```

**Example:**
> 🚀 Your [Product] is on the way
> Track your package → arriving Thursday

**Rules:**
- No marketing in transactional pushes. These are trust maintenance, not conversion.
- If you must cross-sell, add it after the transactional info as a soft suffix: "Your order shipped. While you wait — 20% off accessories in the app."

---

### 2. Re-engagement Push ("We miss you")

```
[LOSS AVERSION] They're missing something.
[IN-GROUP] They're absent from the community.
[SUNK COST] They've built something — it's still there.
```

**Pattern:** "Your [streak/balance/progress] is about to reset" or "[Name], the community noticed you're gone."

**Example:**
> 🔥 Your 47-day streak ends tomorrow
> 3 minutes to keep it alive

**Rules:**
- Must reference something SPECIFIC the user built or earned. Generic "We miss you" is instant mute.
- Frequency cap: max 1 re-engagement push per 10 days of inactivity. After 30 days of silence, stop entirely.

---

### 3. Time-Sensitive Offer Push

```
[LOSS AVERSION] + [SCARCITY] Compressed into 50 characters.
[ANCHORING] Price contrast in minimal words.
[RISK REVERSAL] One word: "Free" or "Guaranteed."
```

**Pattern:** "[Specific benefit] expires in [time] — [action]"

**Example:**
> ⏳ Your 30% off expires in 4 hours
> Tap to claim → no code needed

**Rules:**
- Scarcity must be GENUINE (see anti-pattern #6). Push notifications with fake timers are the fastest path to uninstall.
- Max 2 time-sensitive pushes per month. Beyond that, every push is "urgent," so none are.

---

### 4. Content/Value Push ("New post / episode / feature you'll want")

```
[AVAILABILITY] Concrete, specific curiosity gap.
[CONFIRMATION] Validate something they already suspect.
[FRAMING] Not "we published" — "here's what you'll gain."
```

**Example (bad):**
> 📝 New blog post: 10 Tips for Better Sleep

**Example (good):**
> 😴 The sleep tip your tracker won't tell you
> It's not about hours. It's about this 90-second ritual.

**Rules:**
- The title must create a curiosity gap the lock-screen reader can't resist.
- Never use "New post," "Just published," "Check out our." That's your content calendar, not their problem.

---

### 5. Social/Community Push

```
[SOCIAL PROOF] Someone did something relevant to YOU.
[FALSE CONSENSUS] "People like you are..."
[IN-GROUP] Shared experience in the notification.
```

**Example:**
> 👋 3 people from [Your Company] just joined
> [Name], [Name], and [Name] are already inside

**Rules:**
- Social proof in push must be SPECIFIC — names, numbers, roles. "Someone liked your post" is lazy. "Sarah Chen, VP Ops at Merge, commented on your thread" is not.
- Frequency cap: max 1 social push per day. Social noise is the #1 notification mute reason.

---

### 6. SMS-Specific Rules

SMS is higher trust AND higher intrusion than push. A text message competes with mom, partner, boss.

**Structure (160 chars):**
```
[Personalization] — [Value in 8 words or fewer] — [Link (short)] — [Opt-out]
```

**Example:**
> Alex: Your free trial ends Thursday. Tap to keep everything you built → [short.link] Reply STOP to opt out.

**Non-negotiable rules:**
- Always include opt-out.
- Always personalize (name or context-specific reference).
- Max 2 SMS per month for marketing. Transactional SMS (codes, receipts) don't count toward this limit.
- Never send SMS outside business hours in the recipient's timezone.

---

## ANTI-PATTERNS SPECIFIC TO PUSH

### Push AP-1: The Notification That Lies
**What happens:** "You have a new message!" → Tap → "Check out our holiday sale!"
**Why it fails:** This is a trust violation. The user granted notification permission for specific value. Using that permission for bait-and-switch burns the channel permanently.
**Fix:** The notification preview must accurately represent what's on the other side of the tap. Always.

### Push AP-2: The 6 AM Buzz
**What happens:** Marketing push at 6:03 AM local time.
**Why it fails:** Waking someone up with marketing is the fastest path to uninstall. The notification wasn't checked — it was swiped away in anger.
**Fix:** Respect quiet hours. Marketing pushes: 10 AM – 8 PM local time. Transactional and critical alerts only outside that window.

### Push AP-3: The Emoji Dump
**What happens:** "🔥🔥 DON'T MISS OUT!!! 🚀🚀🚀 LIMITED TIME!!! 💯💯"
**Why it fails:** Looks like spam. The lock screen is intimate. Screaming in someone's pocket is not marketing — it's harassment.
**Fix:** Max 1 emoji per push. Zero in SMS. Let the words do the work.

### Push AP-4: Frequency Insanity
**What happens:** 3+ pushes per day.
**Why it fails:** Users don't read push #3. They mute the app. Push #1 and #2 are now also dead.
**Fix:** Aggregate. If you have 3 things to say, send 1 push with the most important thing. The rest goes to the in-app inbox.

---

## PUSH BIAS STACKS (Quick Reference)

| Push Type | Bias Stack | Max Length | Max Frequency |
|-----------|-----------|------------|---------------|
| Transactional | Status Quo + Endowment | 120 chars | As needed |
| Re-engagement | Loss Aversion + In-Group + Sunk Cost | 100 chars | 1 per 10 inactive days |
| Time-sensitive offer | Loss Aversion + Scarcity + Anchoring + Risk Reversal | 120 chars | 2 per month |
| Content/value | Availability + Confirmation + Framing | 120 chars | 1 per day |
| Social/community | Social Proof + False Consensus + In-Group | 120 chars | 1 per day |
| SMS marketing | Reciprocity + Loss Aversion + Risk Reversal | 160 chars | 2 per month |
| SMS transactional | Status Quo | 160 chars | As needed |

---

## DEFAULT CULTURAL ADAPTATION FOR PUSH

Push notifications are the most culturally sensitive format because they appear in the user's most personal space — their lock screen or SMS inbox. Adjust per `cultural-matrix.md`:

- **High Power Distance:** Authority signals in push (certified by, official, approved) increase trust. "From your [industry body]" in the sender name.
- **Collectivist:** Group framing in re-engagement pushes: "Your team is waiting" > "We miss you."
- **High Uncertainty Avoidance:** Risk Reversal must be explicit even in 50 characters: "Free to try. Cancel anytime."
- **High Context:** Curiosity gaps must be culturally resonant — what's intriguing in the US may be confusing in Japan. Test with a native speaker.
