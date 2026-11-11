# LLD | Low Level Design (baseline do laboratório)

**Idiomas:** [Português](README.MD) | [English](README.en.md)

Este documento organiza **propostas de configuração**, não arquivos `running-config` verificados. O plano original possui mais exemplos e opções; aqui mantemos um baseline consistente para evoluir com testes.

## Modelo de endereçamento

Para uma filial com identificador `ID` entre 1 e 254, reserva-se `10.ID.0.0/16` como espaco **lógico de alocação**, segmentado em sub-redes /24. Cada site deve possuir `ID` único. O Data Center de exemplo utiliza ID `0`. As redes ficticias de demonstração estão em [`inventory/sites.json`](../inventory/sites.json).

| VLAN | Função | Sub-rede ilustrativa | Aplicacao |
| ---: | --- | --- | --- |
| 5 | Nativa dedicada (sem hosts) | Não se aplica | Apenas onde trunk exigir; evitar nativa de usuário |
| 100 | Gerenciamento | `10.ID.0.0/24` | Acesso administrativo restrito |
| 110 | Usuários cabeados | `10.ID.10.0/24` | PCs corporativos |
| 120 | Wi-Fi corporativo | `10.ID.20.0/24` | SSID autenticado |
| 130 | Wi-Fi convidados | `10.ID.30.0/24` | Internet apenas |
| 140 | Voz | `10.ID.40.0/24` | VoIP, QoS posterior |
| 150 | Impressoras | `10.ID.50.0/24` | Acesso por portas/serviços explicitos |
| 160 | CCTV | `10.ID.60.0/24` | Video e sistemas de segurança |
| 170 | Controle de acesso | `10.ID.70.0/24` | Catracas, leitores e afins |
| 200 | Transito core/firewall | `10.ID.254.0/30` | Apenas Gold e Silver no baseline |
| 700 | Quarentena | `10.ID.200.0/24` | NAC futuro; sem acesso geral |
| 999 | Parking/blackhole | Sem IP | Interfaces não utilizadas, conforme capacidade do switch |

A VLAN 700 e a 999 são **reservas de design**, não funcionalidades NAC já implementadas. **Atribuições de endereços e gateways dependem do papel de cada equipamento**; não presumir IP virtual HA ativo em configurações de um firewall único.

## Exemplo de IDs de laboratório

| Site | ID | Pool reservado | Papel |
| --- | ---: | --- | --- |
| DC | 0 | `10.0.0.0/16` | Hub / serviços |
| Gold | 10 | `10.10.0.0/16` | Alta disponibilidade |
| Silver | 20 | `10.20.0.0/16` | Redundancia parcial |
| Bronze | 30 | `10.30.0.0/16` | Baseline enxuto |

Esses IDs **não constam como implantação real no PIF**: foram escolhidos para inventário demonstrativo. Redes WAN de exemplo devem empregar blocos reservados para documentação (RFC 5737), como `198.51.100.0/24` e `203.0.113.0/24`, sem se apresentar como endereçamento público alocado.

## Roteamento por perfil

| Perfil | LAN | WAN corporativa | Rota padrão |
| --- | --- | --- | --- |
| Gold | Gateway redundante via HSRP/VRRP **a testar** | OSPF no caminho definido e backup VPN sob teste | Internet local no firewall |
| Silver | Switch L3 | Rotas estáticas para DC; OSPF apenas extensao | Internet local no firewall |
| Bronze | Firewall como gateway ou switch L3, após escolha | Rotas estáticas sobre IPsec e failover monitorado | Internet local |
| DC | Roteador/core central e terminacao VPN | Rotas para filiais com retorno simetrico | Conforme desenho do lab |

A VPN não deve receber NAT de origem para tráfego intersite, salvo excecao explicitamente justificada. As regras, adjacencias e convergência serão descritas por site quando os enlaces forem montados.

## Matriz inicial de acesso entre redes

| Origem | Destino | Acao proposta | Validação necessaria |
| --- | --- | --- | --- |
| Guest (130) | Internet | Permitir DNS/HTTP(S) via NAT | Teste positivo |
| Guest (130) | Redes RFC1918 corporativas | Negar | Teste negativo |
| User (110) | Serviços específicos no DC | Permitir apenas portas requeridas | Registro de tráfego |
| Management (100) | Interfaces de gerência | Permitir somente host de administracao | Teste de origem autorizada/não autorizada |
| Quarantine (700) | Redes de produção | Negar | Validar quando NAC existir |

**Não usar 'any-to-any' como prova de política de segurança.** Revisar interfaces, serviços, objetos e ordem de regras por vendor.

## Artefatos pendentes

- Tabela por dispositivo com hostname, imagem/versão, interface, VLAN, IP e MAC da VM.
- Escolha do modelo de gateway em Silver/Bronze e metodo de retorno no DC.
- Configs versionadas separadas de segredos, com `show`/logs e resultados reais.
- Definicao de IKEv2/IPsec e parametros negociados por pares, considerando compatibilidade das imagens.

[Voltar ao Enterprise-1](../README.MD)

**Exemplo prático do recorte Gold:** [M1: VLAN 110/130, endereços e ACL em core L3](../labs/M1-GOLD-LAN/README.md). Os arquivos de configuração são modelos pendentes de validação.
