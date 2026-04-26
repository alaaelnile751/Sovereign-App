import streamlit as st
import time
import random

# --- 1. إعدادات المسرح الملكي ---
st.set_page_config(page_title="Okort Mega Factory", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    .main-title { 
        background: linear-gradient(90deg, #D4AF37, #FFFFFF, #D4AF37);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-size: 50px; font-weight: 900; text-align: center; margin-bottom: 0px;
    }
    .metric-box {
        background-color: #111; border: 1px solid #D4AF37; border-radius: 15px;
        padding: 15px; text-align: center; box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
    }
    .m-val { color: #ffffff; font-size: 28px; font-family: 'Courier New', monospace; font-weight: bold; }
    
    /* عداد الإبهار - عملاق وذهبي */
    .mega-counter {
        background: radial-gradient(circle, #D4AF37 0%, #AA8413 100%);
        color: black; padding: 20px 80px;
        border-radius: 100px; font-weight: 900; font-size: 45px;
        display: inline-block; box-shadow: 0 0 50px rgba(212, 175, 55, 0.8);
        border: 4px solid #fff; margin: 20px 0;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); box-shadow: 0 0 30px #D4AF37; }
        50% { transform: scale(1.05); box-shadow: 0 0 60px #D4AF37; }
        100% { transform: scale(1); box-shadow: 0 0 30px #D4AF37; }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🛡️ OKORT SOVEREIGN FACTORY</p>', unsafe_allow_html=True)

# إدارة الحالة
if 'stats' not in st.session_state:
    st.session_state.stats = {"ms": "0.00", "byte": "0", "eff": "100%", "cpu": "0%", "tier": "ULTIMATE"}
if 'mega_input' not in st.session_state: st.session_state.mega_input = ""

def sync_input(): st.session_state.mega_input = st.session_state.ui_area

# --- 2. عدادات التوثيق ---
cols = st.columns(5)
m_data = [
    ("سرعة التدفق (ms)", st.session_state.stats["ms"]),
    ("الكتلة الرقمية (Byte)", st.session_state.stats["byte"]),
    ("ثبات التشفير", st.session_state.stats["eff"]),
    ("حمل النواة", st.session_state.stats["cpu"]),
    ("تصنيف السيادة", st.session_state.stats["tier"])
]
for i, (l, v) in enumerate(m_data):
    with cols[i]: st.markdown(f'<div class="metric-box"><div style="color:#D4AF37; font-size:12px;">{l}</div><div class="m-val">{v}</div></div>', unsafe_allow_html=True)

st.divider()

# --- 3. عداد الإبهار اللحظي ---
raw = st.session_state.mega_input
count = 0
if raw:
    t = raw.replace(" ", "").lower()
    if "اس" in t or "^" in t:
        try:
            sep = "اس" if "اس" in t else "^"
            b, p = t.split(sep)
            count = (len(b)-1) + int(p) if b == "10" else len(b) + int(p)
        except: count = len(t)
    else: count = len(t)

st.markdown(f'<div style="text-align:center;"><div class="mega-counter">💎 القوة الحالية: {count:,} خانة</div></div>', unsafe_allow_html=True)

# --- 4. منطقة الإدخال اللانهائي ---
st.text_area("أدخل الكتلة الرقمية أو الصيغة الأسية (لا يوجد حد أقصى):", 
             key="ui_area", on_change=sync_input, height=200, placeholder="ضع هنا ملايين الأصفار أو استخدم صيغة 10اس1000000...")

# --- 5. زر التوثيق النهائي ---
if st.button("🚀 إصدار وثيقة السيادة النهائية"):
    if count > 0:
        with st.spinner("جاري استخلاص النتائج السيادية..."):
            st.session_state.stats.update({
                "ms": f"{random.uniform(100, 300):.2f}",
                "byte": f"{count:,}",
                "cpu": f"{random.randint(1, 5)}%",
                "tier": "TIER S-MAX+" if count > 1000 else "SUPREME"
            })
            st.balloons()
            st.rerun()
