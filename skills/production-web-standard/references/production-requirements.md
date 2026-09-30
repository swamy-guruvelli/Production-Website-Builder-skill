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

### Feedback and notifications

- Choose the feedback surface based on severity, persistence, and whether the user must act:
  - field-level validation belongs next to the affected field;
  - multiple form errors also need a summary that links to each affected field;
  - non-blocking success or status updates may use a short, dismissible toast or status region;
  - persistent or actionable errors belong inline or in a visible banner;
  - blocking or high-risk situations may require a dialog or full-page error state.
- Do not use a toast as the only location for a critical, persistent, or actionable error.
- Keep notifications concise, specific, and action-oriented. Avoid repeating the same information in the title and body.
- Non-critical notifications may dismiss automatically only when users do not need to act or refer back to them. Critical and actionable messages must remain available long enough to read and use.
- Make dynamic status updates programmatically determinable without stealing focus. Use polite status semantics for ordinary updates and reserve assertive alerts for important, time-sensitive problems.
- Notifications must be keyboard accessible, dismissible where appropriate, usable on small screens, and must not cover the control or content the user needs next. Respect reduced-motion preferences.
- Do not create a global toast system for a simple static site unless the site has interactions that benefit from it. Inline confirmation or a success page may be clearer for a contact form.

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

### Content and visual quality

- Design from the product, audience, subject matter, and existing brand rather than applying a generic visual or copy template.
- Treat words as part of the interface. Use specific, plain, active language that tells users what the product does or what an action will do.
- Taglines are optional. Use one only when it communicates a useful brand or product idea; never use a tagline to explain the prompt, design process, agent reasoning, component structure, or technical implementation.
- Headlines and section headings should be understandable when scanned alone, describe the content that follows, and avoid unsupported hype or stacked abstract nouns. Use a clear page heading and a meaningful semantic hierarchy; do not choose heading elements only for visual size.
- Keep repeated actions consistent across navigation, hero sections, forms, dialogs, and completion messages. A control and its result should use the same user vocabulary.
- Do not fabricate testimonials, customer logos, statistics, certifications, awards, guarantees, reviews, pricing, availability, or performance claims. Omit unsupported content or identify supplied placeholders clearly.
- Use a deliberate type scale, readable content width, responsive wrapping, and sufficient contrast. Do not force line breaks or visual treatments that fail on mobile, at increased text sizes, or with longer translated content.
- Preserve an existing brand voice and information architecture during a redesign unless the request explicitly includes a content or brand rewrite.

## Architecture and design system

- Reuse existing buttons, inputs, cards, modals, containers, navigation, tables, badges, loading/error/empty states, pagination, and search patterns.
- Keep components composable with clear responsibilities. Avoid both obvious repetition and speculative abstraction.
- Reuse or derive consistent tokens for typography, spacing, color, surfaces, borders, radii, shadows, widths, breakpoints, motion, icons, and z-index.
- Preserve existing project structure, libraries, routes, analytics hooks, and working behavior unless the requested change requires otherwise.

## Error disclosure and diagnostics

- Separate the user-facing error from the diagnostic record. Users should receive the minimum safe information needed to understand the problem and recover.
- For unexpected failures, show a short, contextual message, a safe next step, and a non-sensitive reference ID when support or an administrator may need to investigate. Do not display raw exception messages, stack traces, SQL, filesystem paths, framework details, secrets, tokens, request headers, or sensitive request data.
- Validation and business-rule errors may be specific when the user can safely correct them. Do not make every error vague when a clear, non-sensitive correction is available.
- Record full diagnostics in protected server-side logs or an authorized administrator/support surface. Enforce access server-side and use least-privilege roles; a hidden frontend control is not authorization.
- Redact passwords, session identifiers, access tokens, payment data, and unnecessary personal information from logs. Keep the public reference ID separate from internal database identifiers and exception details.
- Ensure production builds and default server configuration do not expose development error pages or debugging overlays. Test representative failure responses for information leakage.

## Accessibility

- Use semantic HTML, logical headings, correct button/link semantics, meaningful link text, labels, alternative text, table semantics, logical tab order, visible focus, and sufficient contrast.
- Provide keyboard operation and appropriate focus trapping, focus restoration, and Escape behavior for overlays.
- Announce dynamic status and validation messages accessibly. Use ARIA only where native semantics are insufficient.
- Respect reduced-motion preferences for nonessential motion.

## Performance

- Avoid obvious waste: oversized media, poor font loading, unnecessary hydration, duplicate requests, avoidable renders, needless client JavaScript, layout shift, and expensive work on hot paths.
- Apply image optimization, lazy loading, code splitting, caching, route-level loading, virtualization, and server/client boundaries only where beneficial.
- Do not add complexity to optimize trivial code without evidence.

## Resilience and recovery

- Handle request timeouts, cancellation, offline conditions, failed dependencies, expired sessions, partial responses, and server failures where they can occur.
- Preserve useful user-entered data after recoverable failures and prevent accidental duplicate submissions.
- Provide retry, undo, recovery, or a clear alternative path where appropriate. Do not blindly retry destructive or non-idempotent operations.
- Make unsaved changes and data-loss risks visible before navigation, reload, timeout, or destructive action when the product can detect them.

## Localization and content expansion

- Keep important text out of images and avoid layouts that depend on one exact string length.
- Test long headings, labels, names, validation messages, dates, currencies, time zones, and translated content when relevant.
- Support right-to-left layout and locale-specific formats when the audience or product requires them.

## Project decision records

- Inspect the project root for an existing `DECISIONS.md`, `ARCHITECTURE.md`, or ADR convention before making material technical choices.
- Create or update a root-level `DECISIONS.md` when a choice affects architecture, cost, security, data, maintenance, deployment, external services, or user-visible behavior, or when the user explicitly requests a decision record.
- Each entry should record the date, status, decision, source (`User-directed`, `Existing-project constraint`, or `Agent recommendation`), context, alternatives considered, rationale, consequences, and a condition that would justify revisiting it.
- Keep decision records concise and historical. Do not use them as a package inventory, task log, changelog, secrets file, or place to copy stack traces or private data.

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
