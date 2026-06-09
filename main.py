# PRO111 - HITO 4
# Control de asistencia y rendimiento académico
# Inicialización de contadores
total_estudiantes = 0
total_aprobados = 0
total_reprobados_nota = 0
total_reprobados_asistencia = 0
continuar = "S"
while continuar.upper() == "S":
    print("\n====================================")
    print("REGISTRO DE ESTUDIANTE")
    print("====================================")
    nombre = input("Nombre completo: ")
    clases_programadas = int(input("Cantidad de clases programadas: "))
    clases_asistidas = int(input("Cantidad de clases asistidas: "))
    nota = float(input("Calificación final (0 - 100): "))
    # Calcular porcentaje de asistencia
    asistencia = (clases_asistidas / clases_programadas) * 100
    # Determinar condición del estudiante
    if asistencia < 80:
        estado = "Reprobado por asistencia"
        total_reprobados_asistencia += 1
    elif nota >= 51:
        estado = "Aprobado"
        total_aprobados += 1
    else:
        estado = "Reprobado por nota"
        total_reprobados_nota += 1
    # Actualizar total de estudiantes
    total_estudiantes += 1
    # Mostrar resultado individual
    print("\n----- RESULTADO DEL ESTUDIANTE -----")
    print("Nombre:", nombre)
    print("Asistencia: {:.2f}%".format(asistencia))
    print("Nota final:", nota)
    print("Estado:", estado)
    # Preguntar si desea continuar
    continuar = input(
        "\n¿Desea registrar otro estudiante? (S/N): ")
# Resumen final
if total_estudiantes > 0:
    porcentaje_aprobados = (
        total_aprobados / total_estudiantes
    ) * 100
else:
    porcentaje_aprobados = 0
print("\n====================================")
print("RESUMEN FINAL DEL CURSO")
print("====================================")
print("Total de estudiantes procesados:",
      total_estudiantes)
print("Cantidad de aprobados:",
      total_aprobados)
print("Cantidad de reprobados por nota:",
      total_reprobados_nota)
print("Cantidad de reprobados por asistencia:",
      total_reprobados_asistencia)
print("Porcentaje de aprobados: {:.2f}%"
      .format(porcentaje_aprobados))
print("====================================")