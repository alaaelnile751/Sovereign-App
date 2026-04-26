import streamlit as st
import time
# استدعاء المحرك بالاسم الصحيح الذي كتبناه في الملف الآخر
from engine import sovereign_engine

# إعدادات الصفحة
st.set_page_config(page_title="Okort Sovereign Engine", page_icon="🛡️", layout="wide")

# تصميم الواجهة - اللون الأسود والذهبي
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, label, p { color: #D4AF37 !important; }
    .stButton>button { background-color: #D4AF37; color: black; border-radius: 20px; font-weight: bold; width: 100%; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: #D4AF37; border: 1px solid #D4AF37; }
    </style>
""", unsafe_allow_html=True)

# محتوى الصفحة
st.title("🛡️ OKORT SOVEREIGN ENGINE")
st.subheader("نظام المعالجة السيادية - شور")

user_input = st.text_input("أدخل البيانات المراد معالجتها:")

if st.button("تفعيل المحرك"):
    if user_input:
        with st.spinner("جاري الاتصال بالمحرك السيادي..."):
            time.sleep(1)
            # استخدام الوظيفة
            output = sovereign_engine(user_input)
            st.success("تمت المعالجة!")
            st.write(f"📊 النتيجة: {output}")
    else:
        st.warning("برجاء إدخال بيانات")
