import streamlit as st
import pandas as pd
import json

# Configuration de la page
st.set_page_config(
    page_title="Pays, nationalités et langues",
    page_icon="🇩🇪",
    layout="wide" # Optionnel : pour utiliser toute la largeur
)

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

st.title("Pays, nationalités et langues")

# Chargement des données depuis le fichier JSON
try:
    with open('data/pays.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Création du DataFrame
    df = pd.DataFrame(data)
    
    # Mise en index du pays
    df = df.set_index('Pays (das Land)')

    st.markdown("Voici un tableau avec quelques pays, leurs nationalités et les langues parlées.")
    
    # Affichage de la table
    st.table(df)

except FileNotFoundError:
    st.error("Le fichier 'pays.json' est introuvable. Veuillez vérifier son emplacement.")

st.markdown("""
**Remarques importantes:**
- En allemand, les noms de pays sont généralement neutres (`das Land`). Il y a quelques exceptions, par exemple `die Schweiz` (la Suisse), `die Türkei` (la Turquie), `die Vereinigten Staaten` (les États-Unis, pluriel).
- Les langues et les nationalités sont souvent des adjectifs et ne prennent pas de majuscule, sauf s'ils sont utilisés comme des noms. Par exemple : `Er ist Deutscher.` (Il est Allemand.) mais `Er spricht deutsch.` (Il parle allemand.)
- Pour former le féminin des nationalités, on ajoute généralement le suffixe `-in` au masculin.
- Pour dire d'où l'on vient, on utilise la préposition `aus` : `Ich komme aus Deutschland.` (Je viens d'Allemagne).
- Pour dire que l'on va dans un pays, on utilise `nach` pour la plupart des pays (`nach Deutschland`) et `in` pour les pays avec un article (`in die Schweiz`).
""")