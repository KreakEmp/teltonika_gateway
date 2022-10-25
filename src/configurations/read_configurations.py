import json

SERVER_DETAILS = "server_details"
PARAMETER_DETAILS = "parameter_details"
INDUSTRY_DETAILS = "industry_details"
MEASUREMENT_METHOD = "measurement_method"
SITE_DETAILS = "site_details"
AUTH_TOKEN = "authentication_token"
KEYS = "keys"
HOST = "host"
PORT = "port"


def read_json_file(config_filepath):
    try:
        with open(config_filepath, "r") as f:
            data = json.load(f)
        f.close()
        return data
    except Exception as e:
        print(e)


def get_server_address(config_filepath):
    try:
        addr = ()
        config = read_json_file(config_filepath)
        if (
            SERVER_DETAILS in config
            and HOST in config[SERVER_DETAILS]
            and PORT in config[SERVER_DETAILS]
        ):
            addr = (config[SERVER_DETAILS][HOST], config[SERVER_DETAILS][PORT])
    except Exception as e:
        print(e)
    return addr


def get_parameter_details(config_filepath):
    try:
        configs = read_json_file(config_filepath)
        if PARAMETER_DETAILS in configs:
            return configs[PARAMETER_DETAILS]
    except Exception as e:
        print(e)



def get_auth_token(config_filepath):
    try:
        configs = read_json_file(config_filepath)
        if AUTH_TOKEN in configs:
            return configs[AUTH_TOKEN]
    except Exception as e:
        print(e)

def get_industry_details(config_filepath):
    try:
        configs = read_json_file(config_filepath)
        if INDUSTRY_DETAILS in configs:
            return configs[INDUSTRY_DETAILS]
    except Exception as e:
        print(e)

def get_measurement_methods(config_filepath):
    try:
        configs = read_json_file(config_filepath)
        if MEASUREMENT_METHOD in configs:
            return configs[MEASUREMENT_METHOD]
    except Exception as e:
        print(e)

def get_site_details(config_filepath):
    try:
        configs = read_json_file(config_filepath)
        if SITE_DETAILS in configs:
            return configs[SITE_DETAILS]
    except Exception as e:
        print(e)

def get_keys(config_filepath):
    try:
        configs = read_json_file(config_filepath)
        if KEYS in configs:
            return configs[KEYS]
    except Exception as e:
        print(e)
