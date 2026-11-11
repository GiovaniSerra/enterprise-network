# Troubleshooting | Cenários planejados

**Idiomas:** [Português](README.MD) | [English](README.en.md)

Os roteiros abaixo são **hipóteses e planos de teste**, não relatos de incidentes já observados.

| Caso | Situação simulada | Foco |
| --- | --- | --- |
| [01](Scenario-1/README.MD) | Usuário perde acesso ao DC | VLAN, gateway, ACL, rota e retorno |
| [02](Scenario-2/README.MD) | Caminho WAN principal cai | Failover, VPN, tempos de convergência |
| [03](Scenario-3/README.MD) | VPN IPsec não sobe | IKEv2, seletores, rotas, policies e DPD |

## Metodo padrão

**Sintoma -> escopo -> hipóteses -> coleta -> alteração minima -> reteste -> evidência -> licoes aprendidas.** Diferenciar falha do host, Layer 2, Layer 3, firewall e túnel antes de alterar configurações.

Para cada caso, preencher evidências com valor observado e timestamp no [`modelo`](../evidence/README.md). Não tratar 'ping funcionou' como prova suficiente de política, criptografia ou failover.
