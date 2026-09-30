# Production Web Standard

> Make “build this website” mean complete, usable, and ready to verify.

`production-web-standard` is an open-source Codex skill that turns ordinary website and web-application requests into a production-quality contract. It gives the agent a durable Definition of Done, then routes implementation work to the strongest relevant specialist skills already installed in the environment.

It is designed to make quality the default without turning one skill into a framework manual.

## What it provides

The skill automatically accounts for the parts of a professional website that are often forgotten when a request is short:

- Responsive layouts across mobile, tablet, desktop, and large displays
- Functional navigation, controls, forms, dialogs, search, filters, and primary journeys
- Loading, empty, validation, success, failure, offline, permission, and retry states
- Clear content, headings, taglines, CTAs, and non-robotic interface wording
- Deliberate visual hierarchy without default split headers or generic AI layouts
- Consistent spacing, typography, color, motion, and component tokens
- Keyboard access, focus management, semantic HTML, contrast, and reduced-motion support
- Safe user-facing errors with reference IDs instead of stack traces
- Protected admin diagnostics, redacted logs, and server-side authorization
- Privacy, consent, security, SEO, and public-site metadata where relevant
- Recovery from timeouts, failed dependencies, duplicate submissions, and unsaved changes
- Browser verification at representative viewport sizes
- Root-level `DECISIONS.md` records for meaningful architectural choices

Requirements are applied proportionally. A marketing page does not receive a database or authentication system by default. A production SaaS application does receive deeper state, permission, security, and failure handling.

## How it works

```text
User request
    ↓
production-web-standard
    ↓
Project and framework detection
    ↓
Relevant frontend, framework, security, data, testing, and deployment skills
    ↓
Implementation → browser verification → fix and re-test
```

The top-level skill owns the quality contract. Specialist skills own implementation details such as framework APIs, component code, security hardening, browser automation, and deployment workflows.

## Use it

Automatic discovery is enabled. A normal request is enough:

```text
Build this website from the specification.
```

You can also invoke it explicitly:

```text
Use $production-web-standard to build or modify this web project.
```

Useful requests include:

```text
Build a responsive marketing site for this product.
```

```text
Redesign this dashboard without breaking its existing data flows.
```

```text
Fix the mobile layout and verify the primary user journey.
```

```text
Add authentication and protect the admin actions.
```

```text
Prepare this site for deployment, but do not publish it.
```

The full production standard applies unless the request explicitly asks for a prototype, mockup, experiment, proof of concept, or intentionally incomplete result.

## Content and visual quality

The skill treats copy and layout as part of product quality, not decoration.

- Taglines are optional and must communicate a useful product or brand idea.
- User-facing copy must not reveal prompts, agent reasoning, component structure, or implementation notes.
- Headings should be specific, useful when scanned alone, and semantically structured.
- A split header is not a default. A heading should receive enough width to express itself naturally; a two-column header needs a real content relationship.
- Use the project’s spacing scale for padding, margins, and gaps. Avoid arbitrary values and spacing that only works at one viewport.
- Do not fabricate testimonials, customer logos, statistics, certifications, awards, reviews, guarantees, pricing, or performance claims.

## Errors, notifications, and diagnostics

The skill separates what users need from what maintainers need.

Users receive a short, contextual message, a useful next step, and a safe reference ID when support may need to investigate. Production interfaces do not expose stack traces, SQL, filesystem paths, tokens, secrets, framework internals, or raw exception messages.

Full diagnostics belong in protected server-side logs or an authorized admin/support surface. Logs must redact passwords, session identifiers, access tokens, payment data, and unnecessary personal information.

Feedback uses the right surface for the situation:

- Field validation appears beside the field.
- Multiple form errors also receive a linked error summary.
- Non-blocking success may use a short toast or status message.
- Persistent or actionable errors stay visible in context.
- Critical or high-risk situations use a banner, dialog, or full-page state.

## Decision records

For meaningful technical choices, the skill checks for an existing `DECISIONS.md`, `ARCHITECTURE.md`, or ADR convention. If none exists, it can create a root-level `DECISIONS.md` for decisions affecting architecture, cost, security, data, maintenance, deployment, or user-visible behavior.

Each entry should record the decision, date, source, context, alternatives, rationale, consequences, and when it should be revisited. User-directed decisions are marked explicitly. The file is not a package inventory, changelog, secrets file, or stack-trace archive.

## Install

Clone or download this repository, then run the installer from the repository root.

### Windows PowerShell

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install.ps1
```

### macOS or Linux

```bash
chmod +x scripts/install.sh
./scripts/install.sh
```

The installer copies the skill to `$CODEX_HOME/skills/production-web-standard`, or to `~/.codex/skills/production-web-standard` when `CODEX_HOME` is not set. It refuses to overwrite an existing installation; review or remove the existing installation before reinstalling.

Restart Codex or begin a new session after installation so the skill catalog refreshes.

## Specialist integrations

The repository contains the production orchestration skill, not every framework or platform skill. When compatible specialists are available, `production-web-standard` routes to them only when the project needs them.

Typical integrations include:

- `frontend-ui-engineering` for accessible, responsive UI implementation
- `frontend-design` for visual direction and distinctive design systems
- Playwright or an equivalent browser-testing skill for runtime verification
- `security-best-practices` for security-sensitive functionality
- React/Next.js or another framework-specific best-practices skill
- Database, backend, and deployment skills when the project contains those technologies

Useful upstream sources include [OpenAI Skills](https://github.com/openai/skills) for browser automation, security, and deployment workflows; [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills) for React and Next.js guidance; and [Next.js](https://github.com/vercel/next.js) for version-matched framework documentation.

These capabilities are not bundled or relicensed here. Any strong installed equivalent may be used.

## Repository structure

```text
skills/production-web-standard/  Installable skill package
  SKILL.md                      Routing and Definition of Done
  references/                   Production requirements and verification
  agents/openai.yaml            Codex UI metadata
docs/                            Original design specification
scripts/                         Installation and validation tools
.github/workflows/               Continuous validation
```

## Validate

Run the standard-library-only validator from the repository root:

```bash
python scripts/validate.py
```

It checks the package metadata, references, UI metadata, and unfinished placeholders. For a change, also run the repository’s formatting or whitespace checks and review the resulting diff.

## Scope and ownership

`production-web-standard` owns:

- Production completeness and proportionality
- Quality gates and the Definition of Done
- Responsive, accessibility, security, privacy, and error-handling baselines
- Content and visual-quality outcomes
- Specialist skill routing
- Browser verification expectations
- Decision-record guidance

Specialist skills own framework idioms, component implementation, security-specific techniques, browser automation, backend/data conventions, and deployment behavior. This separation keeps the skill maintainable as frameworks and platforms change.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Keep the master skill focused on outcomes and routing. Put detailed, conditional guidance in the relevant reference or specialist skill. Do not add micro-skills for individual controls, states, viewports, or visual flourishes.

## License

This repository is released under the [MIT License](LICENSE).

Original concept and production requirements by Swamy. The initial reusable skill package and repository were created collaboratively with OpenAI Codex. Upstream projects and trademarks remain the property of their respective owners; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
