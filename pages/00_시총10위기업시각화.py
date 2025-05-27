import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="글로벌 시총 10위 기업 주가 시각화", layout="wide")

st.title("🌎 글로벌 시총 10위 기업 주가 시각화 (2024~2025)")
st.markdown("""
이 Streamlit 앱은 **2024년 1월부터 2025년 5월까지** 글로벌 시가총액 상위 10개 기업의 주가 데이터를 시각화합니다.
""")

# 티커 리스트 (Yahoo Finance 기준)
tickers = {
    'Apple': 'AAPL',
    'Nvidia': 'NVDA',
    'Microsoft': 'MSFT',
    'Amazon': 'AMZN',
    'Alphabet (Google)': 'GOOGL',
    'Meta Platforms': 'META',
    'Berkshire Hathaway': 'BRK.B',  # BRK-B가 아닌 BRK.B
    'Tesla': 'TSLA',
    'TSMC': 'TSM',
    'Visa': 'V'  # Saudi Aramco는 야후 파이낸스에 티커 없음 또는 제한적 접근
}

selected_tickers = st.multiselect(
    "📌 시각화할 기업을 선택하세요",
    options=list(tickers.keys()),
    default=list(tickers.keys())
)

if selected_tickers:
    st.info("데이터를 불러오는 중입니다...")
    ticker_symbols = [tickers[company] for company in selected_tickers]

    data = yf.download(ticker_symbols, start="2024-01-01", end="2025-05-26", group_by="ticker")

    fig = go.Figure()

    for company in selected_tickers:
        ticker = tickers[company]
        try:
            adj_close = data[ticker]['Adj Close']
            fig.add_trace(go.Scatter(x=adj_close.index, y=adj_close, mode='lines', name=company))
        except KeyError:
            st.warning(f"❌ 데이터가 누락된 기업: {company}")

    fig.update_layout(
        title="📈 시가총액 상위 10개 기업의 주가 추이",
        xaxis_title="날짜",
        yaxis_title="조정 종가 (USD)",
        template="plotly_dark",
        legend_title="기업"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("👆 하나 이상의 기업을 선택해주세요.")
