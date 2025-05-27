import streamlit as st
import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# 서초구 고등학교 예시 데이터
school_data = pd.DataFrame({
    "학교명": ["서울고등학교", "양재고등학교", "세화고등학교", "반포고등학교"],
    "위도": [37.4922, 37.4823, 37.4887, 37.5040],
    "경도": [127.0112, 127.0366, 127.0142, 127.0129],
    "유형": ["공립", "공립", "사립", "공립"]
})

# Streamlit 앱 제목
st.title("📍 서울 서초구 고등학교 위치 지도")

# 지도 초기 위치: 서초구 중심
center_lat = 37.4836
center_lon = 127.0327

# Folium 지도 생성
m = folium.Map(location=[center_lat, center_lon], zoom_start=13)

# 학교마다 마커 추가
for i, row in school_data.iterrows():
    popup_text = f"<b>{row['학교명']}</b><br>유형: {row['유형']}"
    folium.Marker(
        location=[row['위도'], row['경도']],
        popup=popup_text,
        icon=folium.Icon(color="blue" if row["유형"] == "공립" else "green")
    ).add_to(m)

# 지도 출력
st_folium(m, width=700, height=500)
