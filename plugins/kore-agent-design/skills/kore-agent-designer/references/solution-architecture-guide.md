# Solution architecture guide

Read this reference when creating or updating `technical/architecture.md`.

## Required structure

```markdown
<!-- kore-agent-design:architecture:v2 -->
# Solution Architecture: <Agent Name>

## Document Metadata

<Use the metadata block from general-design-guidance.md.>

## Architecture Drivers and Traceability

| Functional or NFR IDs | Driver | Architectural treatment | Evidence status |
|---|---|---|---|

## System Context and Trust Boundaries

<Actors, channels, Kore.ai components, upstream/downstream systems, sources of truth, trust boundaries, and as-is/to-be diagrams.>

## Kore.ai Product and Component Mapping

| Need | Proposed component or pattern | Functional IDs | Evidence status | Rationale |
|---|---|---|---|---|
| <need> | <component or pattern> | <UC/FR/NFR IDs> | Confirmed \| Documented capability \| Proposed \| Not verifiable | <why this treatment fits> |

## Agent and Workflow Responsibilities

<Routing, reasoning boundaries, deterministic workflow, events, wait states, human tasks, and terminal states.>

## Environments and Configuration Promotion

<Development, test, staging, production, workspace/tenant boundaries, configuration ownership, promotion, and approvals.>

## State, Persistence, and Resumption

<Conversation state, durable state, correlation, checkpoints, resume events, duplicate handling, cancellation, and terminal-state ownership.>

## Model, Prompt, Tools, Knowledge, and Guardrails

<Model constraints, instruction hierarchy, tool boundaries and schemas, knowledge/retrieval placement, grounding, confirmation controls, reasoning boundaries, unsupported-action behavior, and evaluation needs.>

## Architecture Decisions

| ID | Decision | Functional IDs | Rationale and evidence | Status | Approver |
|---|---|---|---|---|---|

## Risks and Open Questions

| ID or risk | Impact | Evidence needed or mitigation | Owner | Blocking? |
|---|---|---|---|---|
```

## Category rules

- Every component must exist for a functional or non-functional reason.
- Record evidence for product-specific claims; use `Not verifiable` when current evidence is unavailable.
- Show trust boundaries and sources of truth, not only component boxes.
- For process agents, make persistence, human tasks, resume events, and terminal states explicit.
- Keep API fields, authentication mechanics, and operational runbooks in their dedicated technical files.
