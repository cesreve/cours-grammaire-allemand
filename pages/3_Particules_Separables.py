import streamlit as st

st.set_page_config(
    page_title="Particules Séparables",
    page_icon="🇩🇪",
)

st.title("Les particules des verbes séparables")

st.markdown("""En allemand, de nombreux verbes sont formés avec une particule (un préfixe) qui peut se séparer du verbe principal. Cette particule modifie le sens du verbe.""")

st.header("Qu'est-ce qu'un verbe à particule séparable ?")
st.markdown("""Un verbe à particule séparable est un verbe dont le préfixe se détache et se place à la fin de la phrase conjuguée au présent ou au prétérit.

*Exemple :* `anrufen` (appeler)
> Ich **rufe** dich **an**. (Je t'appelle.)
""")

st.header("Liste des particules séparables courantes")
st.markdown("""Voici une liste de particules séparables courantes avec leur signification générale et des exemples.""")
st.markdown("""
| Particule | Signification | Exemple | Traduction |
| --- | --- | --- | --- |
| **an-** | contact, début d'une action | `anrufen` | appeler |
| **auf-** | ouverture, mouvement vers le haut | `aufstehen` | se lever |
| **aus-** | sortie, extension | `ausgehen` | sortir |
| **ein-** | entrée, introduction | `einkaufen` | faire les courses |
| **mit-** | accompagnement | `mitkommen` | venir avec |
| **nach-** | répétition, direction | `nachdenken` | réfléchir |
| **vor-** | avant, présentation | `vorstellen` | présenter, imaginer |
| **zu-** | fermeture, ajout | `zumachen` | fermer |
""")

st.header("Particules de sens contraire")
st.markdown("""Certaines particules ont des significations opposées, ce qui peut aider à les mémoriser.""")
st.markdown("""
| Particule 1 | Signification 1 | Particule 2 | Signification 2 | Exemple |
| --- | --- | --- | --- | --- |
| **auf-** | ouverture | **zu-** | fermeture | `aufmachen` (ouvrir) / `zumachen` (fermer) |
| **an-** | allumer | **aus-** | éteindre | `anmachen` (allumer) / `ausmachen` (éteindre) |
| **ein-** | entrée | **aus-** | sortie | `einatmen` (inspirer) / `ausatmen` (expirer) |
""")
