# Guided intake

Use this intake when the user starts from an idea, thin notes, or an incomplete design. The objective is a productive conversation, not completion of a form.

## Conversation pattern

Ask two to five related questions in a round. Prefer questions the current user can answer; identify the role or evidence source needed for questions they cannot answer. After each round, summarize confirmed facts, proposals, assumptions, open questions, and what can now be drafted.

Do not repeat an answered question because the answer appeared outside its expected section. Do not block progress on noncritical unknowns. Give each unresolved question an `OQ-###` identifier as soon as it affects scope, behavior, architecture, security, or readiness.

## Round 1: establish the agent charter

Discover enough to state:

- the business problem and why an agent is appropriate;
- primary users and stakeholders;
- initiating event or user request;
- desired outcome and how success will be measured;
- initial scope and explicit exclusions; and
- likely operating model: conversational, process, or hybrid.

Offer a short working charter and ask the user to correct it. Do not ask the user to select an agent type without explaining the observed signals.

## Round 2: inventory the work

Identify distinct user goals or process outcomes. For each candidate use case, capture the trigger, actors, preconditions, inputs, normal outcome, important branches, failure outcomes, and any human involvement.

Separate user-initiated business goals from welcome behavior, fallback, background events, reminders, lifecycle hooks, and default escalation. Combine variants only when they share the same business outcome and differ by a small rule or channel detail.

Draft the use-case inventory as soon as the goals are distinguishable. Assign stable `UC-###` identifiers and never reuse a retired identifier.

## Round 3: deepen the functional SOPs

Work through one use case or a small related group at a time. Ask for:

- business-level steps in sequence;
- information collected, source, validation, and permitted correction;
- decisions and business rules;
- alternative and exception paths;
- confirmation, completion, and handoff behavior;
- knowledge or content needed;
- systems involved and the business action each performs; and
- acceptance scenarios that demonstrate the outcome.

Describe what the agent and other actors do. Keep endpoints, payloads, credentials, node types, and code out of the functional SOP.

## Process and hybrid branch

When work can pause, run asynchronously, or involve a person, ask about:

- how a request is identified and how duplicate requests are handled;
- what state must survive the wait;
- who owns the human task and how they are authorized;
- what evidence the person sees before deciding;
- approve, reject, request-changes, reassign, expire, cancel, and escalate outcomes;
- deadlines, reminders, and service levels;
- what resumes the workflow and where it resumes;
- retries, recovery, and compensating actions; and
- status visibility, notifications, and audit evidence.

Do not assume that a long-running task is a conversational session held open. Treat persistence, correlation, wait state, and resumption as explicit design concerns.

## Round 4: establish technical constraints

Begin the technical design as soon as functional scope is stable enough to ask useful questions. Discover:

- relevant Kore.ai products or components;
- channels, languages, identity, and access model;
- environment and deployment expectations;
- orchestration pattern and agent responsibilities;
- model, prompt, tool, knowledge, and guardrail needs;
- integrations, authentication references, contracts, and data mappings;
- session, request, workflow, and durable state;
- human-task and approval implementation;
- failure, retry, timeout, cancellation, and recovery behavior;
- security, privacy, compliance, and retention constraints;
- observability, support ownership, and service objectives; and
- test, release, rollback, and operational-readiness expectations.

Use current platform documentation for product-specific claims. When documentation cannot be reached, phrase questions product-neutrally and mark the implementation choice `Not verifiable`.

## Round 5: reconcile and decide readiness

Cross-check the two documents:

- every in-scope use case has an SOP and acceptance criteria;
- every functional requirement is addressed or explicitly deferred;
- every technical component has a functional or non-functional reason;
- process wait states and human decisions have technical treatment;
- assumptions and open questions have owners or next actions;
- platform-dependent choices have evidence or are marked unverified; and
- security, operations, testing, and release responsibilities are not silently omitted.

Apply the review rubric. If the design is ready for project setup, offer a public implementation handoff checklist covering the approved scope, target environment, dependencies, remaining decisions, and acceptance evidence. If it is not ready, ask only the questions that materially improve the next verdict.
