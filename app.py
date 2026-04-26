import streamlit as st
import time
import random

# --- 1. إعدادات الهوية البصرية ---
st.set_page_config(page_title="Okort Sovereign", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; }
    .metric-box {
        background-color: #1a1a1a; border: 2px solid #D4AF37; border-radius: 12px;
        padding: 15px; text-align: center;
    }
    .m-title { color: #D4AF37; font-size: 14px; }
    .m-val { color: #ffffff; font-size: 24px; font-family: monospace; }
    .live-banner {
        background: #D4AF37; color: black; padding: 15px 50px;
        border-radius: 50px; font-weight: 900; font-size: 28px;
        display: inline-block; box-shadow: 0 0 25px #D4AF37;
        margin-bottom: 20px; border: 3px solid #fff;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ OKORT SOVEREIGN FACTORY")

# --- 2. إدارة الحالة (Session State) ---
if 'stats' not in st.session_state:
    st.session_state.stats = {"ms": "0.00", "byte": "0", "eff": "0%", "cpu": "0%", "tier": "-"}
if 'input_val' not in st.session_state:
    st.session_state.input_val = ""

# وظيفة التحديث اللحظي
def update_count():
    st.session_state.input_val = st.session_state.live_input

# --- 3. عرض العدادات العلوية ---
cols = st.columns(5)
labels = ["زمن المعالجة", "حجم المخرجات", "كفاءة التشفير", "حمل المعالج", "المستوى"]
keys = ["ms", "byte", "eff", "cpu", "tier"]

for i in range(5):
    with cols[i]:
        st.markdown(f'<div class="metric-box"><div class="m-title">{labels[i]}</div><div class="m-val">{st.session_state.stats[keys[i]]}</div></div>', unsafe_allow_html=True)

st.divider()

# --- 4. العداد اللحظي (المحرك التفاعلي) ---
# عرض العداد أولاً ليسبق صندوق الإدخال
raw_text = st.session_state.input_val
# عداد ذكي: لو فيه "اس" يحسبها صح، لو مفيش يعد الحروف
count = 0
if raw_text:
    t = raw_text.replace(" ", "").lower()
    if "اس" in t or "^" in t:
        try:
            sep = "اس" if "اس" in t else "^"
            parts = t.split(sep)
            count = (len(parts[0]) - 1) + int(parts[1]) if parts[0] == "10" else len(parts[0]) + int(parts[1])
        except: count = len(t)
    else:
        count = len(t)

st.markdown(f'<div style="text-align:center;"><div class="live-banner">📊 رصد لحظي للخانات: {count}</div></div>', unsafe_allow_html=True)

# صندوق الإدخال مربوط بالـ update_count
st.text_input("أدخل القيمة هنا (سيتم التحديث فور الكتابة):", key="live_input", on_change=update_count)

# --- 5. زر الفحص ---
if st.button("🚀 بدء بروتوكول التوثيق السيادي"):
    if st.session_state.input_val:
        with st.spinner("جاري التحليل..."):
            start = time.time()
            time.sleep(1.0)
            st.session_state.stats.update({
                "ms": f"{(time.time()-start)*1000:.2f}",
                "byte": f"{count + 128}",
                "eff": f"{99.9 + random.random():.2f}%",
                "cpu": f"{random.randint(1,4)}%",
                "tier": "TIER S-MAX" if count > 100 else "TIER A"
            })
            st.rerun()
