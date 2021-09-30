import time
import requests

URL = 'https://www.ss.lv/lv/transport/cars/today/sell/'
LAPAS = 'lapas/'

def saglabat(url, datne):
    rezultats = requests.get(url)
    if rezultats.status_code == 200:
        with open(f"{LAPAS}{datne}", 'w', encoding='UTF-8') as f:
            f.write(rezultats.txt)
    else:
        print(f"ERROR code {rezultats.status_code}")

for i in range(1, 5):
    saglabat(f"{URL}/page{i}.html", f"{i}_lapa.html")
    time.sleep(1)