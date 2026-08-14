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
3. Search the full repository for obsolete phone numbers, including `706-897-6177`, `850-348-5791`, alternate formatting, and stale `tel:` links.
4. Inventory every phone-number occurrence and classify it as current, obsolete, or historical/documentation-only.
5. Re-run the searches after edits to prove obsolete live-site references are gone or document that none existed.

## Out of scope
- Renaming website services.
- Redesigning pages.
- Changing prices.
- Adding or changing business policies.
- Editing Booksy, Facebook, Google Business Profile, or other external listings.
- Broad marketing-copy rewrites where the existing wording is subjective rather than incorrect.

## Verification
- Compare the development branch against `main` and confirm only intended copy/documentation changes were made.
- Search for all known old phone numbers and common numeric variants.
- Search for all `tel:` links and confirm they use `tel:+19805981864`.
- Check all edited HTML for valid surrounding markup and unchanged Booksy/service names.
