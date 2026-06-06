import unittest
from monitor import SystemPulse

class TestSystemPulseMetrics(unittest.TestCase):
    def setUp(self):
        self.engine = SystemPulse()

    def test_telemetry_schema_integrity(self):
        """Ensures the hardware metric parsing maps keys perfectly."""
        metrics = self.engine.gather_telemetry()
        self.assertIn("timestamp", metrics)
        self.assertIn("cpu_metrics", metrics)
        self.assertIn("memory_metrics", metrics)
        self.assertIn("storage_metrics", metrics)

    def test_cpu_ranges_logical(self):
        """Validates that real-time tracking percentages fall within global 0-100 bounds."""
        metrics = self.engine.gather_telemetry()
        cpu_pct = metrics["cpu_metrics"]["overall_utilization_pct"]
        self.assertTrue(0 <= cpu_pct <= 100)

if __name__ == "__main__":
    unittest.main()
