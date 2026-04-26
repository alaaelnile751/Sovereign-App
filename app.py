import streamlit as st
import time
import math
import sys

# زيادة حد الحروف المسموح بها في النظام لتجنب الانهيار في الأرقام الضخمة
sys.set_recursionlimit(2000)

def sovereign_engine(data):
    clean_data = str(data).replace(',', '')
    return f"OKORT-{clean_data}-PRIME"

st.set_page_config(page_title="Okort Infinite Factory", layout="wide")
st.title("🛡️ OKORT SOVEREIGN FACTORY")
st.subheader("وحدة اختبار القدرة القصوى (Maximum Capacity Test)")

# العدادات
if 'process_time' not in st.session_state: st.session_state.process_time = "0.00"
if 'data_size' not in st.session_state: st.session_state.data_size = "0"
if 'digit_count' not in st.session_state: st.session_state.digit_count = "0"

c1, c2, c3, c4 = st.columns(4)
c1.metric("زمن المعالجة (ms)", f"{st.session_state.process_time}")
c2.metric("حجم المخرجات (Byte)", f"{st.session_state.data_size}")
c3.metric("عدد الخانات", f"{st.session_state.digit_count}")
c4.metric("حالة المحرك", "مفتوح")

st.divider()

# منطقة الإدخال
exp_input = st.text_input("اختبار الأُس العالي (مثلاً: 10اس1000):", placeholder="أدخل أساً ضخماً هنا")

if st.button("تفعيل بروتوكول المعالجة القصوى"):
    if exp_input:
        start_time = time.time()
        try:
            # معالجة ذكية للأرقام الضخمة جداً
            if "اس" in exp_input or "^" in exp_input:
                sep = "اس" if "اس" in exp_input else "^"
                base, pwr = exp_input.split(sep)
                # حساب الرقم الضخم
                computed_val = int(base) ** int(pwr)
                final_val = str(computed_val)
            else:
                final_val = exp_input

            # تنفيذ المعالجة السيادية
            output = sovereign_engine(final_val)
            
            # حساب النتائج
            end_time = time.time()
            st.session_state.process_time = f"{(end_time - start_time) * 1000:.2f}"
            st.session_state.data_size = f"{len(output)}"
            st.session_state.digit_count = f"{len(final_val)}"
            
            st.success(f"✅ تم معالجة رقم بطول {len(final_val)} خانة بنجاح!")
            st.rerun()
        except Exception as e:
            st.error(f"⚠️ تجاوزت القدرة المسموحة للمتصفح: {e}")

st.caption("نظام أوكورت السيادي | وحدة اختبار الإجهاد الرقمي")
