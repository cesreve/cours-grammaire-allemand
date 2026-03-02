
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Adjectifs",
    page_icon="🇩🇪",
)

st.title("Les adjectifs et leurs contraires")

# Charger les données
@st.cache_data
def load_data():
    df = pd.read_json("data/adjectifs.json")
    return df

adjectifs_df = load_data()

# Renommer les colonnes pour l"affichage
adjectifs_df.columns = ["Adjectif (Allemand)", "Traduction française", "Contraire (Allemand)", "Traduction française"]

st.dataframe(adjectifs_df)
