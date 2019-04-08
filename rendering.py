#Universidad del Valle de Guatemala
#Graficas por computadora
#Modulo que contiene los metodos basicos para realizar un software render 
#Maria Fernanda Lopez Diaz - 17160
#Metodos como glLine,Load, Triangle, Triangle2 y bbox fueron tomados del ejemplo dado en clase

import random
from bitmap import *
from obj import *
import shader as shader
from collections import namedtuple
import cProfile
import math

i = None
vx = 0
vy = 0
vwidth = 0
vheight = 0
x1 = 0
y1 = 0

v2 = namedtuple('Vertex2', ['x','y'])
v3 = namedtuple('Vertex2', ['x','y','z'])

model = []
Viewport = []
projection = []
View = []

def sum(v0,v1):
        return v3(v0.x + v1.x, v0.y + v1.y, v0.z + v1.z)


def sub(v0,v1):
        return v3(v0.x - v1.x, v0.y - v1.y, v0.z - v1.z)

#def mul(v0,v1):
 #       return v3(v0.x *i, v0.y * j, v0.z * k)


def dot(v0,v1):
        return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z

def cross(v0,v1):
        return v3(
                v0.y * v1.z - v0.z * v1.y,
                v0.z * v1.x - v0.x * v1.z,
                v0.x * v1.y - v0.y * v1.x       )

def length(v0):
        return (v0.x**2 + v0.y**2 + v0.z**2)**0.5

#incompleto
def normalizar_vector(v0):
        l = length(v0)

        if not l:
                return v3(0,0,0)
        return v3(v0.x/l, v0.y/l, v0.z/l)

def multiplicacion(matriz1, matriz2):
    matrizR = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    for x in range(0,4):
        for y in range(0,4):
            for z in range(0,4):
                matrizR[x][y]+= matriz1[x][z] * matriz2[z][y]
    return matrizR

def transform(vertx, translate=(0,0,0), scale=(1,1,1), rotate=(0,0,0), eye=[0,0,1], center=[0,0,0], up=[0,1,0]):
        """
        return v3(
                round((vertx[0] + translate[0]) * scale[0]),
                round((vertx[1] + translate[1]) * scale[1]),
                round((vertx[2] + translate[2]) * scale[2])
        )  """

        aumented = [[vertx[0],0,0,0], [vertx[1],0,0,0], [vertx[2],0,0,0], [1,0,0,0]]
        lookAt(eye, center, up)
        loadModelMatriz(translate,scale,rotate)
        loadViewportMatrix()
        #print (model)
        #print (View)
        #print (projection)
        #print (Viewport)
        #multiplicacion de matrices
        prueba1 = multiplicacion(Viewport, projection)
        prueba2 = multiplicacion(prueba1, View)
        final = multiplicacion(prueba2, model)  
        final2 = multiplicacion(final, aumented)
        #print (final)
        
        
        tv = [
                round((final2[0][0]/final2[3][0])),  #aqui tira division por cero
                round((final2[1][0]/final2[3][0])),
                round((final2[2][0]/final2[3][0]))
        ]

        #print (tv)
        return v3(*tv)

def lookAt(eye=[0,0,1], center=[0,0,0], up=[0,1,0]):

        eye = v3(*eye)
        center = v3(*center)
        up = v3(*up)

        #estos tres vectores en junto son la camara

        z = normalizar_vector(sub(eye, center))
        #x siempre va a ser opuesto a z y u, por lo que se utiliza el producto cruz
        x = normalizar_vector(cross(up, z))
        y = normalizar_vector(cross(z,x))
        loadViewMatriz(x,y,z,center)
        #una buena aproximacion viene de 1 partido el largo de la distancia del ojo y del center
        #es inversa
        #el menos es por como se definio el z, 
        algo = normalizar_vector(sub(eye, center))
        loadProjectionMatriz(-1 / length(algo))

def loadViewportMatrix(x = 0, y = 0):
        #el 128 es lo normal porque hay que proyectarlo en z igual
        global Viewport
        """
        self.Viewport = matrix([
                [self.width/2, 0, 0, x + self.width/2],
                [0, self.height/2, 0, y + self.height/2],
                [0, 0, 128, 128],
                [0,0,0,1]

        ]) """

        Viewport = [[vwidth/2, 0, 0, x + vwidth/2],
                [0, vheight/2, 0, y + vheight/2],
                [0, 0, 128, 128],
                [0, 0, 0, 1]]

def loadModelMatriz(translate, scale, rotate):
        global model
        #la implementacion de llenado de matrices cambia, porque se esta utilizando numpy en el ejemplo dado en clase
        #se pueden convertir los parametros a v3 para más fácil su lectura pero no es necesario
        #con indices es mas eficiente
        #en la rotacion se le aplica el sq solo a las que no queremos (?)
        #la transpuesta de coordenadas del modelo se puede multiplicar por la matriz grandota 
        #los angulos del rotate estan en radianes
        translate_matrix = [
                [1, 0, 0, translate[0]],
                [0, 1, 0, translate[1]],
                [0, 0, 1, translate[2]],
                [0, 0, 0, 1],
        ]

        scale_matrix = [
                [scale[0], 0, 0, 0],
                [0, scale[1], 0, 0],
                [0, 0, scale[2], 0],
                [0, 0, 0, 1]

        ]

        a = rotate[0]
        rotation_matrix_x = [
                [1, 0, 0, 0],
                [0, math.cos(a), -(math.sin(a)), 0],
                [0, math.sin(a), math.cos(a), 0],
                [0, 0, 0, 1]
        ]

        b = rotate[1]
        rotation_matrix_y = [
                [math.cos(b), 0, math.sin(b),0],
                [0, 1, 0, 0],
                [-(math.sin(b)), 0, math.cos(b), 0],
                [0, 0, 0, 1]
        ]

        c = rotate[2]
       
        rotation_matrix_z = [
                [math.cos(c), -(math.sin(c)),0,0],
                [0, 1, 0, 0],
                [math.sin(c), 0, math.cos(c), 0],
                [0,0,0,1]
        ]


        res1 = multiplicacion(rotation_matrix_z, rotation_matrix_y)
        rotation_matrix = multiplicacion(res1, rotation_matrix_x)
        #rotation_matrix = rotation_matrix_x @ rotation_matrix_y @ rotation_matrix_z     #solo se va poder rotar en un eje (pensar en blender)
        res2 = multiplicacion(rotation_matrix, translate_matrix)
        model = multiplicacion(res2, scale_matrix)

def loadProjectionMatriz(coeff):
        #solo en z interesa la transformacion
        global projection
        projection =[
                [1,0,0,0],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,coeff,1]
        ]

#ya lo pase en teoria
def loadViewMatriz(x,y,z,center):
        global View
        M = [
                [x.x, x.y, x.z, 0],
                [y.x, y.y, y.z, 0],
                [z.x, z.y, z.z, 0],
                [0, 0,0,1]

        ]

        O = [
                [1,0,0, -center.x],
                [0,1,0, -center.y],
                [0,0,1, -center.z],
                [0,0,0,1]
        ]

        View = multiplicacion(M, O)
def triangleS(A,B,C,nA, nB, nC, filename):
        bbox_min, bbox_max = bbox(A,B,C)

        #puede que el for este al revez

        #model = Texture(textureFile)
        for x in range(bbox_min.x, bbox_max.x + 1):
                for y in range(bbox_min.y, bbox_max.y + 1):
                        w, v, u = barycentric(A,B,C, v2(x,y))
                        if w < 0 or v < 0 or u < 0:
                                continue
                        #tx = tA.x*w + tB.x*v + tC.x*u
                        #ty = tA.y*w + tB.y*v + tC.y*u

                        
                        z = A.z*w + B.z*v + C.z*u
                        
                        if filename == 'esferatriangulada.obj':
                                color = shader.sol(y, x, z, bar = (w,v,u), varying_normals = (nA, nB, nC))
                        elif filename == 'nube.obj':
                                color = shader.nube(y, x, z, bar = (w,v,u), varying_normals = (nA, nB, nC))


                        if x < len(i.zbuffer) and y < len(i.zbuffer[x]) and z > i.zbuffer[x][y]:
                                if y >= 0 and x >= 0:
                                        i.point(y,x,color)
                                        print(x,y)
                                        i.zbuffer[x][y] = z

def triangleT(A,B,C,texture,tA, tB, tC, intensity):
        bbox_min, bbox_max = bbox(A,B,C)

        #puede que el for este al revez

        model = Texture(texture)
        for x in range(bbox_min.x, bbox_max.x + 1):
                for y in range(bbox_min.y, bbox_max.y + 1):
                        w, v, u = barycentric(A,B,C, v2(x,y))
                        if w < 0 or v < 0 or u < 0:
                                continue

                        tx = tA.x*w + tB.x*v + tC.x*u
                        ty = tA.y*w + tB.y*v + tC.y*u
                        color = model.get_color(ty,tx,intensity)
                    
                        
                        z = A.z*w + B.z*v + C.z*u
                        if z > i.zbuffer[x][y]:
                               #i.point(y,x,color(r,g,b))
                               i.point(y,x,color)
                               i.zbuffer[x][y] = z
            
#Cuadro minimo que puede contener al triangulo
def bbox(A,B,C):
        xs = sorted([A.x, B.x, C.x])
        ys = sorted([A.y, B.y, C.y])
        return v2(xs[0], ys[0]), v2(xs[-1], ys[-1])

#Funcion para determinar si un punto se encuentra dentro de un triangulo o no
#Se utilizan coordenadas baricentricas para a traves de los vector en x o y saber si un punto se encuentra dentro o no
#Input: coordenadas de los puntos
#output: si se encuentra o no dentro del triangulo
def barycentric(A,B,C,P):
        cx, cy, cz = cross(
                v3(B.x - A.x, C.x - A.x, A.x - P.x),
                v3(B.y - A.y, C.y - A.y, A.y - P.y)
        )

        #[cx/cz, cy/cz, cz7cz] = [u,v,1]

        if cz == 0:    
                return -1,-1,-1
        u = cx/cz
        v = cy/cz
        w = 1 - (u + v)

        return w,v,u


def triangle2(A,B,C,r,g,b):
        bbox_min, bbox_max = bbox(A,B,C)

        #puede que el for este al revez

        for x in range(bbox_min.x, bbox_max.x + 1):
                for y in range(bbox_min.y, bbox_max.y + 1):
                        w, v, u = barycentric(A,B,C, v2(x,y))
                        if w < 0 or v < 0 or u < 0:
                                continue

                        z = A.z*w + B.z*v + C.z*u
                       
                        if x < len(i.zbuffer) and y < len(i.zbuffer[x]) and z > i.zbuffer[x][y]:
                               if y >= 0 and x >= 0:
                                        i.point(y,x,color(r,g,b))
                                        i.zbuffer[x][y] = z

 

#Funcion para inicialir algun parametro necesario en el uso de rendering
def glInit():
	pass

#Funcion para crear las dimensiones de la ventana de la imagen, toma como parametros el ancho y el alto
def glCreateWindow(width, height):
        global i
        i = Bitmap(width, height)

#Funcion para definir un viewport, toma como parametros el punto inicial en 'x' y 'y' y el ancho y alto del cual se desea realizar
def glViewPort(x, y, width, height):
	global vx
	vx = x
	global vy
	vy = y
	global vwidth
	vwidth = width
	global vheight
	vheight = height

#Llena la imagen de color negro
def glClear(r,g,b):
	i.clear(r,g,b)

#Cambia el color de la imagen a uno determinado, solo toma como parametros numeros del 0 al 1
def glClearColor(r, g, b):
	r1 = round(r*255)
	g1 = round(g*255)
	b1 = round(b*255)
	glClear(r1,g1,b1)

#Dibuja un punto en un area del viewport
#Toma coordenadas entre -1 y 1 y las convierte a coordenadas del mundo 
def glVertex(x,y):
        global x1
        global y1
        x1 = round(((x + 1) * (vwidth/2)) + vx)
        y1 = round(((y + 1) * (vheight/2)) + vy)
        if x1==vwidth:
                x1 = x1 - 1
        if y1==vheight:
                y1 = y1 - 1                
        i.point(y1,x1,color(255,255,255))


#Cambia el color de punto dibujado en el area del viewport        
def glColor(r,g,b):
        r1 = round(r * 255)
        g1 = round(g * 255)
        b1 = round(b * 255)
        i.point(y1,x1,color(r1,g1,b1))

#Crea el bitmap con el nombre que se desea
def glFinish(nombre):
        #Crea la imagen
        nombre = nombre + ".bmp"
        i.write(nombre)



#Funcion para realizar una linea desde el punto inicial hasta el final
#Toma como parametros el punto inicial en (x,y) y el punto final en (x,y)
#Las coordenadas en (x,y) deben de ser dadas entre -1 y 1
def glLine(x1, y1, x2, y2, r, g, b):

        #x1 = int(((x11 + 1) * (vwidth/2)) + vx)
        #y1 = int(((y11 + 1) * (vheight/2)) + vy)
        #x2 = int(((x22 + 1) * (vwidth/2)) + vx)
        #y2 = int(((y22 + 1) * (vheight/2)) + vy)
        dy=abs(y2-y1) 
        dx=abs(x2-x1)

        steep=dy>=dx

        if steep:
                x1,y1=y1,x1
                x2,y2=y2,x2

                dy=abs(y2-y1)
                dx=abs(x2-x1)

    #Condicion para cuando se quiere comenzar la linea de derecha a izquierda
        if x1>x2:
                x1,x2=x2,x1
                y1,y2=y2,y1

    #se multiplica por dx para poder obtener la 'pendiente' y no tener que hacer la division directamente
        offset = 0 * 2 * dx

        #limite a donde va a llegar la linea
        threshold = 0.5 * dx

        y=y1

        for x in range(x1,x2+1):
                if steep:
                        i.point(x,y,color(r,g,b))
                   
                else:
                        i.point(y,x,color(r,g,b))
                        
                offset += dy
                if offset>=threshold:
                        y += 1 if y1<y2 else -1
                        threshold += 1*dx

#Funcion para cargar un obj y leer sus vertices y caras 
# Para poder dibujar las lineas que conforman estas y cargar el modelo a un bitmap      
def load(filename, texture = None, translate = (0,0,0), scale=(1,1,1), rotate=(0,0,0), eye=[0,0,1], center=[0,0,0], up=[0,1,0]):
        model = Obj(filename)

        light = normalizar_vector(v3(0,1,1))
        

        for face in model.faces:
                vcount = len(face)

                if vcount == 3:
                        f1 = face[0][0] - 1
                        f2 = face[1][0] - 1
                        f3 = face[2][0] - 1

                        a = transform(model.vertices[f1], translate, scale, rotate, eye, center, up)
                        b = transform(model.vertices[f2], translate, scale, rotate, eye, center, up)
                        c = transform(model.vertices[f3], translate, scale, rotate, eye, center, up)
                        normal = normalizar_vector(cross(sub(b,a), sub(c,a)))
                        intensity = dot(normal, light)
                        gray = round(255*intensity)

                        if texture == None:                              
                                
                                if gray < 0:
                                        continue
                                elif gray > 255:
                                        gray = 255
               
                                triangle2(a, b, c, gray, gray, gray)
                        else:
                                #se cargan los vertices de la textura por cada cara
                                t1 = face[0][1] - 1
                                t2 = face[1][1] - 1
                                t3 = face[2][1] - 1

                                #se obtienen sus valores en x,y,z
                                #en z tiene que ser 0 porque no existen texturas en 3D
                                tA = v3(*model.textureV[t1])
                                tB = v3(*model.textureV[t2])
                                tC = v3(*model.textureV[t3])

                                triangleT(a,b,c,texture, tA, tC, tB, intensity)
                
                else:
                        #si es un cuadrado y no un triangulo se tendra un cuarto vertice
                        f1 = face[0][0] - 1
                        f2 = face[1][0] - 1
                        f3 = face[2][0] - 1
                        f4 = face[3][0] - 1   

                        a = transform(model.vertices[f1], translate, scale)
                        b = transform(model.vertices[f2], translate, scale)
                        c = transform(model.vertices[f3], translate, scale)
                        d = transform(model.vertices[f4], translate, scale) 
                        vertices = [ a, b, c, d]

                        normal = normalizar_vector(cross(sub(vertices[0], vertices[1]), sub(vertices[1], vertices[2])))
                        intensity = dot(normal, light)
                        
        
                        a, b, c, d = vertices 

                        if not texture:
                                gray = round(255 * intensity)
                                if gray < 0:
                                        continue 
               
                                triangle2(a, b, c, gray, gray, gray)
                                triangle2(a, c, d, gray, gray, gray)
                        else: 
                                t1 = face[0][1] - 1
                                t2 = face[1][1] - 1
                                t3 = face[2][1] - 1
                                t4 = face[3][1] - 1
                                tA = v3(*model.textureV[t1])
                                tB = v3(*model.textureV[t2])
                                tC = v3(*model.textureV[t3])
                                tD = v3(*model.textureV[t4])

                                triangleT(a,b,c,texture,tA,tB,tC,intensity)
                                triangleT(a,c,d,texture, tA, tC, tD, intensity)
                
               
                       


def PolygonArea(poligono):
    n = len(poligono) 
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += poligono[i][0] * poligono[j][1]
        area -= poligono[j][0] * poligono[i][1]
    area = abs(area) / 2.0
    return area

#Determina si un punto se encuentra dentro de un poligono
#Poligono es una lista con todos los puntos (x,y)
#si es true pinta el punto de lo contrario no 
#Basado en el pseudocodigo encontrado en https://rosettacode.org/wiki/Ray-casting_algorithm 
#Modificado del algoritmo de https://joseguerreroa.wordpress.com/2015/09/22/puntos-en-poligonos-utilizando-el-algoritmo-ray-casting-en-pyqgis/
def rellenar_poligono(x, y, poligono, r, g, b):
        i = 0
        j = len(poligono) - 1
        punto = False
        for i in range(len(poligono)):
                if (poligono[i][1] < y and poligono[j][1] >= y) or (poligono[j][1] < y and poligono[i][1] >= y):
                        if poligono[i][0] + (y - poligono[i][1]) / (poligono[j][1] - poligono[i][1]) * (poligono[j][0] - poligono[i][0]) < x:
                                punto = not punto
                j = i
        if punto:
                #si punto es true es porque el punto random que entra se encuentra dentro del poligono entonces se pinta un punto
                glLine(x,y,x,y,r,g,b)
        
                

