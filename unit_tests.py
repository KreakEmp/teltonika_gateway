import unittest
from src.configurations.read_configurations import get_server_address
from src.parseserialdata.parsing_serial_data import create_datoms_data_packet_data


class TestLibFunctions(unittest.TestCase):
    def test_get_server_address(self):
        actual = get_server_address("test_config.json")
        expected = ("127.0.0.1", 5050)
        self.assertEqual(actual, expected)

    def test_create_datoms_data_packet_data(self):
        actual = create_datoms_data_packet_data(
            "test_config.json", "#12.456+4.890+6.2345+7.890+0.0000+99.99999"
        )
        expected = {
            "so2": "12.456",
            "co2": "4.890",
            "po2": "6.2345",
            "ao2": "7.890",
            "ro2": "0.0000",
            "wo2": "99.99999",
        }
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
