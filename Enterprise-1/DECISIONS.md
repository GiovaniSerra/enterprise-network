# Registro de decisões de arquitetura (ADRs)

Este registro separa **escolhas de baseline** de **alternativas presentes no material academico**. As decisões podem ser revistas após testes no EVE-NG.

## ADR-001 | Exercicio incremental, não implantacao pronta

- **Decisao:** publicar design, inventario, testes e resultados em etapas.
- **Motivo:** evita confundir documentação de planejamento com configuração validada.
- **Impacto:** cada funcionalidade precisa de evidências antes de receber status `validada`.

## ADR-002 | Diferencas de roteamento entre documentos

- **Observação:** o LLD trata Gold com OSPF, Silver com rotas estáticas/OSPF opcional e Bronze com estáticas. O Plano de Implementação menciona OSPF no escopo geral e no Silver.
- **Decisao de baseline:** Gold = OSPF; Silver = estático, com teste posterior de OSPF; Bronze = estático monitorado. DC exige retorno roteavel para cada filial.
- **Pendente:** especificar como OSPF e transferido pelo transporte MPLS e/ou overlay VPN sem criar adjacencia indevida.

## ADR-003 | Dual WAN e SD-WAN

- **Observação:** o Plano Macro descreve Bronze com internet principal e rotas monitoradas, enquanto outra secao lista SD-WAN para todos os sites.
- **Decisao:** iniciar failover Bronze com rotas estáticas monitoradas; SD-WAN fica como extensao. Não tratar MPLS como criptografia.

## ADR-004 | Enderecamento e segregacao

- **Decisao:** manter convencao `10.ID.X.0/24` por segmento e ID de site exclusivo. VLAN 200 /30 em Gold/Silver; Bronze sem transito dedicado na topologia de referencia.
- **Pendência:** validar gateway exato, HA virtual, interfaces trunk e plano IP definitivo antes de configurar.

## ADR-005 | Sanitizacao de segurança

- **Observação:** o material de implementação contem exemplos com PSK literal e comunidade SNMP `public`, e exemplos de gerência liberada em WAN.
- **Decisao:** **não copiar** segredos, SNMPv2c de exemplo ou gestão HTTPS/SSH exposta em WAN para o repositorio. Preferir SNMPv3, privilegio minimo, controles por endereço de origem e variáveis/secret store locais.
- **Pendência:** matriz de compatibilidade de comandos por versao FortiOS/Cisco IOS e evidências de teste.

## ADR-006 | Escopo de simulação

- **Decisao:** laboratórios de quatro domínios (DC/Gold/Silver/Bronze) representam o case de 30->70 sites, sem afirmar simulação da escala integral.
- **Motivo:** reduzir custo computacional e tornar o troubleshooting reproduzivel.

[Ver roadmap](ROADMAP.md)
