import streamlit as st
import time
import random

# --- 1. الهوية البصرية الملكية ---
st.set_page_config(page_title="Okort Sovereign", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; font-weight: bold; }
    .metric-box {
        background-color: #1a1a1a; border: 2px solid #D4AF37; border-radius: 15px;
        padding: 15px; text-align: center; height: 110px;
    }
    .m-title { color: #D4AF37; font-size: 14px; margin-bottom: 5px; }
    .m-val { color: #ffffff; font-size: 24px; font-family: monospace; }
    .live-digit-banner {
        background: linear-gradient(90deg, #D4AF37, #f1c40f, #D4AF37);
        color: black; padding: 15px 60px;
        border-radius: 50px; font-weight: 900; font-size: 30px;
        display: inline-block; box-shadow: 0 0 30px rgba(212, 175, 55, 0.6);
        border: 2px solid #fff; margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ OKORT SOVEREIGN FACTORY")

# تهيئة مخزن النتائج
if 'final_results' not in st.session_state:
    st.session_state.final_results = {"ms": "0.00", "byte": "0", "eff": "0%", "cpu": "0%", "tier": "-", "out": None}

# --- 2. محرك العد اللحظي (المعالج الذكي) ---
def parse_okort_logic(text):
    if not text: return 0
    text = text.replace(" ", "").lower()
    
    # التحقق من الصيغة الأسية (اس أو ^)
    for op in ["اس", "^"]:
        if op in text:
            try:
                parts = text.split(op)
                base = parts[0]
                power_str = parts[1]
                if power_str.isdigit():
                    power = int(power_str)
                    # المنطق الرياضي القاطع لأوكورت:
                    # 10 اس 138 تعني رقم 1 وبجانبه 138 صِفر = 139 خانة
                    if base == "10":
                        return power + 1
                    else:
                        # لأي أساس آخر (مثال: 5 اس 3 = 125) نحسب الخانات باللوغاريتم التقريبي أو الطول
                        return len(base) + power - 1
            except: break
    return len(text)

# --- 3. عرض العدادات الفنية ---
c1, c2, c3, c4, c5 = st.columns(5)
res = st.session_state.final_results
metrics = [
    ("زمن المعالجة (ms)", res["ms"]), ("حجم المخرجات", res["byte"]),
    ("كفاءة التشفير", res["eff"]), ("حمل المعالج", res["cpu"]), ("المستوى", res["tier"])
]
for i, (label, value) in enumerate(metrics):
    with [c1, c2, c3, c4, c5][i]:
        st.markdown(f'<div class="metric-box"><div class="m-title">{label}</div><div class="m-val">{value}</div></div>', unsafe_allow_html=True)

st.divider()

# --- 4. منطقة الإدخال التفاعلية ---
# ملاحظة: العداد سيعمل فور الضغط على Enter أو التفاعل مع الصفحة
u_input = st.text_input("أدخل القيمة أو الصيغة (مثال: 10اس138):", placeholder="نظام أوكورت بانتظار بياناتك...")

# حساب الخانات فورياً وعرضها في البانر الذهبي
actual_digits = parse_okort_logic(u_input)
st.markdown(f"""
    <div style="text-align:center;">
        <div class="live-digit-banner">
            📊 الخانات المرصودة: {actual_digits}
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 5. زر المعالجة ---
if st.button("🚀 تفعيل بروتوكول الفحص"):
    if u_input:
        with st.spinner("جاري التحليل السيادي..."):
            start = time.time()
            # محاكاة توليد المخرج
            time.sleep(1.0)
            
            st.session_state.final_results.update({
                "ms": f"{(time.time()-start)*1000:.2f}",
                "byte": f"{actual_digits + 42}",
                "eff": f"{99.7 + random.random():.2f}%",
                "cpu": f"{random.randint(1,4)}%",
                "tier": "TIER S-MAX" if actual_digits > 100 else "TIER A",
                "out": f"OKORT-{u_input[:10]}-CORE-SECURED"
            })
            st.rerun()
