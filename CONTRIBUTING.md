# Como contribuir e registrar evolucoes

1. Abra uma issue ou descreva a mudanca com objetivo, premissas e risco.
2. Trabalhe em branch (`feature/<funcionalidade>`) e não inclua credenciais.
3. Execute `python scripts/validate_inventory.py` e `python -m unittest discover -s tests -v`.
4. Inclua os resultados **reais** com comandos e evidências sanitizadas.
5. Atualize [Roadmap](Enterprise-1/ROADMAP.md), [HLD](Enterprise-1/HLD/README.MD) e/ou [LLD](Enterprise-1/LLD/README.MD) conforme o impacto.
6. Abra PR com checklist: design atualizado, validação executada, limites conhecidos e rollback documentado.

## Convenções

- Markdown em portugues técnico com nomes das tecnologias e comandos originais.
- Diagrama Mermaid para fluxos editaveis, imagens existentes preservadas.
- Estados oficiais: `planejado`, `em execucao`, `validado` e `bloqueado`.
- Design ou snippet encontrado em manual **não** substitui prova em ambiente de laboratório.
