import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Til Qainat ❤️",
    page_icon="❤️",
    layout="centered"
)

# Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff1f2, #ffe4e6, #fdf2f8);
}
h1, h2, h3, p {
    text-align: center;
}
.love-box {
    background-color: white;
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.12);
    text-align: center;
}
.big-heart {
    font-size: 70px;
    text-align: center;
}
@keyframes fadeIn {
    from {opacity: 0; transform: scale(0.95);}
    to {opacity: 1; transform: scale(1);}
}
</style>
""", unsafe_allow_html=True)

# Top
st.markdown("<div class='big-heart'>❤️</div>", unsafe_allow_html=True)
st.title("Til Qainat")
st.subheader("Bare en lille hjemmeside lavet med kærlighed")

st.write("")

# 💌 Kuvert / brev
st.markdown("### En lille besked til dig 💌")

if st.button("Åbn kuverten 💌"):
    st.markdown("""
    <div style="
        background:white;
        padding:30px;
        border-radius:20px;
        box-shadow:0 6px 20px rgba(0,0,0,0.15);
        text-align:center;
        font-size:18px;
        line-height:1.7;
        animation: fadeIn 1s;
    ">
        <div style="font-size:80px;">💌</div>
        <h3>Til min Qainat</h3>
        <p>Jeg elsker dig ❤️</p>
        <p>Selv når tingene ikke er helt nemme, så er du stadig den, jeg vil være sammen med.</p>
        <p>Vi har vores udfordringer, men jeg ved, vi kan komme igennem dem – sammen.</p>
        <p>Jeg giver ikke op på os, og jeg tror på det, vi har.</p>
        <p>Du betyder virkelig meget for mig.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# Dropdown
reason = st.selectbox(
    "Tryk her og vælg en grund ❤️",
    [
        "Du har det smukkeste smil",
        "Du gør mig glad uden at prøve",
        "Du er min yndlingsperson",
        "Jeg elsker at tænke på vores fremtid",
        "Du betyder mere for mig, end jeg kan forklare"
    ]
)

st.success(reason)

st.write("")

# Kærlighedsberegner
st.markdown("### Lille kærlighedsberegner")

name = st.text_input("Skriv dit navn")
wife = st.text_input("Skriv hendes navn", value="Qainat")

if st.button("Beregn kærlighed ❤️"):
    if name:
        st.balloons()
        st.markdown(f"## {name} + {wife} = 100% meant to be ❤️")
        st.write("Ingen diskussion 😄")
    else:
        st.warning("Skriv lige dit navn først 😄")

st.write("")

# 🎞️ Slideshow billeder
st.markdown("### Vores minder ❤️")

images = ["os1.jpg", "os2.jpg", "os3.JPG", "os4.JPG", "os5.JPG", "os6.JPG"]

if "photo_index" not in st.session_state:
    st.session_state.photo_index = 0

col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    if st.button("⬅️"):
        st.session_state.photo_index = (st.session_state.photo_index - 1) % len(images)

with col2:
    st.image(
        images[st.session_state.photo_index],
        use_container_width=True,
        caption=f"Minde {st.session_state.photo_index + 1} af {len(images)} ❤️"
    )

with col3:
    if st.button("➡️"):
        st.session_state.photo_index = (st.session_state.photo_index + 1) % len(images)

if st.button("Næste minde ❤️"):
    st.session_state.photo_index = (st.session_state.photo_index + 1) % len(images)

st.write("")

# 💋 Godnat kys
st.markdown("### Godnat ❤️")

if st.button("Tryk for godnatkys 💋"):
    st.markdown(
        "<div style='text-align:center; font-size:180px;'>💋</div>",
        unsafe_allow_html=True
    )
    st.balloons()
    st.success("Godnat min skat ❤️")

# Footer
st.caption(f"Lavet med kærlighed den {date.today().strftime('%d-%m-%Y')} ❤️")
