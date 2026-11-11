# Cenário 03 | VPN IPsec não estabelece

**Idiomas:** [Português](README.MD) | [English](README.en.md)

**Estado:** roteiro ainda não executado.

**Objetivo:** investigar falha em túnel IPsec entre filial e hub do DC em ambiente isolado.

## Matriz de diagnóstico

| Camada | Pergunta | Evidencia |
| --- | --- | --- |
| Underlay | Peer IP alcancavel? UDP 500/4500 ou ESP, se pertinente, trafegam? | Ping/traceroute/captura na WAN |
| IKE | IKEv2, identificadores e autenticação compatíveis? | Logs da fase 1 |
| Child SA | Propostas/seletores concordam? | Estado phase2/SA |
| Roteamento | Prefixos de origem/destino seguem para o túnel? | Tabela de rotas |
| Firewall/NAT | Policies permitem tráfego e preservam endereços privados? | Log e tabela de sessões |
| Liveness | DPD e saída/retorno por WAN correta? | Estado/contadores do túnel |

## Aceite

- Túnel negocia com parametros documentados e sem segredos públicos.
- RX/TX cresce ao gerar tráfego corporativo autorizado.
- Tráfego intersite não sofre NAT inesperado e acessos negados permanecem bloqueados.
- Teste positivo e negativo com evidências sanitizadas.

[Modelo de evidência](../../evidence/README.md).
