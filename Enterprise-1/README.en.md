# Enterprise-1 | Integrated enterprise networking case study

**Languages:** [Português](README.MD) | [English](README.en.md) | [Home](../README.en.md)

A fictional credit union must connect a central Data Center to Gold, Silver and Bronze branch classes. The design originates from two academic reports written by the author and has been reorganized into an **incremental, evidence-driven network engineering project**.

![Gold reference topology](Topology/Gold%20site/Gold%20-%20topology.png)

> **Status: design stage.** This image is a conceptual reference, not proof of running links, HA, VLANs or VPN tunnels. Silver+ is an optional design variant, outside the initial scope.

## Requirements

1. Connect branches to central services with valid return paths and explicit access policies.
2. Isolate users, guests, management, voice, printers and security systems.
3. Apply resiliency proportionally without assuming HA on Bronze sites.
4. Design primary WAN and backup IPsec paths without equating MPLS with encryption.
5. Document real failures, verification procedures and limitations as well as configuration.

## Site tiers

| Site | Representative scope | Proposed LAN / security | Baseline routing | Status |
| --- | --- | --- | --- | --- |
| DC | Central services and VPN hub | Network services + NGFW | To be designed/tested | Planned |
| Gold | ~100-150 users | Dual L3 core, NGFW HA, dual WAN | OSPF, future phase | Planned |
| Silver | Up to ~60 users | Single L3 core, alternate WAN | Static; optional OSPF | Planned |
| Bronze | Up to ~30 users | Single switch and firewall | Static | Planned |

## Project guides

| Topic | Document |
| --- | --- |
| HLD architecture | [High Level Design](HLD/README.en.md) |
| LLD addressing and VLANs | [Low Level Design](LLD/README.en.md) |
| Topology gallery | [Topologies](Topology/README.en.md) |
| Traffic flows | [Flows](FLOW/README.en.md) |
| Implementation plan | [Implementation phases](Implementation/README.en.md) |
| **Reproducible labs** | **[Lab index](labs/README.en.md)** |
| **M1: Gold LAN segmentation** | **[Full lab guide](labs/M1-GOLD-LAN/README.en.md)** |
| Operations and security | [Security](SECURITY.en.md) and [Troubleshooting](Troubleshooting/README.en.md) |
| Evidence and QA | [Evidence guidelines](evidence/README.en.md) and [Inventory](inventory/README.en.md) |
| Decisions and references | [ADRs](DECISIONS.en.md) and [Academic sources](SOURCES.en.md) |
| Milestones | [Roadmap](ROADMAP.en.md) |

## Evidence requirements

Every module should contain a topology, port mapping, software images/versions, sanitized configuration, commands, expected versus observed outcomes, packet captures and failure analysis. `Validated` status requires actual test execution. No fabricated test evidence has been added.
