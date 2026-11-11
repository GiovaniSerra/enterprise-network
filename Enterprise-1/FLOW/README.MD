# Fluxos de tráfego | Design e testes planejados

Os diagramas a seguir são **fluxos esperados**, não capturas de pacotes nem logs já coletados.

## 1. Usuario corporativo -> Data Center

```mermaid
sequenceDiagram
  participant U as Host VLAN 110
  participant C as Core L3
  participant F as NGFW filial
  participant W as WAN privada / VPN IPsec
  participant D as Servidor DC
  U->>C: Requisicao a servico privado
  C->>F: Encaminha para rota corporativa
  F->>F: Política + rota, sem NAT corporativo
  F->>W: Transporte corporativo
  W->>D: Entrega ao servico
  D-->>U: Resposta por caminho com rota de retorno
```

**Aceite:** caminho de ida e retorno conhecido, servidor responde, origem preservada, políticas registradas. Não inferir que OSPF esteja ativo em todos os sites.

## 2. Wi-Fi de convidados -> Internet

```mermaid
flowchart LR
 G["Guest VLAN 130"] --> FW["Firewall: permitir web e DNS, negar intranet"]
 FW --> SNAT["SNAT/PAT"] --> INT[("Internet simulada")]
 G -.->|Bloqueado| DC["Redes corporativas"]
```

**Aceite:** navegacao prevista funciona e acesso a sub-redes corporativas falha por política; coletar log de bloqueio.

## 3. IPsec hub-and-spoke

```mermaid
flowchart TB
 DC["Data Center: terminacao IPsec"]
 NET[("Internet simulada")]
 G["Gold"] --> NET
 S["Silver"] --> NET
 B["Bronze"] --> NET
 NET --> DC
```

**Aceite:** SAs IKE/Child SA negociadas, tráfego cifrado no underlay, contadores RX/TX aumentam, espelhamento de rotas/seletores e NTP conferidos.

## 4. Falha no caminho primario

```mermaid
flowchart LR
 A["Monitorar health-check / rota"] --> B{"Caminho primario saudavel?"}
 B -->|Sim| P["Usar WAN principal"]
 B -->|Não| Q["Usar caminho alternativo"]
 Q --> T["Validar rota, tunel e conectividade"]
 T --> R["Medir perda, convergência e logs"]
```

**Aceite:** retorno previsivel e medicao real da interrupcao; não prometer failover < 10s sem medir. Sessoes existentes podem cair durante troca de WAN/NAT.
