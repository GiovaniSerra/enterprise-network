#!/usr/bin/env python3
"""Validate the synthetic multi-site IP plan using only the standard library."""
from __future__ import annotations

import ipaddress
import json
from pathlib import Path

DEFAULT_INVENTORY = Path(__file__).resolve().parents[1] / "Enterprise-1/inventory/sites.json"
TYPES = {"datacenter", "gold", "silver", "bronze"}
VLAN_TO_THIRD = {100: 0, 110: 10, 120: 20, 130: 30, 140: 40, 150: 50,
                 160: 60, 170: 70, 700: 200, 200: 254}


def validate(data: dict) -> list[str]:
    """Return human-readable errors; empty result means the design is consistent."""
    errors: list[str] = []
    if not isinstance(data, dict) or not isinstance(data.get("sites"), list):
        return ["A chave 'sites' precisa ser uma lista."]
    ids: set[int] = set()
    all_networks: list[tuple[str, ipaddress.IPv4Network]] = []
    dc_count = 0
    for idx, site in enumerate(data["sites"]):
        location = f"sites[{idx}]"
        if not isinstance(site, dict):
            errors.append(f"{location}: objeto esperado")
            continue
        name = str(site.get("name", f"id-{idx}"))
        sid = site.get("site_id")
        tier = site.get("tier")
        if type(sid) is not int or not 0 <= sid <= 254:
            errors.append(f"{name}: site_id deve ser inteiro entre 0 e 254")
            continue
        if sid in ids:
            errors.append(f"{name}: site_id duplicado {sid}")
        ids.add(sid)
        if tier not in TYPES:
            errors.append(f"{name}: tier invalido {tier!r}")
        if tier == "datacenter":
            dc_count += 1
            if sid != 0:
                errors.append(f"{name}: Data Center de exemplo usa site_id 0")
        elif sid == 0:
            errors.append(f"{name}: ID 0 reservado ao Data Center")
        try:
            pool = ipaddress.IPv4Network(site.get("site_pool"), strict=True)
            if pool != ipaddress.IPv4Network(f"10.{sid}.0.0/16"):
                errors.append(f"{name}: site_pool inesperado {pool}")
        except (ValueError, TypeError) as exc:
            errors.append(f"{name}: site_pool invalido ({exc})")
            continue
        vlans = site.get("vlans")
        if not isinstance(vlans, list):
            errors.append(f"{name}: vlans precisa ser lista")
            continue
        seen_vlan_ids: set[int] = set()
        for entry in vlans:
            if not isinstance(entry, dict):
                errors.append(f"{name}: entrada de VLAN invalida")
                continue
            vid = entry.get("vlan_id")
            if type(vid) is not int or vid not in VLAN_TO_THIRD:
                errors.append(f"{name}: ID de VLAN nao permitido {vid!r}")
                continue
            if vid in seen_vlan_ids:
                errors.append(f"{name}: VLAN {vid} duplicada")
            seen_vlan_ids.add(vid)
            if vid == 200 and tier not in {"gold", "silver"}:
                errors.append(f"{name}: VLAN 200 so no Gold/Silver no baseline")
            try:
                subnet = ipaddress.IPv4Network(entry.get("subnet"), strict=True)
            except (ValueError, TypeError) as exc:
                errors.append(f"{name}: subnet invalida da VLAN {vid} ({exc})")
                continue
            expected_prefix = 30 if vid == 200 else 24
            expected = ipaddress.IPv4Network(
                f"10.{sid}.{VLAN_TO_THIRD[vid]}.0/{expected_prefix}")
            if subnet != expected:
                errors.append(f"{name}: VLAN {vid} deveria usar {expected}, nao {subnet}")
            if not subnet.subnet_of(pool):
                errors.append(f"{name}: {subnet} fora de {pool}")
            for other_name, other_net in all_networks:
                if subnet.overlaps(other_net):
                    errors.append(f"{name}: {subnet} sobrepoe {other_name}: {other_net}")
            all_networks.append((f"{name}/VLAN{vid}", subnet))
        if not {100, 110, 130}.issubset(seen_vlan_ids):
            errors.append(f"{name}: faltam VLANs basicas 100, 110 ou 130")
        if tier in {"gold", "silver"} and 200 not in seen_vlan_ids:
            errors.append(f"{name}: falta VLAN 200 de transito")
    if dc_count != 1:
        errors.append(f"Era esperado exatamente um Data Center, encontrados {dc_count}")
    return errors


def main() -> int:
    with DEFAULT_INVENTORY.open(encoding="utf-8") as file:
        data = json.load(file)
    errors = validate(data)
    if errors:
        print("Inventario INVALIDO:")
        for problem in errors:
            print(f" - {problem}")
        return 1
    print(f"Inventario VALIDO: {len(data['sites'])} sites, sem sobreposicoes de VLANs/sub-redes.")
    print("Nota: validacao de dados, nao de dispositivos de rede.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
