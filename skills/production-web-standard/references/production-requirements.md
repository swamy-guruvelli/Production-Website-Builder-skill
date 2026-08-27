# Production Requirements

Apply these requirements according to the product and affected surface. They define outcomes; specialized skills own stack-specific implementation.

## Responsive behavior

- Use mobile-first or appropriately adaptive layouts.
- Prevent unintended page-level horizontal scrolling.
- Make navigation, sidebars, grids, cards, forms, tables, modals, charts, media, sticky elements, typography, spacing, and touch targets usable at narrow and wide widths.
- Prefer reusable layout primitives and natural reflow over separate implementations for each screen size.
- Handle overflow intentionally. Tables may scroll, stack, or condense depending on their content and use.

## Interactions and application states

- Implement buttons, links, navigation, menus, tabs, dialogs, drawers, search, filters, sorting, pagination, form controls, CRUD actions, uploads/downloads, copy controls, tooltips, profile controls, themes, and notifications when they are visible.
- Provide appropriate hover, focus, active, selected, disabled, loading, success, and error feedback.
- Cover relevant initial, loading, skeleton, empty, success, validation, failure, unauthorized, permission-denied, offline, not-found, server-failure, partial-data, and retry states.
- Make destructive actions deliberate and recoverable where practical. Do not blindly retry destructive operations.

## Forms

- Use semantic labels, required indicators, correct input types, autocomplete, keyboard support, and accessible validation messages.
- Choose clear validation timing and preserve useful entered values after recoverable errors.
- Prevent duplicate submissions and show submitting, success, and failure states.
- Validate on the server whenever a backend exists. Sanitize or encode untrusted data according to its destination.

## Site completeness

- Add the application shell appropriate to the requested product: header, navigation, footer, current-year copyright, branding, favicon, titles, descriptions, responsive navigation, skip navigation, breadcrumbs, and legal links where they provide real value.
- Public production sites should receive appropriate canonical URLs, Open Graph/social metadata, robots directives, sitemap, useful URL structure, internal links, semantic headings, and structured data when strongly relevant.
- Provide useful 404, error, loading, and empty states.
- Use real, context-appropriate content. Do not pad pages with generic sections.

## Architecture and design system

- Reuse existing buttons, inputs, cards, modals, containers, navigation, tables, badges, loading/error/empty states, pagination, and search patterns.
- Keep components composable with clear responsibilities. Avoid both obvious repetition and speculative abstraction.
- Reuse or derive consistent tokens for typography, spacing, color, surfaces, borders, radii, shadows, widths, breakpoints, motion, icons, and z-index.
- Preserve existing project structure, libraries, routes, analytics hooks, and working behavior unless the requested change requires otherwise.

## Accessibility

- Use semantic HTML, logical headings, correct button/link semantics, meaningful link text, labels, alternative text, table semantics, logical tab order, visible focus, and sufficient contrast.
- Provide keyboard operation and appropriate focus trapping, focus restoration, and Escape behavior for overlays.
- Announce dynamic status and validation messages accessibly. Use ARIA only where native semantics are insufficient.
- Respect reduced-motion preferences for nonessential motion.

## Performance

- Avoid obvious waste: oversized media, poor font loading, unnecessary hydration, duplicate requests, avoidable renders, needless client JavaScript, layout shift, and expensive work on hot paths.
- Apply image optimization, lazy loading, code splitting, caching, route-level loading, virtualization, and server/client boundaries only where beneficial.
- Do not add complexity to optimize trivial code without evidence.

## Security and permissions

Load a security skill when the work includes authentication, authorization, APIs, persistence, user content, uploads, cookies, sessions, secrets, payments, personal data, admin functions, webhooks, or third-party integrations.

- Never expose secrets in client code or logs.
- Enforce authorization and ownership on the server, not only through hidden UI.
- Protect against injection, XSS, unsafe HTML, CSRF where applicable, unsafe redirects, insecure uploads/cookies, broken access control, IDOR, excessive data exposure, and sensitive error leakage.
- Handle signed-in, signed-out, loading, expired-session, unauthorized, and logout states. Do not reveal protected content before authorization resolves.
- Use established framework/platform mechanisms; never invent cryptography.

## APIs and data

- Validate input and authorization server-side; return consistent, non-sensitive errors and meaningful status codes.
- Handle malformed responses, cancellation when useful, duplicate submission, and conservative retries.
- Use appropriate constraints, migrations, indexes, transactions, and referential integrity when persistence exists.
- Handle missing and unique records, avoid unjustified N+1 queries, and never trust client-supplied ownership or permission fields.
