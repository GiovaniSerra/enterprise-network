# Cenário 01 | Usuario não acessa servico no DC

**Estado:** roteiro ainda não executado.

**Sintoma simulado:** host `10.10.10.50` na VLAN 110 (Gold) não alcanca servico de exemplo `10.0.10.10` no DC. Esses endereços são exclusivamente ilustrativos.

## Hipoteses e verificacoes

1. **Layer 2:** verificar VLAN, porta access, trunk, MAC address-table e STP.
2. **Gateway:** validar IP, mascara, ARP e gateway do host.
3. **Roteamento:** conferir rota Gold -> DC e DC -> Gold, inclusive next-hop de retorno.
4. **Segurança:** política NGFW/ACL para origem/destino/porta e log de negacao.
5. **WAN/VPN:** se o caminho esperado for tunel, verificar SA e contadores.

## Evidencias a coletar

- Configuração mascarada da porta/svi; `show vlan brief`, `show ip route`, `traceroute`.
- Estado de sessão/política no firewall; teste de porta da aplicação.
- Resultado observado antes e depois da alteração e causa raiz comprovada.

**Aceite:** comunicação ao servico especificado, política restrita validada e retorno simetrico documentado. [Modelo de evidência](../../evidence/README.md).
