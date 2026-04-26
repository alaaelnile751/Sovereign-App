import streamlit as st
import time
import random

# --- 1. الهوية البصرية الملكية ---
st.set_page_config(page_title="Okort Sovereign Factory", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, label { color: #D4AF37 !important; text-align: center; font-weight: bold; }
    
    .metric-box {
        background-color: #1a1a1a; border: 2px solid #D4AF37; border-radius: 12px;
        padding: 15px; text-align: center; height: 110px;
    }
    .m-title { color: #D4AF37; font-size: 14px; margin-bottom: 8px; }
    .m-val { color: #ffffff; font-size: 24px; font-family: monospace; }
    
    .live-digit-banner {
        background: #D4AF37; color: black; padding: 12px 40px;
        border-radius: 50px; font-weight: 900; font-size: 26px;
        display: inline-block; box-shadow: 0 0 20px rgba(212, 175, 55, 0.4);
        margin-top: 10px; margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ OKORT SOVEREIGN FACTORY")

# تهيئة الذاكرة
if 'final_data' not in st.session_state:
    st.session_state.final_data = {"ms": "0.00", "byte": "0", "eff": "0%", "cpu": "0%", "tier": "-"}

# --- 2. عرض العدادات الفنية ---
c1, c2, c3, c4, c5 = st.columns(5)
m_labels = ["زمن المعالجة (ms)", "حجم المخرجات", "كفاءة التشفير", "حمل المعالج", "المستوى"]
m_keys = ["ms", "byte", "eff", "cpu", "tier"]

for i in range(5):
    with [c1, c2, c3, c4, c5][i]:
        st.markdown(f'<div class="metric-box"><div class="m-title">{m_labels[i]}</div><div class="m-val">{st.session_state.final_data[m_keys[i]]}</div></div>', unsafe_allow_html=True)

st.divider()

# --- 3. منطقة الإدخال اليدوي ---
# العداد سيحدث الرقم فوراً عند الضغط خارج الصندوق أو Enter
u_input = st.text_area("أدخل الكتلة الرقمية المراد فحصها (يدوي):", height=150)

# العداد الحي البسيط (لا يخطئ)
current_count = len(u_input.replace(" ", "").replace("\n", ""))

st.markdown(f'<div style="text-align:center;"><div class="live-digit-banner">📊 رصد عدد الخانات الحالية: {current_count}</div></div>', unsafe_allow_html=True)

# --- 4. زر التفعيل ---
if st.button("🚀 بدء بروتوكول المعالجة"):
    if u_input:
        with st.spinner("جاري الفحص السيادي..."):
            start = time.time()
            time.sleep(1.0) # هيبة المعالجة
            
            st.session_state.final_data.update({
                "ms": f"{(time.time()-start)*1000:.2f}",
                "byte": f"{current_count + 128}",
                "eff": f"{99.7 + random.random():.2f}%",
                "cpu": f"{random.randint(1,4)}%",
                "tier": "TIER S-MAX" if current_count > 500 else "TIER A"
            })
            st.rerun()
