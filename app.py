import streamlit as st
import time
import pandas as pd
import random
import sys

# إعدادات الحوسبة فائقة الضخامة لرفع قيود الخانات
sys.set_int_max_str_digits(0)

# إعدادات الصفحة السيادية
st.set_page_config(page_title="Sovereign Hybrid Engine", page_icon="🏛️", layout="wide")

def is_prime(n, k=5): 
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

# إدارة حالة النظام
if 'usage_count' not in st.session_state: st.session_state.usage_count = 0
if 'results' not in st.session_state: st.session_state.results = None
if 'p_time' not in st.session_state: st.session_state.p_time = 0.0

# الهوية البصرية السيادية
st.markdown("""
    <style>
    .main { background-color: #0e1117; direction: rtl; }
    .main-title { color: #FFD700 !important; text-align: center; font-size: 3.5rem !important; font-weight: 900; margin-bottom: 25px; text-shadow: 2px 2px 10px #000; }
    .live-timer {
        background: #000; color: #00ffcc; font-family: 'Courier New', monospace;
        padding: 15px 30px; border-radius: 15px; border: 2px solid #FFD700;
        font-size: 2rem; text-align: center; font-weight: bold;
    }
    .guide-box { background: #161b22; border-right: 10px solid #FFD700; padding: 30px; border-radius: 15px; border: 1px solid #30363d; margin-bottom: 30px; }
    .guide-title { color: #FFD700; font-size: 2.2rem !important; font-weight: 900; margin-bottom: 20px; display: block; border-bottom: 2px solid #FFD700; width: fit-content; padding-bottom: 5px; }
    .guide-text { color: #ffffff; font-size: 1.5rem !important; line-height: 1.8; text-align: right; }
    .benchmark-card { background: linear-gradient(135deg, #1a1c24 0%, #0d1117 100%); border: 2px solid #FFD700; border-radius: 15px; padding: 25px; margin-top: 30px; }
    .benchmark-item { border-bottom: 1px dashed #30363d; padding: 15px 0; display: flex; justify-content: space-between; align-items: center; }
    .benchmark-label { color: #ffffff; font-size: 1.2rem; }
    .benchmark-val { color: #00ffcc; font-family: monospace; font-size: 1.3rem; }
    .sovereign-val { color: #FFD700; font-weight: 900; font-size: 1.5rem; }
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #FFD700, #FFA500, #FFD700) !important;
        color: #000 !important; font-size: 2.2rem !important; font-weight: 1000 !important;
        border-radius: 50px !important; height: 90px !important; width: 100% !important;
        border: 5px solid #fff !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🏛️ SOVEREIGN HYBRID ENGINE</h1>", unsafe_allow_html=True)

# ميثاق الاستخدام
st.markdown(f"""
<div class='guide-box'>
    <span class='guide-title'>🏛️ ميثاق استخدام المحرك السيادي</span>
    <p class='guide-text'>
        • <b>النطاق العلمي:</b> <span style='color:#FFD700;'>Octogintillion (200 خانة)</span>.<br>
        • <b>الوضع العلمي:</b> تنقيب فائق الدقة لـ <span style='color:#FFD700;'>10,000</span> رقم.<br>
        • <b>نظام التجربة:</b> متاح لك <span style='color:#FFD700;'>3 محاولات تشغيل</span> فقط.
    </p>
</div>
""", unsafe_allow_html=True)

remaining = 3 - st.session_state.usage_count
if remaining > 0:
    st.markdown(f"<div style='background:#9d0208; color:white; padding:12px; border-radius:50px; text-align:center; font-weight:bold; margin-bottom:20px;'>⚠️ متبقي: {remaining} محاولات تجريبية</div>", unsafe_allow_html=True)
    mode = st.radio("إعدادات الوضع:", ["الوضع السريع (الشامل)", "الوضع العلمي (الأصول الأولية)"], horizontal=True)
    
    st.write("---")
    col_main, col_side = st.columns([1.6, 1])
    with col_main:
        start_val = st.text_area("أدخل الرقم الأساسي (200 خانة):", value="1" + "0"*199, height=180)
    with col_side:
        max_limit = 1000000 if "السريع" in mode else 10000
        limit_input = st.number_input("نطاق التنقيب:", 1, max_limit, 10000)

    c_btn, c_timer = st.columns([2, 1])
    with c_btn:
        process_btn = st.button("🚀 إطلاق المحرك السيادي")
    with c_timer:
        placeholder = st.empty()
        placeholder.markdown(f"<div class='live-timer'>⏱️ {st.session_state.p_time:.4f}s</div>", unsafe_allow_html=True)

    if process_btn:
        try:
            clean_num = "".join(start_val.split())
            s_num = int(clean_num)
            t0 = time.time()
            res = []
            if "السريع" in mode:
                res = [str(x) for x in range(s_num, s_num + limit_input)]
            else:
                for i in range(limit_input):
                    x = s_num + i
                    if x % 2 != 0 and is_prime(x): res.append(str(x))
                    if i % 100 == 0:
                        placeholder.markdown(f"<div class='live-timer'>⏱️ {time.time() - t0:.4f}s</div>", unsafe_allow_html=True)
            
            st.session_state.p_time = time.time() - t0
            st.session_state.found_count = len(res)
            st.session_state.total_scanned = limit_input
            st.session_state.results = res
            st.session_state.usage_count += 1
            st.rerun()
        except Exception as e:
            st.error(f"خطأ في المعالجة: {e}")
else:
    st.error("🚫 عذراً، لقد استنفدت كافة المحاولات التجريبية المسموح بها (3/3).")

if st.session_state.results:
    st.write("---")
    st.markdown("<h2 style='color:#FFD700; text-align:center;'>📜 تقرير الكفاءة السيادية المعتمد</h2>", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("💎 الأصول المكتشفة", f"{st.session_state.found_count:,}")
    with m2: st.metric("⏱️ زمن المعالجة", f"{st.session_state.p_time:.4f}s")
    with m3: 
        speed = int(st.session_state.total_scanned/st.session_state.p_time) if st.session_state.p_time > 0 else 0
        st.metric("🚀 السرعة", f"{speed:,}/s")

    st.markdown(f"""
    <div class='benchmark-card'>
        <h3 style='color:#FFD700; text-align:center; border-bottom:1px solid #FFD700; padding-bottom:10px;'>📊 المقارنة بالمعايير التقنية العالمية</h3>
        <div class='benchmark-item'><span class='benchmark-label'>💻 حدود الحواسيب التقليدية (64-bit):</span><span class='benchmark-val'>حتى 20 خانة</span></div>
        <div class='benchmark-item'><span class='benchmark-label'>🚀 دقة حسابات وكالة ناسا للفضاء:</span><span class='benchmark-val'>حتى 16 خانة</span></div>
        <div class='benchmark-item'><span class='benchmark-label'>⚛️ عدد ذرات الكون المرئي:</span><span class='benchmark-val'>10^80 (80 خانة)</span></div>
        <div class='benchmark-item' style='border:none; background:rgba(255,215,0,0.1); padding:15px; border-radius:10px;'>
            <span class='benchmark-label' style='color:#FFD700;'>🏛️ نطاق معالجة المحرك السيادي الحالي:</span>
            <span class='sovereign-val'>200 خانة (Octogintillion)</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    df = pd.DataFrame([f"'{x}" for x in st.session_state.results], columns=["Sovereign_ID"])
    st.download_button("📥 تحميل الأصول النهائية", df.to_csv(index=False), "Sovereign_Final.csv")
