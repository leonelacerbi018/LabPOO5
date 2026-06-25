class Empleado:
    def calcularSalario(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class EmpleadoPorHora(Empleado):
    def __init__(self, horas_trabajadas, tarifa_hora):
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora
    
    def calcularSalario(self):
        return self.horas_trabajadas * self.tarifa_hora

class EmpleadoFijo(Empleado):
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual
    
    def calcularSalario(self):
        return self.salario_mensual


def main():
    empleados = [
        EmpleadoPorHora(40, 15),
        EmpleadoFijo(3000)
    ]
    
    salario_total = 0
    
    for empleado in empleados:
        salario = empleado.calcularSalario()
        salario_total += salario
        print(f"Salario de {empleado.__class__.__name__}: ${salario}")
    
    print(f"Salario total de todos los empleados: ${salario_total}")

if __name__ == "__main__":
    main()
