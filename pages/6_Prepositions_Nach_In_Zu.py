import streamlit as st
import json
import random

st.set_page_config(
    page_title="Leçon et Pratique",
    page_icon="🇩🇪",
)

st.title("Les prépositions NACH, IN et ZU")

with st.expander("Leçon"):
    st.markdown("""# Les prépositions NACH, IN et ZU

## NACH

Utilisé pour les destinations sans article (villes, pays, continents).

*Exemples:*
*   Ich fahre **nach** Deutschland. (Je vais en Allemagne.)
*   Wir fliegen **nach** New York. (Nous volons vers New York.)

## IN

Utilisé pour les destinations avec un article, ou pour indiquer qu'on entre dans un lieu fermé.

*Exemples:*
*   Ich gehe **in** die Schweiz. (Je vais en Suisse.)
*   Er geht **in** den Supermarkt. (Il va au supermarché.)

## ZU

Utilisé pour indiquer une direction vers une personne ou un lieu, souvent avec l'idée d'un but ou d'une activité.

*Exemples:*
*   Ich gehe **zu** meinem Freund. (Je vais chez mon ami.)
*   Wir fahren **zum** Bahnhof. (Nous allons à la gare.)
""")

with st.expander("Exercices"):
    # Charger les données
    @st.cache_data
    def load_practice_data():
        with open('data/prepositions_pratique.json', 'r') as f:
            data = json.load(f)
        return data

    practice_data = load_practice_data()

    st.header('Mode Pratique')

    # Menu déroulant pour sélectionner le cas
    all_cases = ['Tous'] + list(set([ex['cas'] for ex in practice_data]))
    selected_case = st.selectbox('Choisissez une préposition à pratiquer :', all_cases)

    # Filtrer les exercices en fonction du cas sélectionné
    if selected_case == 'Tous':
        filtered_practice_data = practice_data
    else:
        filtered_practice_data = [ex for ex in practice_data if ex['cas'] == selected_case]

    if 'question_indices_prepositions' not in st.session_state or st.session_state.get('selected_case_prepositions') != selected_case:
        st.session_state.question_indices_prepositions = list(range(len(filtered_practice_data)))
        random.shuffle(st.session_state.question_indices_prepositions)
        st.session_state.selected_case_prepositions = selected_case
        if 'answered_prepositions' in st.session_state:
            del st.session_state['answered_prepositions']
        if 'user_answer_input_prepositions' in st.session_state:
            st.session_state.user_answer_input_prepositions = ''
    
    def reset_session_prepositions():
        st.session_state.question_indices_prepositions = list(range(len(filtered_practice_data)))
        random.shuffle(st.session_state.question_indices_prepositions)
        if 'answered_prepositions' in st.session_state:
            del st.session_state['answered_prepositions']
        if 'user_answer_input_prepositions' in st.session_state:
            st.session_state.user_answer_input_prepositions = ''
        st.rerun()

    if not st.session_state.question_indices_prepositions:
        st.success('🎉 Bravo ! Vous avez terminé tous les exercices pour cette sélection.')
        if st.button('Recommencer'):
            reset_session_prepositions()
        st.stop()

    def next_question_callback_prepositions():
        st.session_state.answered_prepositions = False
        st.session_state.user_answer_input_prepositions = ''
        st.session_state.question_indices_prepositions.pop(0)

    def verify_answer_callback_prepositions():
        st.session_state.answered_prepositions = True

    current_question_index = st.session_state.question_indices_prepositions[0]
    exercise = filtered_practice_data[current_question_index]

    st.markdown(f'<h3>{exercise["phrase"]}</h3>', unsafe_allow_html=True)
    st.markdown(f'<i>{exercise["traduction"]}</i>', unsafe_allow_html=True)


    # Champ de réponse
    user_answer = st.text_input('Votre réponse', key='user_answer_input_prepositions')

    st.button('Vérifier', on_click=verify_answer_callback_prepositions)

    if 'answered_prepositions' in st.session_state and st.session_state.answered_prepositions:
        if user_answer.lower() == exercise['reponse'].lower():
            st.balloons()
            st.success('Correct !')
        else:
            st.error(f'Incorrect. La bonne réponse est **{exercise["reponse"]}**.')
            st.info(f'**Règle :** {exercise["regle"]}')
        
        st.button('Suivant', on_click=next_question_callback_prepositions)
