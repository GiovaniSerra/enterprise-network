# Evidencias | Padrao de validação

**Estado:** nenhum resultado de rede foi inserido nesta fundacao. Preencher cada evidência **apenas depois de executar o teste**.

## Modelo para cada evidência

```text
ID do teste:
Marco / site:
Data e horario (fuso):
Autor:
Ambiente (EVE-NG, versao de imagem/software):
Objetivo:
Topologia / caminho esperado:
Pre-condicoes:
Comando ou procedimento:
Resultado esperado:
Resultado observado (transcricao ou print sanitizado):
Passou? (sim/não/parcial):
Duracao / perda / metricas (se houver):
Limitacoes e próximo passo:
Referencia a commit de configuração:
```

## Regras de publicacao

- Os screenshots devem conter contexto e versao, mas **não** senhas, PSKs, IPs reais, dados de clientes ou licencas.
- Capturas e logs são evidências, mas necessitam interpretacao escrita.
- Uma imagem de interface sem teste não prova failover, HA, filtragem, nem IKE/IPsec.
- Cada teste deve conter tanto o caso **positivo** quanto o **negativo** quando relevante.
- Expor restrições conhecidas e falhas não resolvidas: resultados negativos tambem demonstram troubleshooting.

Modelo de nome: `M1-GOLD-T01-vlan110-gateway.md`, `M3-DC-T03-ipsec-rxtx.md`.
