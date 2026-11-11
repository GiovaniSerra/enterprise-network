# Segurança e boas práticas do laboratório

**Idiomas:** [Português](SECURITY.md) | [English](SECURITY.en.md)

Este arquivo descreve controles **propostos** e cuidados para publicar conteudo técnico no portfolio.

## Controles de design

- **Menor privilégio:** gerenciamento somente pela VLAN 100 ou rede de administracao; restringir SSH/HTTPS por endereços autorizados e perfis administrativos.
- **Segmentação:** VLAN 130 (guest) sem acesso a redes privadas; VLAN 700 reservada para quarentena; segmentação entre usuários e equipamentos de infraestrutura.
- **Firewall:** regras explicitas com `implicit deny`, logs de bloqueio e teste de tráfego autorizado e negado.
- **VPN IPsec:** IKEv2 como preferencia de design, autenticação e algoritmos conforme suporte real; segredos fora do repositório, seletores/rotas coerentes em ambas as pontas.
- **Monitoramento:** NTP, syslog e SNMPv3 em fase operacional; coletar e revisar alertas após validar as fontes de log.
- **Resiliencia:** testes de queda e de retorno do enlace documentados, incluindo perda de sessões e efeitos de NAT.

## Política de publicacao no Git

**Não publicar:** senhas, chaves pre-compartilhadas, tokens, arquivos de licença, contas reais, endereços de clientes, topologias de terceiros, configurações de produção sem sanitizar e capturas com dados pessoais.

**Pode publicar:** topologias sintéticas, modelos sem credenciais, saídas de teste mascaradas, matrizes de acesso, screenshots com timestamps e endereços de laboratório.

Os PDFs originais do PIF são fontes privadas de trabalho e **não foram copiados** para este repositório. Se um arquivo sensivel for commitado, a remocao do arquivo no HEAD não apaga o histórico: revisar historia e rotacionar credenciais expostas.

## Testes de segurança previstos

| Teste | Resultado esperado | Evidencia |
| --- | --- | --- |
| Guest -> servidor DC | Bloqueado | Log deny + comando no cliente |
| Usuário autorizado -> servico específico DC | Permitido | Fluxo, rota e log allow |
| Origem não autorizada -> IP de gerência | Bloqueado | Log/ACL e timeout |
| VPN filial -> DC | Criptografada | Estado de IKE/Child SA e RX/TX |
| NAC não conforme -> VLAN 700 | Quarentena, **após implantação** | Evento NAC e isolamento |

Nenhum desses testes e marcado como realizado até evidências serem adicionadas a [`evidence/`](evidence/README.md).
