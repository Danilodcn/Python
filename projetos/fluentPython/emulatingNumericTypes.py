from math import hypot

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __str__(self):
		return f"Vector({self.x}, {self.y}) "
		
	def __repr__(self):
		return str(self)
	
	def __abs__(self):
		return hypot(self.x, self.y)
		
	def __len__(self):
		return int(hypot(self.x, self.y))
		
	def __bool__(self):
		return bool(abs(self))
		
	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)
		
	def __mul__(self, scalar):
		return Vector(self.x * scalar, self.y * scalar)
		
v1 = Vector(0, 3)
v2 = Vector(3, 4)
print(v1 + v2, abs(v1), abs(v2), v1 * 3, abs(v1 * 3))

print(len(v1), v1.__repr__())


class Nova:
	def __init__(self, x):
		self.x = x
		
	def __len__(self):
		return self.x
	
	def __bool__(self):
		return bool(self.x)
		
	def __iq__(self, other):
		return other.x == self.x
		
a = Nova(2)
b = Nova(3)
c = Nova(2)
print(a == b, a == c, bool(a))



























