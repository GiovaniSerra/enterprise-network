# Evidence | Verification standard

**Languages:** [Português](README.md) | [English](README.en.md)

**Current state:** no enterprise networking test outputs were published in the foundation release. Complete this form **only after executing the test**.

## Required record

```text
Test ID:
Milestone / site:
Date and time (with timezone):
Author:
Actual lab platform and image/software version:
Objective:
Topology / expected path:
Prerequisites:
Command or procedure:
Expected result:
Observed result (sanitized output/screenshot):
Pass / fail / partial:
Time / packet loss / metrics (where applicable):
Known limitations and follow-up:
Configuration commit reference:
```

## Publication rules

- Screenshots must contain useful context and software versions but **never** secrets, PSKs, customer data, license files or real credentials.
- Captures, logs and screenshots need written technical interpretation.
- A device screenshot alone does not prove failover, policy enforcement, HA or encryption.
- Include positive and negative cases when relevant.
- Document failed tests and unknown root causes; do not fabricate success.

Example naming convention: `M1-GOLD-T01-vlan110-gateway.md`, `M3-DC-T03-ipsec-rxtx.md`. For the initial lab, use the bilingual [M1 results template](../labs/M1-GOLD-LAN/RESULTS.template.en.md).
