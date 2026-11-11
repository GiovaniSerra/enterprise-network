# Demonstration inventory

**Languages:** [Português](README.md) | [English](README.en.md)

[`sites.json`](sites.json) models **four fictional sites only** for IP planning consistency. It is not a production CMDB/IPAM or a live device export.

- `site_id` is used as the second octet in `10.<site_id>.0.0/16`.
- User-function VLANs use /24 networks; VLAN 200 transit uses /30 only at Gold and Silver.
- VLAN 5 and 999 have no host subnets; VLAN 700 is reserved for future quarantine.
- The Python validator detects duplicate IDs and subnet overlaps. It does **not** connect to network devices.

From the repository root:

```bash
python scripts/validate_inventory.py
python scripts/render_inventory.py
```

[LLD addressing plan](../LLD/README.en.md) | [M1 Gold LAN](../labs/M1-GOLD-LAN/README.en.md)
