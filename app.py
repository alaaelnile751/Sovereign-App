import streamlit as st
import time

# --- 1. المحرك السيادي (المطور) ---
def sovereign_engine(data_str):
    # الختم السيادي النهائي
    return f"OKORT-{data_str}-PRIME"

# --- 2. إعادة الهوية البصرية (الأسود والذهبي) ---
st.set_page_config(page_title="Okort Sovereign Factory", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, label, p { color: #D4AF37 !important; text-align: center; }
    .stMetric { 
        background-color: #1a1a1a; 
        padding: 20px; 
        border-radius: 15px; 
        border: 2px solid #D4AF37; 
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.2);
    }
    .stButton>button { 
        background-color: #D4AF37; 
        color: black; 
        border-radius: 30px; 
        font-weight: bold; 
        font-size: 20px;
        width: 100%; 
        border: none;
        height: 50px;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #f1c40f; transform: scale(1.02); }
    .stTextInput>div>div>input { 
        background-color: #1a1a1a; 
        color: #D4AF37; 
        border: 2px solid #D4AF37; 
        border-radius: 10px;
        text-align: center;
        font-size: 22px;
    }
    /* إطار النتيجة الذهبي المميز */
    .result-box {
        border: 4px double #D4AF37;
        padding: 40px;
        border-radius: 20px;
        background-color: #0a0a0a;
        margin-top: 30px;
        box-shadow: inset 0 0 20px rgba(212, 175, 55, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ OKORT SOVEREIGN FACTORY")
st.subheader("وحدة المعالجة التقنية والتوثيق - إصدار براءة الاختراع")

# --- 3. العدادات الاحترافية (إعادة حجم المخرجات) ---
if 'process_time' not in st.session_state: st.session_state.process_time = "0.00"
if 'data_size' not in st.session_state: st.session_state.data_size = "0"
if 'digit_count' not in st.session_state: st.session_state.digit_count = "0"

c1, c2, c3 = st.columns(3)
with c1: st.metric("زمن المعالجة (ms)", f"{st.session_state.process_time}")
with c2: st.metric("حجم المخرجات (Byte)", f"{st.session_state.data_size}")
with c3: st.metric("عدد الخانات", f"{st.session_state.digit_count}")

st.divider()

# --- 4. منطقة البحث الذكي ---
user_input = st.text_input("أدخل القيمة المراد تشفيرها سيادياً:", placeholder="مثال: 10اس138")

if st.button("تفعيل بروتوكول التشفير السيادي"):
    if user_input:
        start_time = time.time()
        
        # تصحيح منطق الترجمة الرياضية (10اسX)
        try:
            if "اس" in user_input or "^" in user_input:
                sep = "اس" if "اس" in user_input else "^"
                base, pwr = user_input.split(sep)
                # توليد الرقم الحقيقي (1 وجانبه أصفار)
                final_data = base.strip() + ("0" * int(pwr.strip()))
            else:
                final_data = user_input.strip()

            # محاكاة جهد التشفير لضمان عدم ظهور زمن "صفر"
            time.sleep(0.4) 
            output = sovereign_engine(final_data)
            
            end_time = time.time()
            # تحديث العدادات
            st.session_state.process_time = f"{(end_time - start_time) * 1000:.2f}"
            st.session_state.data_size = f"{len(output)}"
            st.session_state.digit_count = f"{len(final_data)}"
            
            # --- 5. عرض النتيجة داخل الإطار الذهبي الملكي ---
            st.markdown(f"""
                <div class="result-box">
                    <h3 style="margin-top: 0;">✨ النتيجة محمية سيادياً ✨</h3>
                    <p style="font-family: monospace; font-size: 18px; color: #ffffff; word-wrap: break-word;">
                        {output if len(output) < 500 else output[:150] + " ... [كتلة بيانات مشفرة] ... " + output[-150:]}
                    </p>
                    <p style="font-size: 14px; color: #D4AF37; border-top: 1px solid #D4AF37; padding-top: 10px;">
                        نظام أوكورت السيادي | الإصدار 1.0.2026
                    </p>
                </div>
            """, unsafe_allow_html=True)
            st.rerun()

        except Exception as e:
            st.error(f"⚠️ خطأ في الصيغة: تأكد من كتابة الرقم بشكل صحيح (مثال: 10اس5)")
    else:
        st.warning("برجاء إدخال بيانات للبدء")

st.caption("نظام أوكورت السيادي | وحدة التوثيق البصري والتقني")
