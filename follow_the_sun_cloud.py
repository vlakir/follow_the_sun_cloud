import requests
import json
import warnings

warnings.filterwarnings("ignore")

url = 'https://kmm.simct.ru:7443/api/v1/follow_the_sun.json'

params = {
                            "token": "891afd98-764d-423b-b62a-df351c5ef2a3",
                            "status_vector_sat_ascending_node": {
                                "x": 4951.209053138 * 1000,
                                "y": -4653.856628012 * 1000,
                                "z": 0.0,
                                "v_x": 2.896991154055 * 1000,
                                "v_y": 3.110415318743 * 1000,
                                "v_z": 6.001929490957 * 1000,
                                "time": "2021-07-23T20:33:25",
                                "frame": 'itrs'
                            },
                            "time_m": 60,
                          }


if __name__ == '__main__':
    response = requests.post(url, verify=False, data=json.dumps(params)).json()
    pretty_string = json.dumps(response, sort_keys=False, indent=4, ensure_ascii=False)
    print(pretty_string)
