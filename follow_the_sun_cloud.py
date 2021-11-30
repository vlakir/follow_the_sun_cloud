import requests
import json
import warnings

"""
    Пример получения векторов состояния ИСЗ в ГСК, Солнца в ГСК и Солнца в ОСК с момента прохождения восходящего узла 
    с облачного сервера
    
    Принимает вектор состояния в момент прохождения восходящего узла, время прохождения восходящего узла 
    и период расчета в минутах (см. params):

    Результат выдает в терминал в виде json в формате:
    {
        "sat_status_vectors_km": [
            {
                "x": значение,
                "y": значение,
                "z": значение,
                "v_x": значение,
                "v_y": значение,
                "v_z": значение,
                "time": значение,
                "frame": "itrs"
            },
            ...
        ],
        "sun_status_vectors_km": [
        {
                "x": значение,
                "y": значение,
                "z": значение,
                "v_x": значение,
                "v_y": значение,
                "v_z": значение,
                "time": значение,
                "frame": "itrs"
            },
            ...
        ],
        "sun_status_vectors_ors_km": [
        {
                "x": значение,
                "y": значение,
                "z": значение,
                "v_x": значение,
                "v_y": значение,
                "v_z": значение,
                "time": значение,
                "frame": "ors"
            },
            ...
        ]

    }

    Размерности:
    составляющие радиус-вектора - м;
    составляющие скорости - м/c;

    Формат времени:
    "yyyy-mm-ddThh:mm:ss"
    Временная зона - UTC (при использовании любой другой, например Московской, расчет будет некорректным!) 

    В случае возникновения ошибки будет выдано сообщение в формате:
    {"errors": [{"error":"описание ошибки"}]}
    
    Перед первым запуском необходимо установить необходимые библиотеки:
    pip install -r requirements.txt
    
    Внимание! Для ускорения расчета не рекомендуется использовать period существенно более 60 минут  
    """

warnings.filterwarnings("ignore")

url = 'https://kmm.simct.ru:7443/api/v1/follow_the_sun.json'

params = {
                            "token": "84980637-164d-4571-a3a2-c0e1216547ac",
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
