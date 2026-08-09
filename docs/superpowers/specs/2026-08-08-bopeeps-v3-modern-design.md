# BoPeeps v3 Modern Website Design

## Goal

Build a launch-ready, mobile-first website for **BoPeeps Details & More** that keeps the approved modern black/red detailing aesthetic, uses Booksy for booking, highlights real customer work, and remains fast and simple on phones.

## Approved visual direction

- Dark black/charcoal background with strong red accents and white text.
- Clean modern detailing look rather than a busy tuner/performance-car theme.
- Customer-facing brand name: **BoPeeps Details & More**.
- Large detailing hero image, bold headline, Booksy-first CTA, secondary phone CTA.
- Compact trust/value strip beneath the hero.
- Service cards for the three current Booksy services.
- A compact location/map card next to the business address in the contact area.
- Mobile layout is the primary design target; desktop expands the same structure rather than becoming a separate experience.

## Launch content

### Business information

- Name: **BoPeeps Details & More**
- Phone: **706-897-6177**
- Email: **hello@bopeepsdetails.com**
- Address: **1516 US-64, Hayesville, NC 28904**
- Hours: **Monday-Saturday 7:00 AM-5:00 PM; Sunday closed**
- Facebook: `https://www.facebook.com/people/BoPeeps-Detail/61591634832181/`
- Booksy: `https://booksy.com/en-us/1808686_bopeeps-detail-more_other_26564_hayesville`

### Service cards

1. **Express Wash And Spray Wax** — from **$60+** — approximately **1 hour**.
2. **Deluxe Detail Package** — from **$85+** — approximately **2 hours**.
3. **Jacky Jones Premium Detail** — from **$150+** — approximately **4 hours**.

Each service card links to the public BoPeeps Booksy profile. The site must not imply that Booksy supports stable service-specific deep links.

## Page structure

### 1. Header

- Logo/brand at left.
- Desktop nav: Home, Services, Gallery, About, Contact.
- Primary **Book on Booksy** button.
- Mobile hamburger menu with large tap targets.

### 2. Hero

- Real BoPeeps vehicle/detailing photo.
- Headline: **Detailing Done Right.**
- Supporting line: **Cleaner. Shinier. Protected.**
- Short description focused on professional interior/exterior detailing.
- Primary CTA: **Book on Booksy**.
- Secondary CTA: **Call 706-897-6177**.

### 3. Trust strip

Four compact points:

- Quality products
- Attention to detail
- Reliable service
- Customer first

On mobile these stack vertically or become a compact two-column layout depending on width.

### 4. Services

- Three visually consistent service cards.
- Each card includes image, service name, starting price, estimated duration, short description, and Booksy CTA.
- On narrow screens cards are swipeable horizontally with scroll-snap, while remaining keyboard accessible.
- Below cards: **View all services & pricing on Booksy**.

### 5. Interactive work section

Use real BoPeeps work, not generic stock content.

Primary interaction:

- A touch/mouse **clean-reveal** experience where a simulated haze/grime layer is wiped away to reveal a finished vehicle photo.
- The simulated layer must be clearly presented as an interaction, not a factual before photo.
- After sufficient reveal, show a subtle shine sweep and CTA to book.

Secondary content:

- Genuine before/after photo pair(s) when matching real images are available.
- Lightweight gallery using approximately 6-8 optimized images on the homepage.
- Link to Facebook for more work.

### 6. Why choose BoPeeps

Four concise benefits:

- Quality work
- All vehicles
- Satisfaction-focused
- Local & trusted

Avoid unverifiable superlatives or fabricated review counts.

### 7. Contact/location

- Phone, email, address, and hours.
- Small live map/embed or lightweight map card beside the address on desktop and immediately below it on mobile.
- Map opens directions for **1516 US-64, Hayesville, NC 28904**.
- Facebook link.

### 8. Mobile sticky actions

On phones, provide a compact bottom action bar:

- Call
- Directions
- Book

It must not cover page content and must respect device safe-area insets.

## Sound

- No autoplay sound.
- Optional sound control may be included for the clean-reveal interaction.
- Sound can only begin after explicit user interaction.
- If audio is unavailable or blocked, the interaction remains fully functional without it.
- Sound is secondary to launch readiness and must not delay the core site.

## Technical approach

- Static HTML, CSS, and vanilla JavaScript suitable for GitHub Pages.
- No backend required for v1.
- Booksy handles booking.
- GitHub Pages remains on the temporary GitHub URL during development; `bopeepsdetails.com` is connected only after approval.
- Preserve `main` and existing preview implementations unchanged while building on branch **`bopeeps-v3-modern`**.
- Public repository must contain no passwords, private API keys, mail credentials, Porkbun credentials, or Booksy account credentials.

## Asset strategy

- Reuse approved BoPeeps logo assets already present in the repository when appropriate.
- Select launch imagery from the uploaded Bopeeps photo set, prioritizing real finished work and real before/after content.
- Optimize images for mobile delivery, target modern formats where practical, and avoid loading all source images on the homepage.
- Include explicit width/height or aspect-ratio handling to reduce layout shift.

## Accessibility and UX

- Minimum comfortable touch targets on mobile.
- Visible keyboard focus states.
- Semantic headings and landmarks.
- Descriptive alt text for meaningful images.
- Respect `prefers-reduced-motion` for reveal animations and shine effects.
- Maintain readable contrast throughout the black/red theme.
- Booksy, phone, email, Facebook, and directions links must work without JavaScript.

## SEO/local metadata

- Page title and description use **BoPeeps Details & More** and Hayesville, NC.
- LocalBusiness/AutomotiveBusiness structured data contains the confirmed 706 phone number, public email, address, and hours.
- Remove outdated 828-number artwork references from text metadata and remove the older 706/828 inconsistencies from the new branch implementation.
- Use a canonical URL only when the custom domain is ready for go-live.

## Launch acceptance criteria

The v3 branch is ready for domain cutover when:

1. The homepage closely matches the approved black/red modern mockup.
2. Mobile widths from roughly 320px upward are usable without horizontal page overflow.
3. Every Book button reaches the correct BoPeeps Booksy profile.
4. Phone links use **706-897-6177**.
5. Public email is **hello@bopeepsdetails.com**.
6. Address and hours match the confirmed business information.
7. Service prices match the currently confirmed Booksy prices.
8. Map/directions points to the confirmed Hayesville address.
9. The interactive clean-reveal works with touch and mouse and degrades gracefully.
10. No secrets or credentials are present in the repository.
11. Existing `main` and `hybrid-preview` versions are preserved until the new version is explicitly approved.
12. Final domain/DNS changes happen only after visual and functional approval.
