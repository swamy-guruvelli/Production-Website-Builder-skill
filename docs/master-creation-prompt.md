Create a reusable **Production Website Builder skill system** for building complete, production-ready websites and web applications end-to-end.

The objective is that when I say something simple such as:

> "Build this website."

the agent should automatically understand that I expect a complete, responsive, functional, polished website without requiring me to separately request mobile responsiveness, working buttons, loading states, footer copyright, accessibility, metadata, validation, error handling, testing, security checks, or other standard production requirements.

# Core architecture

Use a layered skill architecture.

Do **not** put every implementation rule into one enormous skill.

Create one custom top-level orchestration/quality skill:

`production-web-standard`

This skill should define the **Definition of Done**, production expectations, completion criteria, and skill-routing behavior.

Then use specialized skills for implementation:

- `frontend-app-builder`
- `frontend-testing-debugging`
- `security-best-practices`
- framework-specific best-practices skill
- deployment skill when relevant

The architecture should be:

`User request`
→ `production-web-standard`
→ project/framework detection
→ `frontend-app-builder`
→ framework-specific skill
→ backend/security/data skills where relevant
→ `frontend-testing-debugging`
→ deployment skill only when requested/relevant

The top-level skill should **coordinate and enforce standards**, not duplicate hundreds of framework-specific implementation instructions.

Specialized skills should remain independently maintainable.

If an official, installed, or higher-quality equivalent of a specialized skill already exists, use it instead of creating a duplicate.

---

# 1. Create the primary skill

Create:

`production-web-standard`

Its purpose is:

> Establish the universal production Definition of Done for website and web-application work and automatically route work to the appropriate implementation, testing, security, framework, and deployment skills.

It should automatically apply whenever creating, modifying, redesigning, extending, reviewing, or debugging a web application unless I explicitly request a prototype, mockup, experiment, proof of concept, or intentionally incomplete implementation.

This skill should enforce the requirements below.

---

# Responsive design

Every website must work properly across:

- Mobile phones
- Tablets
- Laptops
- Desktop displays
- Large displays

Do not require me to specify individual responsive behavior for every component.

Automatically determine sensible responsive behavior based on the component and context.

Requirements:

- Mobile-first or appropriately adaptive layouts
- No unintended horizontal scrolling
- Navigation collapses appropriately
- Grids automatically adjust column count
- Cards resize/reflow naturally
- Forms remain usable on small screens
- Tables become scrollable, stacked, condensed, or otherwise usable
- Modals fit within small screens
- Images and media remain within their containers
- Typography scales sensibly
- Spacing remains balanced
- Touch targets remain usable
- Sticky/fixed elements must not block important content
- Sidebars adapt appropriately
- Dashboards remain usable on smaller screens
- Charts resize correctly
- Overflow is handled intentionally
- Test representative viewport sizes before completion

Do not create separate implementations for every screen size unless technically necessary.

Prefer reusable layout primitives and responsive components.

---

# Complete interaction behavior

Every visible interactive element must actually work.

This includes:

- Buttons
- Links
- Menus
- Dropdowns
- Tabs
- Accordions
- Modals
- Drawers
- Search
- Filters
- Pagination
- Sort controls
- Forms
- Checkboxes
- Radio buttons
- Toggles
- Sliders
- Date pickers
- Navigation
- Breadcrumbs
- Authentication controls
- CRUD actions
- Download controls
- Upload controls
- Copy buttons
- Tooltips
- Context menus
- User profile controls
- Command palettes
- Theme controls
- Notification controls

Never create a control that visually appears interactive but has no meaningful behavior unless explicitly requested as a visual-only mockup.

Automatically implement appropriate:

- Hover states
- Focus states
- Active states
- Selected states
- Disabled states
- Loading states
- Success feedback
- Error feedback

---

# Application states

For every relevant feature automatically account for:

- Initial state
- Loading state
- Skeleton state where appropriate
- Empty state
- Success state
- Error state
- Validation state
- Disabled state
- Unauthorized state
- Permission-denied state
- Offline/network failure where relevant
- Not-found/404 state
- Server/API failure where relevant
- Partial-data state where relevant
- Retry behavior where appropriate

Do not only implement the happy path.

---

# Forms

Forms must automatically include appropriate:

- Labels
- Validation
- Error messages
- Required indicators
- Correct input types
- Loading/submitting state
- Success feedback
- Disabled submit handling
- Duplicate submission prevention
- Accessible error messaging
- Keyboard usability
- Sensible autocomplete attributes
- Server-side validation when backend functionality exists
- Input sanitization where appropriate
- Clear validation timing
- Error recovery
- Preservation of useful user-entered values after recoverable errors

Do not require me to specify these individually.

---

# Feedback, notifications, and error disclosure

Choose the feedback surface based on the severity of the problem, whether it persists, and whether the user must act.

- Show field validation beside the affected field.
- For multiple form errors, show a linked error summary as well as the individual field messages.
- Use short, non-blocking toasts or polite status messages for ordinary success and status updates.
- Keep persistent or actionable errors visible in the relevant page or section.
- Use a banner, dialog, or full-page state for critical or blocking situations.
- Do not use a disappearing toast as the only way to communicate a critical or actionable error.
- Keep dynamic messages keyboard accessible, screen-reader discoverable, dismissible where appropriate, usable on small screens, and respectful of reduced motion.

Separate user-facing messages from internal diagnostics:

- Give users a short, contextual explanation, a useful next step, and a safe reference ID when support may need to investigate.
- Never expose stack traces, raw exception messages, SQL, filesystem paths, tokens, secrets, framework internals, request headers, or sensitive request data in production interfaces.
- Record full diagnostics in protected server-side logs or an authorized admin/support surface.
- Enforce access to diagnostic details server-side and use least-privilege roles.
- Redact passwords, session identifiers, access tokens, payment data, and unnecessary personal information from logs.

---

# Site completeness

Automatically add reasonable surrounding website requirements where appropriate.

Examples:

- Header
- Navigation
- Footer
- Current-year copyright
- Logo treatment
- Favicon
- Page titles
- Meta descriptions
- Open Graph metadata
- Social sharing metadata
- Robots directives where relevant
- Canonical URLs where relevant
- Sitemap for public production websites
- 404 page
- Error page
- Loading UI
- Empty states
- Basic SEO
- Responsive navigation
- Accessible skip navigation when useful
- Consistent application shell
- Breadcrumbs where appropriate
- Legal/footer navigation where appropriate

Do not add meaningless generic sections just to make a page longer.

Do not fill pages with generic placeholder text.

Do not leave:

- Lorem ipsum
- Dead buttons
- Empty routes
- TODO labels
- Placeholder cards
- Fake links
- Unimplemented primary actions
- Dummy forms
- Fake filters
- Fake pagination

unless I explicitly request placeholders.

---

# Content, visual, and trust quality

Treat copy and layout as part of product quality, not decoration.

- Taglines are optional. Use one only when it communicates a useful product or brand idea.
- Never expose prompts, agent reasoning, design-process notes, component structure, or implementation terminology in user-facing copy.
- Make headings specific, useful when scanned alone, and semantically structured.
- Do not make a split section header the default. Use a two-column header only when both columns contain meaningful content and have adequate readable measure.
- Give the primary heading enough width to express itself naturally. Do not squeeze it into a narrow half-column merely to create symmetry or force a two-line treatment.
- Use a deliberate type scale, readable content width, responsive wrapping, and sufficient contrast.
- Use real, supportable content. Do not fabricate testimonials, logos, statistics, certifications, awards, reviews, guarantees, pricing, availability, or performance claims.
- Preserve an existing brand voice and information architecture during redesign unless a content or brand rewrite is requested.

---

# Component architecture

Build reusable components.

Avoid duplicating:

- Buttons
- Form controls
- Cards
- Modal implementations
- Page containers
- Navigation
- Tables
- Status badges
- Layout primitives
- Error displays
- Loading indicators
- Empty states
- Pagination
- Search interfaces
- Repeated dashboard widgets

Prefer composable components with clear responsibilities.

Maintain a sensible project structure.

When modifying an existing project, follow its existing architecture unless there is a strong reason to improve it.

Do not unnecessarily rewrite working architecture.

Avoid premature abstraction, but eliminate obvious repetition.

---

# Design system

Derive or reuse a consistent design system.

Define reusable:

- Typography
- Spacing
- Radius
- Shadows
- Borders
- Layout widths
- Breakpoints
- Button variants
- Input styles
- Card styles
- Surface hierarchy
- Icons
- Motion rules
- Color tokens
- Semantic colors
- Content widths
- Z-index conventions

If an existing design system exists, use it instead of inventing another.

Maintain visual consistency across the entire application.

Do not create subtly different versions of the same component without reason.

Use the project’s spacing tokens or scale for padding, margins, and gaps. Prefer parent-level layout spacing and `gap` over scattered child margins. Avoid arbitrary one-off values, negative-spacing hacks, and spacing that only works at one viewport.

---

# Accessibility

Target current WCAG accessibility guidance, using WCAG 2.2 AA as a practical target where applicable.

Automatically include appropriate:

- Semantic HTML
- Proper heading hierarchy
- Keyboard navigation
- Visible focus states
- Accessible labels
- ARIA only where semantically necessary
- Alternative text
- Accessible modal behavior
- Focus trapping where appropriate
- Focus restoration
- Escape-to-close where appropriate
- Screen-reader-friendly status/error messages
- Sufficient contrast
- Reduced-motion support where useful
- Correct button vs link semantics
- Proper table semantics
- Logical tab order
- Accessible form validation
- Meaningful link text
- Focus not being obscured by sticky or fixed content
- Usable behavior at increased text sizes and zoom
- Adequate pointer target size
- Accessible authentication where authentication exists

Do not use clickable `<div>` or `<span>` elements when semantic controls are appropriate.

Accessibility must be considered part of implementation, not a final cosmetic pass.

---

# Performance

Avoid obvious performance problems.

Automatically consider:

- Image optimization
- Lazy loading
- Code splitting where beneficial
- Bundle size
- Excessive client-side JavaScript
- Duplicate API requests
- Unnecessary renders
- Caching
- Font loading
- Layout shift
- Large media
- Route-level loading
- Expensive calculations
- Virtualization for genuinely large lists
- Server/client rendering boundaries
- Avoiding needless hydration
- Data-fetching strategy

Do not prematurely optimize trivial code, but correct clear performance problems.

---

# SEO

For public-facing websites automatically implement reasonable SEO fundamentals:

- Unique page titles
- Meta descriptions
- Semantic headings
- Indexable content
- Canonical URLs where appropriate
- Open Graph metadata
- Social metadata
- Sitemap when appropriate
- robots.txt when appropriate
- Structured data when strongly relevant
- Meaningful URL structures
- Useful internal linking
- Image alt text
- Appropriate index/noindex behavior

Do not add SEO machinery to private dashboards where it provides no value.

---

# Privacy, compliance, resilience, and localization

Apply these requirements proportionally and according to the project’s jurisdiction, audience, and industry.

- Do not invent legal notices, consent language, terms, accessibility claims, or regulatory guarantees.
- Where applicable, explain what personal data is collected, why it is used, how long it is retained, and who receives it.
- Where applicable, do not set non-essential cookies or tracking before valid consent. Make consent understandable, freely given, reversible, and no harder to reject than to accept.
- Do not use dark patterns for consent, subscriptions, payment, data collection, or destructive confirmation.
- Handle timeouts, cancellation, offline conditions, failed dependencies, expired sessions, partial responses, and server failures where they can occur.
- Preserve useful user-entered data after recoverable errors and prevent duplicate submissions.
- Provide retry, undo, recovery, or a clear alternative path where appropriate. Do not blindly retry destructive or non-idempotent operations.
- Test long headings, labels, names, dates, currencies, time zones, translated content, and right-to-left layout when relevant.
- Keep important text out of images and avoid layouts that depend on one exact string length.

---

# Security

Apply secure defaults whenever the application includes:

- Authentication
- Authorization
- APIs
- Databases
- User-generated content
- File uploads
- Cookies
- Sessions
- Secrets
- Payments
- Personal information
- Admin functionality
- Webhooks
- Third-party integrations

Never expose secrets in client code.

Check for:

- Authorization failures
- Input validation
- Injection vulnerabilities
- XSS
- CSRF where applicable
- Unsafe redirects
- Insecure file uploads
- Improper secret handling
- Insecure cookies
- Broken access control
- Excessive API exposure
- Sensitive error messages
- Untrusted HTML
- Unsafe external URLs
- Missing server-side permission checks
- Insecure direct object references

Do not implement custom cryptography.

Use established framework/platform security mechanisms.

---

# Authentication and permissions

When authentication exists:

- Handle signed-in state
- Handle signed-out state
- Protect private routes
- Check authorization server-side where applicable
- Handle expired sessions
- Provide useful unauthorized behavior
- Handle authentication loading states
- Avoid exposing protected content before authorization completes
- Use secure session handling
- Implement logout properly

Do not rely only on hidden frontend controls for access control.

If roles exist, enforce role permissions in the backend/API as well as the interface.

---

# API behavior

When APIs are involved:

- Use a consistent client abstraction
- Handle loading
- Handle failures
- Handle malformed responses
- Validate required input
- Avoid leaking internal errors
- Use appropriate HTTP methods
- Use meaningful status codes
- Protect sensitive routes
- Prevent duplicate submissions where relevant
- Handle retries carefully
- Avoid retrying destructive operations blindly
- Support cancellation where useful
- Validate authorization server-side
- Return consistent error formats

---

# Database behavior

When persistence exists:

- Use appropriate constraints
- Use migrations
- Validate data
- Handle missing records
- Avoid unnecessary N+1 queries
- Use transactions when multiple writes must succeed atomically
- Preserve referential integrity
- Avoid destructive schema changes without clear need
- Add useful indexes when justified
- Handle unique constraints
- Avoid trusting client-provided ownership/permission fields
- Preserve data consistency during failure cases

---

# Browser verification

Do not consider a website finished because the code compiles.

Before completion, verify the actual rendered application whenever browser/runtime tooling is available.

Test representative:

- Desktop viewport
- Tablet viewport
- Mobile viewport

Exercise important:

- Navigation
- Forms
- Buttons
- Dialogs
- Dropdowns
- Search
- Filters
- CRUD flows
- Authentication flows where applicable
- Responsive menus
- Primary user journeys

Check for:

- Console errors
- Runtime errors
- Broken layouts
- Overflow
- Broken links
- Dead controls
- Missing states
- Incorrect routing
- Obvious accessibility problems
- Layout shifts
- Invisible content
- Overlapping controls
- Broken mobile navigation
- Unjustified split headers or headings squeezed into narrow columns
- Padding, margins, or gaps that break the intended spacing rhythm at other widths
- User-facing stack traces, raw exception details, secrets, or unnecessary personal data in failure responses
- Notifications that disappear before they can be read or obscure the next required control

Fix discovered problems before declaring the task complete whenever tooling allows it.

Re-run affected flows after fixes.

---

# Completion behavior

Before reporting completion, internally check:

- Does every primary visible control work?
- Is every important route functional?
- Does the site work on mobile?
- Does it work at tablet widths?
- Are loading/error/empty states covered?
- Are forms validated?
- Are there console/runtime errors?
- Are there unfinished placeholders?
- Is navigation complete?
- Are accessibility fundamentals present?
- Are security fundamentals applied?
- Is metadata appropriate?
- Is the footer/site shell complete where appropriate?
- Has the primary user journey been tested?
- Are destructive actions handled responsibly?
- Are API failures handled?
- Are protected actions actually protected?
- Are user-facing errors safe, actionable, and linked to protected diagnostics?
- Are notifications using the right surface and accessible status semantics?
- Are headings and copy specific, natural, and free from prompt or implementation language?
- Are trust claims, reviews, logos, and statistics supplied and supportable?
- Is consent and tracking behavior appropriate for the relevant jurisdiction?
- Is a root-level `DECISIONS.md` or existing ADR record updated for meaningful technical choices?
- Does the implementation follow the existing architecture?

Do not make me explicitly request these checks.

---

# Specialized skill: frontend-app-builder

Add, install, or use an existing equivalent:

`frontend-app-builder`

Purpose:

Design and implement modern frontend applications end-to-end.

Responsibilities:

- Page composition
- Component architecture
- Responsive design
- UI implementation
- Interaction logic
- Routing
- Forms
- State management
- Design-system reuse
- Accessibility
- Responsive navigation
- Application states
- Asset handling
- Client/server boundaries where relevant
- Data presentation
- Reusable UI patterns

Use automatically during frontend implementation.

If an official or installed equivalent already exists, use that rather than creating a duplicate skill.

---

# Specialized skill: frontend-testing-debugging

Add, install, or use an existing equivalent:

`frontend-testing-debugging`

Purpose:

Verify that websites actually work after implementation.

Responsibilities:

- Run/build the application
- Inspect runtime errors
- Inspect browser console errors
- Test desktop layouts
- Test tablet layouts
- Test mobile layouts
- Exercise important buttons
- Exercise forms
- Exercise navigation
- Test dialogs/dropdowns
- Test search and filters
- Test primary user journeys
- Identify layout overflow
- Identify dead controls
- Identify broken routes
- Identify inconsistent states
- Fix issues discovered during testing
- Re-test after fixes
- Run existing automated tests where appropriate

Use automatically near the end of frontend implementation or whenever debugging UI behavior.

Testing should be a separate verification pass rather than assuming implementation is correct.

---

# Specialized skill: security-best-practices

Add, install, or use an existing equivalent:

`security-best-practices`

Purpose:

Apply secure implementation practices appropriate to the application's technology stack.

Responsibilities:

- Authentication security
- Authorization
- Input validation
- Secret management
- XSS prevention
- CSRF prevention where applicable
- SQL/NoSQL injection prevention
- File-upload security
- Cookie/session security
- API authorization
- Dependency/security considerations
- Secure headers where applicable
- Protection of sensitive data
- Safe redirects
- Server-side permission enforcement
- Webhook verification where relevant
- Third-party integration security

Use automatically whenever security-sensitive functionality is present.

If an official security skill exists, prefer it rather than duplicating it.

---

# Framework-specific skills

Automatically detect the project's framework before selecting the framework skill.

Do not load every framework skill simultaneously.

## React / Next.js

Use or create:

`react-next-best-practices`

Cover:

- Component architecture
- Server vs client components where applicable
- State placement
- Hooks
- Rendering performance
- Data fetching
- Routing
- Error boundaries
- Suspense/loading behavior
- Image optimization
- Metadata
- Accessibility
- Bundle optimization
- Caching
- Route organization
- Server actions/API boundaries where applicable

## Vue / Nuxt

Use an equivalent:

`vue-nuxt-best-practices`

## Svelte / SvelteKit

Use an equivalent:

`sveltekit-best-practices`

## Angular

Use an equivalent:

`angular-best-practices`

## Other frameworks

If another framework is detected, use the strongest available framework-specific skill rather than forcing React conventions onto it.

Do not load irrelevant framework skills.

---

# Backend framework skills

When a real backend is part of the application, optionally route to an appropriate backend skill.

Examples:

- Node.js / Express / Fastify
- NestJS
- Django
- FastAPI
- Rails
- Laravel
- ASP.NET
- Go
- Spring Boot

Backend-specific skills should own framework conventions.

`production-web-standard` should own the production-quality expectations.

Avoid duplicating framework documentation inside the top-level skill.

---

# Database-specific skills

When a project uses a database or ORM, use relevant specialized guidance when available.

Examples:

- PostgreSQL
- MySQL
- MongoDB
- Prisma
- Drizzle
- Supabase
- Firebase
- SQLAlchemy
- Django ORM

Do not add database skills to static websites.

---

# Deployment skill

Install or use only the deployment skill relevant to the project.

Examples:

- `vercel-deploy`
- `netlify-deploy`
- `cloudflare-deploy`
- AWS deployment workflow
- Docker/server deployment workflow
- Railway/Fly.io/etc. where relevant

Responsibilities:

- Production build
- Environment variables
- Build configuration
- Deployment configuration
- Routing configuration
- Production validation
- Framework deployment requirements
- Runtime configuration

Do not automatically deploy unless I explicitly request deployment.

The skill may prepare the project to be deployable without publishing it.

---

# Skill ownership rules

Avoid instruction duplication.

Use the following ownership model:

## `production-web-standard`

Owns:

- Definition of Done
- Production completeness
- Required application states
- Responsive expectations
- Accessibility baseline
- Quality gates
- Testing requirement
- Skill routing
- Completion checklist
- Determining whether the result is production-ready

## `frontend-app-builder`

Owns:

- Frontend implementation
- UI architecture
- Components
- Layouts
- Interaction implementation
- Frontend state
- Styling

## framework skill

Owns:

- Framework idioms
- Recommended patterns
- Framework performance behavior
- Framework APIs
- Project structure conventions

## `security-best-practices`

Owns:

- Security review
- Security-sensitive implementation
- Threat-related guidance
- Authentication/authorization security

## `frontend-testing-debugging`

Owns:

- Independent verification
- Runtime inspection
- Interaction testing
- Responsive testing
- Regression checks
- Fix/retest loop

## deployment skill

Owns:

- Hosting/platform-specific deployment behavior

This separation is important.

Do not turn `production-web-standard` into a giant replacement for all specialized skills.

It should be the **orchestrator and quality contract**.

---

# Skill discovery and reuse

Before creating a specialized skill:

1. Inspect available installed skills.
2. Check whether an official equivalent already exists.
3. Prefer official or well-maintained existing skills.
4. Avoid installing two skills with essentially identical responsibilities.
5. Create a custom skill only when the capability is missing or when my production standards need customization.

Always create/retain the custom:

`production-web-standard`

because it represents my preferred Definition of Done and orchestration behavior.

Specialized skills may be official/existing equivalents.

---

# Automatic skill routing

Skills should activate based on task intent.

Example:

> "Build me a SaaS dashboard."

Automatically use:

- `production-web-standard`
- `frontend-app-builder`
- detected framework best-practices skill
- `frontend-testing-debugging`

If authentication/database/API functionality exists, additionally use:

- `security-best-practices`
- relevant backend/database skills

Example:

> "Fix the mobile layout."

Use:

- `production-web-standard`
- `frontend-app-builder`
- detected framework skill
- `frontend-testing-debugging`

Example:

> "Add authentication."

Use:

- `production-web-standard`
- relevant frontend/framework skill
- backend/authentication implementation skills where relevant
- `security-best-practices`
- `frontend-testing-debugging`

Example:

> "Deploy this to Vercel."

Use:

- appropriate project/framework skills where necessary
- `vercel-deploy`
- production validation
- `frontend-testing-debugging` where appropriate

Do not require me to manually name every skill.

---

# Proportional engineering

Do not over-engineer simple sites.

Apply requirements proportionally.

A simple marketing landing page usually does not need:

- Complex state management
- Database infrastructure
- Authentication
- Heavy testing infrastructure
- Microservices
- Complex caching
- Unnecessary backend APIs

But it still needs:

- Responsive design
- Working interactions
- Accessibility fundamentals
- Proper metadata
- Functional navigation
- Good mobile behavior
- Appropriate footer/site shell
- No broken controls
- Browser verification

A production SaaS application should receive substantially deeper treatment.

Complexity should follow actual product needs.

---

# Existing project behavior

When working in an existing repository:

1. Inspect the repository before making architectural decisions.
2. Detect the framework.
3. Detect the package manager.
4. Inspect package/configuration files.
5. Understand the existing architecture.
6. Inspect existing components.
7. Inspect existing styling/design system.
8. Inspect routes.
9. Inspect API/data architecture where relevant.
10. Inspect available scripts.
11. Inspect lint/test/build commands.
12. Reuse existing conventions.
13. Modify the minimum necessary surface.
14. Do not replace frameworks/libraries unnecessarily.
15. Preserve working functionality.
16. Run existing lint/test/build scripts where applicable.
17. Verify affected flows after modification.

Do not rebuild an existing application from scratch merely because another architecture would also work.

Before making a meaningful architectural or operational choice, inspect for `DECISIONS.md`, `ARCHITECTURE.md`, or an existing ADR convention. Create or update a root-level `DECISIONS.md` when a choice affects architecture, cost, security, data, maintenance, deployment, or user-visible behavior, or when the user explicitly requests a decision record. Mark each entry as `User-directed`, `Existing-project constraint`, or `Agent recommendation`, and record the context, alternatives, rationale, consequences, and revisit condition. Do not store secrets, stack traces, or private data in the decision record.

---

# Autonomous completion principle

When a requirement is an obvious consequence of building a professional website, implement it without making me enumerate it.

For example, if I ask:

> "Create a pricing page."

I should not subsequently need to say:

- make it responsive
- make the buttons work
- fix mobile
- add hover states
- add focus states
- add footer
- make navigation work
- add loading states
- add validation
- add metadata
- test it
- remove console errors
- add accessibility
- make cards stack on mobile
- handle empty states
- handle errors

Infer standard production requirements automatically.

Ask me only for genuine product decisions that cannot reasonably be inferred.

Do not ask questions about implementation details that can be resolved using sensible engineering defaults and the existing codebase.

---

# No micro-skills for trivial UI behavior

Do NOT create separate skills for things such as:

- button behavior
- footer behavior
- copyright text
- responsive cards
- mobile menus
- hover states
- form errors
- loading spinners
- empty states
- 404 pages
- tablet layouts
- individual viewport widths

These are production requirements owned by `production-web-standard` and implemented by the relevant engineering skills.

Skills should represent meaningful reusable capability domains rather than individual UI details.

Prefer approximately:

- 1 custom production orchestration skill
- 1 frontend implementation skill
- 1 testing/debugging skill
- 1 security skill
- 1 relevant framework skill
- 1 deployment skill when required
- optional backend/database skills only when the project needs them

Avoid creating 20–50 tiny overlapping skills.

---

# Skill maintenance principle

Keep the system maintainable over time.

When framework guidance changes:

update or replace the framework-specific skill.

When security recommendations change:

update the security skill.

When deployment platforms change:

update deployment skills.

The `production-web-standard` skill should remain relatively stable because it describes product-quality expectations rather than volatile framework APIs.

Avoid copying volatile technical documentation into the top-level skill.

---

# Final behavior expected

After this system is configured, a normal request such as:

> "Build the website from this specification."

should implicitly mean:

- inspect the project
- understand the requested product
- choose the appropriate skills
- implement the complete UI
- make it responsive
- make visible interactions functional
- implement relevant application states
- follow framework conventions
- preserve/reuse the design system
- implement accessibility fundamentals
- apply security standards when relevant
- handle backend/data behavior when present
- test representative user journeys
- test desktop/tablet/mobile
- fix obvious errors
- remove unfinished placeholders
- remove fabricated trust content and prompt-style copy
- keep stack traces and internal diagnostics out of production user interfaces
- preserve a decision record for meaningful technical choices
- verify the application
- report what was completed

without requiring me to repeatedly specify generic production requirements.

# Final setup instruction

Create the custom `production-web-standard` skill first.

Then inspect the currently available skill/plugin catalog and add or enable the strongest appropriate existing equivalents for:

1. Frontend application building
2. Frontend testing and debugging
3. Security best practices
4. The framework(s) I actually use
5. Deployment platform(s) I actually use

Do not duplicate installed capabilities.

Keep `production-web-standard` as the top-level orchestration and Definition-of-Done skill.

Keep implementation, framework, security, testing, backend, database, and deployment knowledge in specialized skills.

Configure automatic skill selection so that I normally do not need to manually mention skill names in website-development prompts.
