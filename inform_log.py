from datetime import datetime
from winreg import HKEY_LOCAL_MACHINE

def write_log():
    FILE_NAME = "inform_log.csv"
    with open(FILE_NAME, "w", encoding="UTF-8") as f:
        f.write(f"{datetime.now().strftime('%d.%m.%Y %H:%M')} Фамилия, Имя, \n")

