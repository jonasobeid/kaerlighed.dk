import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Til Qainat ❤️",
    page_icon="❤️",
    layout="centered"
)

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
</style>
""", unsafe_allow_html=True)

# Top
st.markdown("<div class='big-heart'>❤️</div>", unsafe_allow_html=True)
st.title("Til min smukke Qainat")
st.subheader("Bare en lille hjemmeside lavet med kærlighed")

# Besked
st.markdown("""
<div class="love-box">
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

# BESKED KNAP
st.markdown("### En lille besked til dig")

if st.button("Åbn besked 💌"):
    st.info("""
    Jeg elsker dig ❤️  

    Uanset hvad vi går igennem, så klarer vi det sammen.  
    Jeg giver ikke op på os.
    """)

st.write("")

# 🔥 NYT: BILLEDER
st.markdown("### Vores minder ❤️")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("os1.jpg", use_container_width=True)
    st.image("os4.JPG", use_container_width=True)

with col2:
    st.image("os2.jpg", use_container_width=True)
    st.image("os5.JPG", use_container_width=True)

with col3:
    st.image("os3.JPG", use_container_width=True)
    st.image("os6.JPG", use_container_width=True)

st.write("")

st.caption(f"Lavet med kærlighed den {date.today().strftime('%d-%m-%Y')} ❤️")

st.write("")
st.markdown("### Godnat ❤️")

if st.button("Tryk for godnatkys 💋"):
    st.markdown(
        "<div style='text-align:center; font-size:150px;'>💋</div>",
        unsafe_allow_html=True
    )
    st.balloons()
    st.success("Godnat Qainat ❤️")
    # Footer
