# Scenario 03 | IPsec tunnel does not establish

**Languages:** [Português](README.MD) | [English](README.en.md)

**Status:** procedure not executed.

**Objective:** investigate IPsec negotiation failures between a branch and the DC hub in an isolated lab.

## Diagnostic matrix

| Layer | Question | Evidence |
| --- | --- | --- |
| Underlay | Are peers reachable? Are UDP 500/4500 or ESP traversing where applicable? | WAN trace / packet capture |
| IKE | Compatible IKEv2 proposals, IDs and authentication? | Phase 1 logs |
| Child SA | Compatible proposals and traffic selectors? | Phase 2/SA state |
| Routing | Are the relevant prefixes routed toward the tunnel? | Route tables |
| Firewall/NAT | Are policies correct and intersite sources preserved? | Session and policy logs |
| Liveness | DPD and return path on the right interface? | Tunnel state and counters |

## Acceptance

SAs negotiate using documented parameters without publishing secrets, counters grow when authorized traffic flows, unexpected private NAT is absent, and denied traffic remains denied. Both positive and negative cases require sanitized [evidence](../../evidence/README.en.md).
