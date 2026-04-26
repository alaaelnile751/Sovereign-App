import streamlit as st
import time
import math

# --- 1. المحرك السيادي ---
def sovereign_engine(data):
    clean_data = str(data).replace(',', '')
    return f"OKORT-{clean_data}-PRIME"

# --- 2. الإعدادات والتنسيق ---
st.set_page_config(page_title="Okort Sovereign Factory", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, label, p { color: #D4AF37 !important; }
    .stMetric { background-color: #1a1a1a; padding: 15px; border-radius: 10px; border: 1px solid #D4AF37; }
    .stButton>button { background-color: #D4AF37; color: black; border-radius: 20px; font-weight: bold; width: 100%; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ OKORT SOVEREIGN FACTORY")
st.subheader("وحدة الترجمة المتبادلة والمعالجة السيادية")

# العدادات
if 'process_time' not in st.session_state: st.session_state.process_time = "0.00"
if 'data_size' not in st.session_state: st.session_state.data_size = "0"

c1, c2, c3 = st.columns(3)
c1.metric("زمن المعالجة (ms)", f"{st.session_state.process_time}", "Live")
c2.metric("حجم المخرجات (Byte)", f"{st.session_state.data_size}", "Verified")
c3.metric("المترجم المتبادل", "نشط", "Bi-Directional")

st.divider()

# --- 3. وحدة الترجمة المتبادلة (الخانتين) ---
col_left, col_right = st.columns([1, 3])

with col_left:
    exp_input = st.text_input("صيغة الأُس (10^6):", key="exp")

with col_right:
    num_input = st.text_input("الرقم الكامل (بالفواصل):", key="num")

# منطق الترجمة المتبادلة
final_val = ""

if exp_input and not num_input: # من الأس إلى الرقم
    try:
        sep = "^" if "^" in exp_input else "اس"
        base, pwr = exp_input.split(sep)
        val = int(base) ** int(pwr)
        final_val = "{:,}".format(val)
        st.info(f"🔄 ترجمة الأُس إلى رقم: {final_val}")
    except: pass

elif num_input and not exp_input: # من الرقم إلى الأس
    try:
        val = int(num_input.replace(',', ''))
        if val > 0 and (math.log10(val) % 1 == 0):
            pwr = int(math.log10(val))
            final_val = num_input
            st.info(f"🔄 ترجمة الرقم إلى أُس: 10^{pwr}")
    except: pass
else:
    final_val = num_input if num_input else exp_input

# --- 4. التفعيل ---
if st.button("تفعيل بروتوكول المعالجة"):
    if final_val:
        start_time = time.time()
        with st.status("🛠️ جاري المعالجة السيادية...", expanded=True) as status:
            time.sleep(0.6)
            output = sovereign_engine(final_val)
            st.session_state.process_time = f"{(time.time() - start_time) * 1000:.2f}"
            st.session_state.data_size = f"{len(output)}"
            status.update(label="✅ اكتملت العملية", state="complete", expanded=False)
        
        st.markdown(f"""
            <div style="border: 2px solid #D4AF37; padding: 25px; border-radius: 15px; background-color: #1a1a1a; text-align: center; margin-top: 20px;">
                <h3 style="color: #D4AF37; margin: 0;">🛡️ المخرج السيادي النهائي</h3>
                <h1 style="color: #ffffff; letter-spacing: 2px;">{output}</h1>
            </div>
        """, unsafe_allow_html=True)
        st.rerun()

st.caption("نظام أوكورت السيادي | وحدة الترجمة المتبادلة - إصدار براءة الاختراع")
