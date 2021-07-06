from tp_programado_78771 import soporte

class Cliente:
    def __init__(self, id, estado, tipo, tiempo_inicio):
        self.id = id
        self.estado = estado
        self.tipo = tipo
        self.tiempo_inicio = tiempo_inicio
        self.fin_permanencia = ""

    def salonSiguiente(self):  # definir a que salon va el cliente segun la probabilidad
        if self.estado == "Salon 1":  # el cliente esta en el salon 1
            salon = soporte.salonSiguiente()
            salon_str = "Salon " + salon
            return salon_str
        else:
             return "se fue"

    def finPermanencia(self, reloj):
        if self.estado == "Salon 1":
            if self.tiempo_inicio <= (3600 * 2):
                fin_permanencia = soporte.generar_permanencia(180, reloj)
                return fin_permanencia
            elif self.tiempo_inicio <= (3600 * 5):
                fin_permanencia = soporte.generar_permanencia(240, reloj)
                return fin_permanencia
            else:
                fin_permanencia = soporte.generar_permanencia(210, reloj)
                return fin_permanencia
        elif self.estado == "Salon 2":
            if self.tiempo_inicio <= (3600 * 2):
                fin_permanencia = soporte.generar_permanencia(210, reloj)
                return fin_permanencia
            elif self.tiempo_inicio <= (3600 * 5):
                fin_permanencia = soporte.generar_permanencia(270, reloj)
                return fin_permanencia
            else:
                fin_permanencia = soporte.generar_permanencia(300, reloj)
                return fin_permanencia
        else:
            if self.estado == "se fue":
                self.fin_permanencia = ""
                return
            if self.tiempo_inicio <= (3600 * 2):
                fin_permanencia = soporte.generar_permanencia(210, reloj)
                return fin_permanencia
            elif self.tiempo_inicio <= (3600 * 5):
                fin_permanencia = soporte.generar_permanencia(270, reloj)
                return fin_permanencia
            else:
                fin_permanencia = soporte.generar_permanencia(300, reloj)
                return fin_permanencia

    def ejecutar(self, reloj):

        if self.fin_permanencia == "":  # si esta vacio le creo el fin de permanencia
            self.fin_permanencia = self.finPermanencia(reloj)
            return
        else:
            if reloj == self.fin_permanencia:
                self.estado = self.salonSiguiente()
                if self.estado != "se fue":
                    self.fin_permanencia = self.finPermanencia(reloj)  # verificar si este era el error
                else:
                    self.fin_permanencia = "-"
                    self.tipo = "F"
                    return
                return
            else:
                return



class Salones:
    def __init__(self, id, cantidad):
        self.id = id
        self.cantidad = cantidad
