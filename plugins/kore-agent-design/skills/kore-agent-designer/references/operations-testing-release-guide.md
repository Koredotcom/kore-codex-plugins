# Operations, testing, and release guide

Read this reference when creating or updating `technical/operations-testing-release.md`.

## Required structure

```markdown
<!-- kore-agent-design:operations-testing-release:v2 -->
# Operations, Testing, and Release: <Agent Name>

## Document Metadata

<Use the metadata block from general-design-guidance.md.>

## Service Objectives and Operational Ownership

| ID | Objective or responsibility | Threshold/scope | Owner | Evidence or status |
|---|---|---|---|---|

## Observability

<Traces, logs, metrics, business events, audit events, correlation, dashboards, alerts, and sensitive-data restrictions.>

## Support and Runbooks

<Support tiers, triage ownership, diagnostic context, escalation, manual recovery, business continuity, and runbook requirements.>

## Test Strategy and Traceability

| Test area | UC/FR/NFR/EXP/AC/API IDs | Scenarios | Environment or fixture | Evidence | Owner |
|---|---|---|---|---|---|

## Wave 1 Verification

<Foundation checks, selected use-case acceptance, experience validation, integration/contract tests, security evidence, performance evidence, and business-outcome measurement.>

## Release Plan

<Versioning, environment promotion, approvals, configuration checks, migration/coexistence, pilot/canary/phased release, communications, and go-live criteria.>

## Rollback and Recovery

<Rollback triggers, configuration/code/data rollback, in-flight work, compensation, recovery validation, and decision authority.>

## Post-Release Validation

<Smoke tests, monitoring period, success metrics, incident threshold, ownership, and closeout evidence.>

## Operational Decisions and Open Questions

| ID | Decision or question | Affected IDs | Evidence needed | Owner | Blocking? |
|---|---|---|---|---|---|
```

## Category rules

- Map acceptance criteria into tests; do not use an untraceable generic test checklist.
- Include business events and outcomes, not only infrastructure telemetry.
- Define release and rollback for the actual Wave 1 shape and in-flight state.
- Give every critical alert, runbook, manual action, and go-live decision an owner.
- Keep thresholds `TBD` when unconfirmed and treat blocking missing evidence accordingly.
