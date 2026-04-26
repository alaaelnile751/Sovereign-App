import streamlit as st
import time
from engine import engine

# 1. إعدادات الصفحة السيادية
st.set_page_config(
    page_title="Okort | Sovereign Engine",
    page_icon="🛡️",
    layout="centered"
)

# 2. تصميم الواجهة (CSS) - روح النوبة وتكنولوجيا المستقبل
st.markdown("""
    <style>
    .stApp {
        background-color: #0f0f0f;
    }
    /* تصميم بطاقات Okort */
    .okort-card {
        background: linear-gradient(145deg, #1e1e1e, #141414);
        padding: 25px;
        border-radius: 15px;
        border-right: 6px solid #FFD700; /* الذهب النوبي */
        border-left: 2px solid #4B0082;  /* الأرجواني الملكي */
        margin-bottom: 20px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
        color: white;
    }
    /* أنيميشن الشور النوبي */
    @keyframes rotate-shour {
        0% { transform: rotate(0deg); border-color: #FFD700; }
        50% { border-color: #cc0000; }
        100% { transform: rotate(360deg); border-color: #FFD700; }
    }
    .shour-loader {
        width: 80px;
        height: 80px;
        margin: 20px auto;
        border: 6px dotted #FFD700;
        border-radius: 50%;
        animation: rotate-shour 2s linear infinite;
    }
    h1 { color: #FFD700 !important; text-align: center; font-family: 'Arial'; }
    .stButton>button {
        background: linear-gradient(to right, #4B0082, #6A0DAD);
        color: white; border: 1px solid #FFD700;
        border-radius: 10px; width: 100%; font-weight: bold;
    }
    </style>
    """, unsafe_allow_config=True)

# 3. واجهة المستخدم
st.markdown("<h1>🛡️ OKORT ENGINE</h1>", unsafe_allow_config=True)
st.markdown("<p style='text-align: center; color: #aaa;'>نظام الحماية الرقمية المستوحى من التراث النوبي (الشور)</p>", unsafe_allow_config=True)

input_data = st.text_area("أدخل الرقم المراد تأمينه ومعالجته (نطاق سيادي):", placeholder="مثال: 1234...")

if st.button("🚀 بدء المعالجة وتفعيل حماية الشور"):
    if input_data:
        # عرض أيقونة الشور أثناء التحميل
        placeholder = st.empty()
        with placeholder.container():
            st.markdown('<div class="shour-loader"></div>', unsafe_allow_config=True)
            st.markdown("<p style='text-align: center; color: #FFD700;'>جاري التغطية بنظام الشور السيادي...</p>", unsafe_allow_config=True)
            
            # استدعاء المحرك
            res = engine.process_sovereign_number(input_data)
            time.sleep(1.2) # لحظة جمالية لمشاهدة الشور
        
        placeholder.empty() # مسح أيقونة التحميل بعد الانتهاء

        # عرض النتائج
        st.success("تمت المعالجة بنجاح!")
        st.markdown(f"""
            <div class="okort-card">
                <h3 style='color: #FFD700; margin-top:0;'>📊 تقرير الأداء السيادي</h3>
                <p style='font-size: 1.3em;'>⚡ زمن المعالجة: <span style='color: #00ff00;'>{res['duration_micro']} μs</span></p>
                <p>📏 طول السلسلة: {res['length']} خانة</p>
                <p>🔒 وضع الحماية: <span style='color: #FFD700;'>نشط (الشور النوبي)</span></p>
                <hr style='border-color: #333;'>
                <p style='font-size: 0.8em; color: #888;'>تم توثيق هذه العملية بنظام Okort المبتكر.</p>
            </div>
        """, unsafe_allow_config=True)
    else:
        st.error("يرجى إدخال الرقم المطلوب.")

st.markdown("<br><p style='text-align: center; color: #444; font-size: 0.7em;'>Okort v1.0 | Patent Pending © 2026</p>", unsafe_allow_config=True)
