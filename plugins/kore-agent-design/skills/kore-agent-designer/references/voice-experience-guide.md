# Voice experience guide

Read this reference when voice, IVR, or telephony is in scope. Create `experience/voice.md` and keep it focused on behavior that differs from text or asynchronous channels.

## Required structure

```markdown
<!-- kore-agent-design:voice-experience:v2 -->
# Voice Experience: <Agent Name>

## Document Metadata

<Use the metadata block from general-design-guidance.md.>

## Voice Scope and Telephony Context

<Applicable use cases and waves, inbound/outbound direction, entry points, carrier or contact-center dependencies, authentication context, languages, locales, operating hours, and exclusions.>

## Persona, Speaking Style, and Prompt Shape

<Tone, pace, vocabulary, sentence length, disclosure, pronunciation needs, and rules for making content speakable.>

## Turn-Taking and Conversation Control

| ID | Situation | Expected behavior | Timing or limit | Applicable use cases |
|---|---|---|---|---|
| EXP-### | <opening, listening, interruption, pause, repair, closing> | <behavior> | <threshold or TBD> | UC-### |

## Recognition and Understanding

<ASR assumptions, confidence handling, no-input/no-match behavior, accent/noise considerations, spelling and digit capture, language detection, and fallback.>

## Confirmation and Sensitive Values

<What requires implicit or explicit confirmation; normalization and read-back for dates, times, currency, identifiers, and numbers; masking and rules against speaking sensitive values.>

## Latency and Long-Running Actions

<Response-time targets, progress cues, silence prevention, hold behavior, asynchronous completion, callback or notification, and timeout recovery.>

## Transfer and Human Handoff

<Transfer triggers, destination, hours and availability, queue behavior, context package, warm/cold transfer, failure handling, and what the caller hears.>

## Errors, Degradation, and Recovery

<Telephony failure, recognition failure, backend delay, repeated misunderstanding, disconnect, reconnect or callback, and safe termination.>

## Accessibility, Locale, and Compliance Constraints

<Supported accessibility needs, locale-specific phrasing and formats, recording or consent requirements supplied by the user, and retention or disclosure constraints.>

## Voice Acceptance Criteria

| ID | Scenario | Given | When | Then | Measurement or evidence |
|---|---|---|---|---|---|

## Open Questions

| ID | Question | Affected use cases | Owner or evidence needed | Blocking? |
|---|---|---|---|---|
```

## Category rules

- Specify no-input, no-match, barge-in, interruption recovery, and disconnect behavior; happy-path prompts alone are insufficient.
- Design prompts for listening: concise chunks, clear choices, and progressive disclosure. Do not read tables, markup, long identifiers, or raw URLs aloud.
- Define confirmation proportional to consequence. Avoid repeatedly speaking sensitive values.
- State latency thresholds when confirmed. When unknown, mark them `TBD` and define the experience during delay.
- Trace each `EXP-###` and voice `AC-###` to applicable `UC-###` identifiers.
- Keep provider-specific settings in technical documents unless the setting directly changes caller behavior.
