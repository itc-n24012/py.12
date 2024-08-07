class Nigiri:
    category = 'にぎり'
    top = 'かつお'
    base = 'しゃり'

    def show_attributes(self):
        print('top: {}, base: {}, category: {}'.format(self.top, self.base, self.category))

class Katsuo(Nigiri):
    price = 100
    topping = '生姜とネギ'
    def show_attributes(self):
        super().show_attributes()
        print('price: {}円'.format(self.price))
        print('topping: {}'.format(self.topping))
n1 = Katsuo()
n1.show_attributes()
