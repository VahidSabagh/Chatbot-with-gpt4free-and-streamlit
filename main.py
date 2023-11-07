import g4f
import streamlit as st
from langdetect import detect
st.markdown(
    """
    <style>
    body {
        background-color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div style="direction: rtl; text-align: center; font-size: 50px; color: black; font-family: iransans; font-weight: bold;">چت‌بات شخصی من</div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)  # ایجاد یک خط خالی بین دو مورد

st.write(f'<div style="font-family: iransans; text-align: center;">هر سوالی دوست داری بپرس</div>', unsafe_allow_html=True)
inp = st.text_area('', key="text_area", value="", placeholder="Send a message")



ok = st.button('جواب بده')

if inp != "" and ok:
    response = g4f.ChatCompletion.create(
        # model="gpt-3.5-turbo",
        model=g4f.models.default,
        messages=[{"role": "user", "content": inp}],
        stream=True,
    )

    text = ""  # ایجاد یک متغیر برای جمع آوری متن جواب
    for message in response:
        text += "".join(message)  # اضافه کردن هر پیام به متن جواب

    # تشخیص زبان متن و ترتیب متن بر اساس زبان
    lang = detect(inp)
    if lang == "fa":  # اگر زبان فارسی باشد
        st.markdown(f'<div style="direction: rtl;font-family: iransans; text-align: right;">{text}</div>', unsafe_allow_html=True)
    else:  # در غیر این صورت
        st.markdown(f'<div style="direction: ltr; text-align: left;">{text}</div>', unsafe_allow_html=True)

    # st.write(text)  # نمایش متن جواب به صورت یک خط
st.markdown('<br>', unsafe_allow_html=True)  # ایجاد یک خط خالی بین دو مورد

st.markdown('<div style="direction: rtl; text-align: right; font-size: 10px; color: darkblue; font-family: iransans; font-weight: bold;">ایجاد شده توسط وحید صباغ</div>', unsafe_allow_html=True)
