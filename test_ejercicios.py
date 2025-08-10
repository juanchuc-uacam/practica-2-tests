import math
import pytest
import importlib


def try_import(module_name, func_name):
    """
    Intenta importar un módulo y obtener la función especificada.
    Si falla, el test se marcará como SKIPPED en lugar de romper toda la ejecución.
    """
    try:
        module = importlib.import_module(module_name)
        return getattr(module, func_name)
    except (ModuleNotFoundError, AttributeError):
        pytest.skip(f"Módulo o función no encontrada: {module_name}.{func_name}")


# -------------------------
# Ejercicios originales (1-7)
# -------------------------

@pytest.mark.parametrize("r, h, esperado", [
    (1, 1, math.pi * 1 * 1 * 1),
    (2, 5, math.pi * 4 * 5),
    (3, 0.5, math.pi * 9 * 0.5),
])
def test_volumen_cilindro(r, h, esperado):
    func = try_import("volumen_cilindro", "volumen_cilindro")
    assert math.isclose(func(r, h), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("precio, cantidad, esperado", [
    (10, 5, 50),
    (99.99, 2, 199.98),
    (0, 100, 0),
])
def test_costo_proyecto(precio, cantidad, esperado):
    func = try_import("costo_proyecto", "costo_proyecto")
    assert math.isclose(func(precio, cantidad), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("metros, cm_esp, pulg_esp", [
    (1, 100, 39.3701),
    (2, 200, 78.7402),
    (0.5, 50, 19.68505),
])
def test_convertir_longitud(metros, cm_esp, pulg_esp):
    func = try_import("convertir_longitud", "convertir_longitud")
    cm, pulgadas = func(metros)
    assert math.isclose(cm, cm_esp, rel_tol=1e-6)
    assert math.isclose(pulgadas, pulg_esp, rel_tol=1e-6)


@pytest.mark.parametrize("altura, longitud, esperado", [
    (2, 3, 12),
    (3, 5, 30),
    (4.5, 2, 18),
])
def test_area_total_paredes(altura, longitud, esperado):
    func = try_import("area_paredes", "area_total_paredes")
    assert math.isclose(func(altura, longitud), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("a, b, esperado", [
    (3, 4, 12),   # Hipotenusa = 5
    (5, 12, 30),  # Hipotenusa = 13
    (8, 15, 40),  # Hipotenusa = 17
])
def test_perimetro_triangulo_rectangulo(a, b, esperado):
    func = try_import("perimetro_triangulo", "perimetro_triangulo_rectangulo")
    assert math.isclose(func(a, b), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("volumen, densidad, esperado", [
    (1, 2400, 2400),
    (2, 2400, 4800),
    (0.5, 2400, 1200),
])
def test_masa_columna(volumen, densidad, esperado):
    func = try_import("masa_columna", "masa_columna")
    assert math.isclose(func(volumen, densidad), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("kg, esperado", [
    (1, 2.204062),
    (10, 22.04062),
    (0.5, 1.102031),
])
def test_kg_a_libras(kg, esperado):
    func = try_import("kg_a_libras", "kg_a_libras")
    assert math.isclose(func(kg), esperado, rel_tol=1e-6)


# -------------------------
# Ejercicios nuevos (8-12)
# -------------------------

@pytest.mark.parametrize("radio, esperado", [
    (1, math.pi * 1 * 1),
    (2, math.pi * 4),
    (0.5, math.pi * 0.25),
])
def test_area_circulo(radio, esperado):
    func = try_import("area_circulo", "area_circulo")
    assert math.isclose(func(radio), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("celsius, esperado", [
    (0, 32),
    (100, 212),
    (-40, -40),
])
def test_celsius_a_fahrenheit(celsius, esperado):
    func = try_import("celsius_a_fahrenheit", "celsius_a_fahrenheit")
    assert math.isclose(func(celsius), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("a, b, c, esperado", [
    (1, 2, 3, 2),
    (10, 20, 30, 20),
    (5, 5, 5, 5),
])
def test_promedio_tres(a, b, c, esperado):
    func = try_import("promedio_tres", "promedio_tres")
    assert math.isclose(func(a, b, c), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("base, altura, esperado", [
    (2, 3, 6),
    (5, 10, 50),
    (7.5, 4, 30),
])
def test_area_rectangulo(base, altura, esperado):
    func = try_import("area_rectangulo", "area_rectangulo")
    assert math.isclose(func(base, altura), esperado, rel_tol=1e-6)


@pytest.mark.parametrize("minutos, h_esp, m_esp", [
    (120, 2, 0),
    (125, 2, 5),
    (59, 0, 59),
])
def test_minutos_a_horas_y_minutos(minutos, h_esp, m_esp):
    func = try_import("minutos_a_horas", "minutos_a_horas_y_minutos")
    horas, mins = func(minutos)
    assert horas == h_esp
    assert mins == m_esp
