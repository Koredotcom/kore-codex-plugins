# Kore Agent Designer forward-test scenarios

Run substantial revisions in a clean task with the repository-source or freshly installed skill. Judge observable decisions and artifacts, not exact wording.

## Scenario 1: start a conversational agent from one sentence

Prompt:

> Use `$kore-agent-designer` to help me design an authenticated employee HR policy assistant. I only have the idea so far.

Expected behavior:

- Starts with two to five high-value charter questions rather than the entire template.
- Identifies the design as likely conversational and asks the user to correct that proposal.
- Separates confirmed facts, proposals, assumptions, and open questions.
- Progressively creates the fixed functional design and a traceable technical skeleton.
- Marks process-only sections `Not applicable` with a reason instead of treating them as gaps.

## Scenario 2: process agent with human approval and a long wait

Prompt:

> Use `$kore-agent-designer` to design a vendor-access request process. An employee submits a request, security runs predefined checks, the data owner may approve a week later, and provisioning resumes after approval. Rejections, expiration, cancellation, reminders, and audit records matter.

Expected behavior:

- Classifies the design as process-oriented or hybrid based on the interaction surface.
- Asks about correlation, persisted state, task assignment and authorization, evidence shown, every decision outcome, deadlines, resumption, duplicate events, recovery, and audit.
- Does not model the week-long wait as an open conversational session.
- Keeps business behavior in the functional SOP and persistence or workflow mechanics in the technical design.

## Scenario 3: review an unstructured document

Prompt:

> Use `$kore-agent-designer` to review this free-form agent design. Do not rewrite it yet; tell me whether it is ready for technical design and what I must resolve.

Expected behavior:

- A structural preflight may return `UNRECOGNIZED_FORMAT`, but that is not reported as a defect.
- Reads the complete artifact and judges facts wherever they occur.
- Uses the fixed review report, criterion statuses, and a supported readiness verdict.
- Writes findings as gap or conflict, impact, exact ask or action, and affected identifiers or sections.

## Scenario 4: ready design and implementation handoff

Prompt:

> Review these completed functional and technical designs and recommend what I should do next.

Expected behavior:

- Checks semantic completeness, consistency, traceability, platform evidence, and blockers even if the structural preflight passes.
- Uses `READY FOR PROJECT SETUP` only when the documented boundary is met.
- Produces a bounded handoff covering the approved first slice, target product and environment, dependencies, tracked gaps, traceability, and acceptance evidence.
- Does not create or modify platform resources based only on the review request.
- States which later implementation actions would require explicit user authorization.

## Scenario 5: platform documentation unavailable

Prompt:

> Draft the technical design, but I cannot connect you to a Kore environment or documentation service today.

Expected behavior:

- Continues with product-neutral architecture questions and documented user facts.
- Marks product-specific claims `Not verifiable` rather than relying on memory or inventing support.
- Does not block functional progress solely because the platform connection is unavailable.
- Does not issue `READY FOR PROJECT SETUP` when an unverified platform dependency determines the architecture.


## Scenario 6: explicitly authorized project setup

Prompt:

> The reviewed design is ready. Start project setup for its first approved use case in my confirmed development workspace. Use the available platform tools.

Expected behavior:

- Reuses confirmed workspace and scope; asks only for missing project identifiers or blockers.
- Discovers the available project-builder contract before mutation.
- Implements only the authorized slice and preserves requirement traceability.
- Verifies unknown outcomes before retrying; reports unavailable capabilities honestly.
- Falls back to a handoff checklist if no platform tools are available.
