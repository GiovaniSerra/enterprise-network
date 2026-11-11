# Plano de implementação | EVE-NG

**Idiomas:** [Português](README.MD) | [English](README.en.md)

Este plano adapta o PIF acadêmico a uma execução de laboratório por marcos. O Plano de Implementação original considera validação, instalação, configuração, serviços, testes, monitoramento, riscos e rollback. Neste repositório, **nenhuma configuração de rede e dada como validada antes de resultados reproduzíveis**.

## M0 | Preparacao

1. Inventariar VMs, imagens/versões e requisitos de RAM/CPU/licenças.
2. Definir nomes dos dispositivos, interfaces, rede de gerenciamento e IDs de site.
3. Rodar `python scripts/validate_inventory.py` e conferir `Enterprise-1/inventory/sites.json`.
4. Estabelecer baseline limpo e snapshot (quando suportado).
5. Registrar versão e imagem utilizada antes de adicionar templates CLI.

## M1 | LAN minima DC + Gold

1. Instalar um switch de acesso, um core L3, um firewall e dois hosts isolados em rede de laboratório.
2. Configurar VLAN 100 (gerência), VLAN 110 (usuário) e VLAN 130 (guest).
3. Configurar trunks **somente com VLANs necessárias**; porta de acesso e portfast/BPDU guard onde apropriado.
4. Validar IP/gateway, ARP, MAC, STP e reachability.
5. Impedir Guest -> redes internas com política no ponto de roteamento efetivo.

### Matriz de aceite: M1 LAN e extensão posterior de gestão

| Teste | Resultado esperado | Como comprovar |
| --- | --- | --- |
| Host 110 -> gateway da VLAN 110 | Responde | `ping` e tabela ARP |
| Host 130 -> servidor corporativo | **Bloqueado** | Log deny/ACL e tentativa do host |
| Admin autorizado -> gerência (**fase posterior**) | Permitido após configuração de gestão | Sessão SSH + origem |
| Host não autorizado -> gerência (**fase posterior**) | Bloqueado após configuração de gestão | ACL/policy + tentativa |
| Trunk e VLANs | Apenas VLANs previstas | `show interfaces trunk`, `show vlan brief` |
| STP | Root e portas coerentes | `show spanning-tree` |

**Nota de escopo:** o [guia M1 Gold LAN](../labs/M1-GOLD-LAN/README.md) cobre primeiro um subconjunto da LAN Gold; a integração ao DC e ao FortiGate permanece posterior. A VLAN 100 é reservada nesse exemplo, sem gestão SSH já habilitada.

## M2 | Roteamento e WAN

1. Validar OSPF em um segmento de laboratório Gold/DC antes de adicionar VPN.
2. Definir transporte privado MPLS simulado e caminhos sob falha.
3. Configurar IPsec route-based onde suportado; verificar IKE e Child SA nas duas pontas.
4. Impedir NAT em comunicação privada; permitir NAT para a Internet.
5. Medir failover e rota de retorno com logs e conectividade contínua. Não assumir objetivos de convergência sem medicao.

## M3 | Silver e Bronze

Repetir controles LAN; Silver com rotas estáticas no baseline, evoluindo para OSPF somente se documentado e testado. Bronze com equipamento interno único e rotas estáticas monitoradas; validar limites do failover e documentar pontos únicos de falha.

## Controle de mudancas e rollback

- **Antes:** salvar configuração segura, snapshot quando disponível, baseline de conectividade e objetivo.
- **Durante:** executar uma mudanca por vez; usar console de emergência; acompanhar logs.
- **Depois:** comparar testes positivos e negativos, coletar tabelas de rota, estado de VPN e metricas.
- **Reversao:** restaurar configuração anterior/snapshot caso os critérios de aceite falhem. O limite de 30 min do PIF e referência de janela planejada, não garantia de recuperação.

## Onde registrar resultados

Salvar relato de cada teste no modelo de [`evidence/README.md`](../evidence/README.md), sem segredos. Para cada cenário, registrar **expected / observed / pass-fail / data / versão / comando**.
