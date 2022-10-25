import sys
import datetime
import pytz
import json

sys.path.append(".")
from src.configurations.read_configurations import get_parameter_details


def create_list_of_param_values(message_string):
    val_list = message_string.replace("#", "").split("+")
    return val_list


def create_datoms_data_packet_data(config_filepath, message_string):
    dp = {}
    try:
        value_list = create_list_of_param_values(message_string)
        params_details = get_parameter_details(config_filepath)
        if len(value_list) == len(params_details):
            for i, param_detail in enumerate(params_details):
                dp[param_detail["name"]] = value_list[param_detail["ch_no"] - 1]
        else:
            raise Exception(
                "[MISMATCH] Number of parameters and number of values mismatch"
            )
    except Exception as e:
        print(e)
    return dp


def get_current_date_time():
    current_time = datetime.datetime.now(pytz.timezone("Asia/Kolkata")).strftime(
        "%d-%m-%Y %H:%M:%S"
    )
    date = str(current_time).split(" ")[0]
    time = str(current_time).split(" ")[1]
    return date, time


def parse_serial_data(config_filepath, message_string):
    dp = create_datoms_data_packet_data(config_filepath, message_string)
    data_packet = {"type": "data", "message": {"d": "", "t": "", "dp": {}}}
    date, time = get_current_date_time()
    data_packet["message"]["d"] = str(date)
    data_packet["message"]["t"] = str(time)
    data_packet["message"]["dp"] = dp
    return json.dumps(data_packet)
