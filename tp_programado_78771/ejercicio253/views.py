import numpy as np
from django.shortcuts import render
from django.views import generic
from .forms import ParametersForm
from tp_programado_78771 import soporte, clases


class simulacion(generic.FormView):
    form_class = ParametersForm
    template_name = 'TP.html'

    def form_valid(self, form):

        # parametros de entrada por form
        fin = form.cleaned_data['fin']
        relojFin = form.cleaned_data['min_fin']
        relojInicio = form.cleaned_data['min_inicio']

        # seteo de variables
        matriz = [[''] * 10 for f in range(1)]
        matriz_personas = [[''] * 2 for f in range(1)]
        reloj = 0
        eventos = ["Inicializacion", "llegada_Cliente_A", "llegada_Cliente_B", "Fin Permanencia", "Apertura Puerta"]
        evento = ''
        estados_cliente = ["Salon 1", "Salon 2", "Salon 3"]
        Salones = []
        vector_personas = []
        init = True
        tipo_cliente = ''
        llegada_cliente = False
        llegada_cliente_A = False
        llegada_cliente_B = False
        proxima_llegada_A = 0
        proxima_llegada_B = 0
        promedio = 0
        contador = 0
        clientes = []
        id_cliente = 0
        estado = ''
        acumulador = 0
        estadia = 0
        personas_sistema = 0
        salidas = 0
        prom = 0
        apertura = True
        min = 0
        max = 1800

        # seteo de objetos permanentes
        Salones = [clases.Salones(1, 0),
                   clases.Salones(2, 0),
                   clases.Salones(3, 0)]

        while reloj <= fin:
            personas_sistema = 0
            # inicializacion
            if init:
                evento = eventos[0]
                proxima_llegada_A = reloj + soporte.generar_llegada_A()
                init = False

            # inicio de los trabajos
            elif llegada_cliente:
                # FIJARSE QUE TIPO DE CLIENTE ES
                if reloj < 3600:  # una hora
                    evento = eventos[1]
                    tipo_cliente = 'A'
                    estado = estados_cliente[0]
                    proxima_llegada_A = reloj + soporte.generar_llegada_A()

                else:
                    if reloj == proxima_llegada_A:
                        evento = eventos[1]
                        tipo_cliente = 'A'
                        estado = estados_cliente[0]
                        proxima_llegada_A = reloj + soporte.generar_llegada_A()
                    else:
                        evento = eventos[2]
                        tipo_cliente = 'B'
                        estado = estados_cliente[0]
                        proxima_llegada_B = reloj + soporte.generar_llegada_B()

                llegada_cliente = False  # por las dudas
                id_cliente += 1  # sumo para agregar un nuevo cliente al vector de clientes
                estado = estados_cliente[0]  # porque es llegada
                clientes.append(clases.Cliente(id_cliente, estado, tipo_cliente, reloj))
                matriz_cliente = [[''] * 2 for f in range(len(matriz))]  # para agregar el nuevo cliente a la matriz
                matriz = np.hstack((matriz, matriz_cliente))
                for Cliente in clientes:
                    Cliente.ejecutar(reloj)

            elif reloj == 3600 and apertura:
                temporal_tiempo = 3600
                llegada_cliente = False
                llegada_cliente_A = False
                llegada_cliente_B = False
                evento = eventos[4]
                proxima_llegada_B = reloj + soporte.generar_llegada_B()
                apertura = False

            else:
                evento = eventos[3]  # es un evento de fin de permanencia
                for Cliente in clientes:
                    if Cliente.estado != "se fue":
                        Cliente.ejecutar(reloj)
                    else:
                        pass
                        #if Cliente.fin_permanencia == "-" and Cliente.tipo == "F":  # falta validar otra cosa mas
                        #"    contador += 1
                        #"    acumulador += reloj - Cliente.tiempo_inicio
                        #"    Cliente.asignar()

            # Metricas
            for Cliente in clientes:
                if Cliente.tipo != "F" and Cliente.estado != "se fue":
                    personas_sistema += 1

            if min == 0 and reloj > 1800:
                min = 1800
                max = min + 1800
            if reloj >= min and reloj < max:
                vector_personas.append(personas_sistema)
                min = max
                max = min + 1800

            for Cliente in clientes: #contador OKKKKKK
                if Cliente.estado == "se fue" and Cliente.tipo == "F":
                    contador += 1
                    Cliente.tipo = "D"
                    estadia = reloj - Cliente.tiempo_inicio
                    acumulador += estadia



          # #metrica del promedio
          # for Cliente in clientes:
          #     if Cliente.fin_permanencia == reloj:
          #         acumulador += reloj - Cliente.tiempo_inicio
          #         contador += 1

            # logica de guardado
            if reloj <= relojFin and reloj >= relojInicio:
                matriz[-1][0] = evento
                matriz[-1][1] = reloj
                matriz[-1][2] = proxima_llegada_A
                matriz[-1][3] = proxima_llegada_B

                matriz[-1][4] = contador
                matriz[-1][5] = acumulador
                matriz[-1][6] = personas_sistema
                matriz[-1][7] = prom

                for i in range(id_cliente):
                    matriz[-1][8 + (i * 2)] = clientes[i].estado  # OJO
                    matriz[-1][9 + (i * 2)] = clientes[i].fin_permanencia  # OJO

                vector_temporal = [''] * len(matriz[0])
                matriz = np.vstack([matriz, vector_temporal])

            # logico proximo evento
            temporal_tiempo = proxima_llegada_A
            if proxima_llegada_B < temporal_tiempo and proxima_llegada_B > reloj:
                llegada_cliente_B = True
                llegada_cliente = True
                temporal_tiempo = proxima_llegada_B
            else:
                llegada_cliente = True
                llegada_cliente_A = True

            for i in range(len(clientes)):
                if clientes[i].fin_permanencia != "" and clientes[i].estado != "se fue":
                    if clientes[i].fin_permanencia < temporal_tiempo:
                        temporal_tiempo = clientes[i].fin_permanencia
                        llegada_cliente = False
                        llegada_cliente_A = False
                        llegada_cliente_B = False

            if 3600 <= temporal_tiempo and apertura:
                temporal_tiempo = 3600

            reloj = temporal_tiempo

        if contador != 0:
            promedio = str(round(acumulador/contador, 2)) + " segundos"
        else:
            promedio = "no hay personas que se hayan ido de la exposicion"

        vector_resultado = [''] * len(matriz[0])
        vector_resultado[0] = evento
        vector_resultado[1] = relojFin
        vector_resultado[2] = proxima_llegada_A
        vector_resultado[3] = proxima_llegada_B

        vector_resultado[4] = contador
        vector_resultado[5] = acumulador
        vector_resultado[6] = personas_sistema
        vector_resultado[7] = promedio

        for i in range(id_cliente):
            vector_resultado[8 + (i * 2)] = clientes[i].estado
            vector_resultado[9 + (i * 2)] = clientes[i].fin_permanencia


        if len(vector_personas) > 1:
            np.delete(vector_personas, 0)
            for i in range(len(vector_personas)):  # recorro teniendo una fila por cada elemento del vector

                if i != 0:
                    vector_temporal = [0] * 2
                    matriz_personas = np.vstack([matriz_personas, vector_temporal])
                    matriz_personas[i][0] = str(30 * i) + " minutos"
                    matriz_personas[i][1] = vector_personas[i]
                else:
                    pass


        return render(self.request, self.template_name, {"vectorResultado": vector_resultado, "matrizResultado": matriz,
                                                         "vectorEntrada": [fin, relojInicio, relojFin],
                                                         "clientes": clientes, "matriz_personas": matriz_personas, "promedio": promedio})
