# Production Web Standard

An open-source Codex skill that turns ordinary website requests into a production-quality contract: responsive layouts, working interactions, complete application states, accessibility, security-aware routing, and real browser verification.

The repository contains one deliberately focused master skill. Framework, security, testing, and deployment knowledge stay in specialized upstream skills so this project remains maintainable.

## What it does

`production-web-standard` activates automatically for website and web-application creation, modification, redesign, review, and debugging unless the user explicitly asks for a prototype or intentionally incomplete result.

It:

- establishes the production Definition of Done;
- detects the project stack before selecting implementation guidance;
- routes to relevant frontend, framework, security, testing, data, and deployment skills;
- requires responsive, accessible, functional behavior and appropriate application states;
- requires build, runtime, browser, and primary-journey verification when tooling is available;
- scales engineering depth to the actual product instead of over-engineering simple sites.

Read the full [skill entrypoint](skills/production-web-standard/SKILL.md) and the original [master creation prompt](docs/master-creation-prompt.md).

## Install

Clone or download this repository, then run one installer from the repository root.

### Windows PowerShell

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install.ps1
```

### macOS or Linux

```bash
chmod +x scripts/install.sh
./scripts/install.sh
```

The installer copies the skill to `$CODEX_HOME/skills/production-web-standard`, or to the standard `~/.codex/skills` location when `CODEX_HOME` is unset. It refuses to overwrite an existing installation.

Restart Codex or begin a new session after installation so the skill catalog refreshes.

## Use

Automatic discovery is enabled. A normal request is enough:

```text
Build this website from the specification.
```

You can also invoke it explicitly:

```text
Use $production-web-standard to build this application.
```

The skill remains useful without any optional integrations. When compatible specialist skills are installed, it routes to them only when the detected stack or task needs them.

## Optional integrations

These projects are not bundled or relicensed here:

- [OpenAI Skills](https://github.com/openai/skills): Playwright browser automation, security best practices, and Vercel, Netlify, or Cloudflare deployment workflows.
- [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills): React and Next.js performance guidance.
- [Next.js](https://github.com/vercel/next.js): version-matched bundled framework documentation and generated agent rules for current Next.js releases.

Any strong installed equivalent can be used. Deployment skills prepare or publish only when deployment is relevant and authorized.

## Repository structure

```text
skills/production-web-standard/  Installable skill package
docs/                            Original design specification
scripts/                         Local install and validation tools
.github/workflows/               Continuous validation
```

## Validate

```bash
python scripts/validate.py
```

The validator uses only the Python standard library and checks the package metadata, references, UI metadata, and unfinished placeholders.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Keep the master skill stable and outcome-focused; put volatile framework knowledge in the relevant upstream specialist skill.

## Credits and license

Original concept and production requirements by Swamy. The initial reusable skill package and repository were created collaboratively with OpenAI Codex.

Upstream projects and trademarks remain the property of their respective owners. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for attribution and scope.

This repository's original content is released under the [MIT License](LICENSE).
