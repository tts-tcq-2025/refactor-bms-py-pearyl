
from time import sleep
import sys

def temperature_ok(temperature):
  return 95 <= temperature <= 102

def pulseRate_ok(pulseRate):
  return 60 <= pulseRate <= 100

def spo2_ok(spo2):
  return spo2 >= 90

def alert(msg):
  print(msg)
  for i in range(6):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(1)

def vitals_ok(temperature, pulseRate, spo2):
  if not temperature_ok(temperature):
    alert('Temperature critical!')
    return False
  elif not pulseRate_ok(pulseRate):
    alert('Pulse Rate is out of range!')
    return False
  elif not spo2_ok(spo2):
    alert('Oxygen Saturation out of range!')
    return False
