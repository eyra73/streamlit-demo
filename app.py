import streamlit as st

st.markdown("""
<style>
.marquee {
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
}

.marquee p {
    display: inline-block;
    animation: move 8s linear infinite;
    font-size: 30px;
    font-weight: bold;
}

@keyframes move {
    from {
        transform: translateX(100%);
    }
    to {
        transform: translateX(-100%);
    }
}
</style>

<div class="marquee">
    <p>PYTHON PROGRAMMING! 🎉</p>
</div>
""", unsafe_allow_html=True)
