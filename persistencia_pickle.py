import pickle
def store(var, Coches):
    pickle.dump(var, open(Coches, "wb"))

def retrieve(Coches):
    try:
        f_o = open(Coches, "rb" )
    except:
        print("Error al abrir el archivo", Coches)
        return None
    content = pickle.load(f_o)
    f_o.close()
    return content