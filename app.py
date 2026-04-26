import streamlit as st
import time
# التأكد من استيراد الوظيفة بالاسم الصحيح
from engine import sovereign_engine

# 1. إعدادات الصفحة
st.set_page_config(page_title="Okort Sovereign Engine", page_icon="🛡️", layout="wide")

# 2. تصميم الواجهة (تعديل السطر 13 الشهير)
st.markdown("""
    <style>
    .stApp { background-color: #0f0f0f; }
    h1, h2, h3, label { color: #D4AF37 !important; }
    .stButton>button { background-color: #D4AF37; color: black; border-radius: 25px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 3. محتوى الصفحة
st.title("🛡️ OKORT SOVEREIGN ENGINE")
st.write("---")

user_input = st.text_input("أدخل البيانات المراد معالجتها بنظام الشور:")

if st.button("بدء معالجة الشور"):
    if user_input:
        with st.spinner("جاري استحضار الشور النوبي..."):
            time.sleep(1.5)
            # استدعاء الوظيفة التي عرفناها في engine.py
            result = sovereign_engine(user_input)
            st.success("تمت المعالجة بنجاح")
            st.write(f"🛡️ النتيجة السيادية: {result}")
    else:
        st.warning("برجاء إدخال بيانات أولاً")
