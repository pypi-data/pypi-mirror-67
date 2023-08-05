import json
import urllib.request
import pandas as pd


def _get_server():
    return 'http://207.148.28.62:5000'
    #return 'http://127.0.0.1:5000'


class Setify:

    def __init__(self):
        pass

    @staticmethod
    def country_birth_rate(country_code):
        with urllib.request.urlopen(_get_server() + "/country_birth_rate/" + country_code + "/") as url:
            data = json.loads(url.read().decode())
            df = pd.DataFrame(data)
            df['year'] = df['year'].astype(int)
            return df

    @staticmethod
    def country_death_rate(country_code):
        with urllib.request.urlopen(_get_server() + "/country_death_rate/" + country_code + "/") as url:
            data = json.loads(url.read().decode())
            df = pd.DataFrame(data)
            df['year'] = df['year'].astype(int)
            return df

    @staticmethod
    def logic_gate_not():
        with urllib.request.urlopen(_get_server() + "/logic_gate_not") as url:
            data = json.loads(url.read().decode())
            df = pd.DataFrame(data)
            df.columns = ['x', 'y']
            return df

    @staticmethod
    def logic_gate_and():
        with urllib.request.urlopen(_get_server() + "/logic_gate_and") as url:
            data = json.loads(url.read().decode())
            df = pd.DataFrame(data)
            df.columns = ['x1', 'x2', 'y']
            return df

    @staticmethod
    def logic_gate_nand():
        with urllib.request.urlopen(_get_server() + "/logic_gate_nand") as url:
            data = json.loads(url.read().decode())
            df = pd.DataFrame(data)
            df.columns = ['x1', 'x2', 'y']
            return df

    @staticmethod
    def logic_gate_or():
        with urllib.request.urlopen(_get_server() + "/logic_gate_or") as url:
            data = json.loads(url.read().decode())
            df = pd.DataFrame(data)
            df.columns = ['x1', 'x2', 'y']
            return df

    @staticmethod
    def logic_gate_nor():
        with urllib.request.urlopen(_get_server() + "/logic_gate_nor") as url:
            data = json.loads(url.read().decode())
            df = pd.DataFrame(data)
            df.columns = ['x1', 'x2', 'y']
            return df

    @staticmethod
    def logic_gate_xor():
        with urllib.request.urlopen(_get_server() + "/logic_gate_xor") as url:
            data = json.loads(url.read().decode())
            df = pd.DataFrame(data)
            df.columns = ['x1', 'x2', 'y']
            return df

    @staticmethod
    def logic_gate_xnor():
        with urllib.request.urlopen(_get_server() + "/logic_gate_xnor") as url:
            data = json.loads(url.read().decode())
            df = pd.DataFrame(data)
            df.columns = ['x1', 'x2', 'y']
            return df

    @staticmethod
    def temperatures_daily_min():
        with urllib.request.urlopen(_get_server() + "/temperatures_daily_min") as url:
            data = json.loads(url.read().decode())
            df = pd.DataFrame(data)
            df.columns = ['date', 'temp']
            df['date'] = df['date'].astype('datetime64[ns]')
            return df

    @staticmethod
    def shampoo_sales():
        with urllib.request.urlopen(_get_server() + "/shampoo_sales") as url:
            data = json.loads(url.read().decode())
            df = pd.DataFrame(data)
            df.columns = ['month', 'sales']
            return df

    @staticmethod
    def monthly_sunspot():
        with urllib.request.urlopen(_get_server() + "/monthly_sunspot") as url:
            data = json.loads(url.read().decode())
            df = pd.DataFrame(data)
            df.columns = ['month', 'sunspot']
            return df

    @staticmethod
    def daily_female_births():
        with urllib.request.urlopen(_get_server() + "/daily_female_births") as url:
            data = json.loads(url.read().decode())
            df = pd.DataFrame(data)
            df.columns = ['date', 'birth']
            df['date'] = df['date'].astype('datetime64[ns]')
            return df

    @staticmethod
    def occupancy_data():
        with urllib.request.urlopen(_get_server() + "/occupancy_data") as url:
            data = json.loads(url.read().decode())
            df = pd.DataFrame(data)
            df.columns = ['date', 'temperature', 'humidity', 'light', 'co2', 'humidity_ratio', 'occupancy']
            df['date'] = df['date'].astype('datetime64[ns]')
            return df
