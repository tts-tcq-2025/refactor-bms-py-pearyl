# Programming Paradigms

Health Monitoring Systems

[Here is an article that helps to understand the Adult Vital Signs](https://en.wikipedia.org/wiki/Vital_signs)

[Here is a reference to Medical monitoring](https://en.wikipedia.org/wiki/Monitoring_(medicine))

## Purpose

Continuous monitoring of vital signs, such as respiration and heartbeat, plays a crucial role in early detection and prediction of conditions that may affect the wellbeing of a patient. 

Monitoring requires accurate reading and thresholding of the vitals.

## Extension Implemented

### Accept input in different units (New Feature)

Some sensors report the **temperature in Celsius** instead of Fahrenheit.  
We added support for specifying the unit (`"F"` or `"C"`) along with the measurement.  

To avoid duplicating thresholds in different units, the code **first translates all temperature values into a common unit (Fahrenheit)**, and then applies the same thresholds:

- upto 95°F: **HYPO_THERMIA**  
- 95°F to 96.53°F: **NEAR_HYPO**  
- 96.54°F to 100.47°F: **NORMAL**  
- 100.48°F to 102°F: **NEAR_HYPER**  
- 102°F and above: **HYPER_THERMIA**
