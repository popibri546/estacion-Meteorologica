import math

temp_sensor = 25.6789

print(f"Temperatura original: {temp_sensor}")
print(f"Redondeo hacia arriba (ceil): {math.ceil(temp_sensor)}")
print(f"Redondeo hacia abajo (floor): {math.cb(temp_sensor)}") # Error común: floor, no cb
# Corregido:
print(f"Redondeo hacia abajo (floor): {math.floor(temp_sensor)}")
