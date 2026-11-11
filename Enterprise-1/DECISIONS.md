# Registro de decisões de arquitetura (ADRs)

**Idiomas:** [Português](DECISIONS.md) | [English](DECISIONS.en.md)

Este registro separa **escolhas de baseline** de **alternativas presentes no material acadêmico**. As decisões podem ser revistas após testes no EVE-NG.

## ADR-001 | Exercicio incremental, não implantação pronta

- **Decisão:** publicar design, inventário, testes e resultados em etapas.
- **Motivo:** evita confundir documentação de planejamento com configuração validada.
- **Impacto:** cada funcionalidade precisa de evidências antes de receber status `validada`.

## ADR-002 | Diferencas de roteamento entre documentos

- **Observação:** o LLD trata Gold com OSPF, Silver com rotas estáticas/OSPF opcional e Bronze com estáticas. O Plano de Implementação menciona OSPF no escopo geral e no Silver.
- **Decisão de baseline:** Gold = OSPF; Silver = estático, com teste posterior de OSPF; Bronze = estático monitorado. DC exige retorno roteável para cada filial.
- **Pendente:** especificar como OSPF e transferido pelo transporte MPLS e/ou overlay VPN sem criar adjacencia indevida.

## ADR-003 | Dual WAN e SD-WAN

- **Observação:** o Plano Macro descreve Bronze com internet principal e rotas monitoradas, enquanto outra seção lista SD-WAN para todos os sites.
- **Decisão:** iniciar failover Bronze com rotas estáticas monitoradas; SD-WAN fica como extensao. Não tratar MPLS como criptografia.

## ADR-004 | Endereçamento e segregacao

- **Decisão:** manter convencao `10.ID.X.0/24` por segmento e ID de site exclusivo. VLAN 200 /30 em Gold/Silver; Bronze sem transito dedicado na topologia de referência.
- **Pendência:** validar gateway exato, HA virtual, interfaces trunk e plano IP definitivo antes de configurar.

## ADR-005 | Sanitizacao de segurança

- **Observação:** o material de implementação contém exemplos com PSK literal e comunidade SNMP `public`, e exemplos de gerência liberada em WAN.
- **Decisão:** **não copiar** segredos, SNMPv2c de exemplo ou gestão HTTPS/SSH exposta em WAN para o repositório. Preferir SNMPv3, privilégio minimo, controles por endereço de origem e variáveis/secret store locais.
- **Pendência:** matriz de compatibilidade de comandos por versão FortiOS/Cisco IOS e evidências de teste.

## ADR-006 | Escopo de simulação

- **Decisão:** laboratórios de quatro domínios (DC/Gold/Silver/Bronze) representam o case de 30->70 sites, sem afirmar simulação da escala integral.
- **Motivo:** reduzir custo computacional e tornar o troubleshooting reproduzível.

[Ver roadmap](ROADMAP.md)

## ADR-007 | Evidências, bilinguidade e autoria individual

- **Decisão:** disponibilizar guias em português e inglês, modelos explicitamente não testados e resultados apenas após execução no EVE-NG.
- **Motivo:** tornar o portfólio acessível a recrutadores brasileiros e internacionais sem apresentar planejamento como implantação validada.
- **Autoria:** o repositório é pessoal e não recebe contribuições externas; consulte [Política do projeto](../PERSONAL_PROJECT.md).
