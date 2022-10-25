import json
import socket
import sys
import time

sys.path.append(".")
from src.configurations.read_configurations import get_auth_token, get_server_address


def check_client_is_connected(client):
    try:
        client.send(b"ping")
        return True
    except:
        return False


def send_message_to_server(client, message_string: str, encoding: str):
    if isinstance(message_string, str) and isinstance(encoding, str):
        client.send(message_string.encode(encoding))
        response_encoded = client.recv(1024)
        response = response_encoded.decode(encoding)
        # print(f"[RESPONSE] {response}")
        return response
    else:
        raise Exception("[TYPE ERROR] Message Type or Encoding Type Error")


def get_auth_message(auth_token):
    auth_message = ""
    auth_pack = {"type": "auth", "message": {"token": ""}}
    auth_pack["message"]["token"] = auth_token
    auth_message = json.dumps(auth_pack)
    return auth_message


def is_authenticated(client, authentication_token, encoding: str):
    authenticated = False
    try:
        auth_message = get_auth_message(authentication_token)
        auth_message_response = send_message_to_server(client, auth_message, encoding)
        response_dict = eval(auth_message_response)
        if (
            "type" in response_dict
            and "message" in response_dict
            and response_dict["type"] == "auth_response"
        ):
            if response_dict["message"]["status"] == "success":
                authenticated = True
    except Exception as e:
        print(e)
    return authenticated


def create_client():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def is_client_connected(client, config_file, encoding: str):
    connected = False
    addr = get_server_address(config_file)
    auth_token = get_auth_token(config_file)
    if not (check_client_is_connected(client)):
        try:
            client.connect(addr)
            if is_authenticated(client, auth_token, encoding):
                connected = True
        except socket.error as socketerror:
            print("Error: ", socketerror)
    else:
        connected = True
    return connected


def send_parsed_data_to_datoms_server(
    client, config_file, parsed_serial_data: str, encoding: str
):
    count = 0
    # print(f"Connected {is_client_connected(client, config_file,encoding)}")
    if is_client_connected(client, config_file, encoding):
        server_response = send_message_to_server(client, parsed_serial_data, encoding)
        return server_response
    else:
        addr = get_server_address(config_file)
        while count <= 2:            
            try:
                client.connect(addr)
            except Exception as e:
                print(e)
            if is_client_connected(client, config_file, encoding):
                return
            count += 1
        raise Exception("[CONN ERR] Error in Connecting Datoms Server")


# def functional_client(config_file, encoding: str):
#     count = 0
#     client = create_client()
#     if is_client_connected(client, config_file):
#         auth_token = get_auth_token(config_file)  # Check auth while connecting
#         if is_authenticated(client, auth_token, encoding):
#             print("I AM AUTHENTICATED")
#             while count <= 5:
#                 data_pac = create_full_datoms_packet(
#                     "test_config.json", "#12.456+4.890+6.2345+7.890+0.0000+99.99999"
#                 )
#                 # print(count)
#                 # print(data_pac)
#                 mes_response = send_message_to_server(client, data_pac, "utf-8")
#                 time.sleep(3)
#                 count += 1
#             client.close()
#     return


# functional_client("test_config.json", "utf-8")
