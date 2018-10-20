# As classes são coleçoes de objetos com caracteristicas e
# metodos semelhantes. São usadas para criação de objetos


class Cachorro():
    cobertura = "pelos"
    alimento = "carne"
    patas = 4
    habitat = "domestico"
    nome = "rex"

class Galinhas():
    cobertura= "penas"
    alimento = "graos"
    patas = 2
    habitat = "domestico"
    bico = "pequeno"

class Pai():
    nome = "Eduardo"
    sobrenome = "Santos"
    residencia = "Açailandia"

class Filha(Pai):
    nome = "Cristina"
    olhos = "Castanhos"

class Neta(Pai):
    nome = "Samara"


print(help(Pai))
