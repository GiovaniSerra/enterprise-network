"""Regression checks for the illustrative enterprise network inventory."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_inventory import validate  # noqa: E402

with (ROOT / "Enterprise-1/inventory/sites.json").open(encoding="utf-8") as stream:
    SAMPLE = json.load(stream)


class TestInventory(unittest.TestCase):
    def test_sample_is_valid(self):
        self.assertEqual(validate(SAMPLE), [])

    def test_duplicate_site_id_is_detected(self):
        data = copy.deepcopy(SAMPLE)
        data["sites"][2]["site_id"] = data["sites"][1]["site_id"]
        self.assertTrue(any("duplicado" in e for e in validate(data)))

    def test_overlap_is_detected(self):
        data = copy.deepcopy(SAMPLE)
        data["sites"][1]["vlans"][1]["subnet"] = data["sites"][1]["vlans"][0]["subnet"]
        self.assertTrue(any("sobrepoe" in e for e in validate(data)))

    def test_bronze_transit_rejected(self):
        data = copy.deepcopy(SAMPLE)
        data["sites"][3]["vlans"].append({"vlan_id": 200, "purpose": "Invalid transit", "subnet": "10.30.254.0/30"})
        self.assertTrue(any("Gold/Silver" in e for e in validate(data)))

    def test_invalid_site_pool_rejected(self):
        data = copy.deepcopy(SAMPLE)
        data["sites"][1]["site_pool"] = "10.90.0.0/16"
        self.assertTrue(any("site_pool inesperado" in e for e in validate(data)))


if __name__ == "__main__":
    unittest.main()
