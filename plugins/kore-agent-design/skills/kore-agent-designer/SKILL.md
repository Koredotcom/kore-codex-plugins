---
name: kore-agent-designer
description: Guide a Kore.ai agent from an initial idea or supplied material to a traceable functional design and technical design. Use for guided discovery, drafting, updating, design review, gap analysis, readiness assessment, or an implementation handoff. Do not estimate effort or create or modify a Kore.ai project.
---

# Kore Agent Designer

Create or review two traceable artifacts:

1. an **Agent Functional Design (SOP)** describing business behavior; and
2. an **Agent Technical Design** describing a feasible implementation approach.

Support conversational agents, long-running process agents, and hybrids. Do not assume a particular Kore.ai component, deployment environment, integration, or custom-code capability without evidence.

## Choose the operating mode

- **Guide from scratch:** progressively discover the design from an idea.
- **Draft:** turn supplied notes, diagrams, requirements, or SOPs into the templates.
- **Review:** judge the substance of an existing functional or technical design without requiring the source to use these templates.
- **Update:** incorporate new facts while preserving identifiers and traceability.
- **Prepare for implementation:** assess readiness and produce a bounded handoff checklist.

Infer the mode when the request makes it clear. Ask only when the choice would materially change the result.

## Preserve evidence and authority

Keep these states distinct:

- `Confirmed` — stated by the user or supported by supplied evidence.
- `Documented capability` — supported by current public product documentation or environment evidence.
- `Proposed` — a recommendation awaiting a decision.
- `Assumption` — a necessary working premise not yet confirmed.
- `TBD` — an unanswered design question.
- `Not verifiable` — requires unavailable product, environment, security, or architecture evidence.
- `Not applicable` — irrelevant to the design, with a reason.

Never present an inference as an existing capability or approved decision. Missing exported configuration, tool visibility, or secret values are evidence gaps, not proof that an integration or control does not exist.

## Work progressively

For a new idea or thin input, read [references/guided-intake.md](references/guided-intake.md). Ask two to five related questions at a time, starting with the business problem, users, trigger, outcome, and likely operating model. After each meaningful round, summarize confirmed facts, proposals, assumptions, and open questions, then draft what can already be supported.

Build the functional design far enough to anchor the solution before making detailed technical choices. Start the technical design as a working skeleton once those questions become useful; mark gaps instead of inventing answers.

## Create the design artifacts

Read [references/functional-design-template.md](references/functional-design-template.md) before creating or updating the functional design. Read [references/technical-design-template.md](references/technical-design-template.md) before creating or updating the technical design.

For skill-authored documents:

- preserve the template marker and all level-two headings in order;
- retain non-applicable sections with a short reason;
- keep business behavior in the functional design and implementation detail in the technical design;
- preserve stable identifiers rather than renumbering to close gaps;
- use relative companion links when files share a directory; and
- default filenames to `<agent-slug>_functional_design.md`, `<agent-slug>_technical_design.md`, and `<agent-slug>_design_review.md`.

Use these identifiers:

| Prefix | Meaning |
|---|---|
| `UC-###` | User goal or process use case |
| `FR-###` | Functional requirement |
| `BR-###` | Business rule |
| `NFR-###` | Non-functional requirement |
| `INT-###` | Integration requirement |
| `AC-###` | Acceptance criterion |
| `TD-###` | Technical decision |
| `OQ-###` | Open question |

When reviewing a free-form document, judge facts wherever they appear. Different headings are not themselves a design defect.

## Treat process behavior as first-class

For process or hybrid agents, explicitly capture request identity, persisted state, wait and resume events, human-task authorization, decision outcomes, deadlines, cancellation, duplicate events, retries, recovery, audit, and terminal states. Do not model a long-running process as a chat session held open indefinitely.

Use `Not applicable` for process-only sections in a purely conversational design.

## Verify platform-specific claims

Use current public Kore.ai documentation or user-provided environment evidence when product behavior affects the design. Record the evidence used. If authoritative evidence is unavailable, continue with product-neutral questions and mark the implementation choice `Not verifiable`.

Use only documentation and tools available to the user. A connected Kore.ai environment is not required for functional discovery, and this skill must not connect to or modify an environment.

## Review and assess readiness

For review or readiness work, read [references/review-rubric.md](references/review-rubric.md). Review the complete supplied artifact set and use the rubric's statuses, fixed report structure, and readiness verdicts. Do not calculate a numerical score.

Write each finding as:

> missing, weak, or conflicting fact → effect on the design or implementation → exact question or action → affected identifiers

The bundled structural checker is advisory. It helps with documents created from these templates but never replaces semantic review:

```bash
python3 "${PLUGIN_ROOT}/skills/kore-agent-designer/scripts/check_design_structure.py" \
  --functional "<agent>_functional_design.md" \
  --technical "<agent>_technical_design.md"
```

When `PLUGIN_ROOT` is unset during repository-source testing, resolve the script relative to this `SKILL.md`. Treat `PASS`, `WARN`, and `UNRECOGNIZED_FORMAT` only as structural evidence.

## Prepare a public implementation handoff

When the verdict permits project setup, recommend a handoff containing:

- the approved scope and first implementation slice;
- confirmed target product, workspace, and environment—or explicit open questions;
- functional-to-technical traceability;
- integration, identity, data, security, and operational dependencies;
- blocking and nonblocking gaps with owners;
- acceptance tests and release evidence; and
- actions that still require explicit user authorization.

Do not create a project, agent, workflow, integration, deployment, or other platform resource. If the user later asks for implementation, treat it as a separate authorized task and use only tools available to that user.
