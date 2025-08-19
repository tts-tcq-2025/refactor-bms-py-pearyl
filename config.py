# Global language: "EN" or "DE"
LANG = "EN"

# Messages dictionary: flexible for adding more languages
MESSAGES = {
    "EN": {
        "HYPO": "Low {vital} - Hypo condition",
        "NEAR_HYPO": "Warning: Approaching low {vital}",
        "NORMAL": "{vital} is normal",
        "NEAR_HYPER": "Warning: Approaching high {vital}",
        "HYPER": "High {vital} - Hyper condition"
    },
    "DE": {
        "HYPO": "Niedriges {vital} - Hypo-Zustand",
        "NEAR_HYPO": "Warnung: Nähern sich niedrigem {vital}",
        "NORMAL": "{vital} ist normal",
        "NEAR_HYPER": "Warnung: Nähern sich hohem {vital}",
        "HYPER": "Hohes {vital} - Hyper-Zustand"
    }
}

# Vital sign boundary definitions (in Fahrenheit or raw values)
# Format: (lower_limit, upper_limit)
LIMITS = {
    "Temperature": (95, 102),    # Fahrenheit
    "Pulse": (60, 100),          # BPM
    "SPO2": (90, 100)            # Percent
}
