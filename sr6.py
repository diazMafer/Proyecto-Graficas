from rendering import *
import cProfile
import re

#se interpolan valores porque la z esta unicamente en los vertices
#line se puede calcular bary igual, se puede hacer interpolaciones lineales, pendientes diagonales interpolar y despues horizontalmente
#interpolar las lineas horizontales

print("Se esta ejecutando la imagen que renderiza a una tierra (se tarda aproximadamente 1 minuto)")
glCreateWindow(1024,1024)
glViewPort(0,0,1024,1024)


#se aplico un dutch shot al sol para que tuviera el angulo que se deseaba y estuviese en una esquina

"""
glLine(13,1014,433,1014,255,255,255)
glLine(13,1014,433,1014,255,255,255)
glLine(13,1014,371,698,255,255,255)
glLine(13,1014,371,698,255,255,255)
glLine(10,1000,253,648,255,255,255)
glLine(10,1000,253,648,255,255,255)
#glLine(13,1000,253,420,255,255,255)
#glLine(13,1014,44,236,255,255,255)
#glLine(13,1014,13,152,255,255,255)
"""

load("nube.obj", None, translate = (0,1,0), scale=(3,0.8,0.8), rotate=(0,0,0), eye=[0,0,1], center=[0,0,0], up=[0,1,0])
load("esferatriangulada.obj", None, translate = (0,1.3,0), scale=(1,0.8,0.8), rotate=(0,0,0), eye=[0,0,10], center=[0,0,0], up=[1,1,0])



print("La imagen se renderizo con el nombre 'retrato'")
glFinish("retrato")
