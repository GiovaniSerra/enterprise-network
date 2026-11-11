# Inventario demonstrativo

[`sites.json`](sites.json) modela **somente quatro sites fictícios** para validar a consistencia do plano IP. Não e CMDB, IPAM de produção ou exportacao de configurações reais.

- `site_id` e o segundo octeto em `10.<site_id>.0.0/16`.
- Cada VLAN de usuários usa um /24; o transito 200 usa /30 somente em Gold e Silver.
- Os planos de VLAN 5/999 não recebem IPs; 700 e reserva para quarentena.
- A verificacao automatica valida duplicidades e sobreposicoes, mas não alcanca dispositivos.

Da raiz: `python scripts/validate_inventory.py` e `python scripts/render_inventory.py`.
