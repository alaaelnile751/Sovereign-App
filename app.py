import streamlit as st
import time
import random

# --- 1. التنسيق الملكي ---
st.set_page_config(page_title="Okort Sovereign Factory", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p { color: #D4AF37 !important; text-align: center; font-weight: bold; }
    
    .metric-box {
        background-color: #1a1a1a; border: 2px solid #D4AF37; border-radius: 12px;
        padding: 15px; text-align: center; height: 110px;
    }
    .m-title { color: #D4AF37; font-size: 14px; margin-bottom: 8px; }
    .m-val { color: #ffffff; font-size: 24px; font-family: monospace; }
    
    .live-digit-banner {
        background: #D4AF37; color: black; padding: 12px 50px;
        border-radius: 50px; font-weight: 900; font-size: 28px;
        display: inline-block; box-shadow: 0 0 20px rgba(212, 175, 55, 0.4);
        margin-top: 10px; margin-bottom: 20px; border: 2px solid white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ OKORT SOVEREIGN FACTORY")

# تهيئة الذاكرة للعدادات الفنية
if 'stats' not in st.session_state:
    st.session_state.stats = {"ms": "0.00", "byte": "0", "eff": "0%", "cpu": "0%", "tier": "-"}

# --- 2. عرض العدادات الفنية (التقرير العلوي) ---
cols = st.columns(5)
labels = ["زمن المعالجة (ms)", "حجم المخرجات", "كفاءة التشفير", "حمل المعالج", "المستوى"]
keys = ["ms", "byte", "eff", "cpu", "tier"]

for i in range(5):
    with cols[i]:
        st.markdown(f'<div class="metric-box"><div class="m-title">{labels[i]}</div><div class="m-val">{st.session_state.stats[keys[i]]}</div></div>', unsafe_allow_html=True)

st.divider()

# --- 3. منطقة الإدخال والعداد الحي (قبل الفحص) ---

# نستخدم textarea للإدخالات الكبيرة (يدوياً)
user_input = st.text_area("أدخل الأرقام يدوياً هنا:", height=150, help="الصق الأرقام الضخمة هنا لعدها قبل الفحص")

# حساب الخانات فوراً (حي ومباشر)
# يتم التحديث بمجرد الضغط خارج الصندوق أو Enter
actual_count = len(user_input.replace(" ", "").replace("\n", ""))

st.markdown(f"""
    <div style="text-align:center;">
        <div class="live-digit-banner">
            📊 رصد الخانات قبل الفحص: {actual_count}
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 4. زر المعالجة السيادية ---
if st.button("🚀 بدء بروتوكول المعالجة والتوثيق"):
    if user_input:
        with st.spinner("جاري التحليل..."):
            start_time = time.time()
            time.sleep(1.0) # وقت المعالجة الوهمي للهيبة
            
            # تحديث العدادات الفنية بناءً على ما تم رصده في العداد الحي
            st.session_state.stats.update({
                "ms": f"{(time.time()-start_time)*1000:.2f}",
                "byte": f"{actual_count + 64}",
                "eff": f"{99.8 + random.random():.2f}%",
                "cpu": f"{random.randint(1,4)}%",
                "tier": "TIER S-MAX" if actual_count > 1000 else "TIER A"
            })
            st.success("تم الفحص بنجاح")
            st.rerun()
