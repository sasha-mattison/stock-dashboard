import yfinance as yf
import json
from enum import Enum

class Valid_Time_Periods(Enum):
    ONE_DAY = "1d"
    FIVE_DAYS = "5d"
    ONE_MONTH = "1mo"
    THREE_MONTHS = "3mo"
    SIX_MONTHS = "6mo"
    ONE_YEAR = "1y"
    TWO_YEARS = "2y"
    FIVE_YEARS = "5y"
    TEN_YEARS = "10y"
    YEAR_TO_DATE = "ytd"
    MAX = "max"
 

def get_current_price(stock: str):
    data = yf.Ticker(stock)
    return data.fast_info['last_price']


def get_historic_data(stock: str, time: Valid_Time_Periods):
    data = yf.Ticker(stock)
    return data.history(period=time.value)
