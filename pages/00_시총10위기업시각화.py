import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="글로벌 시총 10위 기업 주가 시각화", layout="wide")

st.title("🌎 글로벌 시총 10위 기업 주가 시각화 (2024~2025)")
st.markdown("""
이 Streamlit 앱은 **2024년 1월부터 2025년 5월까지** 글로벌 시가총액 상위 10개 기업의 주가 데이터를 시각화합니다.
""")

# Yahoo Finance 티커
tickers = {
    'Apple': 'AAPL',
    'Nvidia': 'NVDA',
    'Microsoft': 'MSFT',
    'Amazon': 'AMZN',
    'Alphabet (Google)': 'GOOGL',
    'Meta Platforms': 'META',
    'Berkshire Hathaway': 'BRK.B',  # 올바른 티커
    'Tesla': 'TSLA',
    'TSMC': 'TSM',
    'Visa': 'V'  # Saudi Aramco 대체
}

selected_tickers = st.multiselect(
    "📌 시각화할 기업을 선택하세요",
    options=list(tickers.keys()),
    default=list(tickers.keys())
)

if selected_tickers:
    st.info("데이터를 불러오는 중입니다...")
    ticker_symbols = [tickers[company] for company in selected_tickers]

    data = yf.download(ticker_symbols, start="2024-01-01", end="2025-05-26", group_by="ticker", auto_adjust=True)

    fig = go.Figure()

    for company in selected_tickers:
        ticker = tickers[company]
        try:
            if len(ticker_symbols) == 1:
                # 단일 선택일 경우 구조 다름
                adj_close = data['Adj Close']
            else:
                adj_close = data[ticker]['Adj Close']
            fig.add_trace(go.Scatter(x=adj_close.index, y=adj_close, mode='lines', name=company))
        except Exception as e:
            st.warning(f"❌ 데이터가 누락된 기업: {company} | 오류: {e}")

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
