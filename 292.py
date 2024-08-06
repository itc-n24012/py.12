class Cylinder:
    pi = 3.14

    def __init__(self, radius=1, height=1):
        self.radius = float(radius)
        self.height = float(height)

    def calc_base_area(self):
        pi = Cylinder.pi
        a = self.radius
        return pi * a * a

    def calc_side_area(self):
        pi = Cylinder.pi
        a = self.radius
        b = self.height
        return 2 * pi * a * b

    def calc_surface_area(self):
        c = self.calc_base_area()
        d = self.calc_side_area()
        return 2 * c + d

    def calc_volume(self):
        c = self.calc_base_area()
        b = self.height
        return c * b

    def show_results(self):
        a = self.radius
        b = self.height
        S = self. calc_surface_area()
        V = self.calc_volume() 
        print('半径: {}, 高さ: {}, 表面積: {}, 体積: {}'. format(a, b, S, V))

a1 = Cylinder()
a1.show_results()
a2 = Cylinder(2., 5.)
a2.show_results()
a3 = Cylinder(1., 1.)
a3.show_results()
a4 = Cylinder(4., 3.)
a4.show_results()























