import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.cupones import aplicar_cupon, calcular_precio_final


def test_descuento_oferta10():
    assert aplicar_cupon(100, "OFERTA10") == 90.0

def test_descuento_super20():
    assert aplicar_cupon(200, "SUPER20") == 160.0

def test_descuento_bienvenida():
    assert aplicar_cupon(100, "BIENVENIDA") == 85.0

def test_precio_final_con_impuesto():
    assert calcular_precio_final(100, "OFERTA10") == 107.1
