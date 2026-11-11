#!/usr/bin/env python3
"""Print a Markdown report of the sample network inventory."""
import json
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Enterprise-1/inventory/sites.json"
with path.open(encoding="utf-8") as stream:
    data = json.load(stream)

print("| Site | Tier | ID | Pool | VLANs |")
print("| --- | --- | ---: | --- | ---: |")
for site in data["sites"]:
    print(f"| {site['name']} | {site['tier']} | {site['site_id']} | "
          f"`{site['site_pool']}` | {len(site['vlans'])} |")
