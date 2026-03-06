st.set_page_config(page_title="StudyNest", layout="wide")

# ---------------- BACK BUTTON ----------------
if st.button("⬅ Back to Home"):
    st.switch_page("main.py")

# ---------------- CSS STYLE ----------------
st.markdown("""
<style>

/* 🌑 Professional Dark Background */
.stApp {
    background-color: #0f172a;   /* Deep Navy Professional Color */
}

/* ✨ Title */
.fade-text {
    text-align: center;
    font-size: 48px;
    color: #FFD700;
    animation: fadeIn 2s ease-in;
    margin-top: 40px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 22px;
    color: #e5e7eb;
    margin-bottom: 40px;
}

/* Fade animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Banner */
.top-banner {
    background: #FFD700;
    padding: 12px;
    text-align: center;
    color: black;
    font-size: 22px;
    font-weight: bold;
    border-radius: 8px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TEXT ----------------
st.markdown('<h1 class="fade-text">Welcome to StudyNest</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Learn • Practice • Grow with Interactive Notes</p>', unsafe_allow_html=True)

# ---------------- BANNER ----------------
st.markdown("""
<div class="top-banner">
✨ 📘 Welcome to StudyNest – Your Smart Learning Hub ✨
</div>
""", unsafe_allow_html=True)