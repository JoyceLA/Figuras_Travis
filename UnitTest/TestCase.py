#!/usr/bin/env python

import unittest
from Figuras import Figuras

class TestCase(unittest.TestCase):
	def test_validar_figuras(self):
		fig = Figuras()
		fig.areaRectangulo(3,4)
		self.assertEqual("rectangulo", fig.probarFigura())

	def test_area_Square1(self):
		fig = Figuras()
		self.assertEqual(4.0,fig.areaCuadrado(2.0))	
	def test_area_Square2(self):
		fig = Figuras()
		self.assertEqual(25.0,fig.areaCuadrado(5.0))
	def test_area_Square3(self):
		fig = Figuras()
		self.assertEqual(12.25,fig.areaCuadrado(3.5))	
	
	def test_area_Triang1(self):
		fig = Figuras()
		self.assertEqual(10,fig.areaTriangulo(4,5))
	def test_area_Triang2(self):
		fig = Figuras()
		self.assertEqual(4.5,fig.areaTriangulo(3.0,3.0))
	def test_area_Triang3(self):
		fig = Figuras()
		self.assertEqual(10,fig.areaTriangulo(2,10))


	def test_area_Circle1(self):
		fig = Figuras()
		self.assertEqual(50.2656,fig.areaCirculo(4.0))
	def test_area_Circle2(self):
		fig = Figuras()
		self.assertEqual(28.2744,fig.areaCirculo(3.0))
	def test_area_Circle3(self):
		fig = Figuras()
		self.assertEqual(113.0976,fig.areaCirculo(6.0))


	def test_area_Recta1(self):
		fig = Figuras()
		self.assertEqual(12, fig.areaRectangulo(3,4))
	def test_area_Recta2(self):
		fig = Figuras()
		self.assertEqual(35, fig.areaRectangulo(5,7))
	def test_area_Recta3(self):
		fig = Figuras()
		self.assertEqual(32, fig.areaRectangulo(4,8))

	def test_area_Rombo1(self):
		fig = Figuras()
		self.assertEqual(12.5,fig.areaRombo(5.0,5.0))
	def test_area_Rombo2(self):
		fig = Figuras()
		self.assertEqual(9.0,fig.areaRombo(6.0,3.0))
	def test_area_Rombo3(self):
		fig = Figuras()
		self.assertEqual(25,fig.areaRombo(5,10))

if __name__ == "__main__":
	unittest.main()
