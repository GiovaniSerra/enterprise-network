# Enterprise-1 | Rede Corporativa Multi-Site

**Escopo:** Data Center + Gold + Silver + Bronze, com ramificacoes futuras para segurança e cloud.

![Topologia de referencia Gold](Topology/Gold%20site/Gold%20-%20topology.png)

> As imagens representam **arquiteturas de referencia**. Recursos descritos nelas não devem ser interpretados como já configurados no laboratório.

## Requisitos de negocio e engenharia

1. Conectar filiais a servicos centralizados com controle de acesso e segmentacao por função.
2. Separar tráfego corporativo, convidados, voz, impressoras, dispositivos de segurança e gerenciamento.
3. Definir resiliencia por categoria: Gold (alta disponibilidade), Silver (redundância seletiva) e Bronze (baixo custo, riscos explicitados).
4. Adotar caminho principal e contingencia WAN, privilegiando integridade do roteamento e políticas de firewall.
5. Criar evidências técnicas reproduzíveis para cada funcionalidade implementada.

## Escopo por site

| Site | Porte no case | Topologia proposta | Roteamento baseline | Status |
| --- | --- | --- | --- | --- |
| DC | Servicos centralizados | Hub VPN, servicos de infra, SIEM futuro | Roteamento a definir na fase 1 | Planejado |
| Gold | 100 a 150 usuários | Dual core L3, FortiGate HA, WAN principal + backup | OSPF, sujeito a teste | Planejado |
| Silver | Ate ~60 usuários | Core L3 único e duas WANs | Rotas estáticas; OSPF como evolucao | Planejado |
| Bronze | Ate ~30 usuários | Um switch e firewall único | Rotas estáticas monitoradas | Planejado |

## Navegacao

- [HLD - arquitetura e decisão de design](HLD/README.MD)
- [LLD - endereçamento, VLANs e inventario](LLD/README.MD)
- [Topologias e diagramas](Topology/README.MD)
- [Fluxos de tráfego](FLOW/README.MD)
- [Segurança](SECURITY.md)
- [Plano de implementação e testes](Implementation/README.MD)
- [Cenários de troubleshooting](Troubleshooting/README.MD)
- [Roadmap](ROADMAP.md)
- [Registro de decisões](DECISIONS.md)
- [Evidencias e aceite](evidence/README.md)

## Rastreabilidade

O projeto deriva de dois documentos do PIF de 2026: um **LLD academico** e um **Plano de Implementação**, ambos enviados pelo autor. O material contem propostas, comandos e algumas inconsistencias; por segurança e confiabilidade, o repositorio **não** pública os PDFs originais nem reproduz chaves, comunidades SNMP inseguras ou trechos não validados. Veja [DECISIONS](DECISIONS.md).
