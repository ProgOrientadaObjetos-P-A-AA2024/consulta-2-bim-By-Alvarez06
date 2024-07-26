class Estudiante:
    def __init__(self, nombres, apellidos, identificacion, edad):
        self._nombres_estudiante = nombres
        self._apellidos_estudiante = apellidos
        self._identificacion_estudiante = identificacion
        self._edad_estudiante = edad

    def establecer_nombres_estudiante(self, nombres):
        self._nombres_estudiante = nombres

    def establecer_apellido_estudiante(self, apellidos):
        self._apellidos_estudiante = apellidos

    def establecer_identificacion_estudiante(self, identificacion):
        self._identificacion_estudiante = identificacion

    def establecer_edad_estudiante(self, edad):
        self._edad_estudiante = edad

    def obtener_nombres_estudiante(self):
        return self._nombres_estudiante

    def obtener_apellido_estudiante(self):
        return self._apellidos_estudiante

    def obtener_identificacion_estudiante(self):
        return self._identificacion_estudiante

    def obtener_edad_estudiante(self):
        return self._edad_estudiante

    def __str__(self):
        return f"Nombre: {self._nombres_estudiante}\n" \
               f"Apellido: {self._apellidos_estudiante}\n" \
               f"Identificación: {self._identificacion_estudiante}\n" \
               f"Edad: {self._edad_estudiante}"


class EstudianteDistancia(Estudiante):
    def __init__(self, nombres, apellidos, identificacion, edad):
        super().__init__(nombres, apellidos, identificacion, edad)
        self._numero_asignaturas = 0
        self._costo_asignatura = 0.0
        self._matricula_distancia = 0.0

    def establecer_numero_asignaturas(self, numero):
        self._numero_asignaturas = numero

    def establecer_costo_asignatura(self, costo):
        self._costo_asignatura = costo

    def calcular_matricula_distancia(self):
        self._matricula_distancia = self._numero_asignaturas * self._costo_asignatura

    def obtener_numero_asignaturas(self):
        return self._numero_asignaturas

    def obtener_costo_asignatura(self):
        return self._costo_asignatura

    def obtener_matricula_distancia(self):
        return self._matricula_distancia

    def __str__(self):
        return super().__str__() + f"\nNumero de asignaturas: {self._numero_asignaturas}\n" \
                                   f"Valor de asignatura: {self._costo_asignatura:.2f}\n" \
                                   f"Valor matricula: {self.obtener_matricula_distancia():.2f}"


class EstudiantePresencial(Estudiante):
    def __init__(self, nombres, apellidos, identificacion, edad):
        super().__init__(nombres, apellidos, identificacion, edad)
        self._numero_creditos = 0
        self._costo_credito = 0.0
        self._matricula_presencial = 0.0

    def establecer_numero_creditos(self, numero):
        self._numero_creditos = numero

    def establecer_costo_credito(self, costo):
        self._costo_credito = costo

    def calcular_matricula_presencial(self):
        self._matricula_presencial = self._numero_creditos * self._costo_credito

    def obtener_numero_creditos(self):
        return self._numero_creditos

    def obtener_costo_credito(self):
        return self._costo_credito

    def obtener_matricula_presencial(self):
        return self._matricula_presencial

    def __str__(self):
        return super().__str__() + f"\nNumero de creditos: {self._numero_creditos}\n" \
                                   f"Valor de credito: {self._costo_credito:.2f}\n" \
                                   f"Valor matricula: {self.obtener_matricula_presencial():.2f}"


def main():
    nombre = "René"
    apellido = "Elizalde"
    identificacion = "110011"
    edad = 36

    est_distancia = EstudianteDistancia(nombre, apellido, identificacion, edad)
    est_distancia.establecer_numero_asignaturas(5)
    est_distancia.establecer_costo_asignatura(100)
    est_distancia.calcular_matricula_distancia()

    est_presencial = EstudiantePresencial(nombre, apellido, identificacion, edad)
    est_presencial.establecer_numero_creditos(2)
    est_presencial.establecer_costo_credito(150)
    est_presencial.calcular_matricula_presencial()

    print(est_distancia)
    print()
    print(est_presencial)


if __name__ == "__main__":
    main()
