# streamlit_app.py
import streamlit as st

st.set_page_config(page_title="소득 수준 & 세금 계산기")

st.title("소득 수준 & 세금 계산기")
st.write("고소득 50%, 중산층 25%, 저소득 10% 세율 규칙을 적용합니다.")

# 입력값
github_account = st.text_input("GitHub 계정(URL 또는 아이디)", placeholder="https://github.com/your-id")
income = st.number_input("소득을 입력하세요 (예: 월 소득)", min_value=0, value=3500, step=1)

# 계산
if st.button("계산"):
    if income >= 5000:
        rate, level = 0.5, "고소득자"
    elif income >= 3000:
        rate, level = 0.25, "중산층"
    else:
        rate, level = 0.1, "저소득자"

    tax = income * rate

    st.subheader("결과")
    st.write(f"**소득:** {income:,.0f}원")
    st.write(f"**소득 수준:** {level}")
    st.write(f"**세율:** {int(rate*100)}%")
    st.write(f"**세금:** {tax:,.0f}원")
    if github_account:
        st.caption(f"GitHub 계정: {github_account}")
