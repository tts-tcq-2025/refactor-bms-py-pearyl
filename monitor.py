from config import LANG, MESSAGES, LIMITS

def c_to_f(temp_c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return temp_c * 9/5 + 32

def classify(value: float, vital: str) -> str:
    """Map vital measurement to condition band."""
    lower, upper = LIMITS[vital]
    tol = 0.015 * upper  # 1.5% of upper limit

    if value < lower:
        return "HYPO"
    elif lower <= value < lower + tol:
        return "NEAR_HYPO"
    elif lower + tol <= value <= upper - tol:
        return "NORMAL"
    elif upper - tol < value <= upper:
        return "NEAR_HYPER"
    else:
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

def vitals_ok(vitals: dict) -> bool:
    """Check if all vitals are within acceptable range."""
    results = []
    for vital, (val, unit) in vitals.items():
        msg = analyze_vital(vital, val, unit)
        print(msg)
        results.append("Normal" in msg or "Warnung" in msg or "Warning" in msg)
    return all(results)
