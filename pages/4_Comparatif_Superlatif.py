import streamlit as st
import json
import random

st.set_page_config(
    page_title="Comparatif et Superlatif",
    page_icon="🇩🇪",
)

st.title("Comparatif et Superlatif")

with st.expander("Leçon"):
    with st.expander("Cas général"):
        st.markdown("La formation du comparatif et du superlatif en allemand suit une règle générale assez simple.")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Positif", value="schnell")
        with col2:
            st.metric(label="Comparatif", value="schneller")
        with col3:
            st.metric(label="Superlatif", value="am schnellsten")
        st.markdown("""
        - **Le comparatif de supériorité** se forme en ajoutant le suffixe **-er** à l\"adjectif. Il est suivi de **als** (que) pour introduire le deuxième élément de la comparaison.
        > *Mein Auto ist **schneller als** deins.* (Ma voiture est plus rapide que la tienne.)

        - **Le superlatif** se forme de deux manières :
            - Avec **am** + adjectif se terminant par **-sten**.
            > *Dieses Auto ist **am schnellsten**.* (Cette voiture est la plus rapide.)
            - En tant qu\"épithète, avec l\"article défini et la terminaison **-ste**.
            > *Das ist das **schnellste** Auto.* (C\"est la voiture la plus rapide.)
        """)

    with st.expander("Cas particuliers"):
        st.markdown("Certains adjectifs présentent des particularités lors de la formation du comparatif et du superlatif.")

        st.subheader("Adjectifs courts (monosyllabiques)")
        st.markdown("Les adjectifs courts (souvent d\"une seule syllabe) prennent un Umlaut (tréma) sur la voyelle au comparatif et au superlatif.")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Positif", value="alt")
        with col2:
            st.metric(label="Comparatif", value="älter")
        with col3:
            st.metric(label="Superlatif", value="am ältesten")
        st.markdown("*Autres exemples: **jung** (jeune) -> **jünger**, **groß** (grand) -> **größer**, **kalt** (froid) -> **kälter** *")

        st.subheader("Adjectifs se terminant par -d, -t, -s, -ß, -x, -z")
        st.markdown("Ces adjectifs ajoutent un **-esten** au superlatif pour des raisons de prononciation.")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Positif", value="heiß")
        with col2:
            st.metric(label="Comparatif", value="heißer")
        with col3:
            st.metric(label="Superlatif", value="am heißesten")

        st.subheader("Formes irrégulières")
        st.markdown("Certains adjectifs ont des formes de comparatif et de superlatif complètement irrégulières.")
        st.markdown("""
        | Adjectif/Adverbe | Comparatif | Superlatif |
        |---|---|---|
        | gut (bon) | besser | am besten |
        | viel (beaucoup) | mehr | am meisten |
        | gern (volontiers) | lieber | am liebsten |
        | hoch (haut) | höher | am höchsten |
        | nah (proche) | näher | am nächsten |
        """)

with st.expander("Exercices"):
    # Charger les données
    @st.cache_data
    def load_practice_data():
        with open("data/comparatif_superlatif_pratique.json", "r") as f:
            data = json.load(f)
        return data

    practice_data = load_practice_data()

    st.header("Mode Pratique")

    if "question_indices_comparatif" not in st.session_state:
        st.session_state.question_indices_comparatif = list(range(len(practice_data)))
        random.shuffle(st.session_state.question_indices_comparatif)

    def reset_session_comparatif():
        st.session_state.question_indices_comparatif = list(range(len(practice_data)))
        random.shuffle(st.session_state.question_indices_comparatif)
        if "answered_comparatif" in st.session_state:
            del st.session_state["answered_comparatif"]
        if "user_answer_input_comparatif" in st.session_state:
            st.session_state.user_answer_input_comparatif = ""
        st.rerun()

    if not st.session_state.question_indices_comparatif:
        st.success("🎉 Bravo ! Vous avez terminé tous les exercices.")
        if st.button("Recommencer"):
            reset_session_comparatif()
        st.stop()

    def next_question_callback_comparatif():
        st.session_state.answered_comparatif = False
        st.session_state.user_answer_input_comparatif = ""
        st.session_state.question_indices_comparatif.pop(0)

    def verify_answer_callback_comparatif():
        st.session_state.answered_comparatif = True

    current_question_index = st.session_state.question_indices_comparatif[0]
    exercise = practice_data[current_question_index]

    # Afficher l\"exercice
    st.markdown(f"<h3>{exercise["phrase"]}</h3>", unsafe_allow_html=True)
    st.markdown(f"<i>{exercise["traduction"]}</i>", unsafe_allow_html=True)


    # Champ de réponse
    user_answer = st.text_input("Votre réponse", key="user_answer_input_comparatif")

    st.button("Vérifier", on_click=verify_answer_callback_comparatif)

    if "answered_comparatif" in st.session_state and st.session_state.answered_comparatif:
        if user_answer.lower() == exercise["reponse"].lower():
            st.balloons()
            st.success("Correct !")
        else:
            st.error(f"Incorrect. La bonne réponse est **{exercise["reponse"]}**.")
        
        st.button("Suivant", on_click=next_question_callback_comparatif)
