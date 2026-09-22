# Guided intake

Use this reference when the user starts from an idea, thin notes, or incomplete evidence. The goal is a productive design conversation, not completion of a questionnaire.

Ask two to five related questions at a time. Prefer questions the current user can answer and name the role or evidence source needed for others. After each meaningful round, summarize confirmed facts, proposals, assumptions, open questions, and documents that can now be drafted.

Do not repeat answered questions because the answer appeared in an unexpected source. Do not block on noncritical unknowns. Assign an `OQ-###` when an unresolved point affects scope, wave placement, behavior, architecture, security, or readiness.

## Opening: sources and working folder

Ask for:

- a discovery intake or equivalent customer-approved scope artifact;
- requirements, SOPs, architecture diagrams, API material, and source-of-truth folder;
- the target working folder for generated files; and
- whether an existing modular package should be updated.

If customer-agreed discovery evidence is unavailable, continue with the provisional-scope notice in `SKILL.md`. Do not ask for the working folder again when an explicit destination was already provided.

## Round 1: agent charter

Discover enough to state:

- the business problem and why an agent is appropriate;
- primary users, decision owners, and stakeholders;
- initiating events or user requests;
- desired outcomes and measurable success;
- agent boundaries and explicit exclusions; and
- likely operating model: conversational, process, or hybrid.

Draft the index context and agent definition as soon as this is stable enough. Explain the signals behind the proposed operating model.

## Round 2: scope, waves, and priority

Inventory distinct business outcomes and separate them from welcome behavior, fallback, reminders, lifecycle hooks, and generic escalation. For each candidate use case, capture:

- trigger, actors, outcome, volume, and business value;
- main steps, variations, failures, systems, and data;
- access, API, content, environment, and owner readiness;
- foundation dependencies and channel/language needs;
- Value, Speed, and Readiness scores when supplied or explicitly confirmed; and
- proposed or approved wave placement.

Preserve a customer-approved Wave 1 selection. When scope is only proposed, label it accordingly. Wave 1 contains foundation plus at least one use case and defaults to a 30-working-day planning target unless another target is confirmed.

## Round 3: use-case SOPs

Work through one use case or a small related group at a time. Ask for business-level steps, inputs and validation, rules, branches, terminal outcomes, correction, handoff, knowledge, systems, and acceptance scenarios.

For work that waits, runs asynchronously, or involves a person, ask about correlation, persisted state, task assignment and authorization, evidence shown, every decision outcome, deadlines, reminders, resumption, duplicate events, cancellation, recovery, audit, and status visibility.

Keep endpoints, payloads, node types, prompt text, and code out of functional SOPs.

## Round 4: experience design

Identify where modalities materially change behavior.

- For voice, discover telephony context, identity, languages, persona, turn-taking, interruption, silence, recognition repair, confirmations, sensitive values, latency, transfer, disconnects, accessibility, and acceptance measures.
- For digital channels, discover capability differences, content formats, session/asynchronous behavior, identity, privacy, delivery failure, handoff, accessibility, and channel fallbacks.

Create only applicable experience documents and trace their requirements to use cases.

## Round 5: technical design

Begin technical category documents when functional scope is stable enough to make useful choices. Discover:

- product/component mapping, system context, trust boundaries, environments, state, workflow, model, prompt, tools, knowledge, and guardrails;
- connectivity, service identity, integration behavior, retries, idempotency, and recovery;
- API operations, request/response mappings, errors, authorization, and contract evidence;
- data classification, authorization, retention, privacy, security, and audit; and
- observability, support, testing, release, rollback, and post-release verification.

Use current evidence for platform-specific claims. Mark unavailable evidence `Not verifiable` rather than relying on memory.

## Round 6: reconcile and assess readiness

Cross-check the complete package:

- the index lists every document and matches its metadata;
- wave assignments and approved baselines do not conflict;
- every in-scope use case has SOP and acceptance coverage;
- experience requirements map to use cases;
- functional requirements have technical treatment or explicit blockers;
- integrations and APIs map to functional needs;
- shared facts have one canonical owner;
- open questions and dependencies have owners and next actions; and
- Wave 1 foundation and selected use case have evidence supporting the target.

Run the structural checker, then apply the semantic review and readiness guide. Ask only the questions that can materially improve the next verdict.
