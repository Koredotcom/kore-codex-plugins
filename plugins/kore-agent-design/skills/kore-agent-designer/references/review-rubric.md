# Agent design review rubric

Review facts across the complete artifact set, not merely the expected headings. A differently structured source can be substantively complete. Run the optional structural checker only as supporting evidence.

## Criterion statuses

- `Complete` — specific enough to guide the next stage and supported by the available evidence.
- `Partial` — present but too thin, ambiguous, or incomplete to rely on fully.
- `Missing` — applicable information is absent.
- `Conflicting` — supplied evidence disagrees in a way that affects scope, behavior, architecture, or readiness.
- `Not verifiable` — applicable but requires platform, environment, security, or architecture evidence not available to the reviewer.
- `Not applicable` — irrelevant to the stated design, with a reason.

Do not calculate a numerical score.

## Functional review

Check whether the design makes these facts usable:

- business problem, agent charter, measurable outcome, owner, and intended users;
- agent operating model and boundaries between conversation, workflow, system, and human work;
- in-scope and out-of-scope use cases with triggers and terminal outcomes;
- reconstructible happy paths, branches, validation, failures, and recovery;
- business rules, inputs, source systems, knowledge needs, and ownership;
- human handoff and process approval treated as distinct behaviors;
- long-running state, deadlines, cancellation, resumption, and audit where applicable;
- privacy, authorization, safety, and regulated-decision boundaries;
- measurable non-functional requirements; and
- acceptance criteria that demonstrate each important outcome.

## Technical review

Check whether the design provides:

- traceability from functional needs to technical treatment;
- a bounded system context and justified Kore.ai component mapping;
- platform evidence for product-specific claims;
- environments, configuration ownership, deployment, and promotion expectations;
- conversation, workflow, routing, model, prompt, tool, knowledge, and guardrail design;
- integration contracts, data mapping, authentication references, timeouts, and error mapping;
- session state and durable state with clear sources of truth;
- human-task authorization, decisions, deadlines, handles, audit, and resumption;
- retry, idempotency, compensation, cancellation, and unknown-outcome handling;
- security, privacy, retention, observability, and operational ownership;
- testing tied to acceptance criteria; and
- release, rollback, and post-release verification.

## Consistency checks

- Every in-scope `UC-###` has an SOP and acceptance coverage.
- Functional requirements are technically addressed, explicitly deferred, or identified as blocking.
- Technical components trace to functional or non-functional needs.
- Actors, systems, channels, languages, and environment assumptions agree across documents.
- Human-task outcomes in the functional design have matching technical routes.
- Integration and data names are used consistently.
- Success measures, service objectives, and test thresholds do not contradict one another.
- Confirmed decisions are not simultaneously listed as unresolved assumptions.

## Readiness verdicts

### NOT READY

Use when a missing fact or contradiction would make the next stage materially wrong or unsafe. Examples include no clear agent outcome, unreconstructible core use cases, undefined authorization for a consequential action, no identified source system for required data, unhandled approval outcomes, or an unverified platform dependency that determines the architecture.

### READY FOR TECHNICAL DESIGN

Use when the functional scope and behavior are specific enough to design, but technical choices or evidence remain materially incomplete. List the exact technical decisions and owners needed next.

### READY WITH TRACKED GAPS

Use when project setup and a bounded first implementation slice can begin safely, while nonblocking gaps remain explicitly owned and tracked. State which work must not proceed until each gap is resolved.

### READY FOR PROJECT SETUP

Use when the functional and technical designs support project creation and the intended first slice, no critical blocker remains, platform-dependent architecture has adequate evidence, and risks or minor unknowns have owners.

## Fixed review output

```markdown
# Agent Design Review: <Agent Name>

## Headline

<One or two sentences stating overall readiness and the principal reason.>

## Readiness Verdict

NOT READY | READY FOR TECHNICAL DESIGN | READY WITH TRACKED GAPS | READY FOR PROJECT SETUP

## Critical Blockers

<Blocking findings, or “None.”>

## Functional Coverage

<Concise status by material functional area; emphasize Partial, Missing, Conflicting, and Not verifiable.>

## Technical Coverage

<Concise status by material technical area; emphasize Partial, Missing, Conflicting, and Not verifiable.>

## Traceability

<Unmapped requirements, unjustified components, conflicting identifiers, or “No material traceability gaps found.”>

## Process and Approval Coverage

<Wait, human-task, approval, resumption, deadline, cancellation, recovery, and audit findings; or the reason this is Not applicable.>

## Platform Evidence

<Documentation or environment evidence used, plus every relevant item that remains Not verifiable.>

## Findings

### <Finding title> — <Status>

**Evidence:** <quote, reference, or “not stated”>

**Impact:** <effect on design or build>

**Ask or action:** <exact question or correction>

**Affected IDs:** <identifiers or section>

## Questions to Resolve

<Short, ordered questions suitable for the next conversation.>

## Recommended Next Step

<The smallest useful next action. Include an implementation handoff checklist only when the readiness boundary is met.>
```

List every critical blocker and material contradiction. Avoid cataloging every correct fact when the document is ready.

## Implementation handoff rule

For `READY FOR PROJECT SETUP`, provide a bounded implementation handoff covering the approved first slice, target product and environment, dependencies, unresolved decisions, traceability, acceptance tests, and actions requiring explicit authorization. For `READY WITH TRACKED GAPS`, provide the same handoff only when none of the tracked gaps blocks safe project setup or the bounded first slice. Do not connect to or modify a Kore.ai environment as part of this skill.
