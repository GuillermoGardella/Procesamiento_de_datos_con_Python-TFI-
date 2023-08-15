# Lista de sueldo de Juan por mes durante un año
sueldo_de_Juan = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]

def calcular_promedio_sueldo(sueldos):
    total_sueldos = sum(sueldos)
    sueldo_promedio = total_sueldos / len(sueldos)
    return sueldo_promedio

def evaluar_sueldo(sueldo_promedio):
    if sueldo_promedio < 300:
        return "Sueldo bajo"
    elif sueldo_promedio <= 900:
        return "Sueldo normal"
    else:
        return "Sueldo mejor de lo normal"

# Calcular el promedio de sueldos de Juan
promedio_juan = calcular_promedio_sueldo(sueldo_de_Juan)

# Evaluar la categoría de sueldo de Juan
categoria_sueldo = evaluar_sueldo(promedio_juan)

print(f"El sueldo promedio de Juan es de: ${promedio_juan:.2f}")
print(f"La categoría del sueldo de Juan es: {categoria_sueldo}")
