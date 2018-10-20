class Horario:
    pass

h1 = Horario()
h1.horas = 11
h1.minutos = 34
h1.segundos = 22

h2 = Horario()
h2.horas = 11
h2.minutos = 34
h2.segundos = 23

def imprimeHorario(time):
    print(f"{time.horas}:{time.minutos}:{time.segundos}")

imprimeHorario(h1)
imprimeHorario(h2)

def depois(h1, h2):
    if h1.horas < h2.horas:
        return 1
    elif h1.horas is h2.horas:
        if h1.minutos < h2.minutos:
            return 1
        elif h1.minutos is h2.minutos:
            if h1.segundos < h2.segundos:
                return 1
    return 0

print(depois(h1, h2))