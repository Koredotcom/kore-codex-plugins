---
name: xo-bot-decomposer
description: Analyze Kore.ai XO bot-definition JSON or ZIP exports and produce a business goal decomposition plus a technical reference. Use for understanding dialogs, flows, integrations, entities, scripts, forms, channels, or version-shaped export structure. Do not estimate effort, cost, or implementation scope.
---

# XO Bot Decomposer

Turn a Kore.ai XO bot export into two evidence-based documents:

1. `<bot-slug>_analysis.md` — user goals, business-level steps, events, channels, forms, and PII configuration.
2. `<bot-slug>_technical_reference.md` — integrations, entity definitions, environment references, and script-node evidence.

This skill documents what is present in the supplied export. It does not estimate migration or implementation effort, prescribe a delivery process, or require a connected Kore.ai environment.

## Protect the supplied export

Treat every export and generated artifact as potentially sensitive. Work only with files the user supplied or authorized. Do not upload them, commit them, or copy them into the plugin repository.

The bundled parser redacts likely credential values in service headers, request bodies, URLs, and scripts. Redaction is a safety layer, not a guarantee: inspect generated files before sharing them and describe authentication through header names, profile identifiers, or environment-variable references rather than resolved secrets.

## Select the input and destination

Accept a `.json` definition, `.zip` archive, extracted export directory, or pasted JSON saved to a temporary file.

- If the input is unambiguous, begin without asking the user to restate it.
- If several plausible exports exist, ask the user to select one.
- Use the destination the user provides. Otherwise create a fresh temporary working directory and place final documents in the current task's requested output location.
- Never write generated analysis into a source fixture, read-only directory, or the plugin installation.

The parser recognizes common single-definition export shapes. `botDefinition.json`, earlier-version labels, and ambiguous version metadata use the XO 10-compatible route; `appDefinition.json` or an explicit version of 11 or later uses the XO 11 route. Treat this as parser routing, not proof that every export from a product release has an identical schema.

## Generate deterministic evidence

Run the bundled entry point once for mechanical extraction:

```bash
python3 "${PLUGIN_ROOT}/skills/xo-bot-decomposer/scripts/decompose_bot.py" \
  "<export.zip-or-json-or-folder>" "<fresh-output-directory>"
```

During repository-source testing, when `PLUGIN_ROOT` is unset, resolve `scripts/decompose_bot.py` relative to this `SKILL.md`.

When the user explicitly identifies the export version, pass `--xo-version <major-version>`. The command safely extracts ZIPs and produces:

- `_inventory.json` — structured dialogs, nodes, transitions, services, entities, scripts, forms, environment references, and sub-dialog calls;
- `_inventory.md` — compact counts and coverage;
- `_index.md` — dialogs retained for semantic analysis;
- `_metadata.md` — languages, channels, PII settings, and form summary;
- `_all_dialogs.md` and per-dialog Markdown files — readable flow evidence.

If the parser reports an unsupported shape, preserve the error and inspect only enough source structure to identify whether the export is incomplete or a distinct variant. Use a targeted read-only fallback when reliable; state all coverage limitations.

## Build the business goal decomposition

Read `_inventory.md`, `_index.md`, and `_metadata.md` first. Use `_inventory.json` for exact facts. Read individual dialog files for semantic interpretation and raw JSON only to resolve a specific gap.

A dialog can contain more than one user goal when branches lead to materially different business outcomes. Conversely, a called sub-dialog is normally part of its parent goal:

- Inline a sub-dialog used by only one parent.
- Document a sub-dialog used by multiple parents once under `Shared Sub-Flows` and reference it from each parent.
- Reference a called dialog as another goal only when it is independently user-invokable and has its own business outcome.
- Separate lifecycle behavior such as welcome, fallback, follow-up, and default transfer from user goals.

Name goals as plain-language verb–noun outcomes. Write numbered steps from the agent's perspective and include collection, validation, decisions, service actions, confirmations, failures, and escalation when supported by evidence. Keep HTTP methods, URLs, payloads, code, internal identifiers, and raw configuration out of this document.

For exports with 50 or more candidate dialogs, produce the summary table first and ask which goals the user wants expanded before generating every detailed flow.

Use this shape:

```markdown
# Bot Goal Decomposition: <Bot Name>

**Source:** <export and parser route>
**Analyzed:** <date>
**Total goals identified:** <count>

## Summary
| # | Goal | Source dialog(s) |
|---|---|---|

## Events
<system-triggered or lifecycle behavior>

## Languages and Channels
<configured evidence or “No channel configuration found in export.”>

## Digital Forms
<forms and associated goals, or “No digital forms found.”>

## PII Redaction
<configured evidence, or state that no configuration was found>

## Goal Details
### Goal 1: <Name>
**Trigger evidence:** <utterances, patterns, or inferred source>
1. <business-level step>

## Shared Sub-Flows
<shared flows or “None identified.”>
```

## Build the technical reference

Document only technical evidence associated with user goals and shared sub-flows. Include:

- environment-variable references and inferred purpose;
- service method and sanitized URL;
- authentication requirement, profile reference, and header names with credential values redacted;
- sanitized request shape, response mapping, and observed failure transitions;
- entity type, values or format, prompts, and validation;
- script-node purpose and sanitized code; and
- evidence gaps or configuration that could not be verified.

Do not expose secrets or claim an integration is unauthenticated merely because secured values are absent from an export. Keep system-only flow detail out unless it materially affects a documented event.

## Quality check

Before delivering the two documents:

- account for every non-system dialog as a goal, event, inline flow, shared flow, or explicit exclusion;
- ensure every stated fact is supported by generated or source evidence and label inference;
- verify services, entities, scripts, forms, and environment references against `_inventory.json`;
- confirm business and technical detail remain separated;
- search outputs for unredacted credentials and machine-local paths;
- note missing, ambiguous, or unsupported export evidence; and
- report the files created and the parser route used.
