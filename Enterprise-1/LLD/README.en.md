# LLD | Low Level Design (lab baseline)

**Languages:** [Português](README.MD) | [English](README.en.md)

This document presents **proposed configuration conventions**, not verified device running-configs. The academic materials contain additional options and internal inconsistencies, which are tracked in the [decision register](../DECISIONS.en.md).

## IPv4 convention

Each site has a unique `ID` from 1 through 254 and reserves the **logical allocation pool** `10.ID.0.0/16`. The sample Data Center uses ID 0. The [synthetic JSON inventory](../inventory/sites.json) illustrates this model.

| VLAN | Purpose | Illustrative network | Role |
| ---: | --- | --- | --- |
| 5 | Dedicated native VLAN, no end hosts | N/A | Where required for trunks |
| 100 | Management | `10.ID.0.0/24` | Restricted device access |
| 110 | Wired users | `10.ID.10.0/24` | Corporate endpoints |
| 120 | Corporate Wi-Fi | `10.ID.20.0/24` | Authenticated wireless |
| 130 | Guest Wi-Fi | `10.ID.30.0/24` | Internet-only intent |
| 140 | Voice | `10.ID.40.0/24` | VoIP; QoS in later phases |
| 150 | Printers | `10.ID.50.0/24` | Explicit permitted flows |
| 160 | CCTV | `10.ID.60.0/24` | Physical security devices |
| 170 | Physical access control | `10.ID.70.0/24` | Door controllers/readers |
| 200 | Core-to-firewall transit | `10.ID.254.0/30` | Gold and Silver baseline |
| 700 | Quarantine | `10.ID.200.0/24` | Future NAC use |
| 999 | Unused port VLAN | No address | Where supported |

VLAN 700 and 999 are **reserved design elements**, not evidence of deployed NAC. Gateways, HA virtual addresses and trunk interfaces must be defined per device, not assumed.

## Sample sites

| Site | ID | Logical pool | Role |
| --- | ---: | --- | --- |
| DC | 0 | `10.0.0.0/16` | Core services and hub |
| Gold | 10 | `10.10.0.0/16` | High availability target |
| Silver | 20 | `10.20.0.0/16` | Selective redundancy |
| Bronze | 30 | `10.30.0.0/16` | Cost-optimized baseline |

These are **invented lab IDs**, not deployed academic-case IDs. Any example WAN IPs should come from documentation ranges (RFC 5737) such as `198.51.100.0/24` and `203.0.113.0/24`.

## Proposed routing by tier

| Tier | LAN | Corporate WAN | Default route intent |
| --- | --- | --- | --- |
| Gold | HSRP/VRRP gateways **to be tested** | OSPF where defined and IPsec backup under test | Local firewall for Internet |
| Silver | L3 switching | Static DC routes; OSPF optional | Local firewall |
| Bronze | Firewall gateway or L3 switch after design choice | Static routes over IPsec with monitored failover | Local firewall |
| DC | Central core/router and VPN termination | Explicit symmetric return routing | Depends on lab design |

Avoid unnecessary source NAT on private intersite VPN traffic. Return routing, neighbor state and failover need observed results.

## Initial access matrix

| Source | Destination | Proposed action | Required verification |
| --- | --- | --- | --- |
| Guest (130) | Internet | DNS/HTTP(S) allowed through NAT | Positive test |
| Guest (130) | Corporate RFC1918 networks | Deny | Negative test |
| Users (110) | Specific DC services | Permit required ports only | Traffic/log evidence |
| Management (100) | Management interfaces | Authorize designated admin hosts | Allowed/denied source tests |
| Quarantine (700) | Production networks | Deny | When NAC is implemented |

**An any-to-any rule is not a valid substitute for a security policy.** Actual vendor syntax and ordering must be confirmed in the lab.

## Work required before implementation

- Per-device table with hostname, software version, physical/virtual port, VLAN and IP.
- Gateway selection for Silver/Bronze and return path definition at the DC.
- Sanitized configs, verification outputs and supporting evidence.
- Compatible IKEv2/IPsec parameters, routes and authenticated peers.

[Gold LAN lab M1](../labs/M1-GOLD-LAN/README.en.md) | [Project index](../README.en.md)
