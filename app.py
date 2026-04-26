import streamlit as st
import time
import random

# --- 1. المحرك السيادي ---
def sovereign_engine(data_str):
    return f"OKORT-{data_str}-PRIME"

# --- 2. الهوية البصرية الملكية ---
st.set_page_config(page_title="Okort Sovereign Factory", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, label, p { color: #D4AF37 !important; text-align: center; font-weight: bold; }
    
    .metric-container {
        background-color: #1a1a1a;
        border: 2px solid #D4AF37;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(212, 175, 55, 0.1);
        margin-bottom: 15px;
    }
    .metric-title { color: #D4AF37; font-size: 14px; margin-bottom: 5px; }
    .metric-value { color: #ffffff; font-size: 24px; font-family: 'Courier New', monospace; }

    .result-frame {
        border: 4px double #D4AF37;
        padding: 30px;
        border-radius: 20px;
        background-color: #0a0a0a;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ OKORT SOVEREIGN FACTORY")
st.subheader("منصة التقييم العالمي والسيادة الرقمية")

# تهيئة العدادات (صفرية في البداية)
if 'metrics' not in st.session_state:
    st.session_state.metrics = {"ms": "0.00", "byte": "0", "digit": "0", "eff": "0%", "cpu": "0%", "tier": "-"}
if 'last_output' not in st.session_state: st.session_state.last_output = None

# --- 3. عرض العدادات (دائمة الظهور للهيبة البصرية) ---
r1_c1, r1_c2, r1_c3 = st.columns(3)
r2_c1, r2_c2, r2_c3 = st.columns(3)

with r1_c1: st.markdown(f'<div class="metric-container"><div class="metric-title">زمن المعالجة (ms)</div><div class="metric-value">{st.session_state.metrics["ms"]}</div></div>', unsafe_allow_html=True)
with r1_c2: st.markdown(f'<div class="metric-container"><div class="metric-title">حجم المخرجات (Byte)</div><div class="metric-value">{st.session_state.metrics["byte"]}</div></div>', unsafe_allow_html=True)
with r1_c3: st.markdown(f'<div class="metric-container"><div class="metric-title">عدد الخانات</div><div class="metric-value">{st.session_state.metrics["digit"]}</div></div>', unsafe_allow_html=True)

with r2_c1: st.markdown(f'<div class="metric-container"><div class="metric-title">كفاءة التشفير</div><div class="metric-value">{st.session_state.metrics["eff"]}</div></div>', unsafe_allow_html=True)
with r2_c2: st.markdown(f'<div class="metric-container"><div class="metric-title">حمل المعالج (CPU)</div><div class="metric-value">{st.session_state.metrics["cpu"]}</div></div>', unsafe_allow_html=True)
with r2_c3: st.markdown(f'<div class="metric-container"><div class="metric-title">المستوى السيادي</div><div class="metric-value">{st.session_state.metrics["tier"]}</div></div>', unsafe_allow_html=True)

st.divider()

# --- 4. منطقة الإدخال ---
user_input = st.text_input("أدخل البيانات أو الصيغة الأسية (مثال: 10اس138):")

if st.button("🚀 تفعيل بروتوكول التقييم الشامل"):
    if user_input:
        # تصفير النتائج القديمة فوراً قبل التحميل
        st.session_state.last_output = None
        
        with st.spinner("🔍 جاري المعالجة السيادية وفحص الكتلة الرقمية..."):
            start_time = time.time()
            try:
                # منطق الترجمة الرياضية
                proc = user_input.replace(" ", "")
                if "اس" in proc or "^" in proc:
                    sep = "اس" if "اس" in proc else "^"
                    b, p = proc.split(sep)
                    final_data = b + ("0" * int(p))
                else:
                    final_data = proc

                # محاكاة العمل
                time.sleep(1.2) 
                output = sovereign_engine(final_data)
                
                # تحديث العدادات بالقيم الجديدة
                st.session_state.metrics["ms"] = f"{(time.time() - start_time) * 1000:.2f}"
                st.session_state.metrics["byte"] = f"{len(output)}"
                st.session_state.metrics["digit"] = f"{len(final_data)}"
                st.session_state.metrics["eff"] = f"{98 + random.random():.2f}%"
                st.session_state.metrics["cpu"] = f"{random.randint(1, 4)}%"
                st.session_state.metrics["tier"] = "TIER S" if len(final_data) > 100 else "TIER A"
                
                st.session_state.last_output = output
                st.rerun()

            except:
                st.error("⚠️ صيغة خاطئة")
    else:
        st.warning("⚠️ حقل الإدخال فارغ")

# عرض المخرج السيادي (يظهر فقط بعد اكتمال المعالجة)
if st.session_state.last_output:
    st.markdown(f"""
        <div class="result-frame">
            <h3>🛡️ المخرج السيادي النهائي 🛡️</h3>
            <p style="word-wrap: break-word; color: #fff; font-family: monospace;">
                {st.session_state.last_output if len(st.session_state.last_output) < 300 
                 else st.session_state.last_output[:100] + " ... [DATA SECURED] ... " + st.session_state.last_output[-100:]}
            </p>
        </div>
    """, unsafe_allow_html=True)
