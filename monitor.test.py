import unittest
from unittest.mock import patch
from monitor import vitals_ok, analyze_vital


class TestMonitor(unittest.TestCase):

    def capture_print(self, func, *args, **kwargs):
        """Helper to run a function and capture printed output using mock."""
        with patch("builtins.print") as mock_print:
            result = func(*args, **kwargs)
        printed = [call.args[0] for call in mock_print.call_args_list]
        return result, printed

    def test_vitals_ok_all_normal(self):
        vitals = {
            "Temperature": (98.6, "F"),
            "Pulse": (72, "BPM"),
            "SPO2": (95, "%")
        }

        ok, printed = self.capture_print(vitals_ok, vitals)

        self.assertTrue(ok)
        self.assertIn("Temperature is normal", printed)
        self.assertIn("Pulse is normal", printed)
        self.assertIn("SPO2 is normal", printed)

    def test_vitals_ok_with_hyper(self):
        vitals = {
            "Pulse": (150, "BPM"),
        }

        ok, printed = self.capture_print(vitals_ok, vitals)

        self.assertFalse(ok)
        self.assertIn("High Pulse - Hyper condition", printed)

    def test_vitals_ok_with_hypo(self):
        vitals = {
            "SPO2": (80, "%"),
        }

        ok, printed = self.capture_print(vitals_ok, vitals)

        self.assertFalse(ok)
        self.assertIn("Low SPO2 - Hypo condition", printed)

    def test_temperature_conversion(self):
        # Celsius input should convert to Fahrenheit before analysis
        msg = analyze_vital("Temperature", 37, "C")
        self.assertIn("Temperature is normal", msg)

    def test_near_hypo(self):
        # Just above lower limit
        vitals = {"Pulse": (61, "BPM")}
        ok, printed = self.capture_print(vitals_ok, vitals)

        self.assertTrue(ok)
        self.assertIn("Warning: Approaching low Pulse", printed)

    def test_near_hyper(self):
        # Just below upper limit
        vitals = {"Temperature": (101.5, "F")}
        ok, printed = self.capture_print(vitals_ok, vitals)

        self.assertTrue(ok)
        self.assertIn("Warning: Approaching high Temperature", printed)


if __name__ == "__main__":
    unittest.main()
