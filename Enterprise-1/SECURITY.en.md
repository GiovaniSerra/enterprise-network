# Lab security | Design principles and publication rules

**Languages:** [Português](SECURITY.md) | [English](SECURITY.en.md)

This describes **proposed controls** and safe publishing practices, not verified protections already deployed.

## Proposed controls

- **Least privilege:** management from authorized admin origins only; restrict SSH/HTTPS interfaces and accounts.
- **Segmentation:** VLAN 130 guest with no access to corporate private networks; VLAN 700 reserved for future NAC quarantine.
- **Firewall:** explicit rules with default-deny, allow/deny logging and both positive and negative tests.
- **IPsec:** prefer IKEv2 when supported; check algorithm compatibility, selectors/routes and secret handling.
- **Monitoring:** NTP, syslog and SNMPv3 in later phases, followed by alert verification.
- **Resiliency:** test link failures and recovery, including NAT and established-session behavior.

## Publishing policy

**Never commit:** passwords, PSKs, tokens, private keys, licenses, customer addresses/data, unredacted production configs or real network maps owned by third parties.

**Acceptable in a lab portfolio:** synthetic topologies, secret-free templates, redacted verification output, access matrices and dated screenshots with lab-only addresses.

The original academic PDFs are not included in this repository. If sensitive credentials are accidentally committed, simply deleting them from the latest commit **does not purge history**; examine exposure and rotate compromised secrets.

## Planned security tests

| Test | Expected | Evidence |
| --- | --- | --- |
| Guest -> DC server | Denied | Firewall deny logs and client attempt |
| Authorized user -> specific DC service | Allowed | Connection, route and allow log |
| Unauthorized source -> management IP | Denied | ACL/policy and connection attempt |
| Branch -> DC VPN | Encrypted transport | IKE/Child SA state and RX/TX counters |
| Noncompliant NAC endpoint -> VLAN 700 | Quarantined **after NAC exists** | NAC event and isolation proof |

None of these tests is deemed complete without actual sanitized [evidence](evidence/README.en.md). The [M1 example ACL](labs/M1-GOLD-LAN/README.en.md) is a limited LAN demonstration, **not a substitute** for all perimeter tests.
