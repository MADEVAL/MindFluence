# Changelog

All notable changes to MindFluence are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Version normalized to three-part semver (2.3.0).
- Frontmatter normalized: environment-based `compatibility`, `metadata.author`.
- Reference files are read by relative path from the skill folder instead of GitHub URLs.
- Long dashes replaced with hyphens across all documentation.
- Section canon: added `WHEN NOT TO USE`, renamed the output section to `OUTPUT CONTRACT`.
- Canonical placeholder vocabulary documented: `[N]`, `[DATA NEEDED: ...]`, `[VERIFY: ...]`, `[Source, Year]`, `[illustrative]`.

## [2.3.0] - 2026-10-30

### Added

- **PROVENANCE / TRUTH GATE** as mandatory post-generation check #7: every number, name, quote, testimonial, study, journal, and year must be traceable to user input, a verifiable source, or an explicit placeholder.
- **Data provenance policy**: if data is missing, use placeholders (`[N]`, `[Customer name]`, `[Source, Year]`, `[measurable result]`) and a `[DATA NEEDED]` note, or ask the user in Deep Mode. Never invent specifics to satisfy a formatting check.
- **Two compliant narrative modes**: Mode A - real-data NPSA (full name + location/role + timeline + verbatim quote + visceral detail); Mode B - labeled `[illustrative]` first-person founder narrative or generalized vignette.
- `SECURITY.md` with vulnerability reporting guidance, scope, and supported versions.
- `CHANGELOG.md` (this file).
- Placeholder guidance in AP-1, AP-4, AP-13 and in the verification checks.
- `[DATA NEEDED]` blocks in STANDARD, EXTENDED, and Rewrite output formats.

### Changed

- Completed all 38 Bias Selection Router rows so each row covers Filter + Optimizer + Social categories.
- Post-generation verification expanded from 6 to 7 checks; output templates and all documentation now reference the 7-check gate.
- Narrative requirements now accept Mode A or Mode B; the verification check no longer forces a fabricated named person.
- AP-5 clarifies the cold-outreach exception: value and ask must be separated, and the value must be genuinely standalone.
- All inlined and external examples are now explicitly marked as illustrative; scenario-level AP-1/AP-4 guidance accepts placeholders when data is unavailable.
- README and README.ru updated for v2.3: 38-row router, 7 checks, provenance, two narrative modes, changelog/security links.

### Fixed

- `ANTI-PATTERNS (12)` heading corrected to 13; `anti-patterns.md` now includes AP-13 and an audit checklist covering all 13 anti-patterns plus provenance.
- `RskReversal` typo corrected to `RiskReversal` across the scenario table.
- Bias Blind Spot example no longer violates AP-10 (Insulting Confirmation).
- Unclear "Gilmore Girls" unexpected-detail example replaced with a generic niche-reference example.
- "4 Hofstede dimensions" wording corrected to Hofstede + Hall's high/low-context dimension.
- README claims about the router size (50 → 38), verification count (6 → 7), and anti-pattern count (12 → 13) corrected.
- README tree now includes `README.ru.md`, `CHANGELOG.md`, and `SECURITY.md`.
- OpenCode installation wording corrected: discovery is path-based, not frontmatter-based.

### Security

- Documented the security scope of a prompt-only skill, including prompt injection, fabricated citations, unsafe marketing use, and accidental secret exposure.
- Clarified that `_ship/` is local tooling and must remain out of version control.

## [2.2] - 2026-07-12

### Added

- Self-contained single-file architecture with inlined Bias Selection Router, Scenario Quick-Reference, Cultural Quick-Reference, 13 anti-patterns, 14 power combinations, and 7 tone styles.
- Named Person Story Arc (NPSA) narrative requirement with fallback patterns.
- Rewrite Without Metrics variant with 7 rewrite intents.
- 3-tier output format (COMPACT / STANDARD / EXTENDED) and 6-point post-generation verification.

### Changed

- Replaced the 10-step bias-selection procedure with a single router lookup.
- Added narrative minimums per tone and keyword density caps.

## [2.1] - 2026-07-12

### Added

- Production hardening: refusal policy, error handling, typo sweep, cultural depth.

## [2.0.2] - 2026-07-12

### Fixed

- Patch release after v2.0.1.

## [2.0.1] - 2026-07-12

### Fixed

- Patch release after v2.0.

## [2.0] - 2026-07-12

### Added

- Major rewrite of the skill structure, modes, and scenario coverage.

## [1.3] - 2026-06-25

### Added

- Production hardening: refusal policy, error handling, typo sweep, cultural depth.
- MIT license and repository cleanup completed in the preceding release cycle.
