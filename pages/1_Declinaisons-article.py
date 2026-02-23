import streamlit as st
import json
import random

st.set_page_config(
    page_title="Leçon et Pratique",
    page_icon="🇩🇪",
)

st.title("Déclinaisons Allemandes")

with st.expander("Leçon"):
    st.markdown("""# Les déclinaisons en allemand

En allemand, les noms, les articles et les adjectifs sont déclinés en fonction de leur cas, de leur genre et de leur nombre. Il y a quatre cas en allemand :

*   **Nominatif :** le sujet de la phrase.
*   **Accusatif :** le complément d'objet direct.
*   **Datif :** le complément d'objet indirect.
*   **Génitif :** le complément du nom (possession).

## Déclinaison des articles définis

| | Masculin | Féminin | Neutre | Pluriel |
| --- | --- | --- | --- | --- |
| **Nominatif** | der | die | das | die |
| **Accusatif** | den | die | das | die |
| **Datif** | dem | der | dem | den |
| **Génitif** | des | der | des | der |

*Exemples:*
*   **Der** Mann ist groß. (Le mari est grand.)
*   Ich sehe **den** Mann. (Je vois le mari.)

## Déclinaison des articles indéfinis

| | Masculin | Féminin | Neutre | Pluriel |
| --- | --- | --- | --- | --- |
| **Nominatif** | ein | eine | ein | keine |
| **Accusatif** | einen | eine | ein | keine |
| **Datif** | einem | einer | einem | keinen |
| **Génitif** | eines | einer | eines | keiner |

*Exemples:*
*   **Ein** Mann ist hier. (Un homme est ici.)
*   Ich sehe **einen** Mann. (Je vois un homme.)

## Déclinaison de l'adjectif avec un article défini

| | Masculin | Féminin | Neutre | Pluriel |
| --- | --- | --- | --- | --- |
| **Nominatif** | -e | -e | -e | -en |
| **Accusatif** | -en | -e | -e | -en |
| **Datif** | -en | -en | -en | -en |
| **Génitif** | -en | -en | -en | -en |

*Exemples:*
*   Der gut**e** Mann. (Le bon homme.)
*   Die schön**e** Frau. (La belle femme.)

## Déclinaison de l'adjectif avec un article indéfini

| | Masculin | Féminin | Neutre | Pluriel |
| --- | --- | --- | --- | --- |
| **Nominatif** | -er | -e | -es | -en |
| **Accusatif** | -en | -e | -es | -en |
| **Datif** | -en | -en | -en | -en |
| **Génitif** | -en | -en | -en | -en |

*Exemples:*
*   Ein gut**er** Mann. (Un bon homme.)
*   Eine schön**e** Frau. (Une belle femme.)

## Déclinaison de l'adjectif sans article

| | Masculin | Féminin | Neutre | Pluriel |
| --- | --- | --- | --- | --- |
| **Nominatif** | -er | -e | -es | -e |
| **Accusatif** | -en | -e | -es | -e |
| **Datif** | -em | -er | -em | -en |
| **Génitif** | -en | -er | -en | -er |

*Exemples:*
*   Gut**er** Wein. (Bon vin.)
*   Kalt**es** Wasser. (Eau froide.)
""")

with st.expander("Exercices"):
    # Charger les données
    @st.cache_data
    def load_practice_data():
        with open('data/pratique.json', 'r') as f:
            data = json.load(f)
        return data

    practice_data = load_practice_data()

    st.header('Mode Pratique')

    # Menu déroulant pour sélectionner le cas
    all_cases = ['Tous'] + list(set([ex['cas'] for ex in practice_data]))
    selected_case = st.selectbox('Choisissez un cas à pratiquer :', all_cases)

    # Filtrer les exercices en fonction du cas sélectionné
    if selected_case == 'Tous':
        filtered_practice_data = practice_data
    else:
        filtered_practice_data = [ex for ex in practice_data if ex['cas'] == selected_case]

    if 'question_indices_declinaison' not in st.session_state or st.session_state.get('selected_case_declinaison') != selected_case:
        st.session_state.question_indices_declinaison = list(range(len(filtered_practice_data)))
        random.shuffle(st.session_state.question_indices_declinaison)
        st.session_state.selected_case_declinaison = selected_case
        if 'answered_declinaison' in st.session_state:
            del st.session_state['answered_declinaison']
        if 'user_answer_input_declinaison' in st.session_state:
            st.session_state.user_answer_input_declinaison = ''
    
    def reset_session_declinaison():
        st.session_state.question_indices_declinaison = list(range(len(filtered_practice_data)))
        random.shuffle(st.session_state.question_indices_declinaison)
        if 'answered_declinaison' in st.session_state:
            del st.session_state['answered_declinaison']
        if 'user_answer_input_declinaison' in st.session_state:
            st.session_state.user_answer_input_declinaison = ''
        st.rerun()

    if not st.session_state.question_indices_declinaison:
        st.success('🎉 Bravo ! Vous avez terminé tous les exercices pour cette sélection.')
        if st.button('Recommencer'):
            reset_session_declinaison()
        st.stop()

    def next_question_callback_declinaison():
        st.session_state.answered_declinaison = False
        st.session_state.user_answer_input_declinaison = ''
        st.session_state.question_indices_declinaison.pop(0)

    def verify_answer_callback_declinaison():
        st.session_state.answered_declinaison = True

    current_question_index = st.session_state.question_indices_declinaison[0]
    exercise = filtered_practice_data[current_question_index]

    # Définir la couleur en fonction du genre
    color_map = {
        'Maskulin': 'blue',
        'Feminin': 'pink',
        'Neutrum': 'green',
        'Pluriel': 'purple'
    }
    color = color_map.get(exercise['genre'], 'black')

    # Afficher l'exercice avec la couleur
    st.markdown(f'<h3 style="color:{color};">{exercise["phrase"]}</h3>', unsafe_allow_html=True)
    st.markdown(f'<i>{exercise["traduction"]}</i>', unsafe_allow_html=True)


    # Champ de réponse
    user_answer = st.text_input('Votre réponse', key='user_answer_input_declinaison')

    st.button('Vérifier', on_click=verify_answer_callback_declinaison)

    if 'answered_declinaison' in st.session_state and st.session_state.answered_declinaison:
        if user_answer.lower() == exercise['reponse'].lower():
            st.balloons()
            st.success('Correct !')
        else:
            st.error(f'Incorrect. La bonne réponse est **{exercise["reponse"]}**.')
            st.info(f'**Règle :** {exercise["regle"]}')
        
        st.button('Suivant', on_click=next_question_callback_declinaison)
