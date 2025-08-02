import requests
from functools import lru_cache
import urllib3

# Отключаем предупреждения о небезопасных запросах
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Вывод списка основных API ендпоинтов
def get_api_list():

    print(f"Список основных API ендпоинтов:"
          f"https://nspd.gov.ru/api/registers-manager/v2/pop-up?code=technical_work\n"
          f"https://nspd.gov.ru/api/portal-tools/v1/audit\n"
          f"https://nspd.gov.ru/api/portal-tools/v1/page-assistant/geoportalTectus\n"
          f"https://nspd.gov.ru/assets/map/mf-manifest.json\n"
          f"https://nspd.gov.ru/assets/mf-manifest.json\n"
          f"https://mc.yandex.ru/watch/96513913?wmode=7&page-url=https%3A%2F%2Fnspd.gov.ru%2Fmap%3Fthematic%3DPKK%26zoom%3D5.707706836491453%26coordinate_x%3D7195516.790469242%26coordinate_y%3D7595976.509552433%26baseLayerId%3D235%26theme_id%3D1%26is_copy_url%3Dtrue&page-ref=https%3A%2F%2Fwww.google.com%2F&charset=utf-8&uah=chu%0A%22Not)A%3BBrand%22%3Bv%3D%228%22%2C%22Chromium%22%3Bv%3D%22138%22%2C%22Google%20Chrome%22%3Bv%3D%22138%22%0Acha%0Ax86%0Achb%0A64%0Achf%0A138.0.7204.169%0Achl%0A%22Not)A%3BBrand%22%3Bv%3D%228.0.0.0%22%2C%22Chromium%22%3Bv%3D%22138.0.7204.169%22%2C%22Google%20Chrome%22%3Bv%3D%22138.0.7204.169%22%0Achm%0A%3F0%0Achp%0AWindows%0Achv%0A10.0.0&browser-info=pv%3A1%3Avf%3A1070pi7qlp5u015cyvan3jjxu0lzz%3Afu%3A0%3Aen%3Autf-8%3Ala%3Aru-RU%3Av%3A2145%3Acn%3A1%3Adp%3A0%3Als%3A255480344637%3Ahid%3A476893815%3Az%3A300%3Ai%3A20250801201202%3Aet%3A1754061122%3Ac%3A1%3Arn%3A997192245%3Arqn%3A54%3Au%3A175404818146338358%3Aw%3A693x737%3As%3A1536x864x24%3Ask%3A1.25%3Afp%3A1600%3Awv%3A2%3Ads%3A0%2C0%2C40%2C2%2C2%2C0%2C%2C141%2C0%2C1002%2C1002%2C1%2C831%3Aco%3A0%3Acpf%3A1%3Ans%3A1754061120189%3Aadb%3A1%3Arqnl%3A1%3Ast%3A1754061122%3At%3A%D0%9F%D0%BE%D1%80%D1%82%D0%B0%D0%BB%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D1%85%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20%22%D0%9D%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D1%85%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%22&t=gdpr(14)clc(0-0-0)rqnt(1)aw(1)rcm(1)eco(83952132)ti(1)\n"
          f"https://nspd.gov.ru/api/geoportal/v1/page-search-settings?pageCode=geoportal\n"
          f"https://nspd.gov.ru/api/geoportal/v1/baselayers\n"
          f"https://nspd.gov.ru/api/geoportal/v1/layers-theme\n"
          f"https://nspd.gov.ru/api/geoportal/v1/layers-theme-tree?themeId=1\n"
          f"https://nspd.gov.ru/api/geoportal/v1/search-theme?pageCode=geoportal\n"
          f"https://nspd.gov.ru/api/geoportal/v1/search-theme?pageCode=geoportal\n")

# Поиск слоёв по их категориям
class LayerAPI:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    @lru_cache(maxsize=1)
    def _get_data(self):
        # Добавляем verify=False для игнорирования SSL-сертификатов
        return requests.get(self.endpoint, verify=False).json()

    def get_layers_by_category(self, category_id):
        data = self._get_data()
        return [
            layer for layer in data['layers']
            if layer.get('categoryId') == category_id
        ]

    def find_layer_by_name(self, name_part):
        data = self._get_data()
        return [
            layer for layer in data['layers']
            if name_part.lower() in layer['title'].lower()
        ]


# Использование
api = LayerAPI('https://nspd.gov.ru/api/geoportal/v1/layers-theme-tree?themeId=1')
heritage_layers = api.get_layers_by_category(36940)
get_api_list()
print(f"Найдено слоев культурного наследия: {len(heritage_layers)}")
