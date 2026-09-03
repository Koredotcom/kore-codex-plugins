# Agent Functional Design template

Use this template for every skill-authored functional design. Preserve the marker, document type, all level-two headings, and heading order. Replace angle-bracket prompts with content; do not leave raw prompts in a delivered document. Use `Not applicable — <reason>` when a section does not apply.

```markdown
<!-- kore-agent-design-template:v1 -->
# Agent Functional Design (SOP): <Agent Name>

**Document type:** Functional
**Status:** Working Draft | In Review | Approved
**Companion technical design:** <relative link, TBD, or Not requested>

## Document Control

| Field | Value |
|---|---|
| Owner | <name or role> |
| Contributors | <names or roles> |
| Version | <version> |
| Last updated | <date> |
| Approval status | <status and approver> |
| Evidence sources | <source artifacts or conversations> |

## Agent Purpose and Business Outcome

<Problem, agent charter, expected outcome, measurable value, and success definition.>

## Agent Type and Operating Model

**Type:** Conversational | Process | Hybrid

<How users, events, workflows, agents, and humans participate. State explicitly whether work may pause or outlive a conversation.>

## Users, Stakeholders, and Roles

| Role or persona | Needs and responsibilities | Access or approval authority |
|---|---|---|

## Scope

### In scope

<Bounded capabilities and phase.>

### Out of scope

<Explicit exclusions and later phases.>

## Channels, Languages, and Experience Constraints

<Channels, locales, accessibility, response-time, modality, identity, and experience constraints.>

## Assumptions and Dependencies

| ID | Status | Assumption or dependency | Owner or validation action |
|---|---|---|---|

## User Goals and Use-Case Inventory

| ID | Use case | Actor or trigger | Business outcome | Priority | Status |
|---|---|---|---|---|---|

## Functional SOPs

### UC-### — <Use Case Name>

**Business objective:** <objective>

**Trigger:** <user request or event>

**Actors:** <users, systems, agent, and human roles>

**Preconditions:** <required state>

**Required inputs:** <information and source>

**Functional requirements:** <FR-### references>

**Business rules:** <BR-### references>

**Steps:**

1. <business-level agent or actor action>

**Branches and exceptions:**

- <condition -> behavior and destination>

**Validation and correction:** <validation rules and recovery>

**Human involvement:** <task, approval, handoff, or Not applicable>

**Completion outcome:** <observable terminal result>

**Acceptance criteria:** <AC-### references with testable scenarios>

## Long-Running Workflows, Human Tasks, and Approvals

<For process or hybrid designs: correlation identity, persisted state, waits, task assignment, authorization, information shown, approve/reject/request-changes paths, reminders, timeouts, resumption, cancellation, recovery, audit, and terminal states. For a purely conversational design, state why this is not applicable.>

## Knowledge and Content Requirements

<Content sources, ownership, freshness, permissions, retrieval expectations, citations, gaps, and fallbacks.>

## Functional Integration Requirements

| ID | System | Business action | Data exchanged | Triggering use cases | Failure expectation |
|---|---|---|---|---|---|

## Human Handoff and Escalation

<When, why, and to whom work transfers; context provided; availability behavior; user expectations; and unsuccessful-transfer handling. Distinguish conversational handoff from a process approval task.>

## Guardrails, Privacy, and Compliance

<Allowed and prohibited behavior, authorization boundaries, sensitive data, consent, retention, regulated decisions, and required human oversight.>

## Non-Functional Requirements

| ID | Category | Requirement and measurable threshold | Applies to | Evidence or owner |
|---|---|---|---|---|

## Success Measures and Acceptance Criteria

| ID | Requirement or use case | Given / When / Then or measurable criterion | Evidence method | Owner |
|---|---|---|---|---|

## Risks, Decisions, and Open Questions

### Risks

| Risk | Impact | Mitigation | Owner |
|---|---|---|---|

### Confirmed decisions

| Decision | Rationale | Approver | Date |
|---|---|---|---|

### Open questions

| ID | Question | Why it matters | Owner or next action | Blocking? |
|---|---|---|---|---|
```

## Quality rules

- Give each distinct business outcome its own `UC-###`; do not create use cases for generic welcome, fallback, or lifecycle behavior.
- Steps describe business behavior, not HTTP methods, payloads, platform nodes, prompt text, or code.
- Every branch names its condition and resulting behavior. Avoid an undifferentiated final “error handling” step.
- Human approval is not the same as conversational escalation. Document both when both exist.
- Acceptance criteria must be observable and trace to a use case or requirement.
- Keep deferred scope in the document, clearly marked; do not silently erase it.
