from time import sleep
import sys

TEMP_LIMITS_F = {
    "min": 95,
    "max": 102,
    "message": "Temperature critical!"
}

PULSE_LIMITS = {
    "min": 60,
    "max": 100,
    "message": "Pulse Rate is out of range!"
}

SPO2_LIMITS = {
    "min": 90,
    "message": "Oxygen Saturation out of range!"
}

def is_in_range(value, min_val, max_val=None):
    return value >= min_val if max_val is None else min_val <= value <= max_val


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def alert(msg):
    print(msg)
    for _ in range(6):
        for symbol in ['* ', ' *']:
            print(f'\r{symbol}', end='')
            sys.stdout.flush()
            sleep(1)

def vitals_ok(temperature, pulseRate, spo2, temp_unit="F"):
    if temp_unit.upper() == "C":
        temperature = celsius_to_fahrenheit(temperature)

    checks = [
        (is_in_range(temperature, TEMP_LIMITS_F["min"], TEMP_LIMITS_F["max"]),
         TEMP_LIMITS_F["message"]),
        (is_in_range(pulseRate, PULSE_LIMITS["min"], PULSE_LIMITS["max"]),
         PULSE_LIMITS["message"]),
        (is_in_range(spo2, SPO2_LIMITS["min"]),
         SPO2_LIMITS["message"])
    ]

    for ok, msg in checks:
        if not ok:
            alert(msg)
            return False
    return True
