# Kore.ai Codex Plugins

Kore.ai-maintained skills and plugins that help developers, partners, and customers work more effectively with Kore.ai products.

This repository is available under the MIT License, but it is not currently open for external contributions. Kore.ai maintains and publishes the contents of the **Kore Skills** marketplace.

## What you can do with Kore Skills

Each plugin packages one or more focused workflows for Codex. Depending on the installed plugin, you can ask Codex to work with Kore.ai artifacts, guide a design or implementation task, produce structured documentation, or validate an outcome.

Plugins include their own usage guidance, supported inputs, limitations, and example prompts. Some skills may also bundle scripts, reference material, templates, or connections to external tools.

## Available plugins

### Kore XO Tools

Installs `$xo-bot-decomposer`, which analyzes a Kore.ai XO bot-definition JSON, ZIP, or extracted export and produces:

- a business-level inventory of user goals, events, and flow steps; and
- a technical reference for integrations, entities, scripts, forms, channels, and configuration evidence.

The skill processes supplied files locally, redacts likely credential values from generated evidence, and does not estimate implementation effort.

### Kore Agent Design

Installs `$kore-agent-designer`, which helps users create or review traceable functional and technical designs for conversational, process, or hybrid Kore.ai agents. It supports guided design from an initial idea, document normalization, gap review, readiness assessment, and an implementation handoff without connecting to or modifying a Kore.ai environment.

## Getting started

### 1. Add the marketplace

From a terminal with Codex installed, add the Kore Skills marketplace directly from GitHub:

```bash
codex plugin marketplace add Koredotcom/kore-codex-plugins --ref main
```

### 2. Browse available plugins

```bash
codex plugin list --marketplace kore-skills
```

### 3. Install a plugin

Replace `<plugin-name>` with a plugin listed by the previous command:

```bash
codex plugin add <plugin-name>@kore-skills
```

### 4. Start using it

Start a new Codex task after installation. Describe the outcome you want in plain language and attach any files the workflow needs. Codex can select an applicable skill automatically, or you can explicitly request one by name—for example:

```text
Use $<skill-name> to analyze the attached Kore.ai artifact.
```

Review each plugin's documentation for supported product versions, required inputs, expected outputs, and any setup steps.

### Keep the marketplace current

Refresh the marketplace when Kore.ai publishes updates:

```bash
codex plugin marketplace upgrade kore-skills
```

> [!TIP]
> **Using another coding agent?** The underlying `SKILL.md` instructions are often portable, but plugin marketplaces and integrations are tool-specific. You can clone this repository and ask an agent such as Claude Code or Devin to adapt a selected skill and its supporting files to that agent's native format, then install the adapted copy. Review the changes, scripts, integrations, and requested permissions before enabling it; the Codex marketplace metadata itself will not install unchanged in every agent.

## Repository structure

```text
.
├── .agents/
│   └── plugins/
│       └── marketplace.json      # Kore Skills marketplace catalog
├── plugins/
│   └── <plugin-name>/
│       ├── .codex-plugin/
│       │   └── plugin.json       # Codex plugin manifest
│       ├── skills/               # Skills and their supporting files
│       ├── scripts/              # Optional deterministic helpers
│       ├── references/           # Optional reference material
│       └── assets/               # Optional templates and media
└── README.md
```

## Data and security

- Review a plugin before installing it, especially when it includes scripts or external integrations.
- Do not commit credentials, private keys, customer data, or confidential implementation material to this repository.
- Treat outputs as working material and validate them against the applicable Kore.ai product documentation and your own requirements.
- Do not disclose security vulnerabilities through a public issue. Private reporting instructions will be published before the first general release.

## Maintenance and support

Kore.ai maintains this repository and is not accepting external pull requests at this time. Plugin-specific support information and known limitations will be documented with each published plugin.

These plugins complement, but do not replace, official Kore.ai product documentation and support channels.

### Maintainer safety checks

This repository includes a versioned pre-commit hook and a matching CI check. The checks use Gitleaks to detect known secret formats and a repository-owned scanner to block machine-local paths and sensitive filenames.

After cloning, maintainers should enable the tracked hooks once:

```bash
git config core.hooksPath .githooks
```

The pre-commit hook fails closed when Gitleaks is unavailable. To run the repository-owned check manually across all tracked and unignored files:

```bash
python3 scripts/check_repository_safety.py --all-files
```

Git hooks can be bypassed, so the GitHub Actions workflow repeats both checks for every push and pull request.

## License

Copyright © 2026 Kore.ai, Inc. Released under the [MIT License](LICENSE).

## Project status

The marketplace is being prepared for its first release. Plugin names, interfaces, and installation details may change until a stable catalog is published.
