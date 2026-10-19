class Vector:
    def __init__(self, x, y, z):
        types = [int, float]
        if type(x) in types and type(y) in types and type(z) in types:
            self.x = x
            self.y = y
            self.z = z
        else:
            print('Error')

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**(0.5)

    def __add__(self, other):
        types = [int, float]
        if type(other) is not Vector:
            return None
        if (type(other.x) in types and
                type(other.y) in types and
                type(other.z) in types):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            print('Error')

    def __sub__(self, other):
        if type(other) is not Vector:
            return None
        types = [int, float]
        if (type(other.x) in types and
                type(other.y) in types and
                type(other.z) in types):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            print('Error')

    def __mul__(self, other):
        types = [int, float]
        if type(other) in types:
            return Vector(other * self.x, other * self.y, other * self.z)
        else:
            print('Error')

    def __mul_scalar__(self, other):
        if type(other) is Vector:
            return self.x * other.x + self.y + other.y + self.z + other.z
        else:
            print('Error')

    def __mul_vector__(self, other):
        if type(other) is Vector:
            x_v = self.y * other.z - self.z * other.y
            y_v = self.z * other.x - self.x * other.z
            z_v = self.x * other.y - self.y * other.x
            return Vector(x_v, y_v, z_v)


# Задание 1.1

def center_of_mass(points):
    total_sum = Vector(0, 0, 0)
    for p in points:
        total_sum = total_sum + p
    n = len(points)

    total_sum *= (1.0 / n)
    return f'{total_sum.x}, {total_sum.y}, {total_sum.z}'


# Задание 1.2

def triangle_existence(ab, ac, bc):
    lengths = [abs(ab), abs(ac), abs(bc)]
    lengths.sort()
    max = lengths.pop(2)
    if max < lengths[0] + lengths[1]:
        return True
    else:
        return False


def max_triangle_area(points):

    n = len(points)
    if n < 3:
        return None
    max_area = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                p1, p2, p3 = points[i], points[j], points[k]
                ab = Vector(p2.x - p1.x, p2.y - p1.y, p2.z - p1.z)
                ac = Vector(p3.x - p1.x, p3.y - p1.y, p3.z - p1.z)
                bc = Vector(p3.x - p2.x, p3.y - p2.y, p3.z - p2.z)
                cross = ab.__mul_vector__(ac)
                area = abs(cross) * 0.5
                if (area * 0.5 > max_area
                        and triangle_existence(ab, ac, bc) is True):

                    max_area = area * 0.5
    return max_area
