import http.client
import os
import unittest
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    # Pruebas para la potencia
    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    # Pruebas para raíz cuadrada
    def test_api_square_root(self):
        url = f"{BASE_URL}/calc/square_root/9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

        # Verificar error al solicitar raíz cuadrada de número negativo
        url = f"{BASE_URL}/calc/square_root/-9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.BAD_REQUEST)

    # Pruebas para logaritmo en base 10
    def test_api_log_base_10(self):
        url = f"{BASE_URL}/calc/log_base_10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

        # Verificar error al solicitar logaritmo de número negativo o cero
        url = f"{BASE_URL}/calc/log_base_10/-10"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.BAD_REQUEST)

        url = f"{BASE_URL}/calc/log_base_10/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.BAD_REQUEST)

        