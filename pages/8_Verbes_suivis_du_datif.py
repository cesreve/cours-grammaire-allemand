import streamlit as st
import pandas as pd
import json

# 1. Configuration de la page en mode LARGE
st.set_page_config(page_title="Apprendre l'Allemand : Verbes au Dativ", layout="wide")

# 2. CSS pour centrer les colonnes et styliser l'index
st.markdown("""
    <style>
        th {
            text-align: center !important;
            background-color: #f0f2f6;
        }
        td {
            text-align: center !important;
        }
    </style>
    """, unsafe_allow_html=True)

st.title("🇩🇪 Apprendre l'Allemand : Les Verbes au Dativ")
st.subheader("Liste des verbes essentiels et exemples d'utilisation")

# 3. Chargement des données depuis le fichier JSON
try:
    with open('data/verbes_datif.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Création du DataFrame et mise du Verbe en index
    df = pd.DataFrame(data).set_index("Verbe")

    # 4. Affichage de la table principale
    st.table(df)

except FileNotFoundError:
    st.error("Le fichier 'verbes_datif.json' est introuvable. Assurez-vous qu'il est dans le même dossier.")