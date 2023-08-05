import json
import urllib.request
import pandas as pd
import numpy as np


def _get_server():
    return 'http://207.148.28.62:5000'


class Setify:

    def __init__(self):
        pass

    @staticmethod
    def country_birth(country_code):
        with urllib.request.urlopen(_get_server() + "/country_birth/" + country_code + "/") as url:
            data = json.loads(url.read().decode())
            return pd.DataFrame(data)
