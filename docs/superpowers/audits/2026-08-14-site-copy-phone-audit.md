# Site Copy and Phone Audit Results

## Scope
This audit covers the current tree of `dev/site-cleanup-phone-audit`. It does not rewrite historical Git commits.

## Website source of truth
- Business name: `BoPeeps Details & More`
- Public phone: `980-598-1864`
- Schema phone: `+1-980-598-1864`
- Click-to-call: `tel:+19805981864`
- Website service names remain unchanged:
  - `Vacuum, Hand Wash & Wax`
  - `Deluxe Detail Package`
  - `BoPeeps Signature Detail`
- Booksy is the booking destination and is to be updated separately to match the website service names.

## Copy corrections made
- Corrected the RV plural on the homepage scrub selector.
- Replaced wording that incorrectly described Booksy as the source of the website service menu.
- Replaced generic `Basic` package references with wording aligned to the website's actual first service.
- Corrected one homepage punctuation issue.
- Narrowed Policies metadata/intro wording so it describes the pricing and vehicle-condition policy actually present on the page.
- Removed an outdated README note about a future DNS cutover.
- Updated historical SEO design/plan documents so they no longer contain obsolete phone or retired service facts.

## Phone audit result
- Customer-facing pages inspected use the current 980 phone and `tel:+19805981864`.
- Former phone-number literals were found in historical SEO documentation and an older regression-test implementation, not in the active customer-facing pages inspected.
- Those obsolete literals were removed from the current branch tree.
- The regression test now constructs known former-number variants from separated number parts and checks text-bearing repository files recursively, so future stale-number reintroduction can be detected without preserving the obsolete full numbers as literals.

## Verification status
- GitHub branch comparison confirms the development branch is ahead-only from `main` and changes are limited to copy, documentation, and regression-test files.
- `main`, CNAME, images, CSS, JavaScript, pricing, and external-service configuration were not changed in this pass.
- Automated pytest execution has not been completed in this connector session because the environment could not clone/materialize the exact repository branch with binary assets. Do not record the suite as passing until it is executed against the branch.
