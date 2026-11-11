# Architecture decision records (ADRs)

**Languages:** [Português](DECISIONS.md) | [English](DECISIONS.en.md)

These records distinguish baseline decisions from alternatives in the original academic materials. Decisions may change after EVE-NG validation.

## ADR-001 | Incremental lab, not a completed deployment

**Decision:** publish design, sample inventory, configuration and verification stages separately. **Reason:** documentation alone is not evidence of working infrastructure. **Effect:** mark technologies validated only after real tests.

## ADR-002 | Routing differences between the source documents

**Observation:** the LLD suggests OSPF for Gold, static routes or optional OSPF for Silver, and static routes for Bronze. The Implementation Plan also references OSPF in broader scope and Silver. **Baseline decision:** Gold OSPF; Silver static with optional future OSPF; Bronze static. The DC requires a return route to each branch. **Open:** explicitly define OSPF transport across simulated MPLS or VPN without unintended adjacencies.

## ADR-003 | Dual WAN and SD-WAN

**Observation:** the academic planning materials describe static/monitored routing for Bronze in some places and SD-WAN for all tiers elsewhere. **Decision:** begin Bronze failover with monitored static routes; consider SD-WAN in a later, separately tested phase. MPLS does not itself encrypt packets.

## ADR-004 | Addressing and segmentation

**Decision:** reserve `10.ID.X.0/24` networks by site and function; use VLAN 200 /30 transit for Gold/Silver. Bronze has no dedicated transit VLAN in the baseline illustration. **Open:** gateways, HA virtual IPs, trunks and actual interface maps must be verified.

## ADR-005 | Secure publication

**Observation:** some original academic snippets contain literal VPN PSKs, a common `public` SNMP community and overly broad WAN management settings. **Decision:** do not reproduce those secrets or insecure examples. Favor SNMPv3, source restrictions, least privilege and local secret storage. Validate software-specific syntax in the lab.

## ADR-006 | Simulation scope

**Decision:** one representative DC/Gold/Silver/Bronze environment models the 30-to-70-site business case without claiming a complete 70-site deployment. **Reason:** control emulation cost and maintain reproducible troubleshooting.

## ADR-007 | Evidence-first examples and personal ownership

**Decision:** publish bilingual lab procedures and clearly marked unverified templates; maintain the repository as a solely authored portfolio without an external contribution workflow. **Reason:** avoid invented implementation outcomes and keep a consistent technical narrative.

[Roadmap](ROADMAP.en.md) | [Personal project policy](../PERSONAL_PROJECT.en.md)
