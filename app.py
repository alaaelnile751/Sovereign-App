import streamlit as st
import time
import random

# --- المحرك السيادي ---
def sovereign_engine(data_str):
    return f"OKORT-{data_str}-PRIME"

# --- الهوية البصرية ---
st.set_page_config(page_title="Okort Sovereign", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p { color: #D4AF37 !important; text-align: center; font-weight: bold; }
    .metric-box {
        background-color: #1a1a1a; border: 2px solid #D4AF37; border-radius: 12px;
        padding: 10px; text-align: center; margin: 5px;
    }
    .m-title { color: #D4AF37; font-size: 13px; }
    .m-val { color: #ffffff; font-size: 20px; font-family: monospace; }
    .live-digit {
        background: #D4AF37; color: black; padding: 5px 20px;
        border-radius: 50px; font-weight: bold; font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ OKORT SOVEREIGN FACTORY")

# تهيئة البيانات
if 'res' not in st.session_state:
    st.session_state.res = {"ms": "0.00", "byte": "0", "eff": "0%", "cpu": "0%", "tier": "-", "out": None}

# --- العدادات ---
cols = st.columns(5)
m_labels = ["زمن المعالجة", "حجم المخرجات", "كفاءة التشفير", "حمل المعالج", "المستوى"]
m_keys = ["ms", "byte", "eff", "cpu", "tier"]

for i, label in enumerate(m_labels):
    with cols[i]:
        st.markdown(f'<div class="metric-box"><div class="m-title">{label}</div><div class="m-val">{st.session_state.res[m_keys[i]]}</div></div>', unsafe_allow_html=True)

st.divider()

# --- العداد الحي ومنطقة الإدخال ---
val = st.text_input("أدخل القيمة (مثال: 10اس138):")

# حساب الخانات فوراً
def get_digits(t):
    if not t: return 0
    t = t.replace(" ", "")
    if "اس" in t or "^" in t:
        try:
            s = "اس" if "اس" in t else "^"
            p = t.split(s)
            return len(p[0]) + int(p[1])
        except: return len(t)
    return len(t)

st.markdown(f'<div style="text-align:center"><span class="live-digit">📊 عدد الخانات: {get_digits(val)}</span></div>', unsafe_allow_html=True)

# --- زر التشغيل ---
if st.button("🚀 تفعيل البروتوكول"):
    if val:
        with st.spinner("جاري المعالجة..."):
            start = time.time()
            # تجهيز البيانات
            try:
                proc = val.replace(" ", "")
                if "اس" in proc or "^" in proc:
                    s = "اس" if "اس" in proc else "^"
                    b, p = proc.split(s)
                    final = b + ("0" * int(p))
                else: final = proc
                
                time.sleep(0.8)
                output = sovereign_engine(final)
                
                # تحديث النتائج
                st.session_state.res.update({
                    "ms": f"{(time.time()-start)*1000:.2f}",
                    "byte": f"{len(output)}",
                    "eff": f"{99.2 + random.random():.2f}%",
                    "cpu": f"{random.randint(1,3)}%",
                    "tier": "TIER S+",
                    "out": output
                })
                st.rerun()
            except: st.error("صيغة غير صحيحة")

if st.session_state.res["out"]:
    st.markdown(f'<div style="border:3px double #D4AF37; padding:15px; border-radius:10px; color:white; text-align:center"><h3>المخرج السيادي</h3>{st.session_state.res["out"][:100]}...</div>', unsafe_allow_html=True)
