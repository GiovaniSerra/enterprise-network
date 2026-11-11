# Implementation plan | EVE-NG

**Languages:** [Português](README.MD) | [English](README.en.md)

This plan adapts the academic implementation report into incremental lab milestones. **No device configuration is considered validated until reproducible results have been collected.**

## M0 | Preparation

1. Inventory image types, software versions, licensing and CPU/RAM capacity.
2. Define device names, port IDs, management network and unique site IDs.
3. Run `python scripts/validate_inventory.py` against the synthetic inventory.
4. Preserve a clean baseline and snapshots if supported.
5. Document the exact software platform before applying configuration templates.

## M1 | Minimal DC/Gold LAN foundation

1. Start with one access switch, one L3 core and test hosts; add the firewall only when its interface roles are settled.
2. Define VLANs 100 (management), 110 (users) and 130 (guests), with unused VLAN 5 where a native VLAN is required.
3. Limit trunk allowed VLANs; apply PortFast/BPDU Guard only to appropriate end-host ports.
4. Verify addressing, VLAN assignment, ARP, MAC learning, STP and routing.
5. Block guest-to-internal traffic at the **actual** routing/security enforcement point.

The [M1 lab guide](../labs/M1-GOLD-LAN/README.en.md) covers an initial **Gold-only LAN subset**; firewall and DC integration require follow-on tests.

### M1 acceptance examples

| Test | Expected | Evidence needed |
| --- | --- | --- |
| User -> VLAN 110 gateway | Replies | Ping and ARP table |
| Guest -> corporate subnet | Denied | Deny log/counter plus client attempt |
| Authorized admin -> management | Allowed in later management phase | Source and authenticated session |
| Unauthorized host -> management | Denied in later management phase | Policy/ACL and failure output |
| VLANs and trunk | Expected VLAN IDs only | `show vlan brief`, `show interfaces trunk` |
| STP | Expected root and port states | `show spanning-tree` |

Management-specific tests are **future acceptance tests**; they are not implemented in the minimal M1 config files.

## M2 | Routing and WAN

Verify OSPF adjacency and routing in a small Gold/DC segment before introducing IPsec. Define simulated private WAN and backup. Configure route-based IPsec where supported; inspect IKE/Child SAs and avoid unwanted corporate NAT. Measure failover and return paths; **do not assume** convergence targets without measurements.

## M3 | Silver and Bronze

Repeat essential LAN policies. Silver begins with static routes, adding OSPF only after documentation and proof. Bronze acknowledges single points of failure and relies on tested static routing/monitored backup when available.

## Change management and rollback

- **Before:** sanitized backup, snapshot if supported, connectivity baseline and test objective.
- **During:** one change at a time, console recovery path and log review.
- **After:** positive/negative tests, routing table, VPN state and measurements.
- **Rollback:** restore the previous validated config/snapshot when acceptance fails. The 30-minute academic change window is a planning reference, **not a recovery guarantee**.

Store observed results according to the [evidence guide](../evidence/README.en.md): expected/observed, date, software version, commands and sanitized artifacts.
