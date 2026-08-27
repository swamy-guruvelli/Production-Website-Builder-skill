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
