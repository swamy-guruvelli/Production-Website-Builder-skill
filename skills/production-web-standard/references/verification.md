# Production Verification

Use the repository's existing tooling first. Match verification depth to the change and risk.

## Static and build checks

- Identify the package manager and available scripts before running commands.
- Run relevant formatting checks, lint, typecheck, automated tests, and a production build.
- Inspect failures; fix those caused by or blocking the requested work. Preserve unrelated user changes.

## Browser and runtime checks

When a runnable application and browser tooling are available:

1. Start the application safely and confirm the expected entry routes load.
2. Check representative mobile, tablet, and desktop viewports; include a large viewport when the layout materially changes there.
3. Exercise primary navigation and the main user journey.
4. Test affected buttons, links, forms, dialogs, dropdowns, search, filters, sorting, pagination, CRUD, authentication, and responsive navigation as relevant.
5. Verify loading, empty, success, validation, failure, disabled, unauthorized, and retry behavior that can occur in the affected flow.
6. Inspect console errors, failed requests, runtime exceptions, broken routes/links, overflow, overlap, invisible content, layout shift, and dead controls.
7. Check keyboard navigation, visible focus, labels, headings, contrast, overlay focus behavior, and obvious screen-reader issues.
8. Fix discovered defects and re-run the affected journey and checks.

Do not mutate real production data merely to test. Use local, disposable, seeded, or clearly authorized test data.

## Content, feedback, and disclosure checks

- Read every visible string, including headings, taglines, buttons, labels, helper text, empty states, errors, toasts, captions, metadata, and footer content.
- Remove prompt language, agent reasoning, implementation terminology, generic filler, unsupported claims, fabricated trust content, and inconsistent action names.
- Read the page using only its headings and confirm that the information structure still makes sense. Check that visual heading styling does not replace semantic heading markup.
- Inspect section headers for an unjustified 50/50 split. Confirm that primary headings have enough readable width, wrap naturally, and are not narrowed merely to make room for filler copy.
- Check padding, margins, and gaps against the project’s spacing scale. Look for arbitrary values, negative-spacing hacks, inconsistent section rhythm, and spacing that breaks at representative widths.
- Test long headings, long labels, 200% text scaling, mobile wrapping, and relevant translated or right-to-left content.
- Trigger validation, network, server, permission, not-found, timeout, and retry states that are relevant to the product.
- Confirm that inline errors are connected to their controls, multi-error forms provide a linked summary, and safe messages give the user a useful next step.
- Confirm that non-critical status messages are announced without stealing focus, actionable or critical messages remain available, and toasts do not obscure the next required control.
- Deliberately inspect production-like failure responses for stack traces, SQL, filesystem paths, framework details, tokens, secrets, request bodies, and unnecessary personal data. Confirm that full diagnostics are available only to authorized administrators or support tooling.
- Check the project root for an existing decision record and update or create `DECISIONS.md` for meaningful technical choices. Mark user-directed decisions clearly.

## Privacy and trust checks

- Confirm that consent and tracking behavior matches the relevant jurisdiction and that non-essential tracking does not run before consent where required.
- Check that privacy, terms, cookie, accessibility, refund, or other legal links exist when relevant and do not contain invented claims or placeholder text.
- Confirm that testimonials, logos, ratings, statistics, certifications, prices, availability, and performance claims are supplied and supportable.
- Check that analytics, logs, error trackers, URLs, and third-party embeds do not receive unnecessary personal or sensitive data.

## Completion gate

Before reporting completion, confirm:

- Primary visible controls and routes work.
- Phone, tablet, and desktop layouts are usable without unintended overflow.
- Relevant loading, error, empty, validation, unauthorized, and API-failure states exist.
- Forms validate and recover from errors without accidental duplicate submission.
- Navigation and site shell are complete for the product.
- Accessibility and security fundamentals are present.
- Public-site metadata is appropriate.
- No unfinished placeholders, TODOs, fake links, or dead primary actions remain.
- Protected actions are protected at the server boundary when applicable.
- The implementation follows the existing architecture and design system.
- The primary user journey was exercised and affected checks were re-run after fixes.

If any item is intentionally omitted, state why it is not relevant or identify the remaining constraint. Do not silently lower the standard.
