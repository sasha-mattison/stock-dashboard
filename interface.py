import yfinance as yf
import json
from enum import Enum


class ValidTimePeriods(Enum):
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

class Interface():
    def getCurrentPrice(self, stock: str) -> float:
        data = yf.Ticker(stock)
        price = data.fast_info["last_price"]
        if price is None:
            raise RuntimeError(f"No current price available for {stock!r}")
        return float(price)
    
    def getHistoricData(self, stock: str, time: ValidTimePeriods):
        data = yf.Ticker(stock)
        return data.history(period=time.value)
