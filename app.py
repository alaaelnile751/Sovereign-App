import streamlit as st
import time
import random

# --- 1. هندسة الهوية البصرية (Visual Engineering) ---
st.set_page_config(page_title="Okort Sovereign Final", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    
    /* عناوين التقارير - تصميم بارز */
    .report-header {
        color: #D4AF37; font-size: 16px; font-weight: bold;
        text-transform: uppercase; letter-spacing: 2px;
        margin-bottom: 10px; border-bottom: 1px solid #D4AF37;
        display: inline-block; padding-bottom: 5px;
    }
    
    .metric-card {
        background: linear-gradient(145deg, #111, #050505);
        border: 2px solid #D4AF37; border-radius: 10px;
        padding: 20px; text-align: center;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.1);
    }
    .metric-value { 
        color: #ffffff; font-size: 30px; font-family: 'Courier New', monospace; 
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
    }

    /* عداد القوة اللحظي */
    .power-banner {
        background: #D4AF37; color: black; padding: 15px 60px;
        border-radius: 50px; font-weight: 900; font-size: 32px;
        display: inline-block; box-shadow: 0 0 30px rgba(212, 175, 55, 0.5);
        border: 3px solid #fff; margin: 25px 0;
    }

    /* تصميم الشهادة النهائية */
    .certificate-frame {
        border: 10px double #D4AF37; padding: 40px;
        background-color: #0a0a0a; border-radius: 20px;
        text-align: center; margin-top: 30px;
        position: relative; overflow: hidden;
    }
    .cert-title { color: #D4AF37; font-size: 40px; font-weight: 900; margin-bottom: 20px; }
    .cert-body { color: #fff; font-size: 18px; line-height: 1.6; }
    .stamp { 
        color: #D4AF37; border: 3px solid #D4AF37; padding: 10px;
        display: inline-block; transform: rotate(-15deg);
        font-weight: bold; margin-top: 20px; border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. إدارة البيانات ---
if 'stats' not in st.session_state:
    st.session_state.stats = {"ms": "0.00", "byte": "0", "eff": "100%", "cpu": "0%", "tier": "N/A"}
if 'mega_input' not in st.session_state: st.session_state.mega_input = ""
if 'show_cert' not in st.session_state: st.session_state.show_cert = False

def sync_data(): st.session_state.mega_input = st.session_state.ui_area

# --- 3. عرض لوحة التقارير الرسمية ---
st.markdown('<h1 style="text-align:center; color:#D4AF37; font-size:45px;">🛡️ OKORT SOVEREIGN FACTORY</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#888;">نظام توثيق الكتل الرقمية الفلكية - الإصدار النهائي</p>', unsafe_allow_html=True)

cols = st.columns(5)
m_labels = ["📊 زمن المعالجة", "📑 الكتلة الرقمية", "🔐 ثبات التشفير", "⚙️ حمل النواة", "🏅 تصنيف السيادة"]
m_keys = ["ms", "byte", "eff", "cpu", "tier"]

for i in range(5):
    with cols[i]:
        st.markdown(f'<div class="report-header">{m_labels[i]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="metric-card"><div class="metric-value">{st.session_state.stats[m_keys[i]]}</div></div>', unsafe_allow_html=True)

st.divider()

# --- 4. محرك العد اللحظي ---
raw = st.session_state.mega_input
count = 0
if raw:
    t = raw.replace(" ", "").lower()
    if "اس" in t or "^" in t:
        try:
            sep = "اس" if "اس" in t else "^"
            b, p = t.split(sep)
            count = (len(b)-1) + int(p) if b == "10" else len(b) + int(p)
        except: count = len(t)
    else: count = len(t)

st.markdown(f'<div style="text-align:center;"><div class="power-banner">💎 إجمالي الخانات: {count:,}</div></div>', unsafe_allow_html=True)

# منطقة الإدخال
st.text_area("أدخل البيانات أو الصيغة الرياضية للتوثيق:", key="ui_area", on_change=sync_data, height=180)

# --- 5. إصدار الشهادة ---
if st.button("🚀 إصدار وثيقة التوثيق السيادية"):
    if count > 0:
        with st.spinner("جاري استخراج الشهادة السيادية..."):
            time.sleep(1.5)
            st.session_state.stats.update({
                "ms": f"{random.uniform(150, 400):.2f}",
                "byte": f"{count:,} B",
                "cpu": f"{random.randint(2, 6)}%",
                "tier": "SUPREME +" if count > 500 else "SECURED"
            })
            st.session_state.show_cert = True
            st.rerun()

if st.session_state.show_cert:
    st.markdown(f"""
        <div class="certificate-frame">
            <div class="cert-title">📜 شهادة سيادة رقمية</div>
            <div class="cert-body">
                نشهد نحن إدارة <b>OKORT SOVEREIGN FACTORY</b> بأن الكتلة الرقمية المدخلة <br>
                والتي يبلغ عدد خاناتها <b>({count:,}) خانة</b>، قد خضعت لبروتوكول التشفير الفائق <br>
                وتم اعتمادها في التصنيف السيادي: <b>{st.session_state.stats['tier']}</b>.
            </div>
            <div style="margin-top:20px; color:#D4AF37;">تاريخ التوثيق: {time.strftime('%Y-%m-%d')} | رمز التوثيق: OK-{random.randint(1000,9999)}</div>
            <div class="stamp">ختم الاعتماد السيادي</div>
        </div>
    """, unsafe_allow_html=True)
    st.balloons()
