# Site Copy and Phone Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Correct objective copy errors across the BoPeeps site and verify that every website phone reference uses the current 980-598-1864 number.

**Architecture:** Keep the existing static-site structure intact. Make only localized text edits in existing HTML/docs, preserve all website service names and prices, and use repository-wide searches as the verification layer for phone-number consistency.

**Tech Stack:** Static HTML/CSS/JavaScript on GitHub Pages; GitHub repository content search and branch-based edits.

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

- [ ] Search for `RV's`, inconsistent BoPeeps spellings, obvious punctuation/grammar errors, stale wording, and accidental repeated phrases.
- [ ] Review each match in context and distinguish objective errors from intentional brand/service wording.
- [ ] Apply minimal corrections without renaming services or changing prices.
- [ ] Re-read changed sentences in context.

### Task 2: Phone-number and `tel:` audit

**Files:**
- Inspect the entire repository, including docs and metadata-bearing HTML.

- [ ] Search for `706-897-6177`, `7068976177`, `850-348-5791`, `8503485791`, and common `+1` variants.
- [ ] Search for every phone-like string and every `tel:` URI.
- [ ] Classify matches as current, obsolete live-site, or historical documentation.
- [ ] Replace obsolete live-site references with the current number if any exist.
- [ ] Confirm every live click-to-call link is exactly `tel:+19805981864`.

### Task 3: Verification

**Files:**
- No new production files expected.

- [ ] Re-run old-number searches and confirm zero obsolete live-site matches.
- [ ] Re-run `tel:` search and verify only the current number is used.
- [ ] Search service headings to confirm website package names were not changed.
- [ ] Compare development branch changes against `main` and confirm scope is limited to copy/audit work.
- [ ] Record a concise audit result for review before any merge to `main`.
