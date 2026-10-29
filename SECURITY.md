# Security Policy

MindFluence is a prompt-only skill. It does not execute code, collect analytics,
or store user data. The security surface is therefore mostly about **what the
model is instructed to generate** and **how the repository is handled**.

## Supported versions

| Version | Supported |
|---------|-----------|
| 2.3.x   | Yes       |
| 2.2.x   | Security fixes only |
| < 2.2   | No        |

## Reporting a vulnerability

Please do **not** open a public issue for a security problem.

Use GitHub's private vulnerability reporting:

1. Open the repository's **Security** tab.
2. Select **Report a vulnerability**.
3. Include the affected version, the prompt or file, the expected behavior, and
   the observed behavior.

If private reporting is unavailable, open a regular issue that says only
"security report — please contact me privately" and wait for a maintainer to
respond. Do not include exploit details, secrets, or personal data in a public
issue.

## What is in scope

- **Prompt injection / instruction bypass** that makes the skill ignore its
  refusal policy, ethical boundaries, or provenance gate.
- **Fabricated evidence** produced by the skill's own instructions — for example,
  a check that rewards invented numbers, names, testimonials, studies, journals,
  or years.
- **Unsafe marketing guidance** that violates the refusal policy (tobacco,
  gambling, weapons, minors, fraudulent health claims, MLM, hate, exploitation
  of vulnerable groups).
- **Secret exposure** in the repository, examples, logs, or local tooling.
- **Supply-chain risks** in scripts used to build, test, or ship the skill.

## What is out of scope

- The truthfulness of third-party statistics or quotes that a user supplies.
- Marketing performance claims (conversion rates, CTR, revenue) — this skill
  does not guarantee outcomes.
- Legal or regulatory compliance in a specific jurisdiction. Users are
  responsible for verifying claims, disclosures, and consent requirements.
- Vulnerabilities in third-party LLM providers or agent platforms.

## Security expectations for users

- Treat every generated name, number, quote, and citation as **unverified**
  until you check it.
- Keep placeholders such as `[N]`, `[Customer name]`, and `[Source, Year]` in
  drafts until real data is available.
- Never paste secrets, API keys, or personal data into a prompt.
- Do not use the skill to fabricate testimonials, scarcity, authority, or
  health claims. The skill's ethical boundaries prohibit this, and the
  provenance gate is designed to catch it.

## Repository handling

- `_ship/` is local release automation and is intentionally ignored by git.
  It must never be committed. It can read a GitHub token from the local
  credential store; treat any machine that runs it as a trusted environment.
- Do not commit `.env` files, tokens, customer data, or private prompt logs.
- If a secret is committed, rotate it immediately and remove it from git
  history before publishing.

## Disclosure policy

We aim to acknowledge reports within 7 days and to publish a fix or mitigation
within 30 days for confirmed issues. Credit is given to reporters unless they
prefer to remain anonymous.
