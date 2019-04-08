""""
    Universidad del Valle de Guatemala
    Maria Fernanda Lopez Diaz
    Shader implementado para crear una tierra y su luna
    El metodo de ruido Perlin's Noise se obtuvo del repositorio: 
    https://github.com/mmchugh/pynoise 

"""

from collections import namedtuple
import random
import math
from perlin import *



def dot(v0,v1):
        return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z

def color(r,g,b):
	return bytes([b, g, r])

v3 = namedtuple('Vertex2', ['x','y','z'])

def nube(y, x, z, **kwargs):
    perlin_generator = Perlin(frequency=15, lacunarity=2)

   

    light = v3(0,0,1)
    #barycentric
    w,v,u=kwargs['bar']

    #varying normals
    nA, nB, nC= kwargs['varying_normals']

    nx=nA[0]*w + nB[0] * v + nC[0] * u
    ny=nA[1]*w + nB[1] * v + nC[1] * u
    nz=nA[2]*w + nB[2] * v + nC[2] * u

    vn=v3(nx,ny,nz)

    #luz de; render...
    intensity = dot(vn, light)

    for i in range(400):
      for j in range(400):
        colour = [int((perlin_generator.value(x/500.0, y/500.0, 0) + 1) * 85), ] * 3
        color1 = v3(*colour)
        return color(int(255*color1.x / 255) if int(255*color1.x / 255) > 0 else 0, 
                int(255*color1.y/255) if int(255*color1.y/255) > 0 else 0, 
                int(255*color1.z/255) if int(255*color1.z/255) > 0 else 0)
    
    

def sol(y, x, z, **kwargs):
    perlin_generator = Perlin(frequency=15, lacunarity=2)

    base = [254,165,0]

    light = v3(0,1,1)
    #barycentric
    w,v,u=kwargs['bar']

    #varying normals
    nA, nB, nC= kwargs['varying_normals']

    nx=nA[0]*w + nB[0] * v + nC[0] * u
    ny=nA[1]*w + nB[1] * v + nC[1] * u
    nz=nA[2]*w + nB[2] * v + nC[2] * u

    vn=v3(nx,ny,nz)

    #luz de; render...
    intensity = dot(vn, light)
    """
    for i in range(400):
      for j in range(400):
        colour = [int((perlin_generator.value(x/900.0, y/800.0, 0) + 1) * 85), ] * 3
        color1 = v3(*colour)
    """
    return color(int(100 * intensity) if int(100 * intensity) > 0 else 0,
                int(75 * intensity) if int(75 * intensity) > 0 else 0,
                0)
        
                   



                
                
    

    
    
     
    
    

    
    


  



   