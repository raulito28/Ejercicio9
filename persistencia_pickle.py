import pickle
def store(var, filename):
    pickle.dump(var, open(filename, "wb"))

def retrieve(filename):
    try:
        archivo = open(filename, "rb" )
    except:
        print("Error al abrir el archivo", filename)
        return None

    content = pickle.load(archivo)
    archivo.close()
    return content