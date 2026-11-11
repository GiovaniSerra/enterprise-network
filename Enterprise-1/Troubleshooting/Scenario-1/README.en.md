# Scenario 01 | User cannot reach a DC service

**Languages:** [Português](README.MD) | [English](README.en.md)

**Status:** procedure not executed.

**Simulated symptom:** Gold VLAN 110 client `10.10.10.50` cannot access a sample DC service at `10.0.10.10`. Both addresses are synthetic.

## Hypotheses and checks

1. **Layer 2:** client VLAN, switch access port, allowed trunk VLANs, learned MACs and STP state.
2. **Gateway:** IP/mask, ARP and correct next hop.
3. **Routing:** Gold-to-DC route and DC-to-Gold return path.
4. **Policy:** NGFW/ACL permits the specific destination/service and does not shadow its allow rule.
5. **WAN/IPsec:** if using a tunnel, validate SAs, selectors and packet counters.

## Evidence to collect

Sanitized interface/SVI configuration, `show vlan brief`, `show ip route`, traceroute, application-port test, firewall policy/session logs and before/after observations.

**Acceptance:** communication to the specified service works under a restrictive rule; return routing and the verified root cause are recorded. [Evidence guide](../../evidence/README.en.md).
