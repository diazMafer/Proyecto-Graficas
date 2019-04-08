import struct



def color(r,g,b):
    return bytes([b,g,r])

class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
        
        self.vertices = []
        self.normales = []
        self.textureV = []
        self.faces = []
        self.read()
    
    def read(self):
    
        for line in self.lines:
            if line:
                prefix, value = line.split(' ',1)

                if prefix == 'v':
                    self.vertices.append(list(map(float, value.split(' '))))
                elif prefix == 'vt':
                    self.textureV.append(list(map(float, value.split(' '))))
                elif prefix == 'vn':
                    self.normales.append(list(map(float, value.split(' '))))
                elif prefix == 'f':
                    #para cada una de las caras se convierte a int y se pasa a una lista
                    self.faces.append([list(map(int, face.split('/'))) for face in value.split(' ')])

class Texture(object):
    def __init__(self, path):
        self.path = path
        self.read()
    

    #cada .seek sirve para saltarse partes del header inecesarios, lo unico que necesitamos son los pixeles de color y sus dimensiones
    def read(self):
        img = open(self.path, "rb")
        img.seek(2 + 4 + 4)
        header_size = struct.unpack("=l", img.read(4))[0]
        img.seek(2 + 4 + 4 + 4 + 4)
        self.width = struct.unpack("=l", img.read(4))[0]
        self.height = struct.unpack("=l", img.read(4))[0]
        self.pixels = []
        img.seek(header_size)

        #suponiendo que no se equivo de izquierda a derecha (si truena poner al reves el for)

        for x in range(self.height):
            self.pixels.append([])
            for y in range (self.width):
                b = ord(img.read(1))
                g = ord(img.read(1)) 
                r = ord(img.read(1)) 
                self.pixels[x].append(color(r, g, b))
        
        img.close()

    def get_color(self, tx, ty, intensity=1):
        
        x = int(tx * self.width)
        y = int(ty * self.height)


        #las condiciones son utilizadas porque al leer el bitmap hay valores que se salen de las dimensiones de este
        #si son mayores o iguales a sus dimensiones se le resta uno para que pueda entrar dentro del rango
        
        if y >= self.height:
            y = self.height - 1

        if x >= self.width:
            x = self.width - 1
  

        return bytes(map(lambda b: round(b*intensity)if b*intensity>0 else 0, self.pixels[y][x]))

