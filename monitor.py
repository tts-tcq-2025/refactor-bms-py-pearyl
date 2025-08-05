from time import sleep
import sys

def is_in_range(value, min_val, max_val=None):
    return value >= min_val if max_val is None else min_val <= value <= max_val

def alert(msg):
    print(msg)
    for _ in range(6):
        for symbol in ['* ', ' *']:
            print(f'\r{symbol}', end='')
            sys.stdout.flush()
            sleep(1)

def vitals_ok(temperature, pulseRate, spo2):
    checks = [
        (is_in_range(temperature, 95, 102), 'Temperature critical!'),
        (is_in_range(pulseRate, 60, 100), 'Pulse Rate is out of range!'),
        (is_in_range(spo2, 90), 'Oxygen Saturation out of range!')
    ]

    for ok, msg in checks:
        if not ok:
            alert(msg)
            return False
    return True
