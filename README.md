# Programming Paradigms

Health Monitoring Systems

[Here is an article that helps to understand the Adult Vital Signs](https://en.wikipedia.org/wiki/Vital_signs)

[Here is a reference to Medical monitoring](https://en.wikipedia.org/wiki/Monitoring_(medicine))

## Purpose

Continuous monitoring of vital signs, such as respiration and heartbeat, plays a crucial role in early detection and prediction of conditions that may affect the wellbeing of a patient. 

Monitoring requires accurate reading and thresholding of the vitals.

---

# Vital Signs Monitor

A simple Python tool to monitor **Temperature**, **Pulse**, and **SPO2** values, classify them into health conditions, and provide **localized messages** in English or German.  

---

## Features
- Supports **multiple vital signs** (Temperature, Pulse, SPO2).  
- Automatic **Celsius → Fahrenheit** conversion for temperature.  
- **Localized messages** in English (`EN`) and German (`DE`).  
- Early warning via **NEAR_HYPO** and **NEAR_HYPER** detection bands.  
- Fully tested with `unittest` (includes mocking of `print`).  

---

## Classification Ranges

Each vital sign is classified into **bands** using its lower and upper limits.  
A **tolerance** of `1.5%` of the upper limit is applied to detect *near-critical* conditions.  

| Vital        | Units      | HYPO (Below) | NEAR_HYPO (Up to) | NORMAL (Range) | NEAR_HYPER (Up to) | HYPER (Above) |
|--------------|------------|--------------|-------------------|----------------|--------------------|---------------|
| **Temperature** | °F (or °C → converted) | `< 95.0` | `95.0 – 96.53` | `96.54 – 100.47` | `100.48 – 102.0` | `> 102.0` |
| **Pulse**      | Beats/min | `< 60` | `60 – 61.5` | `61.6 – 98.5` | `98.6 – 100` | `> 100` |
| **SPO2**       | % Oxygen  | `< 90` | `90 – 91.5` | `91.6 – 98.5` | `98.6 – 100` | `> 100` |

---
