# Roadmap de engenharia e portfolio

Marcos organizados por **prova de funcionamento**, não por quantidade de tecnologias listadas.

| Marco | Objetivo | Entregavel principal | Estado |
| --- | --- | --- | --- |
| M0 | Fundacao da documentação | README, HLD, LLD, inventario, riscos, CI e modelos de evidências | Documentado; revisar CI no GitHub |
| M1 | DC e Gold, conectividade LAN | Topologia EVE-NG, endereços e configs Cisco/FortiGate | Pendente |
| M2 | Roteamento e segmentacao | VLAN, trunk, STP, OSPF Gold, ACLs e testes | Pendente |
| M3 | VPN e contingencia | IPsec, caminho principal/backup, logs de failover | Pendente |
| M4 | Silver e Bronze | Modelos simplificados, rotas estáticas e testes de retorno | Pendente |
| M5 | Segurança e monitoramento | Matriz de firewall, syslog/SNMPv3; SIEM/NAC conforme viabilidade | Pendente |
| M6 | Automacao e validação | Templates sem segredos, lint, backup e testes repetiveis | Pendente |
| M7 | Cloud e ampliacao | Conectividade hibrida opcional e estudo de capacidade | Futuro |

## Definition of Done (por marco)

- [ ] Topologia do marco versionada com imagem e identificação de interfaces.
- [ ] Descricao de objetivo, premissas e escopo verificada.
- [ ] Configuracoes sanitizadas com versao de equipamento/SO anotada.
- [ ] Comandos de teste, origem, destino, resultado esperado e observado documentados.
- [ ] Evidencias e horario registrados e revisados para não expor segredos.
- [ ] Rollback e limitacoes conhecidos.
- [ ] README atualizado para diferenciar **proposto**, **em execucao** e **validado**.

## Proxima atividade prioritária

**Montar DC + Gold minimo no EVE-NG**: um core L3, um switch de acesso, um firewall e dois hosts para validar VLANs 100/110/130, gateway e política guest. Apenas após passar nessa etapa, acrescentar segundo core, segundo firewall, roteamento dinâmico e WAN. Isso reduz superficie de falhas e cria evidências técnicas reais para o portfolio.
