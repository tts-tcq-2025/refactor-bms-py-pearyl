import unittest
from monitor import vitals_ok

class MonitorTest(unittest.TestCase):
    def test_vitals_failures(self):
        failing_cases = [
            (94, 75, 98), # low temp
            (103, 75, 98), # high temp
            (98, 59, 98), # low pulse
            (98, 101, 98), # high pulse
            (98, 75, 89), # low spo2
        ]
        for temp, pulse, spo2 in failing_cases:
            with self.subTest(temp=temp, pulse=pulse, spo2=spo2):
                self.assertFalse(vitals_ok(temp, pulse, spo2))

    def test_vitals_pass_when_all_are_in_range(self):
        passing_cases = [
            (95, 60, 90),
            (98.6, 80, 99),
            (102, 100, 92),
        ]
        for temp, pulse, spo2 in passing_cases:
            with self.subTest(temp=temp, pulse=pulse, spo2=spo2):
                self.assertTrue(vitals_ok(temp, pulse, spo2))

if __name__ == '__main__':
    unittest.main()

