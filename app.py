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

st.markdown("<div class='big-heart'>❤️</div>", unsafe_allow_html=True)
st.title("Til min smukke Qainat")
st.subheader("Bare en lille hjemmeside lavet med kærlighed")

st.markdown("""
<div class="love-box">
<h3>Hvorfor jeg elsker dig</h3>
<p>Fordi du er min ro, min glæde og mit hjem.</p>
<p>Du får selv almindelige dage til at føles specielle.</p>
<p>Og jeg glæder mig til alt det liv, vi skal bygge sammen.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

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
st.markdown("### Lille kærlighedsberegner")

name = st.text_input("Skriv dit navn")
wife = st.text_input("Skriv hendes navn", value="Qainat")

if st.button("Beregn kærlighed ❤️"):
    if name:
        st.balloons()
        st.markdown(f"## {name} + {wife} = 100% meant to be ❤️")
        st.write("Ingen diskussion. Det er videnskabeligt bevist af JonasGPT.")
    else:
        st.warning("Skriv lige dit navn først 😄")

st.write("")
st.markdown("### En lille besked til dig")

if st.button("Åbn besked 💌"):
    st.info("""
    Qainat, jeg lavede den her lille hjemmeside bare for at få dig til at smile.
    
    Du betyder alt for mig, og jeg er så taknemmelig for dig.
    
    Jeg glæder mig til vores fremtid sammen ❤️
    """)

st.write("")
st.caption(f"Lavet med kærlighed den {date.today().strftime('%d-%m-%Y')} ❤️")
