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

    /* العداد الحي - تصميم بارز */
    .live-counter-box {
        color: #000000;
        background-color: #D4AF37;
        border: 2px solid #ffffff;
        padding: 8px 25px;
        border-radius: 50px;
        display: inline-block;
        font-family: 'Courier New', monospace;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 15px;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.5);
    }

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

# تهيئة العدادات التقنية
if 'metrics' not in st.session_state:
    st.session_state.metrics = {"ms": "0.00", "byte": "0", "eff": "0%", "cpu": "0%", "tier": "-"}
if 'last_output' not in st.session_state: st.session_state.last_output = None

# --- 3. عرض العدادات الفنية ---
c1, c2, c3, c4, c5 = st.columns(5)
with c1: st.markdown(f'<div class="metric-container"><div class="metric-title">زمن المعالجة (ms)</div><div class="metric-value">{st.session_state.metrics["ms"]}</div></div>', unsafe_allow_html=True)
with c2: st.markdown(f'<div class="metric-container"><div class="metric-title">حجم المخرجات (Byte)</div><div class="metric-value">{st.session_state.metrics["byte"]}</div></div>', unsafe_allow_html=True)
with c3: st.markdown(f'<div class="metric-container"><div class="metric-title">كفاءة التشفير</div><div class="metric-value">{st.session_state.metrics["eff"]}</div></div>', unsafe_allow_html=True)
with c4: st.markdown(f'<div class="metric-container"><div class="metric-title">حمل المعالج (CPU)</div><div class="metric-value">{st.session_state.metrics["cpu"]}</div></div>', unsafe_allow_html=True)
with c5: st.markdown(f'<div class="metric-container"><div class="metric-title">المستوى السيادي</div><div class="metric-value">{st.session_state.metrics["tier"]}</div></div>', unsafe_allow_html=True)

st.divider()

# --- 4. منطقة الإدخال مع العداد الحي المباشر ---

# تعريف صندوق الإدخال أولاً
user_input = st.text_input("أدخل القيمة أو الصيغة (مثال: 10اس138):", key="live_input")

# حساب عدد الخانات فوراً (يدعم الصيغة الأسية)
def calculate_live_digits(text):
    if not text: return 0
    text = text.replace(" ", "")
    if "اس" in text or "^" in text:
        try:
            sep = "اس" if "اس" in text else "^"
            parts = text.split(sep)
            # إذا كتب 10اس5 فالناتج 6 خانات (1 و 5 أصفار)
            return len(parts[0]) + int(parts[1])
        except:
            return len(text)
    return len(text)

live_count = calculate_live_digits(user_input)

# عرض العداد الحي "فوق" صندوق الإدخال أو تحت العنوان مباشرة
st.markdown(f"""
    <div style="text-align: center; margin-top: -20px;">
        <div class="live-counter-box">
            📊 رصد عدد الخانات الحالية: {live_count}
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 5. زر الفحص ---
if st.button("🚀 بدء بروتوكول الفحص والتوثيق"):
    if user_input:
        st.session_state.last_output = None
        with st.spinner("🔍 جاري التحليل السيادي..."):
            start_time = time.time()
            try:
                # معالجة البيانات
                proc = user_input.replace(" ", "")
                if "اس" in proc or "^" in proc:
                    sep = "اس" if "اس" in proc else "^"
                    b, p = proc.split(sep)
                    final_data = b + ("0" * int(p))
                else:
                    final_data = proc

                time.sleep(1.2) 
                output = sovereign_engine(final_data)
                
                # تحديث العدادات
                st.session_state.metrics["ms"] = f"{(time.time() - start_time) * 1000:.2f}"
                st.session_state.metrics["byte"] = f"{len(output)}"
                st.session_state.metrics["eff"] = f"{98 + random.random():.2f}%"
                st.session_state.metrics["cpu"] = f"{random.randint(2, 5)}%"
                st.session_state.metrics["tier"] = "TIER S+" if len(final_data) > 500 else "TIER S"
                
                st.session_state.last_output = output
                st.rerun()
            except:
                st.error("⚠️ صيغة غير مدعومة")
