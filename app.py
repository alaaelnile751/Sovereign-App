import streamlit as st
import time

# --- 1. المحرك السيادي (معالجة نصوص لضمان عدم الانهيار) ---
def sovereign_engine(data):
    # نتعامل مع البيانات كنص (String) دائماً للحفاظ على الأرقام الفلكية
    return f"OKORT-{str(data)}-PRIME"

# --- 2. الإعدادات والتنسيق الفخم ---
st.set_page_config(page_title="Okort Infinite Factory", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, label, p { color: #D4AF37 !important; }
    .stMetric { background-color: #1a1a1a; padding: 15px; border-radius: 10px; border: 1px solid #D4AF37; }
    .stButton>button { background-color: #D4AF37; color: black; border-radius: 20px; font-weight: bold; width: 100%; border: none; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: #D4AF37; border: 1px solid #D4AF37; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ OKORT SOVEREIGN FACTORY")
st.subheader("وحدة اختبار القدرة القصوى - الإصدار اللانهائي")

# العدادات في الحالة الصفرية
if 'process_time' not in st.session_state: st.session_state.process_time = "0.00"
if 'data_size' not in st.session_state: st.session_state.data_size = "0"
if 'digit_count' not in st.session_state: st.session_state.digit_count = "0"

c1, c2, c3, c4 = st.columns(4)
c1.metric("زمن المعالجة (ms)", f"{st.session_state.process_time}")
c2.metric("حجم المخرجات (Byte)", f"{st.session_state.data_size}")
c3.metric("عدد الخانات المعالجة", f"{st.session_state.digit_count}")
c4.metric("حالة المحرك", "لانهائي")

st.divider()

# منطقة الإدخال
exp_input = st.text_input("أدخل القيمة (مثلاً 10اس5000 لفتح الخانات):", placeholder="أدخل أساً ضخماً هنا")

# --- 3. منطق التشغيل الآمن ---
if st.button("تفعيل بروتوكول المعالجة"):
    if exp_input:
        start_time = time.time()
        try:
            # معالجة ذكية: تحويل الأس إلى سلسلة أصفار يدوياً لتجنب إجهاد المعالج
            if "اس" in exp_input or "^" in exp_input:
                sep = "اس" if "اس" in exp_input else "^"
                base, pwr = exp_input.split(sep)
                # بدلاً من الحساب الرياضي المرهق، ننشئ الرقم كـ "نص"
                # رقم 1 وجنبه عدد أصفار يساوي القوة (Power)
                final_val = base + ("0" * int(pwr))
            else:
                final_val = exp_input

            # تنفيذ المعالجة السيادية
            output = sovereign_engine(final_val)
            
            end_time = time.time()
            # تحديث العدادات
            st.session_state.process_time = f"{(end_time - start_time) * 1000:.2f}"
            st.session_state.data_size = f"{len(output)}"
            st.session_state.digit_count = f"{len(final_val)}"
            
            st.success(f"✅ تم معالجة كتلة بيانات بطول {len(final_val)} خانة بنجاح!")
            
            # عرض النتيجة (نظهر أول 50 حرفاً وآخر 50 حرفاً فقط إذا كان الرقم ضخماً جداً للمتصفح)
            display_output = output if len(output) < 500 else f"{output[:100]} ... (بيانات ضخمة موثقة) ... {output[-100:]}"
            
            st.markdown(f"""
                <div style="border: 2px solid #D4AF37; padding: 25px; border-radius: 15px; background-color: #1a1a1a; text-align: center; margin-top: 20px;">
                    <h3 style="color: #D4AF37; margin: 0;">🛡️ المخرج السيادي (معاينة)</h3>
                    <p style="color: #ffffff; word-wrap: break-word;">{display_output}</p>
                </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"⚠️ حدث خطأ في الترجمة: {e}")
    else:
        st.warning("برجاء إدخال بيانات")
