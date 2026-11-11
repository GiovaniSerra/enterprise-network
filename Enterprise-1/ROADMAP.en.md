# Engineering and portfolio roadmap

**Languages:** [Português](ROADMAP.md) | [English](ROADMAP.en.md)

Progress is measured by **working evidence**, not by the number of technologies listed.

| Milestone | Objective | Main deliverable | Status |
| --- | --- | --- | --- |
| M0 | Documentation foundation | README, HLD, LLD, inventory, risks, CI and evidence templates | Documented; remote CI verification pending |
| M1 | Gold/DC LAN foundation | Real EVE-NG topology, Cisco/FortiGate configs and tests | Pending; example Gold LAN guide available |
| M2 | Routing and segmentation | VLAN, trunk, STP, Gold OSPF, ACL/NGFW testing | Pending |
| M3 | VPN and failover | IPsec, primary/backup paths and measured recovery | Pending |
| M4 | Silver and Bronze | Streamlined branches, static routes and return path tests | Pending |
| M5 | Security and monitoring | Firewall matrix, syslog/SNMPv3; optional NAC/SIEM | Pending |
| M6 | Automation | Sanitized templates, checks, backups and repeatable tests | Pending |
| M7 | Cloud extensions | Optional hybrid connectivity and capacity study | Future |

## Definition of Done

- [ ] Version-controlled topology and interface map.
- [ ] Verified scope, prerequisites and acceptance criteria.
- [ ] Sanitized device configuration with image/software version.
- [ ] Commands, endpoints, expected and observed results.
- [ ] Timestamped sanitized evidence plus explicit limitations.
- [ ] Tested rollback or documented recovery path.
- [ ] Lab README updated to indicate `planned`, `in progress` or `validated` accurately.

## Next milestone

Complete the [M1 Gold LAN lab](labs/M1-GOLD-LAN/README.en.md) first. Validate VLAN 110/130 paths and ACL behavior with real outputs, then add firewall/DC, redundancy, OSPF and WAN transport gradually.
