# Digital experience guide

Read this reference when web, mobile, messaging, collaboration, SMS, or email behavior materially affects the design. Create one experience file per distinct interaction model, not automatically per channel.

## Required structure

```markdown
<!-- kore-agent-design:digital-experience:v2 -->
# Digital Experience: <Experience Name>

## Document Metadata

<Use the metadata block from general-design-guidance.md.>

## Scope and Applicable Channels

<Channels, use cases, waves, authentication context, languages, devices, and exclusions.>

## Interaction and Content Model

<Message length, cards/forms/attachments, navigation, progressive disclosure, citations, accessibility, formatting, and unsupported-content fallback.>

## Session and Asynchronous Behavior

<Session continuity, inactivity, resume, notifications, delayed work, duplicate messages, ordering, and cross-device behavior.>

## Channel Variations

| ID | Channel or condition | Expected behavior | Constraint | Applicable use cases |
|---|---|---|---|---|

## Identity, Privacy, and Confirmation

<Identity signals, reauthentication, sensitive display, confirmation, consent, and shared-device considerations.>

## Handoff and Failure Experience

<Transfer, context package, availability, delivery failure, retry, unavailable features, and recovery.>

## Experience Acceptance Criteria

| ID | Scenario | Given | When | Then | Evidence method |
|---|---|---|---|---|---|

## Open Questions

| ID | Question | Affected use cases | Owner or evidence needed | Blocking? |
|---|---|---|---|---|
```

## Category rules

- Group channels only when their interaction and capability constraints are materially the same.
- Define fallback when a card, form, attachment, deep link, notification, or formatting feature is unavailable.
- Treat email and asynchronous messaging differently from a live chat session when timing and ordering matter.
- Trace each `EXP-###` and experience `AC-###` to applicable use cases.
- Keep transport configuration and payload mechanics in technical documents.
