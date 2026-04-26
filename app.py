import streamlit as st
import time

# --- 1. المحرك السيادي ---
def sovereign_engine(data):
    return f"OKORT-{str(data).replace(',', '')}-PRIME"

# --- 2. التصميم الملكي ---
st.set_page_config(page_title="Okort Sovereign Factory", page_icon="🛡️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, label, p { color: #D4AF37 !important; }
    .stMetric { background-color: #1a1a1a; padding: 15px; border-radius: 10px; border: 1px solid #D4AF37; }
    .stButton>button { background-color: #D4AF37; color: black; border-radius: 20px; font-weight: bold; width: 100%; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: #D4AF37; border: 1px solid #D4AF37; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ OKORT SOVEREIGN FACTORY")
st.subheader("وحدة الترجمة الرياضية والمعالجة السيادية")

# العدادات
if 'process_time' not in st.session_state: st.session_state.process_time = "0.00"
if 'data_size' not in st.session_state: st.session_state.data_size = "0"

c1, c2, c3 = st.columns(3)
c1.metric("زمن المعالجة (ms)", f"{st.session_state.process_time}", "Live")
c2.metric("حجم المخرجات (Byte)", f"{st.session_state.data_size}", "Verified")
c3.metric("حالة المترجم", "نشط", "Ready")

# --- 3. خانة البحث والمترجم الذكي ---
raw_input = st.text_input("أدخل القيمة الأولية (يدعم الصيغة الأسية مثل 10^3):", placeholder="مثال: 10^6")

final_value = raw_input
if raw_input and "^" in raw_input:
    try:
        base, exp = raw_input.split("^")
        computed_val = int(base) ** int(exp)
        final_value = "{:,}".format(computed_val) # إضافة الفواصل
        st.success(f"✅ المترجم الرياضي: تم تحويل القيمة إلى {final_value}")
    except:
        st.error("⚠️ صيغة رياضية غير صحيحة")

# --- 4. التفعيل ---
if st.button("تفعيل بروتوكول المعالجة"):
    if raw_input:
        start_time = time.time()
        with st.status("🛠️ جاري التحليل والمعالجة السيادية...", expanded=True) as status:
            time.sleep(0.6)
            output = sovereign_engine(final_value)
            end_time = time.time()
            
            st.session_state.process_time = f"{(end_time - start_time) * 1000:.2f}"
            st.session_state.data_size = f"{len(output)}"
            status.update(label="✅ تمت العملية بنجاح", state="complete", expanded=False)
        
        st.markdown(f"""
            <div style="border: 2px solid #D4AF37; padding: 25px; border-radius: 15px; background-color: #1a1a1a; text-align: center; margin-top: 20px;">
                <h3 style="color: #D4AF37; margin: 0;">🛡️ المخرج السيادي النهائي</h3>
                <h1 style="color: #ffffff; letter-spacing: 2px;">{output}</h1>
                <p style="color: #D4AF37; font-size: 0.8em; margin-top: 10px;">القيمة المعالجة: {final_value}</p>
            </div>
        """, unsafe_allow_html=True)
        st.rerun()
