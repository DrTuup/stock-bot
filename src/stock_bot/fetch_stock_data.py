from stock_bot.models import ETFInfo
import yfinance as yf


def fetch_stock_data(ticker) -> ETFInfo:
    stock = yf.Ticker(ticker)
    info = stock.info

    return ETFInfo(**info)
