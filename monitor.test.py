import unittest
from monitor import vitals_ok, celsius_to_fahrenheit

class MonitorTest(unittest.TestCase):
    def test_vitals_failures(self):
        failing_cases = [
            (94, 75, 98, "F"),   # low temp
            (103, 75, 98, "F"),  # high temp
            (98, 59, 98, "F"),   # low pulse
            (98, 101, 98, "F"),  # high pulse
            (98, 75, 89, "F"),   # low spo2
        ]
        for temp, pulse, spo2, unit in failing_cases:
            with self.subTest(temp=temp, pulse=pulse, spo2=spo2, unit=unit):
                self.assertFalse(vitals_ok(temp, pulse, spo2, unit))

    def test_vitals_pass_when_all_are_in_range(self):
        passing_cases = [
            (95, 60, 90, "F"),
            (98.6, 80, 99, "F"),
            (102, 100, 92, "F"),
        ]
        for temp, pulse, spo2, unit in passing_cases:
            with self.subTest(temp=temp, pulse=pulse, spo2=spo2, unit=unit):
                self.assertTrue(vitals_ok(temp, pulse, spo2, unit))

    def test_temperature_in_celsius(self):
        # 37°C ≈ 98.6°F (Normal)
        self.assertTrue(vitals_ok(37, 75, 98, "C"))
        # 40°C ≈ 104°F (Too high)
        self.assertFalse(vitals_ok(40, 75, 98, "C"))
        # 34°C ≈ 93.2°F (Too low)
        self.assertFalse(vitals_ok(34, 75, 98, "C"))

    def test_conversion_function(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6, places=1)

if __name__ == '__main__':
    unittest.main()
