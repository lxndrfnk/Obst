import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_plotly_events import plotly_events

farben = {
    "Apfel": "#d62728",     # Rot
    "Banane": "#ffeb3b",    # Gelb
    "Erdbeere": "#ff1744",  # Erdbeerrot
    "Orange": "#ffa500",    # Orange
    "Traube": "#8e24aa",    # Violett
}

df = pd.DataFrame({
    "Obst": ["Apfel", "Banane", "Erdbeere", "Orange", "Traube"],
    "Stimmen": [8, 5, 6, 4, 3],
    "Farbe": ["Rot", "Gelb", "Rot", "Orange", "Violett"],
    "Vitamin C (mg)": [12, 9, 60, 50, 4],
    "Herkunft": ["Deutschland", "Ecuador", "Spanien", "Italien", "Griechenland"],
    "Icon": ["🍎", "🍌", "🍓", "🍊", "🍇"],
})

st.title("Lieblingsobst der Klasse")

st.markdown("---")

fig = px.bar(
    df,
    x="Obst",
    y="Stimmen",
    color="Obst",  # Kategorisch nach Obstsorte einfärben
    color_discrete_map=farben,  # Deine selbstgewählten Farben
    text="Icon"
)
st.plotly_chart(fig)

auswahl = st.selectbox("Wähle eine Obstsorte aus, um weitere Details zu erfahren:", df["Obst"])

ausgewählt = df[df["Obst"] == auswahl].iloc[0]

st.subheader(f"Details zu {auswahl} {ausgewählt['Icon']}")
st.markdown(f"""
- **Farbe:** {ausgewählt['Farbe']}
- **Vitamin C:** {ausgewählt['Vitamin C (mg)']} mg
- **Herkunft:** {ausgewählt['Herkunft']}
- **Stimmen:** {ausgewählt['Stimmen']}
""")