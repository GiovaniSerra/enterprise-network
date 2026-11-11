# Cenário 03 | VPN IPsec não estabelece

**Estado:** roteiro ainda não executado.

**Objetivo:** investigar falha em tunel IPsec entre filial e hub do DC em ambiente isolado.

## Matriz de diagnostico

| Camada | Pergunta | Evidencia |
| --- | --- | --- |
| Underlay | Peer IP alcancavel? UDP 500/4500 ou ESP, se pertinente, trafegam? | Ping/traceroute/captura na WAN |
| IKE | IKEv2, identificadores e autenticação compativeis? | Logs da fase 1 |
| Child SA | Propostas/seletores concordam? | Estado phase2/SA |
| Roteamento | Prefixos de origem/destino seguem para o tunel? | Tabela de rotas |
| Firewall/NAT | Policies permitem tráfego e preservam endereços privados? | Log e tabela de sessões |
| Liveness | DPD e saida/retorno por WAN correta? | Estado/contadores do tunel |

## Aceite

- Tunel negocia com parametros documentados e sem segredos públicos.
- RX/TX cresce ao gerar tráfego corporativo autorizado.
- Trafego intersite não sofre NAT inesperado e acessos negados permanecem bloqueados.
- Teste positivo e negativo com evidências sanitizadas.

[Modelo de evidência](../../evidence/README.md).
