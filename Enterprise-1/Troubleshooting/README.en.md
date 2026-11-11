# Troubleshooting | Planned scenarios

**Languages:** [Português](README.MD) | [English](README.en.md)

The following cases are **hypotheses and test procedures**, not incident reports from completed network simulations.

| Case | Simulated situation | Focus |
| --- | --- | --- |
| [01](Scenario-1/README.en.md) | User cannot reach DC service | VLAN, gateway, policy, route and return path |
| [02](Scenario-2/README.en.md) | Primary WAN link fails | Failover, VPN and convergence measurement |
| [03](Scenario-3/README.en.md) | IPsec tunnel fails to establish | IKEv2, selectors, routes, policy and DPD |

## Investigation method

**Symptom -> scope -> hypotheses -> evidence collection -> minimum change -> retest -> artifact -> lessons learned.** Separate host, L2, L3, firewall and VPN issues before changing configuration.

For each case, record timestamps, observed behavior and sanitized outputs using the [evidence template](../evidence/README.en.md). A successful ping alone is not enough to prove encryption, policy enforcement, HA or failover.
