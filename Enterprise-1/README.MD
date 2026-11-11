# Enterprise-1 | Case integrado de rede corporativa

**Idiomas:** [Português](README.MD) | [English](README.en.md) | [Página inicial](../README.md)

Estudo de uma cooperativa de crédito fictícia que precisa interligar um Data Center a filiais de classes Gold, Silver e Bronze. O modelo deriva de dois documentos acadêmicos do autor e foi reorganizado como um projeto de **engenharia incremental com validação por evidências**.

![Topologia Gold de referência](Topology/Gold%20site/Gold%20-%20topology.png)

> **Status: fase de design.** Esta imagem é uma referência arquitetural; não comprova conexões ativas, HA, VLANs ou VPN. O modelo Silver+ é opcional, fora do escopo inicial.

## Requisitos

1. Conectar filiais aos serviços centralizados mantendo rotas de retorno e políticas explícitas.
2. Segregar usuários, visitantes, gerenciamento, voz, impressoras e sistemas de segurança.
3. Aplicar disponibilidade proporcional à criticidade, sem pressupor HA em sites Bronze.
4. Planejar conectividade WAN principal e contingência IPsec sem confundir MPLS com criptografia.
5. Documentar falhas reais, verificações e limitações, além das configurações.

## Perfis de site

| Site | Escopo representado | LAN / segurança planejada | Roteamento baseline | Status |
| --- | --- | --- | --- | --- |
| DC | Serviços centralizados e hub | Serviços de rede + NGFW | A definir e validar | Planejado |
| Gold | ~100 a 150 usuários | Duplo core L3, NGFW HA, WAN dupla | OSPF, em fase posterior | Planejado |
| Silver | Até ~60 usuários | Um core L3 e acesso WAN alternativo | Estático; OSPF opcional | Planejado |
| Bronze | Até ~30 usuários | Switch e firewall único | Estático | Planejado |

## Guias do projeto

| Tema | Documento |
| --- | --- |
| Arquitetura HLD | [Abrir HLD](HLD/README.MD) |
| Endereçamento e VLANs LLD | [Abrir LLD](LLD/README.MD) |
| Galeria de topologias | [Abrir topologias](Topology/README.MD) |
| Fluxos de tráfego | [Abrir fluxos](FLOW/README.MD) |
| Plano de implementação | [Abrir execução por fases](Implementation/README.MD) |
| **Laboratórios reproduzíveis** | **[Índice dos laboratórios](labs/README.md)** |
| **M1: Gold LAN e segmentação** | **[Guia completo](labs/M1-GOLD-LAN/README.md)** |
| Operação e segurança | [Segurança](SECURITY.md) e [Troubleshooting](Troubleshooting/README.MD) |
| Evidências e QA | [Padrão de evidências](evidence/README.md) e [Inventário](inventory/README.md) |
| Decisões e fontes | [ADRs](DECISIONS.md) e [Fontes do PIF](SOURCES.md) |
| Etapas futuras | [Roadmap](ROADMAP.md) |

## Método de comprovação

Cada módulo deve publicar: topologia, mapa de portas, imagens/versões de software, configuração sem credenciais, comandos, resultado esperado, resultado observado, artefatos de captura e diagnóstico de falhas. O estado `validado` só deve ser atribuído a um teste após sua execução. Não foram adicionadas evidências de rede fictícias.

**Autoria exclusiva:** projeto pessoal sem recebimento de contribuições externas. Consulte [política](../PERSONAL_PROJECT.md).
