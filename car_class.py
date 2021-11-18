class Car:
    def __init__(self, marca , modelo, combustible, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.cilindrada = cilindrada
        self.pos_x = 0
        self.pos_y = 0
    def move_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y
    def move_incr(self, x, y):
        self.pos_x += x
        self.pos_y += y
    def get_pos(self,):
        return self.pos_x, self.pos_y
    def set_wheel(self, wheel):