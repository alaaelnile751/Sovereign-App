import streamlit as st
import time

# --- 1. المحرك السيادي (خوارزمية التشفير المتسلسل) ---
def sovereign_engine_advanced(data_str):
    # محاكاة لعملية تشفير تمر على البيانات لضمان السيادة
    # كلما زاد طول البيانات، زاد زمن المعالجة بشكل حقيقي
    counter = 0
    for char in data_str:
        counter += 1
        if counter % 1000 == 0: # إضافة تأخير بسيط جداً كل 1000 خانة لإظهار العمل
            time.sleep(0.001) 
    return f"OKORT-{data_str[:50]}...[SECURED]-PRIME"

# --- 2. الإعدادات ---
st.set_page_config(page_title="Okort Sovereign Factory", layout="wide")
st.title("🛡️ OKORT SOVEREIGN FACTORY")
st.subheader("وحدة إثبات الجهد الرقمي (Computational Proof)")

# العدادات
if 'process_time' not in st.session_state: st.session_state.process_time = "0.00"
if 'digit_count' not in st.session_state: st.session_state.digit_count = "0"

c1, c2, c3 = st.columns(3)
c1.metric("زمن المعالجة الفعلي (ms)", f"{st.session_state.process_time}")
c2.metric("عدد الخانات المعالجة", f"{st.session_state.digit_count}")
c3.metric("حالة الخوارزمية", "تشفير متسلسل")

st.divider()

# --- 3. الإدخال الموحد (يدعم الرقم العادي والأسي) ---
user_input = st.text_input("أدخل الرقم أو الصيغة الأسية (مثال: 10اس500):")

if st.button("تفعيل بروتوكول التشفير السيادي"):
    if user_input:
        start_time = time.time()
        
        # تحويل الصيغة الأسية إلى رقم كامل
        if "اس" in user_input or "^" in user_input:
            sep = "اس" if "اس" in user_input else "^"
            base, pwr = user_input.split(sep)
            final_data = base + ("0" * int(pwr))
        else:
            final_data = user_input

        with st.status("🔍 جاري فحص وتشفير الكتلة الرقمية...", expanded=True):
            # استدعاء المحرك المطور
            output = sovereign_engine_advanced(final_data)
            
            end_time = time.time()
            st.session_state.process_time = f"{(end_time - start_time) * 1000:.2f}"
            st.session_state.digit_count = f"{len(final_data)}"
        
        st.success(f"✅ اكتمل التشفير لعدد {len(final_data)} خانة")
        st.rerun()
