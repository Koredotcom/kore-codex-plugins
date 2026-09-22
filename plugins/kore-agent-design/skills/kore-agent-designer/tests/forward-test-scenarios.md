# Kore Agent Designer forward-test scenarios

Run substantial revisions in a clean task with the repository-source or freshly installed skill. Judge observable decisions and generated artifacts, not exact wording.

## Scenario 1: idea without discovery material

Prompt:

> Use `$kore-agent-designer` to help me design an authenticated employee HR policy assistant. I have only the idea so far.

Expected behavior:

- Asks for discovery or equivalent evidence and a working folder before writing files.
- Continues without discovery, gives the provisional-scope notice once, and does not imply customer approval.
- Starts with two to five charter questions and creates the index before category documents.
- Uses the modular package and marks unresolved wave placement `Proposed`.

## Scenario 2: customer-approved Wave 1 input

Prompt:

> Use `$kore-agent-designer` to turn this discovery package into a design. It contains agreed foundation scope, Value/Speed/Readiness scores, one selected Phase 1 use case, later phases, and a 30-working-day target. Write to the supplied output folder.

Expected behavior:

- Preserves the approved scope baseline, maps Phase 1 to Wave 1, and records evidence in the index.
- Writes and validates the minimum governed package before expanding into experience and technical categories.
- Creates foundation and prioritization registers without inventing scores or effort.
- Designs at least the selected use case and assesses whether access, dependencies, architecture, integrations, and data support the target.
- Records proposed scope changes separately rather than rewriting the approved baseline.

## Scenario 3: bulk multi-use-case requirements

Prompt:

> Use `$kore-agent-designer` on this large requirements package with six use cases, voice and web, and several integrations.

Expected behavior:

- Establishes source inventory, index, identifier allocation, wave baseline, and document map before parallel work.
- When subagents are available, delegates only independent use cases or categories with bounded source evidence and identifiers.
- Keeps index, agent definition, wave scope, shared identifiers, reconciliation, and final validation under one coordinator.
- Produces the same governed package serially when subagents are unavailable.

## Scenario 4: enterprise voice experience

Prompt:

> Add voice to the approved design for the Wave 1 use case.

Expected behavior:

- Reads the general, index, use-case, and voice references.
- Covers telephony context, turn-taking, silence, barge-in, recognition repair, confirmation, sensitive values, latency, transfer, disconnect, accessibility, and voice tests.
- Traces `EXP-###` and voice acceptance criteria to the applicable use case.
- Updates the index and affected technical/testing documents without duplicating functional behavior.

## Scenario 5: controlled scope change

Prompt:

> Move UC-003 into Wave 1 and update the design.

Expected behavior:

- Preserves the approved baseline and records a `CHG-###` with rationale, status, owner, affected IDs/documents, and effective version.
- Reviews foundation, dependencies, integrations, APIs, experience, tests, and 30-working-day feasibility.
- Updates wave placement only through the index, then reconciles affected metadata and links.
- Does not report readiness while a material feasibility or approval blocker remains.

## Scenario 6: free-form or legacy review

Prompt:

> Review these existing functional and technical designs. Do not rewrite them yet.

Expected behavior:

- Judges facts across the full artifact set rather than penalizing different headings.
- Uses legacy structural checks only as advisory evidence.
- Reports semantic gaps, traceability, drift, and readiness with exact actions.
- Migrates to the modular package only when requested.

## Scenario 7: explicitly authorized setup

Prompt:

> The reviewed Wave 1 design is ready. Start project setup for the first approved use case in my confirmed development workspace.

Expected behavior:

- Reuses confirmed scope and environment, discovers the platform project-builder contract, and builds only the approved slice.
- Verifies unknown outcomes before retrying and reads back created resources where supported.
- Reports implemented scope and remaining gaps.
- Falls back to an implementation handoff when project-building tools are unavailable.
