# Decomposition document detail

Use these requirements when generating the two final documents. Include only source-supported facts and mark gaps; do not pad short workflows with invented steps.

## Business goal decomposition

- Include a summary table mapping each plain-language goal to its source dialogs, followed by an Events table for welcome, fallback, follow-up, and default transfer behavior.
- Identify default and additional languages; list configured channels and their enabled/disabled state when available.
- Name each digital form and the goals that use it. State when forms occur only in system/hidden flows, or when none are found.
- Distinguish global PII redaction settings, masked entity types, and local intent/entity overrides. Say when configuration is absent; distinguish absence in the export from verified deployed behavior.
- For each goal, include trigger utterances or patterns, source-dialog evidence, and numbered business actions covering clarification, collection, validation, decisions, service actions, responses, failures, and escalation when present.
- Describe a form action as “Present a digital form to collect <fields>.” Keep implementation details in the technical reference.
- Inline sub-dialogs used by one parent. Document shared flows once, name their callers, and reference them by name. Reference independently user-invokable goals as “See Goal N: <Name>”; do not duplicate their steps.
- End the business document after Shared Sub-Flows. Keep methods, URLs, payloads, scripts, and platform IDs in the technical document.

## Technical reference structure

Begin with the scope disclaimer, source/version and parser route, analysis date, and a relative companion-document link.

### Integration Configuration

Use a table of environment-variable references, observed usage/base URL, and inferred purpose. Describe authentication through profile identifiers and sanitized headers. Missing secured values do not establish that an integration is unauthenticated.

### API / Service Calls

Create one entry for every distinct service node used by user goals or shared flows. Group by the goals that use it. Each entry includes:

- service name and the goals/steps that use it;
- HTTP method and sanitized URL;
- headers and request body with credential values redacted;
- pre- and post-processors with sanitized code;
- response fields and mappings; and
- observed error transitions or an explicit evidence gap.

### Entity Definitions

Use columns for name, type, allowed values/format, validation, prompt, and invalid-input re-prompt. Include entities from user goals and shared flows.

### Script Nodes

Group entries by function (for example authentication, validation, payment, or session state). For every script in user goals and shared flows, include its name, purpose, where it is used, and full decoded code with credential values redacted. Do not restore secrets from the original source.

Keep system-only scripts out unless they materially explain a documented event. Avoid extra standalone NLU configuration, context-variable catalog, channel/deployment configuration, and form-definition sections by default. Include relevant form-field evidence alongside its associated goal, entity, or integration instead.

## Coverage check

Use the structured inventory to account for every non-system dialog, service, entity, script, form, environment reference, and shared-flow relationship. Check that branch conditions and errors are documented where observed, repeated flows are not double-counted, and each technical entry links back to the business behavior it supports. State unresolved evidence rather than inventing configuration.
