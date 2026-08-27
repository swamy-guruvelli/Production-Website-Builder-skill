---
name: production-web-standard
description: Establishes the production Definition of Done and routes website and web-application work to relevant implementation, framework, security, testing, data, and deployment skills. Use automatically when creating, modifying, redesigning, extending, reviewing, or debugging web UI or full-stack web applications; do not impose the full standard when the user explicitly requests a prototype, mockup, experiment, proof of concept, or intentionally incomplete result.
---

# Production Web Standard

Treat ordinary website and web-application requests as requests for a complete, responsive, functional, accessible, and verified result. Infer standard production requirements without asking the user to enumerate them. Ask only about genuine product decisions that cannot be inferred safely from the brief or repository.

Apply the standard proportionally. A landing page still needs polished responsive behavior, working navigation, accessibility fundamentals, metadata, and browser verification; it does not need authentication, a database, or elaborate infrastructure unless the product requires them.

## Route the Work

Inspect the repository before choosing an approach:

1. Detect the framework, runtime, package manager, routes, styling system, design system, scripts, tests, data layer, authentication, and deployment configuration.
2. Preserve the existing architecture and conventions unless a concrete defect justifies a focused change.
3. Select only skills relevant to the detected stack and requested outcome. Do not load every framework or deployment skill.
4. Use the strongest installed equivalent instead of creating overlapping capability.

Preferred capability routing when available:

- Frontend implementation: `frontend-ui-engineering` (the installed equivalent of `frontend-app-builder`).
- Visual direction: `frontend-design` only when creating or materially reshaping the visual design; the product brief and existing design system remain authoritative.
- React performance and patterns: `vercel-react-best-practices` or the strongest installed equivalent.
- Next.js conventions: use the project's version-matched bundled Next.js docs and generated repository agent rules when available, plus the React skill; use a dedicated Next.js skill only when a current maintained one is installed.
- Other frameworks: the strongest matching installed framework skill; never apply React conventions to a different framework.
- Security-sensitive work: `security-best-practices`.
- Runtime browser verification: `playwright` or `playwright-interactive` as appropriate.
- Platform deployment: exactly the skill matching the requested or already configured platform, such as `vercel-deploy`, `netlify-deploy`, or `cloudflare-deploy`.
- Backend and database guidance: only when the application actually contains that technology.

If a named capability is unavailable, perform the work directly from repository conventions and authoritative documentation rather than fabricating a skill. Deployment skills may prepare configuration, but never publish unless the user requests deployment.

## Own the Quality Contract

This skill owns the Definition of Done, completion criteria, proportionality, and routing. Specialized skills own implementation details:

- Frontend skills own components, layout, styling, state, interaction code, and client/server UI boundaries.
- Framework skills own current APIs, idioms, rendering, caching, routing, and project structure.
- Security skills own threat-sensitive implementation and review.
- Testing skills own runtime inspection, interaction checks, responsive checks, and fix/retest loops.
- Backend, data, and deployment skills own their technology-specific conventions.

Do not copy volatile framework documentation into this skill and do not create micro-skills for buttons, footers, mobile menus, loading indicators, form errors, or individual viewports.

## Build to the Definition of Done

Read [references/production-requirements.md](references/production-requirements.md) before implementation or review. Apply only sections relevant to the product surface.

Key invariants:

- Every visible interactive control has meaningful behavior unless the user explicitly requests a visual-only mockup.
- Important flows cover relevant initial, loading, empty, success, validation, error, disabled, unauthorized, offline, and partial-data states.
- The interface remains usable on representative phone, tablet, laptop, desktop, and large-display widths without unintended horizontal overflow.
- Forms are labeled, keyboard-usable, validated, resilient to submission errors, and protected from accidental duplicate submission.
- Public sites include appropriate shell, metadata, SEO fundamentals, and error/not-found handling; private tools do not receive pointless SEO machinery.
- Accessibility, security, and performance are implementation concerns, not cosmetic final passes.
- Do not ship lorem ipsum, fake links, dead controls, dummy forms, empty routes, unimplemented primary actions, or TODO placeholders unless explicitly requested.
- Reuse the existing design system and architecture. Introduce the minimum necessary abstraction and eliminate only obvious harmful duplication.

## Verify Before Completion

Read and follow [references/verification.md](references/verification.md) near the end of implementation, during review, and whenever debugging.

Do not equate compilation with completion. When runtime/browser tooling is available, render the application at representative desktop, tablet, and mobile sizes; exercise the primary journeys and important controls; inspect console and runtime failures; fix defects; and re-run affected checks.

Run relevant existing lint, typecheck, test, and production-build scripts. If a check cannot run, report the exact constraint and what was verified instead. Never claim a check passed without running it.

## Report the Outcome

Lead with what is complete. Summarize material implementation and verification results, note any remaining limitation or unverified external dependency, and include direct file links when useful. Do not report ordinary production basics as optional extras the user should request later.
