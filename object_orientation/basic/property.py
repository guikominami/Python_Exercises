## evita de quebrar o código se modificar o nome de algum atributo. Por exemplo, estava como color e mudei para color_paint

class Pen:
    def __init__(self, color):
        #old name
        #self.color = color

        #new name
        self.color_paint = color

    @property
    def color(self):
        return self.color_paint

p1 = Pen('blue')
#não chamar como um método com parênteses no final
print(p1.color)