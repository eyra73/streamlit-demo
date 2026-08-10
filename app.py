import streamlit as st

st.set_page_config(
    page_title="Animated Streamlit",
    page_icon="✨",
    layout="wide"
)

# ==============================
# CSS ANIMATION
# ==============================
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #f5f7ff, #e8f0ff);
}

/* MAIN TITLE */
.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    animation: fadeIn 2s ease-in-out;
}

/* GRADIENT TEXT */
.gradient-text {
    text-align: center;
    font-size: 35px;
    font-weight: bold;
    background: linear-gradient(90deg, #ff4b4b, #7b61ff, #00b894);
    -webkit-background-clip: text;
    color: transparent;
    animation: colorMove 4s infinite;
}

/* MARQUEE */
.marquee {
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
    margin-top: 25px;
}

.marquee p {
    display: inline-block;
    font-size: 25px;
    font-weight: bold;
    animation: moveText 12s linear infinite;
}

/* SLIDE TEXT */
.slide-text {
    text-align: center;
    font-size: 28px;
    animation: slideIn 2s ease-out;
}

/* BLINK */
.blink {
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    animation: blink 1.5s infinite;
}

/* FLOATING TEXT */
.float {
    text-align: center;
    font-size: 26px;
    animation: floating 3s ease-in-out infinite;
}

/* FADE */
.fade {
    text-align: center;
    font-size: 24px;
    animation: fadeInOut 3s infinite;
}

/* ANIMATIONS */

@keyframes moveText {
    from {
        transform: translateX(100%);
    }
    to {
        transform: translateX(-100%);
    }
}

@keyframes slideIn {
    from {
        transform: translateX(-100%);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes blink {
    0%, 100% {
        opacity: 1;
    }
    50% {
        opacity: 0.2;
    }
}

@keyframes floating {
    0%, 100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-15px);
    }
}

@keyframes fadeInOut {
    0%, 100% {
        opacity: 0;
    }
    50% {
        opacity: 1;
    }
}

@keyframes colorMove {
    0% {
        filter: hue-rotate(0deg);
    }
    100% {
        filter: hue-rotate(360deg);
    }
}

</style>
""", unsafe_allow_html=True)


# ==============================
# TITLE
# ==============================

st.markdown(
    '<div class="title">✨ WELCOME TO EYRA WEBSITE ✨</div>',
    unsafe_allow_html=True
)


# ==============================
# GRADIENT
# ==============================

st.markdown(
    '<div class="gradient-text">Discover • Explore • Learn • Create • Innovate</div>',
    unsafe_allow_html=True
)


# ==============================
# MARQUEE
# ==============================

st.markdown("""
<div class="marquee">
<p>
🌟 Selamat Datang! Terima kasih kerana mengunjungi laman web kami.
Kami menyediakan pengalaman yang menarik, mudah dan interaktif untuk semua pengguna.
Nikmati setiap bahagian dan terokai maklumat yang tersedia di sini! 🚀
</p>
</div>
""", unsafe_allow_html=True)


# ==============================
# SLIDE
# ==============================

st.markdown("""
<div class="slide-text">
🚀 Explore our amazing features and discover something new!
</div>
""", unsafe_allow_html=True)


# ==============================
# FLOAT
# ==============================

st.markdown("""
<div class="float">
💡 Learn something new every day.
</div>
""", unsafe_allow_html=True)


# ==============================
# BLINK
# ==============================

st.markdown("""
<div class="blink">
🔥 DON'T MISS OUT! CHECK OUT OUR LATEST INFORMATION! 🔥
</div>
""", unsafe_allow_html=True)


# ==============================
# FADE
# ==============================

st.markdown("""
<div class="fade">
🌈 Thank you for visiting our website. We hope you enjoy your experience!
</div>
""", unsafe_allow_html=True)
