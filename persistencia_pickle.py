import pickle
def store(var, Coches):
    pickle.dump(var, open(Coches, "wb"))

def retrieve(Coches):
    try:
        archivo = open(Coches, "rb" )
    except:
        print("Error al abrir el archivo", Coches)
        return None
    content = pickle.load(archivo)
    archivo.close()
    return content