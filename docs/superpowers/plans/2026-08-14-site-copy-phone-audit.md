# Site Copy and Phone Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Correct objective copy errors across the BoPeeps site and verify that every website phone reference uses the current 980-598-1864 number.

**Architecture:** Keep the existing static-site structure intact. Make only localized text edits in existing HTML/docs, preserve all website service names and prices, and use repository-wide checks as the verification layer for phone-number consistency.

**Tech Stack:** Static HTML/CSS/JavaScript on GitHub Pages; GitHub repository content inspection and branch-based edits.

## Global Constraints

- Work only on `dev/site-cleanup-phone-audit` until explicit approval to merge/publish.
- The website service names are correct; do not rename them.
- Current phone: `980-598-1864`; schema form `+1-980-598-1864`; click-to-call form `tel:+19805981864`.
- Official business styling: `BoPeeps Details & More`.
- Do not invent policies, prices, testimonials, or marketing claims.

---

### Task 1: Repository-wide wording audit

**Files:**
- Inspect all `.html`, `.md`, `.js`, and `.css` text-bearing files.
- Modify only files containing objective copy errors.

- [ ] Search for the incorrect possessive plural of RV, inconsistent BoPeeps spellings, obvious punctuation/grammar errors, stale wording, and accidental repeated phrases.
- [ ] Review each match in context and distinguish objective errors from intentional brand/service wording.
- [ ] Apply minimal corrections without renaming services or changing prices.
- [ ] Re-read changed sentences in context.

### Task 2: Phone-number and `tel:` audit

**Files:**
- Inspect the entire repository, including docs, tests, and metadata-bearing HTML.

- [ ] Search for both known former phone-number families, including dashed, digits-only, `+1`, and `tel:` variants, without preserving the obsolete full numbers as repository literals.
- [ ] Search for every phone-like string and every `tel:` URI.
- [ ] Classify matches as current, obsolete live-site, or historical documentation.
- [ ] Remove obsolete references from the current repository and replace customer-facing occurrences with the current number if any are found.
- [ ] Confirm every live click-to-call link is exactly `tel:+19805981864`.

### Task 3: Verification

**Files:**
- Verify production pages, repository documentation, and regression tests.

- [ ] Re-run former-number checks and confirm zero obsolete current-tree matches.
- [ ] Re-run `tel:` checks and verify live customer pages use only the current number.
- [ ] Search service headings to confirm website package names were not changed.
- [ ] Compare development branch changes against `main` and confirm scope is limited to copy, documentation, and audit-test work.
- [ ] Record a concise audit result for review before any merge to `main`.
