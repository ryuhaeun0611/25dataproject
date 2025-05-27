import yfinance as yf
import plotly.graph_objects as go

# 기업 티커 리스트
tickers = ['AAPL', 'NVDA', 'MSFT', 'AMZN', 'GOOGL', 'META', 'BRK-B', 'TSLA', 'TSM', 'V']

# 데이터 다운로드
data = yf.download(tickers, start="2024-01-01", end="2025-05-26")['Adj Close']

# 시각화
fig = go.Figure()

for ticker in tickers:
    fig.add_trace(go.Scatter(x=data.index, y=data[ticker], mode='lines', name=ticker))

fig.update_layout(
    title="Top 10 Global Companies by Market Cap (2025) Stock Prices",
    xaxis_title="Date",
    yaxis_title="Adjusted Close Price (USD)",
    template="plotly_dark",
    legend_title="Companies"
)

fig.show()
