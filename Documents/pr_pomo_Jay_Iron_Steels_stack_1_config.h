#ifndef _PR_POMO_JAY_IRON_STEEL_ADAM_STACK_1_CONFIG_H_
#define _PR_POMO_JAY_IRON_STEEL_ADAM_STACK_1_CONFIG_H_
	
#include "pr_pomo_common.h"

#define USE_SD_CARD
#define QR_CODE_HARCODED                    "BLOME9O6"

#define AUTH_KEY_HARDCODED			"g0I0XkmF25xHuhAmANJ39t6OJIMXKHsvSFxBjgyOj0KLyf8KLQyHLalbybokHM2l"

#define CONFIG_TEMPLATE_HARDCODED           "Jay_Iron_Steels_stack_1_config"

#define NO_OF_PARAMETERS 	2
#define NO_OF_SYSTEMS		1
#define NO_OF_STATIONS 		1

#define INDUSTRY_NAME			"Jay Iron & Steels Ltd."
#define INDUSTRY_ADDR_LINE1		"Odisha"
#define INDUSTRY_ADDR_LINE2		""
#define INDUSTRY_COUNTRY		"India"
#define SITE_CODE				"3058"
#define DATA_QUALITY_FLAG		"U"
#define TIMEZONE_CODE			"Z"

//0 request 1 slave
#define HARDWARE_CONFIG	"{\"type\":\"config\",\"message\":[{\"config_ty\":\"hw_dt\",\"sy_n\":\"1\",\"serial_no\":\"1\",\"serial_br\":\"9600\",\"time_out\":\"0\",\"mode\":\"0\"}],\"message_id\":\"16\"}"
#define PROTOCOL_CONFIG "{\"type\":\"config\",\"message\":[{\"config_ty\":\"pc_dt\",\"sy_n\":\"1\",\"dev_id\":\"11\",\"del_based\":\"1\",\"delim\":\"+-\",\"pkt_identifier\":\">\",\"pkt_end\":\"\r\",\"no_of_channels\":\"8\",\"res_timeout\":\"2500\",\"cmd_type\":\"0\",\"cmdseq_no\":\"0\"}],\"message_id\":\"16\"}"

#define COMMAND_CONFIG "{\"type\":\"config\",\"message\":[{\"config_ty\":\"cmd_dt\",\"sy_n\":\"1\",\"cmd_n\":\"1\",\"cmd\":\"#01\r\",\"res\":\"\",\"res_len\":\"\"}],\"message_id\":\"16\"}"

char *PRARAMETER_CONFIG[NO_OF_STATIONS] =
{
		"{\"type\":\"config\",\"message\":[{\"config_ty\":\"p_dt\",\"p_n\":\"1\",\"sy_n\":\"1\",\"p_type\":\"0\",\"p_name\":\"PM\",\"s_offset\":\"0\",\"s_multiplier\":\"1\",\"pkt_start_id\":\"M000\",\"pkt_end_id\":\"g\/m3\",\"param_id\":\"PM\",\"deli_cnt\":\"9\",\"sta_ch_pos\":\"0\",\"sto_ch_pos\":\"0\",\"range_filter\":\"1\",\"handle_garb\":\"2\",\"handle_no_data\":\"1\",\"recv_unit\":\"mg\/Nm3\",\"offset\":\"0\",\"multiplier\":\"1\",\"min_range\":\"0\",\"max_range\":\"1000\",\"channel\":\"0\",\"s_in_min\":\"4\",\"s_in_max\":\"20\"},{\"config_ty\":\"p_dt\",\"p_n\":\"2\",\"sy_n\":\"1\",\"p_type\":\"0\",\"p_name\":\"SO2\",\"s_offset\":\"0\",\"s_multiplier\":\"1\",\"pkt_start_id\":\"M000\",\"pkt_end_id\":\"g\/m3\",\"param_id\":\"SO2\",\"deli_cnt\":\"9\",\"sta_ch_pos\":\"0\",\"sto_ch_pos\":\"0\",\"range_filter\":\"1\",\"handle_garb\":\"2\",\"handle_no_data\":\"1\",\"recv_unit\":\"mg\/Nm3\",\"offset\":\"0\",\"multiplier\":\"1\",\"min_range\":\"0\",\"max_range\":\"2000\",\"channel\":\"1\"}],\"msg_checksum\":\"37434\",\"message_id\":\"16\"}"
};


param_stations_conf_t stations_data[NO_OF_STATIONS] = {
		[0] = {
				.station_id = "22",
				.station_name = "CEMS_1",
				.analyzers[0] = {
					.analyzer_param_name = DATOMS_ISO_PARAM_PM,
					.analyzer_id = "analyzer_690"
				},
				.analyzers[1] = {
					.analyzer_param_name = DATOMS_ISO_PARAM_SO2,
					.analyzer_id = "analyzer_353"
				}
		}
};


/*Server related detials*/

#define KEY	"c2l0ZV8zMDU4XnZlcl8xLjBeT1NQQ0JeMjAxOS0wOS0xMS0xMTozNjoxNw==####"
#define LONGITUDE		"84.76093"
#define LATITUDE		"22.205922"
#define VERSION			"1.0"

char *server_public_key =
		"-----BEGIN RSA PUBLIC KEY-----\n"
        "MEgCQQCcADcRmHrTtDWsknzx5D64iNdwYscWi0+fI8nh9cO26HtRSeXBnSJuMlJK\n"
        "is7qn+lznsbi3DRwYOdM4w/7Z8bhAgMBAAE=\n"
        "-----END RSA PUBLIC KEY-----\n";

char *site_private_key =
		"-----BEGIN RSA PRIVATE KEY-----\n"
        "MIIBPQIBAAJBAKgybg3vQLQFkxgWvvsatXjPjlwVLzJpCfPKHYrGEfKy/Jk5hsaN\n"
        "/lhGYPOiLaYiV2EZ7vnEAjr+AImV83WOpZECAwEAAQJBAICh+MsNZBWJgeJVWv/d\n"
        "gFYBnmVMCklqTaM1uvwr2E22NeopdkIfdOV67yOl7RC9QF4yGSuIHbx3zTNf0tp6\n"
        "WUUCIwDugM+oKDvGXNAfqG1ZJu/SOOrsX8n6NWlR51aMolhSCyXPAh8AtIk9TSZe\n"
        "/IgcNcOFnsuehUNlTgpdD1In/lihb7afAiMAt9Peujxwfh6xZ4U46vtA42ZtY80c\n"
        "71ZVnARTyEelDW98LwIeSAAH07H+5eX+oi6FJsx8Pxee2l3luUuBqb19PMlvAiJ7\n"
        "Y5p6mQ/xIg20hEZ3mQpU1/WCdLj5Xfx1HN51g/bF7jzU\n"
        "-----END RSA PRIVATE KEY-----\n";

unsigned char iv[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
#endif