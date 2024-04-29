import yfinance as yf
import plotly.graph_objects as go

ticker="TSLA"
userTicker=input("Write ticker name: ")
if userTicker:
    ticker=userTicker

data= yf.download(tickers=ticker, period="36mo", interval="1d", rounding=True)
print("Data from server for ticker: ", ticker)

chart=go.Figure()
chart.add_trace(go.Candlestick(x=data.index,
                               open=data["Open"],
                               high=data["High"],
                               low=data["Low"],
                               close=data["Close"],
                               name=" Price chart for "+ ticker
                               ))
chart.update_layout(title=ticker+ " share price", yaxis_title="Stock price (USD")

chart.show()
