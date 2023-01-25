from time import localtime, time, mktime


class JornadaLaboral:
    def __init__(self, hora_inicio, hora_fin):
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def esHorarioLaboral(self):
        """
        Devuelve 0 si es horario laboral, -1 si es antes, 1 si es despues
        """
        result = localtime()
        esHorario = 0
        if self.hora_inicio > result.tm_hour:
            esHorario = -1
        if self.hora_fin <= result.tm_hour:
            esHorario = 1
        return esHorario

    def tiempoFinTrabajo(self):
        """
        Devuelve la cantidad de segundos para finalizar la jornada laboral
        """
        segundos = time()
        result = localtime()
        horarioFin = mktime((result.tm_year, result.tm_mon,
                            result.tm_mday, self.hora_fin, 0, 0, 0, 0, 0))
        return horarioFin-segundos
