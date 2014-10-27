#!/usr/bin/env python


class Figuras():

    def __init__(self):
        self.figura = ""

    def areaCuadrado(self, lado):
        area = lado**2
        self.figura = "cuadrado"
        return area

    def areaTriangulo(self, base, altura):
        area = (base * altura) / 2
        self.figura = "triangulo"
        return area

    def areaCirculo(self, radio):
        area = (3.1416) * (radio * radio)
        self.figura = "circulo"
        return area

    def areaRectangulo(self, base, altura):
        area = base * altura
        self.figura = "rectangulo"
        return area

    def areaRombo(self, diagonal1, diagonal2):
        area = (diagonal1 * diagonal2) / 2
        self.figura = "rombo"
        return area

    def probarFigura(self):
        return self.figura
