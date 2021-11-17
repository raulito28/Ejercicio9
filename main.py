import persistencia_pickle as pp
import car_class
import random as rd
COCHES = "Coches_obj.txt"
lista_coches = pp.retrieve(COCHES)
if lista_coches == None:
    lista_coches = []
while True:
    marca = input("Marca: ")
    if marca == "fin":
        break
    modelo = input("Modelo: ")
    combustible = input("Combustible: ")
    cilindrada = input("Cilindrada: ")
    coche = car_class.Car(marca, modelo, combustible, cilindrada)
    lista_coches.append(coche)
    coche.move_pos(rd.random()*100, rd.random()*600)
    print("Posición: ", coche.get_pos())
    coche.move_incr(rd.random()*10, rd.random()*60)
    print("Posición", coche.get_pos())
    del(coche)
pp.store(lista_coches, COCHES)
lista_coches = []
lista_coches = pp.load(COCHES)
for car in lista_coches:
    print("Marca, Modelo, Combustible, Cilindrada: ", \
          car.marca, car.modelo, car.combustible, car.cilindrada)
    print("Posición: ", car.get_pos(), "\n")