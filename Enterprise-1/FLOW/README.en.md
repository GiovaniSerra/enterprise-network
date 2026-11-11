# Traffic flows | Proposed designs and test criteria

**Languages:** [Português](README.MD) | [English](README.en.md)

These diagrams depict **expected behavior**, not packet captures or evidence that services are currently running.

## 1. Corporate endpoint to Data Center

```mermaid
sequenceDiagram
  participant U as VLAN 110 host
  participant C as Branch L3 core
  participant F as Branch NGFW
  participant W as Private WAN / IPsec
  participant D as DC application server
  U->>C: Request to internal service
  C->>F: Forward toward corporate path
  F->>F: Apply policy and route, no unexpected NAT
  F->>W: Send over approved transport
  W->>D: Deliver to service
  D-->>U: Reply via valid return route
```

**Acceptance:** verified forward/return routing, service response, unchanged corporate source IP unless documented otherwise, and relevant policy logs. Do not assume OSPF is active at every branch.

## 2. Guest Wi-Fi to Internet

```mermaid
flowchart LR
 G["Guest VLAN 130"] --> FW["Policy: allow approved web/DNS, deny internal"]
 FW --> NAT["SNAT/PAT"] --> NET[("Simulated Internet")]
 G -.->|Deny| DC["Corporate private subnets"]
```

**Acceptance:** approved web/DNS behavior works after NAT is implemented, and private subnet traffic is denied with correlated logs. **The M1 LAN-only lab does not implement Internet/NAT.**

## 3. Hub-and-spoke IPsec

```mermaid
flowchart TB
 DC["Data Center IPsec hub"]
 WAN[("Simulated Internet")]
 GOLD["Gold"] --> WAN
 SILVER["Silver"] --> WAN
 BRONZE["Bronze"] --> WAN
 WAN --> DC
```

**Acceptance:** verified IKE/Child SAs, encryption on underlay, rising tunnel TX/RX counters, and compatible selectors/routes and system clocks.

## 4. Primary WAN failure

```mermaid
flowchart LR
 A["Health-check and routing state"] --> B{"Primary healthy?"}
 B -->|Yes| P["Use primary WAN"]
 B -->|No| Q["Use backup path"]
 Q --> T["Verify route, VPN and reachability"]
 T --> R["Measure loss, recovery and log events"]
```

**Acceptance:** correct forward/return paths and measured interruption duration. Do not promise sub-10-second failover without measurement; session resets may occur during WAN/NAT transition.
