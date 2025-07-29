import unittest
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):
    def test_vitals_fail_when_temperature_is_out_of_range(self):
        self.assertFalse(vitals_ok(94, 75, 98))   # Too low
        self.assertFalse(vitals_ok(103, 75, 98))  # Too high

    def test_vitals_fail_when_pulse_rate_is_out_of_range(self):
        self.assertFalse(vitals_ok(98, 59, 98))   # Too low
        self.assertFalse(vitals_ok(98, 101, 98))  # Too high

    def test_vitals_fail_when_spo2_is_out_of_range(self):
        self.assertFalse(vitals_ok(98, 75, 89))   # Too low

    def test_vitals_pass_when_all_are_in_range(self):
        self.assertTrue(vitals_ok(98.1, 70, 98))

if __name__ == '__main__':
  unittest.main()
