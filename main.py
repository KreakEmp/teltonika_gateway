import time

from src.parseserialdata.parsing_serial_data import parse_serial_data
from src.readserialdata.reading_serial_data import read_serial_data
from src.server.client_connect_to_server import (
    create_client,
    send_parsed_data_to_datoms_server,
)


def main(config_filepath, client):
    serial_data = read_serial_data()
    parsed_data = parse_serial_data(config_filepath, serial_data) #
    print(f"Parsed Data is {parsed_data}")
    server_response = send_parsed_data_to_datoms_server(
        client, config_filepath, parsed_data, "utf-8"
    )
    print(f"[RESPONSE] {server_response}")


if __name__ == "__main__":
    client = create_client()
    number_of_msg = 0
    while number_of_msg < 5:
        main("test_config.json", client)
        number_of_msg += 1
        time.sleep(10)

    client.close()
