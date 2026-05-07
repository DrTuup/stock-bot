from pydantic import BaseModel
from typing import Optional


class ETFInfo(BaseModel):
    symbol: str
    shortName: str
    longName: str
    currency: str
    exchange: str
    fullExchangeName: str
    market: str
    quoteType: str
    typeDisp: str
    language: str
    region: str
    quoteSourceName: str
    fundFamily: str
    legalType: str
    marketState: str

    # Pricing
    regularMarketPrice: float
    regularMarketOpen: float
    regularMarketPreviousClose: float
    regularMarketDayLow: float
    regularMarketDayHigh: float
    regularMarketChange: float
    regularMarketChangePercent: float
    regularMarketDayRange: str
    regularMarketVolume: int
    regularMarketTime: int

    previousClose: float
    open: float
    dayLow: float
    dayHigh: float
    bid: float
    ask: float
    volume: int

    # Averages & ranges
    fiftyDayAverage: float
    twoHundredDayAverage: float
    fiftyDayAverageChange: float
    twoHundredDayAverageChange: float
    fiftyDayAverageChangePercent: float
    twoHundredDayAverageChangePercent: float
    fiftyTwoWeekLow: float
    fiftyTwoWeekHigh: float
    fiftyTwoWeekLowChange: float
    fiftyTwoWeekHighChange: float
    fiftyTwoWeekLowChangePercent: float
    fiftyTwoWeekHighChangePercent: float
    fiftyTwoWeekChangePercent: float
    fiftyTwoWeekRange: str

    # Volume
    averageVolume: int
    averageVolume10days: int
    averageDailyVolume10Day: int
    averageDailyVolume3Month: int

    # Fund specifics
    totalAssets: int
    netAssets: float
    navPrice: float
    allTimeHigh: float
    allTimeLow: float
    fundInceptionDate: int
    firstTradeDateMilliseconds: int

    # Exchange metadata
    exchangeTimezoneName: str
    exchangeTimezoneShortName: str
    gmtOffSetMilliseconds: int
    sourceInterval: int
    exchangeDataDelayedBy: int
    messageBoardId: str
    maxAge: int
    priceHint: int

    # Flags
    tradeable: bool
    triggerable: bool
    cryptoTradeable: bool
    esgPopulated: bool
    hasPrePostMarketData: bool

    # Misc
    phone: Optional[str] = None
    customPriceAlertConfidence: str
    trailingPegRatio: Optional[float] = None
    companyOfficers: list = []
    executiveTeam: list = []
    corporateActions: list = []
