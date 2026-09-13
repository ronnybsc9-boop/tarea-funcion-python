# Definición de la función (recibe 2 parámetros como pide la tarea)
def calcular_salario_semanal(horas_trabajadas, pago_por_hora):
    salario_semanal = horas_trabajadas * pago_por_hora
    return salario_semanal

# Bloque principal del programa
if __name__ == "__main__":
    # Parámetros para un salario semanal de $275 (equivalente a $1100 al mes)
    horas = 40
    pago_hora = 6.875
    
    # Llamada a la función
    resultado = calcular_salario_semanal(horas, pago_hora)
    
    # Mostrar los resultados
    print(f"Horas trabajadas a la semana: {horas}")
    print(f"Pago por hora: ${pago_hora:.2f}")
    print(f"Su salario semanal es: ${resultado:.2f}")
    print(f"Su sueldo mensual aproximado es: ${resultado * 4:.2f}")