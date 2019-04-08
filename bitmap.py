#Universidad del Valle de Guatemala
#Graficas por computadora
#Primera parte de software rendering
#Maria Fernanda Lopez - 17160
#20-01-2019


import struct


def char(c):
	return struct.pack("=c", c.encode('ascii'))

def word(c):
	return struct.pack("=h", c)

def dword(c):
	return struct.pack("=l", c)

def color(r,g,b):
	return bytes([b, g, r])

class Bitmap(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.framebuffer = []
		self.clear(0,0,0)

	def clear(self, r, g, b):
		self.framebuffer = [
			[
				color(r,g,b) 
					for x in range(self.width)
			]
			for y in range(self.height)
		]
		self.zbuffer = [
			[-float('inf')
					for x in range(self.width)
			]
			for y in range(self.height)
		]

	def write(self, filename):
		f = open(filename, 'wb')

		# file header 14
		f.write(char('B'))
		f.write(char('M'))
		f.write(dword(14 + 40 + self.width * self.height * 3))
		f.write(dword(0))
		f.write(dword(14+40))

		# image header 40
		f.write(dword(40))
		f.write(dword(self.width))
		f.write(dword(self.height))
		f.write(word(1))
		f.write(word(24))
		f.write(dword(0))
		f.write(dword(self.width * self.height * 3))
		f.write(dword(0))
		f.write(dword(0))
		f.write(dword(0))
		f.write(dword(0))

			

		for x in range(self.height):
			for y in range(self.width):
				f.write(self.framebuffer[x][y])

		f.close()

	def point(self, x, y, color):
		self.framebuffer[x][y] = color















                



