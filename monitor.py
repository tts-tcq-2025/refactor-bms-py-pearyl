from config import LANG, MESSAGES, LIMITS

def c_to_f(temp_c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return temp_c * 9 / 5 + 32

def classify(value: float, vital: str) -> str:
    """Map vital measurement to condition band (simplified)."""
    lower, upper = LIMITS[vital]
    tol = 0.015 * upper  # 1.5% of upper limit

    bands = [
        (value < lower, "HYPO"),
        (lower <= value < lower + tol, "NEAR_HYPO"),
        (lower + tol <= value <= upper - tol, "NORMAL"),
        (upper - tol < value <= upper, "NEAR_HYPER"),
    ]
    for cond, label in bands:
        if cond:
            return label
    return "HYPER"

def message(condition: str, vital: str) -> str:
    """Return localized message for given condition."""
    return MESSAGES[LANG][condition].format(vital=vital)


def analyze_vital(vital: str, value: float, unit: str = None) -> str:
    """Analyze one vital, with unit conversion if needed."""
    if vital == "Temperature" and unit == "C":
        value = c_to_f(value)
    cond = classify(value, vital)
    return message(cond, vital)

def is_vital_ok(msg: str) -> bool:
    """Check if a vital message indicates acceptable range."""
    txt = msg.lower()
    return "normal" in txt or "warnung" in txt or "warning" in txt

def vitals_ok(vitals: dict) -> bool:
    """Check if all vitals are within acceptable range."""
    results = []
    for vital, (val, unit) in vitals.items():
        msg = analyze_vital(vital, val, unit)
        print(msg)
        results.append(is_vital_ok(msg))
    return all(results)
