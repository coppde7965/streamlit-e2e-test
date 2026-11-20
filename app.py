import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Git Deploy E2E Test",
    page_icon="🚀",
    layout="centered",
)

st.title("部署成功！🚀")

st.success("這個網站已經透過 Git Deploy Platform 啟動。")

st.subheader("E2E Deployment Test")

st.write("Git Clone：專案已成功取得")
st.write("Docker Build：映像檔已成功建置")
st.write("Container：應用程式已啟動")
st.write("Caddy：等待反向代理驗證")

st.divider()

st.write("伺服器時間：", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

st.caption("Git Deploy Platform - End-to-End Test")
