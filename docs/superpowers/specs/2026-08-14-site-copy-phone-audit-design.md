# Site Copy and Phone Audit Design

## Goal
Clean up indisputable wording inconsistencies across the BoPeeps website and prove whether any obsolete phone numbers or `tel:` links remain in the repository.

## Source of truth
- The website service names are correct and must not be renamed in this pass.
- Booksy will be updated separately to match the website.
- Current public phone number: `980-598-1864` / `+1-980-598-1864` / `tel:+19805981864`.
- Official business name styling: `BoPeeps Details & More`.

## Scope
1. Fix clear grammar, punctuation, capitalization, and wording mistakes without changing service/package naming or pricing.
2. Normalize obvious BoPeeps naming inconsistencies where they refer to the business itself.
3. Search the full repository for the former 706-area-code number, the former 850-area-code number, alternate formatting, and stale `tel:` links.
4. Inventory every phone-number occurrence and classify it as current, obsolete, or historical/documentation-only.
5. Remove obsolete contact strings from the current repository and re-run the audit so historical documentation cannot reintroduce stale business facts.

## Out of scope
- Renaming website services.
- Redesigning pages.
- Changing prices.
- Adding or changing business policies.
- Editing Booksy, Facebook, Google Business Profile, or other external listings.
- Broad marketing-copy rewrites where the existing wording is subjective rather than incorrect.

## Verification
- Compare the development branch against `main` and confirm only intended copy/documentation/test changes were made.
- Search for all known former phone-number families and common numeric variants without retaining the obsolete full numbers as repository literals.
- Search for all `tel:` links and confirm live customer pages use `tel:+19805981864`.
- Check all edited HTML for valid surrounding markup and unchanged website service names/prices.
