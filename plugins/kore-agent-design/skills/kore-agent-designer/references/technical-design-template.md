# Agent Technical Design template

Use this template for every skill-authored technical design. Preserve the marker, document type, all level-two headings, and heading order. Replace angle-bracket prompts with content; do not leave raw prompts in a delivered document. Use `Not applicable — <reason>` when a section does not apply.

```markdown
<!-- kore-agent-design-template:v1 -->
# Agent Technical Design: <Agent Name>

**Document type:** Technical
**Status:** Working Draft | In Review | Approved
**Companion functional design:** <relative link>

## Document Control

| Field | Value |
|---|---|
| Owner | <name or role> |
| Contributors | <names or roles> |
| Version | <version> |
| Last updated | <date> |
| Approval status | <status and approver> |
| Platform evidence reviewed | <documentation topics, environment evidence, or Not verifiable> |

## Functional Design Traceability

| Functional ID | Technical treatment | Component or decision | Status | Evidence or open question |
|---|---|---|---|---|

## Solution Context and Architecture

<System boundary, actors, upstream and downstream systems, trust boundaries, and as-is/to-be diagrams or Mermaid when useful.>

## Kore.ai Product and Component Mapping

| Need | Proposed Kore.ai component or pattern | Evidence status | Rationale | Functional IDs |
|---|---|---|---|---|

## Environments and Deployment Model

<Development, test, staging, production, workspace or tenant boundaries, configuration promotion, approvals, and environment-specific dependencies.>

## Conversation and Workflow Orchestration

<Agent responsibilities, routing, deterministic workflow steps, reasoning boundaries, events, terminal states, and component interactions.>

## Channel and Locale Design

<Channel adapters, identity, payload or rendering differences, locale variants, voice or asynchronous considerations, and limitations.>

## Knowledge and Retrieval Design

<Sources, ingestion, access controls, freshness, retrieval, grounding, citations, fallback, and evaluation.>

## Prompt, Model, Tool, and Guardrail Design

<Instruction hierarchy, model selection constraints, tool contracts, confirmation boundaries, output schemas, safety controls, and unsupported-action handling.>

## Integration Architecture

### INT-### — <Integration Name>

- **Functional IDs:** <references>
- **Purpose:** <technical purpose>
- **Interface and operation:** <contract without raw secrets>
- **Request mapping:** <fields and source>
- **Response mapping:** <fields and consumers>
- **Timeout and retry:** <policy>
- **Error mapping:** <behavior>
- **Idempotency or correlation:** <strategy>
- **Dependencies:** <profiles, network, ownership, and environment>

## Authentication and Authorization

<User identity, service identity, authorization checks, delegated access, opaque credential or auth-profile references, and least-privilege boundaries. Never include raw secrets.>

## Data, Context, and Session State

<Data classification, source of truth, session variables, durable request state, schema, lifecycle, retention, deletion, and concurrency.>

## Workflow Persistence and Resumption

<For process or hybrid designs: correlation identity, checkpoints, waits, resume events, duplicate-event handling, deadlines, cancellation, terminal states, and recovery. Otherwise explain why this is not applicable.>

## Human Tasks and Approval Architecture

<Task creation, assignment, authorization, evidence shown, decision capture, approve/reject/request-changes handles, reminders, reassignment, expiration, escalation, audit, and resumption. Distinguish this from conversational agent handoff.>

## Error Handling, Retries, and Recovery

<Failure taxonomy, user-safe responses, retry limits, backoff, idempotency, dead-letter or manual recovery, compensation, and unknown-outcome verification.>

## Human Handoff Design

<Handoff destination, eligibility, availability, context package, transcript or state transfer, failure handling, and return or closure behavior.>

## Security, Privacy, and Compliance

<Trust boundaries, sensitive data, encryption, access, logging restrictions, retention, consent, policy enforcement, threats, and required reviews.>

## Observability and Operational Support

<Traces, logs, metrics, business events, alerts, dashboards, runbooks, ownership, service objectives, audit evidence, and support escalation.>

## Testing Strategy

| Test area | Scenarios and acceptance IDs | Environment or fixture | Evidence | Owner |
|---|---|---|---|---|

## Release and Rollback Plan

<Versioning, configuration promotion, approvals, deployment checks, canary or phased release, rollback triggers, recovery, and post-release validation.>

## Technical Risks, Decisions, and Open Questions

### Risks

| Risk | Impact | Mitigation | Owner |
|---|---|---|---|

### Technical decisions

| ID | Decision | Functional IDs | Rationale and evidence | Approver | Status |
|---|---|---|---|---|---|

### Open questions

| ID | Question | Affected IDs | Evidence needed | Owner or next action | Blocking? |
|---|---|---|---|---|---|
```

## Quality rules

- Every component exists for a functional or non-functional reason; avoid speculative architecture inventory.
- Verify Kore.ai-specific claims in current documentation and record the evidence status.
- Use opaque references for credentials and integrations. Never copy secrets into the document.
- Define durable state and resumption explicitly for long-running work; do not model it as an indefinitely open chat session.
- Give side-effecting operations idempotency or unknown-outcome handling proportional to their risk.
- Map acceptance criteria into the testing strategy and keep unresolved blockers in the open-question register.
