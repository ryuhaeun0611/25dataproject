import yfinance as yf
import plotly.graph_objects as go

# 정확한 티커 목록 (BRK-B는 BRK-B가 아닌 BRK.B로 써야 합니다)
tickers = ['AAPL', 'NVDA', 'MSFT', 'AMZN', 'GOOGL', 'META', 'BRK.B', 'TSLA', 'TSM', 'V']

# 데이터 다운로드
data = yf.download(tickers, start="2024-01-01", end="2025-05-26", group_by='ticker')

# 시각화용 Figure
fig = go.Figure()

for ticker in tickers:
    try:
        adj_close = data[ticker]['Adj Close']
        fig.add_trace(go.Scatter(x=adj_close.index, y=adj_close, mode='lines', name=ticker))
    except KeyError:
        print(f"❌ 데이터 없음: {ticker}")

fig.update_layout(
    title="2024~2025 글로벌 시총 10대 기업 주가 추이",
    xaxis_title="날짜",
    yaxis_title="조정 종가 (USD)",
    template="plotly_dark",
    legend_title="기업"
)

fig.show()

