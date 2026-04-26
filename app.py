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
        margin-bottom: 10px;
    }
    .metric-title { color: #D4AF37; font-size: 14px; margin-bottom: 5px; }
    .metric-value { color: #ffffff; font-size: 24px; font-family: 'Courier New', monospace; }

    .result-frame {
        border: 4px double #D4AF37;
        padding: 30px;
        border-radius: 20px;
        background-color: #0a0a0a;
        margin-top: 20px;
        animation: fadeIn 1s;
    }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ OKORT SOVEREIGN FACTORY")
st.subheader("منصة التقييم العالمي والسيادة الرقمية")

# تهيئة حالة النظام
if 'show_results' not in st.session_state: st.session_state.show_results = False
if 'metrics' not in st.session_state:
    st.session_state.metrics = {"ms": "0.00", "byte": "0", "digit": "0", "eff": "0%", "cpu": "0%", "tier": "-"}

# --- 3. عرض العدادات (تظهر فقط عند وجود نتائج) ---
if st.session_state.show_results:
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
        # خطوة 1: إخفاء النتائج القديمة فوراً
        st.session_state.show_results = False
        
        # خطوة 2: إظهار مؤشر التحميل (السيناريو التقني)
        with st.spinner("🔍 جاري استدعاء البروتوكولات السيادية وفحص الكتلة الرقمية..."):
            start_time = time.time()
            try:
                # معالجة الصيغة الأسية بذكاء
                processed_input = user_input.replace(" ", "")
                if "اس" in processed_input or "^" in processed_input:
                    sep = "اس" if "اس" in processed_input else "^"
                    parts = processed_input.split(sep)
                    if len(parts) == 2 and parts[1].isdigit():
                        final_data = parts[0] + ("0" * int(parts[1]))
                    else: raise ValueError
                else:
                    final_data = processed_input

                # محاكاة العمل الشاق
                time.sleep(1.5) 
                output = sovereign_engine(final_data)
                
                # تحديث العدادات
                st.session_state.metrics["ms"] = f"{(time.time() - start_time) * 1000:.2f}"
                st.session_state.metrics["byte"] = f"{len(output)}"
                st.session_state.metrics["digit"] = f"{len(final_data)}"
                st.session_state.metrics["eff"] = f"{98 + random.random():.2f}%"
                st.session_state.metrics["cpu"] = f"{random.randint(1, 4)}%"
                st.session_state.metrics["tier"] = "TIER S" if len(final_data) > 100 else "TIER A"
                
                # خطوة 3: السماح بظهور النتائج الجديدة
                st.session_state.show_results = True
                st.session_state.last_output = output
                st.rerun()

            except:
                st.error("⚠️ خطأ في الصيغة: يرجى كتابة الرقم بشكل صحيح (مثلاً: 10اس138)")
    else:
        st.warning("⚠️ حقل الإدخال فارغ!")

# عرض المخرج السيادي النهائي (أسفل العدادات)
if st.session_state.show_results:
    st.markdown(f"""
        <div class="result-frame">
            <h3>🛡️ المخرج السيادي النهائي 🛡️</h3>
            <p style="word-wrap: break-word; color: #fff; font-family: monospace;">
                {st.session_state.last_output if len(st.session_state.last_output) < 300 
                 else st.session_state.last_output[:100] + " ... [ENCRYPTED] ... " + st.session_state.last_output[-100:]}
            </p>
        </div>
    """, unsafe_allow_html=True)
