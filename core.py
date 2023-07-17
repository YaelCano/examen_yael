import json


class CitasManager:
    def __init__(self, archivio):
        self.archivio = archivio
        self.citas = self.cargar_citas()
    
    def cargar_citas(self):
        try:
            with open(self.archivio) as archivo_Json:
                citas = json.load(archivo_Json)
                return citas
            
        except FileNotFoundError:
            return []

    def guardar_citas(self):
        with open(self.archivio,'w') as archivo_Json:
            json.dump(self.citas, archivo_Json)
    
    def agregar_cita(self, cita):
        self.citas.append(cita)
        self.guardar_citas()
    
    def buscar_citas(self, criterio):
        citas_encontradas = []
        for cita in self.citas:
            if criterio in cita:
                citas_encontradas.append(cita)
        return citas_encontradas
    
    def modificar_cita(self, cita_modificada):
        for i, cita in enumerate(self.citas):
            if cita['fecha'] == cita_modificada['fecha'] and cita['hora'] == cita_modificada['hora']:
                self.citas[i] = cita_modificada
                self.guardar_citas()
                return True
        return False
    def cancelar_cita(self, cita_cancelada):    
        for i, cita in enumerate(self.citas):
            if cita['fecha'] == cita_cancelada['fecha'] and cita['hora'] == cita_cancelada['hora']:
                del self.citas[i]
                self.guardar_citas()
                return True
        return False    
