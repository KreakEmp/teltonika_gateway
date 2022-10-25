import sys

sys.path.append(".")

from src.configurations.read_configurations import (
    get_industry_details,
    get_measurement_methods,
    get_parameter_details,
    get_site_details,
)

INDUSTRY_NAME = "INDUSTRY_NAME"
INDUSTRY_ADDR_1 = "INDUSTRY_ADDR_LINE1"
INDUSTRY_ADDR_2 = "INDUSTRY_ADDR_LINE2"
INDUSTRY_COUNTRY = "INDUSTRY_COUNTRY"
NO_OF_STATIONS = "NO_OF_STATIONS"
NO_OF_PARAMETERS = "NO_OF_PARAMETERS"
SITE_CODE = "SITE_CODE"

DESCRIPTION_BLOCK = "2"
DATA_BLOCK = "2"

codes = {
    "C3H6O": "C7",
    "C4H8O": "C3",
    "C6H12O": "C4",
    "C3H4O": "C5",
    "C4H6O": "C6",
    "C7H6O": "C8",
    "C8H8O": "C9",
    "C5H8": "VF",
    "C8H18": "VH",
    "C5H12": "VK",
    "C5H10": "VM",
    "C3H8": "VN",
    "C3H6": "VP",
    "C7H8": "VQ",
    "C9H12": "VT",
    "C8H10": "VA",
    "CHCl3": "H0",
    "CH3CCl3": "H1",
    "CCl4": "H2",
    "ClCHCCl2": "H3",
    "C2Cl4": "H4",
    "BaP": "P6",
    "BeP": "P7",
    "BaA": "P8",
    "DBahA": "P9",
    "BghiP": "Pa",
    "COR": "Pb",
    "CH2O": "VB",
    "C2H4O": "C1",
    "Ca": "B2",
    "Fe": "86",
    "Pb": "19",
    "Mg": "89",
    "Mn": "90",
    "Zn": "88",
    "Al3+": "A1",
    "NH4+": "48",
    "Cd2+": "A2",
    "Ca2+": "43",
    "Cl-": "40",
    "H+": "44",
    "Fe3+": "A3",
    "Pb2+": "A5",
    "Mg2+": "46",
    "Mn2+": "A4",
    "NO3-": "41",
    "K+": "45",
    "Na+": "47",
    "SO42-": "42",
    "Zn2+": "A6",
    "C4H6": "V0",
    "C4H8": "V7",
    "C2H2": "V3",
    "C6H6": "V4",
    "C4H10": "V6",
    "C2H6": "V8",
    "C2H4": "V9",
    "C7H16": "VC",
    "C6H14": "VD",
    "C6H12": "VE",
    "NO": "02",
    "NOX": "35",
    "N2O": "36",
    "O3": "08",
    "CH3C(O)OONO2": "09",
    "SO2": "01",
    "SO3": "13",
    "H2SO4": "38",
    "Cl": "98",
    "F": "99",
    "Al": "B1",
    "As": "80",
    "Be": "81",
    "Cd": "B3",
    "Cr": "83",
    "Cu": "84",
    "Hg": "85",
    "Ni": "87",
    "S": "14",
    "Sn": "57",
    "V": "92",
    "NH3": "21",
    "CO2": "17",
    "CO": "04",
    "C": "18",
    "HCl": "07",
    "HF": "06",
    "H2O2": "12",
    "H2S": "05",
    "CH4": "16",
    "HNO3": "37",
    "NO2": "03",
    "PM": "22",
}

industry_details = get_industry_details("src\configurations\config.json")
param_details = get_parameter_details("src\configurations\config.json")
site_details = get_site_details("src\configurations\config.json")
measurement_method = get_measurement_methods("src\configurations\config.json")
number_of_params = int(float(industry_details[NO_OF_PARAMETERS]))
params_det = []
filelines = {}
line_numb = 1

filelines[str(line_numb)] = "\n"
line_numb += 1
filelines[str(line_numb)] = "{:<71}".format(industry_details[INDUSTRY_NAME])[:71] + "\n"
line_numb += 1
filelines[str(line_numb)] = (
    "{:<143}".format(
        industry_details[INDUSTRY_ADDR_1] + industry_details[INDUSTRY_ADDR_2]
    )[:143]
    + "\n"
)
line_numb += 1
filelines[str(line_numb)] = (
    "{:<71}".format(industry_details[INDUSTRY_COUNTRY])[:71] + "\n"
)
line_numb += 1
filelines[str(line_numb)] = (
    "{:>5}".format(DESCRIPTION_BLOCK)[:5] + "{:>5}".format(DESCRIPTION_BLOCK)[:5] + "\n"
)
line_numb += 1
filelines[str(line_numb)] = "{:>3}".format(industry_details[NO_OF_STATIONS])
line_numb += 1

for j, site_d in enumerate(site_details):
    for i in range(number_of_params):
        print(f"Param Details is {param_details[i]}")
        # params_det.append(param_details[i])
        if param_details[i]["p_name"] in codes:
            measureand_code = "{:>2}".format(codes[param_details[i]["p_name"]])
        else:
            measureand_code = "{:>2}".format("  ")
        print(f"Measurand code is {measureand_code}")
        fixed_num = "1"
        measurand_name = "{:<14}".format(param_details[i]["p_name"])
        print(f"Measurand Name is {measurand_name}", len(measurand_name))
        unit = "{:<10}".format(param_details[i]["recv_unit"])
        print(f"Measurand Unit {unit}", len(unit))
        method = "{:<18}".format(measurement_method[i]["analyzer_id"])
        print(f"Measurement method {method}")
        higher_limit = "{:<6}".format(param_details[i]["max_range"])
        lower_limit = "{:<6}".format(param_details[i]["min_range"]) + "\n"
        filelines[str(line_numb)] = "{:>3}".format(industry_details[NO_OF_STATIONS])+measureand_code+measurand_name+unit+method+higher_limit+lower_limit
        line_numb+=1
        site_code = "{:>5}".format(industry_details[SITE_CODE])
        print(f"SITE CODE IS {site_code}")
        site_name = "{:>20}".format(site_details[j]["station_name"])
        print(f"SITE NAME IS {site_name}")
        site_lat = "{:>10}".format(site_details[j]["latitude"])
        site_long = "{:>11}".format(site_details[j]["longitude"])
        site_alt = "{:>5}".format(site_details[j]["altitude"])
        site_scale = "{:>5}".format(site_details[j]["scale"])
        filelines[str(line_numb)] = site_code+site_name+site_lat+site_long+site_alt+site_scale+"\n"
        line_numb+=1
        data_type_parameter = "{:>3}".format("") # Doubt
        data_type_code = "{:>2}".format("") #Doubt
        filelines[str(line_numb)] = "{:>3}".format(codes[param_details[i]["p_name"]]+"1")+site_code+data_type_parameter+data_type_code



print(filelines)

for key in filelines.keys():
    with open("data_file.txt", "a") as f:
        f.write(filelines[key])

f.close()
