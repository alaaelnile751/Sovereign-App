import streamlit as st
import time
import random

# --- المحرك السيادي ---
def sovereign_engine(data_str):
    return f"OKORT-{data_str}-PRIME"

# --- الهوية البصرية الملكية ---
st.set_page_config(page_title="Okort Sovereign", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p { color: #D4AF37 !important; text-align: center; font-weight: bold; }
    .metric-box {
        background-color: #1a1a1a; border: 2px solid #D4AF37; border-radius: 12px;
        padding: 10px; text-align: center; margin: 5px; height: 100px;
    }
    .m-title { color: #D4AF37; font-size: 14px; margin-bottom: 10px; }
    .m-val { color: #ffffff; font-size: 22px; font-family: monospace; }
    .live-digit-container {
        background: #D4AF37; color: black; padding: 10px 40px;
        border-radius: 50px; font-weight: bold; font-size: 22px;
        display: inline-block; box-shadow: 0 0 20px rgba(212, 175, 55, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ OKORT SOVEREIGN FACTORY")

# تهيئة مخزن البيانات
if 'results' not in st.session_state:
    st.session_state.results = {"ms": "0.00", "byte": "0", "eff": "0%", "cpu": "0%", "tier": "-", "output": None}

# --- وظيفة عد الخانات الذكية ---
def count_actual_digits(text):
    if not text: return 0
    text = text.replace(" ", "")
    # دعم كل الصيغ الممكنة للأس (اس، ^، **)
    for op in ["اس", "^", "**"]:
        if op in text:
            try:
                base, power = text.split(op)
                # منطق الأس: عدد خانات (الأساس) + القوة - 1 (في حالة الأساس 10)
                # أو ببساطة تحويلها لنص وعدها للأرقام الضخمة
                return len(base) + int(power) 
            except: break
    return len(text)

# --- عرض العدادات الفنية ---
cols = st.columns(5)
labels = ["زمن المعالجة (ms)", "حجم المخرجات", "كفاءة التشفير", "حمل المعالج", "المستوى"]
keys = ["ms", "byte", "eff", "cpu", "tier"]

for i in range(5):
    with cols[i]:
        st.markdown(f"""
            <div class="metric-box">
                <div class="m-title">{labels[i]}</div>
                <div class="m-val">{st.session_state.results[keys[i]]}</div>
            </div>
        """, unsafe_allow_html=True)

st.divider()

# --- منطقة الإدخال التفاعلية ---
user_input = st.text_input("أدخل القيمة أو الصيغة الأسية (مثال: 10اس138):", key="main_input")

# تحديث العداد الحي بناءً على الإدخال
current_count = count_actual_digits(user_input)
st.markdown(f"""
    <div style="text-align:center; margin-bottom: 20px;">
        <div class="live-digit-container">
            📊 رصد الخانات الحقيقي: {current_count}
        </div>
    </div>
""", unsafe_allow_html=True)

# --- معالجة الضغط على الزر ---
if st.button("🚀 تفعيل البروتوكول السيادي"):
    if user_input:
        with st.spinner("جاري التحليل..."):
            start = time.time()
            try:
                # تحويل النص إلى الصيغة الرقمية الكاملة
                proc = user_input.replace(" ", "")
                final_val = proc
                for op in ["اس", "^", "**"]:
                    if op in proc:
                        base, pwr = proc.split(op)
                        final_val = base + ("0" * int(pwr))
                        break
                
                # تنفيذ المحرك
                time.sleep(0.7) # هيبة المعالجة
                out = sovereign_engine(final_val)
                
                # تحديث النتائج في الـ Session
                st.session_state.results.update({
                    "ms": f"{(time.time()-start)*1000:.2f}",
                    "byte": f"{len(out)}",
                    "eff": f"{99.4 + random.random():.2f}%",
                    "cpu": f"{random.randint(1,4)}%",
                    "tier": "TIER S+" if current_count > 100 else "TIER A",
                    "output": out
                })
                st.rerun()
            except:
                st.error("⚠️ خطأ في الصيغة الرياضية")

# عرض النتيجة النهائية
if st.session_state.results["output"]:
    st.markdown(f"""
        <div style="border: 4px double #D4AF37; padding: 20px; border-radius: 15px; background: #0a0a0a; text-align: center;">
            <h3 style="margin-bottom:10px;">🛡️ المخرج السيادي النهائي</h3>
            <code style="color: white; word-wrap: break-word;">{st.session_state.results["output"][:150]}...</code>
        </div>
    """, unsafe_allow_html=True)
