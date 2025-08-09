# test_ejercicios.py

import math
import pytest
from volumen_cilindro import volumen_cilindro
from costo_proyecto import costo_proyecto
from convertir_longitud import convertir_longitud
from area_paredes import area_total_paredes
from perimetro_triangulo import perimetro_triangulo_rectangulo
from masa_columna import masa_columna
from kg_a_libras import kg_a_libras
from area_circulo import area_circulo
from celsius_a_fahrenheit import celsius_a_fahrenheit
from promedio_tres import promedio_tres
from area_rectangulo import area_rectangulo
from minutos_a_horas import minutos_a_horas_y_minutos


# Ejercicios originales
@pytest.mark.parametrize("r, h, esperado", [
    (1, 1, math.pi * 1 * 1 * 1),
    (2, 5, math.pi * 4 * 5),
    (3, 0.5, math.pi * 9 * 0.5),
])
def test_volumen_cilindro(r, h, esperado):
    assert math.isclose(volumen_cilindro(r, h), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("precio, cantidad, esperado", [
    (10, 5, 50),
    (99.99, 2, 199.98),
    (0, 100, 0),
])
def test_costo_proyecto(precio, cantidad, esperado):
    assert math.isclose(costo_proyecto(precio, cantidad), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("metros, cm_esp, pulg_esp", [
    (1, 100, 39.3701),
    (2, 200, 78.7402),
    (0.5, 50, 19.68505),
])
def test_convertir_longitud(metros, cm_esp, pulg_esp):
    cm, pulgadas = convertir_longitud(metros)
    assert math.isclose(cm, cm_esp, rel_tol=1e-6)
    assert math.isclose(pulgadas, pulg_esp, rel_tol=1e-6)


@pytest.mark.parametrize("altura, longitud, esperado", [
    (2, 3, 12),
    (3, 5, 30),
    (4.5, 2, 18),
])
def test_area_total_paredes(altura, longitud, esperado):
    assert math.isclose(area_total_paredes(altura, longitud), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("a, b, esperado", [
    (3, 4, 12),
    (5, 12, 30),
    (8, 15, 40),
])
def test_perimetro_triangulo_rectangulo(a, b, esperado):
    assert math.isclose(perimetro_triangulo_rectangulo(a, b), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("volumen, densidad, esperado", [
    (1, 2400, 2400),
    (2, 2400, 4800),
    (0.5, 2400, 1200),
])
def test_masa_columna(volumen, densidad, esperado):
    assert math.isclose(masa_columna(volumen, densidad), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("kg, esperado", [
    (1, 2.204062),
    (10, 22.04062),
    (0.5, 1.102031),
])
def test_kg_a_libras(kg, esperado):
    assert math.isclose(kg_a_libras(kg), esperado, rel_tol=1e-6)


# Nuevos ejercicios
@pytest.mark.parametrize("radio, esperado", [
    (1, math.pi * 1 * 1),
    (2, math.pi * 4),
    (0.5, math.pi * 0.25),
])
def test_area_circulo(radio, esperado):
    assert math.isclose(area_circulo(radio), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("celsius, esperado", [
    (0, 32),
    (100, 212),
    (-40, -40),
])
def test_celsius_a_fahrenheit(celsius, esperado):
    assert math.isclose(celsius_a_fahrenheit(celsius), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("a, b, c, esperado", [
    (1, 2, 3, 2),
    (10, 20, 30, 20),
    (5, 5, 5, 5),
])
def test_promedio_tres(a, b, c, esperado):
    assert math.isclose(promedio_tres(a, b, c), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("base, altura, esperado", [
    (2, 3, 6),
    (5, 10, 50),
    (7.5, 4, 30),
])
def test_area_rectangulo(base, altura, esperado):
    assert math.isclose(area_rectangulo(base, altura), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("minutos, h_esp, m_esp", [
    (120, 2, 0),
    (125, 2, 5),
    (59, 0, 59),
])
def test_minutos_a_horas_y_minutos(minutos, h_esp, m_esp):
    horas, mins = minutos_a_horas_y_minutos(minutos)
    assert horas == h_esp
    assert mins == m_esp
