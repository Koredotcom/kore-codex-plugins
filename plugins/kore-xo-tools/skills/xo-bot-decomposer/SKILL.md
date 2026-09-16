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

Treat every export and generated artifact as potentially sensitive. Work only with files the user supplied or authorized. Do not commit them or copy them into the plugin repository. Upload only the completed documents when the user authorizes the optional storage handoff below; never include the source export or intermediate evidence.

The bundled parser redacts likely credential values in service headers, request bodies, URLs, and scripts. Redaction is a safety layer, not a guarantee: inspect generated files before sharing them and describe authentication through header names, profile identifiers, or environment-variable references rather than resolved secrets.

## Select the input and destination

Accept a `.json` definition, `.zip` archive, extracted export directory, or pasted JSON saved to a temporary file.

- If the input is unambiguous, begin without asking the user to restate it.
- If several plausible exports exist, ask the user to select one.
- Use an explicit local destination without asking again, and create it when requested. Otherwise use a fresh temporary directory for evidence and save final documents in the current working directory. Ask only when the destination is ambiguous or unavailable. Handle a cloud-storage destination through the optional handoff after local generation.
- Never write generated analysis into a source fixture, read-only directory, or the plugin installation.

The parser recognizes common single-definition export shapes. `botDefinition.json`, earlier-version labels, and ambiguous version metadata use the XO 10-compatible route; `appDefinition.json` or an explicit version of 11 or later uses the XO 11 route. Treat this as parser routing, not proof that every export from a product release has an identical schema.

## Document scope notice

Place this notice immediately below the title in both the business goal decomposition and technical reference, before source metadata:

> **Scope disclaimer:** SearchAI, SmartAssist start flows, and Agent Assist configurations are not included in the bot export and are therefore not represented in this document.

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
- confirm both documents begin with the scope disclaimer below their titles;
- search outputs for unredacted credentials and machine-local paths; never restore redacted values from the raw export;
- note missing, ambiguous, or unsupported export evidence; and
- report the files created and the parser route used.


## Offer an optional storage handoff

After validation, provide local links and offer a choice: **local files only**, **Google Drive** (My Drive or a shared drive), **OneDrive**, or **SharePoint**. Recommend `<Bot Name> - XO Decomposition` as the upload-folder name, while allowing another name or an existing folder. Honor prior choices without asking again; selecting a local output folder does not authorize upload.

For an accepted upload:

1. Discover the selected provider's available connector tools and guidance. Google Drive uses the `google-drive` skill; OneDrive and SharePoint use their available connector guidance. Verify browsing, upload, readback, and new-folder creation capabilities as needed. These are destination options, not a promise that every environment has the connectors. If a connector or write access is unavailable, explain the limitation and supply the local files for manual upload. Do not require cloud access to finish the documents or substitute a different provider without agreement.
2. Let the user provide a folder URL/ID or choose from accessible folders when browsing is supported. Show names, locations, and links to resolve ambiguity. For OneDrive, resolve the account and drive; for SharePoint, resolve the site, document library, and folder; for Google Drive, resolve My Drive or the shared drive. Ask only for missing details; do not depend on a native folder picker.
3. Keep both documents in one folder. For a new folder, confirm the parent and use the recommended name or the user's alternative. Accepting this choice authorizes creation without another confirmation. Reuse an explicitly chosen existing folder directly. If the user selects a drive or document-library root, create the named folder under it instead of uploading loose files there.
4. Check for an exact-name folder before creating one. Offer reuse or a distinct name such as `<Bot Name> - XO Decomposition - <YYYY-MM-DD>` if it exists. Verify the resolved folder identifier and write access. Preserve sharing settings, and resolve existing filename collisions according to the user's preference before overwriting files.
5. Upload only the two final Markdown documents, preserving their contents and filenames; exclude source exports and intermediate evidence. Convert only when requested, using applicable document/provider guidance and verifying the converted files first.
6. Verify both files and their parent folder through connector readback and return observed folder and file links. Report partial success accurately. Before retrying an uncertain upload, check whether it already created a file and retry only missing or failed uploads.
