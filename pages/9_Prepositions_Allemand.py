import streamlit as st
import json
import random
import os

st.set_page_config(
    page_title="Les Prépositions Allemandes",
    page_icon="🇩🇪",
)

st.title("🇩🇪 Les Prépositions et les Cas en Allemand")

# --- PARTIE LEÇON AVEC TABS ---
st.header("Leçon")

tab_acc, tab_dat, tab_gen, tab_mix, tab_zeit = st.tabs([
    "🎯 Accusatif", 
    "⏳ Datif", 
    "📜 Génitif", 
    "🔄 Mixtes (Wechsel)",
    "⏰ Prépositions de Temps"
])

with tab_acc:
    st.subheader("Prépositions suivies de l'ACCUSATIF")
    st.info("💡 Astuce mémotechnique : **FUDGOB**")
    st.markdown("""
    *   **Für** (pour) : *Das ist für meinen Bruder.*
    *   **Um** (autour de / à [heure]) : *Wir sitzen um den Tisch.*
    *   **Durch** (à travers) : *Er geht durch den Park.* (Masculin : den)
    *   **Gegen** (contre) : *Ich bin gegen diesen Vorschlag.*
    *   **Ohne** (sans) : *Ohne dich gehe ich nicht.*
    *   **Bis** (jusqu'à) : *Bis nächsten Montag.*
    """)

with tab_dat:
    st.subheader("Prépositions suivies du DATIF")
    st.info("💡 Astuce mémotechnique : Mit-Nach-Von-Zu / Aus-Bei-Seit")
    st.markdown("""
    *   **Aus** (hors de, en [matière]) : *Er kommt aus dem Haus.* (Neutre : dem)
    *   **Bei** (chez [quelqu'un], près de) : *Ich wohne bei meinen Eltern.*
    *   **Mit** (avec) : *Ich fahre mit dem Auto.*
    *   **Nach** (après, vers [villes/pays]) : *Nach der Schule / nach Berlin.*
    *   **Seit** (depuis) : *Seit einem Monat lernt er Deutsch.*
    *   **Von** (de la part de, de) : *Das ist ein Brief von meinem Vater.*
    *   **Zu** (vers, chez) : *Ich gehe zum (zu + dem) Arzt.*
    """)

with tab_gen:
    st.subheader("Prépositions suivies du GÉNITIF")
    st.markdown("""
    Ces prépositions expriment des relations logiques, de cause ou de lieu plus formelles.
    *   **Während** (pendant) : *Während der Woche.* (Féminin : der)
    *   **Wegen** (à cause de) : *Wegen des Regens bleiben wir hier.* (Masculin : des ...-s)
    *   **Trotz** (malgré) : *Trotz des Fehlers war es gut.*
    *   **Anstatt / Statt** (au lieu de) : *Statt eines Kaffees trinke ich Tee.*
    """)

with tab_mix:
    st.subheader("🔄 Wechselpräpositionen (Les Prépositions Mixtes)")
    st.warning("C'est le système du directif / locatif (exactement comme в / на en russe !)")
    st.markdown("""
    Les prépositions : **an, auf, hinter, in, neben, über, unter, vor, zwischen**.
    
    *   **Mouvement / Changement de lieu (Wohin? -> Vers où?)** ➔ **ACCUSATIF**
        * *Ich lege das Buch auf den Tisch.* (Je pose le livre sur la table - directif)
    *   **Position fixe / Lieu stable (Wo? -> Où?)** ➔ **DATIF**
        * *Das Buch liegt auf dem Tisch.* (Le livre est sur la table - locatif)
    """)

with tab_zeit:
    st.subheader("⏰ Focus : Les Prépositions de Temps (Temporale Präpositionen)")
    st.markdown("""
    Voici comment exprimer le temps et la durée avec les principales prépositions et leurs cas :

    *   **Beim** (bei + dem + Datif) : Signifie "pendant que l'on fait", exprime la simultanéité d'une action.
        * *Beim Essen sprechen wir nicht.* (Pendant le repas / en mangeant, nous ne parlons pas.)
    *   **Gegen** (+ Accusatif) : Signifie "vers" une heure approximative.
        * *Ich komme gegen acht Uhr.* (Je viens vers huit heures.)
    *   **Während** (+ Génitif) : Signifie "pendant" une période définie.
        * *Während der Sommerferien hat es geregnet.* (Pendant les vacances d'été, il a plu.)
    *   **Innerhalb** (+ Génitif) : Signifie "dans l'espace de" / "en moins de".
        * *Bitte antworten Sie innerhalb einer Woche.* (Veuillez répondre d'ici une semaine.)
    *   **Vor** (+ Datif) : Signifie "avant" ou "il y a" (temporel).
        * *Vor dem Frühstück trinke ich Wasser.* (Avant le petit-déjeuner, je bois de l'eau.)
        * *Ich bin vor einem Jahr angekommen.* (Je suis arrivé il y a un an.)
    *   **Auf** (+ Accusatif) : Utilisé pour projeter une durée dans le futur (souvent avec *für* sous-entendu).
        * *Er reist auf eine Woche nach Paris.* (Il part à Paris pour une semaine.)
    """)

# --- NOUVEL EXPANDER : TABLEAU RÉCAPITULATIF ---
with st.expander("📊 Tableau récapitulatif des prépositions", expanded=False):
    st.markdown("""
    | Préposition | Signification principale | Cas exigé | Type / Usage fréquent |
    | :--- | :--- | :--- | :--- |
    | **Bis** | Jusqu'à | **Accusatif** | Temps / Espace |
    | **Durch** | À travers | **Accusatif** | Espace |
    | **Für** | Pour | **Accusatif** | Attribution |
    | **Gegen** | Contre / Vers (heure) | **Accusatif** | Opposition / Temps (approx.) |
    | **Ohne** | Sans | **Accusatif** | Exclusion |
    | **Um** | Autour de / À (heure pile) | **Accusatif** | Espace / Temps |
    | **Auf** | Sur / Pour (durée future) | **Accusatif (mouvement)** | Espace / Temps |
    | **Aus** | Hors de / Provenance | **Datif** | Origine / Lieu |
    | **Bei / Beim** | Chez / Près de / Pendant | **Datif** | Lieu / Simultanéité temporelle |
    | **Mit** | Avec | **Datif** | Moyen / Accompagnement |
    | **Nach** | Après / Vers (pays/ville) | **Datif** | Temps / Lieu |
    | **Seit** | Depuis | **Datif** | Temps (action continue) |
    | **Von** | De / De la part de | **Datif** | Provenance / Possession |
    | **Zu / Zum** | Vers / Chez | **Datif** | Direction |
    | **Vor** | Avant / Il y a / Devant | **Datif (lieu fixe)** | Temps / Espace |
    | **Während** | Pendant | **Génitif** | Temps (durée) |
    | **Wegen** | À cause de | **Génitif** | Cause |
    | **Trotz** | Malgré | **Génitif** | Concession |
    | **Innerhalb** | En l'espace de / Au sein de | **Génitif** | Temps / Espace |
    """)

# --- PARTIE EXERCICES (EXPANDER) ---
st.divider()
with st.expander("📝 Exercices Pratiques", expanded=True):
    
    # Fonction de chargement sécurisée
    @st.cache_data
    def load_practice_data():
        file_path = 'data/prepositions_allemand.json'
        if not os.path.exists(file_path):
            return []
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    practice_data = load_practice_data()

    if not practice_data:
        st.warning("⚠️ Crée le fichier `data/prepositions_allemand.json` pour charger les exercices.")
    else:
        st.header('Mode Pratique')
        st.caption("Traduisez et complétez les blancs avec la bonne préposition et l'article décliné.")

        # Filtrage par catégorie supprimé ➔ Utilise l'ensemble du fichier de données
        filtered_practice_data = practice_data

        # Gestion du Session State simplifiée
        if 'q_idx_de' not in st.session_state:
            st.session_state.q_idx_de = list(range(len(filtered_practice_data)))
            random.shuffle(st.session_state.q_idx_de)
            st.session_state.answered_de = False

        def reset_session_de():
            st.session_state.q_idx_de = list(range(len(filtered_practice_data)))
            random.shuffle(st.session_state.q_idx_de)
            st.session_state.answered_de = False
            st.rerun()

        if not st.session_state.q_idx_de:
            st.success('🎉 Wunderbar! Vous avez terminé tous les exercices disponibles.')
            if st.button('Recommencer', key="btn_reset_de"):
                reset_session_de()
        else:
            current_question_index = st.session_state.q_idx_de[0]
            exercise = filtered_practice_data[current_question_index]

            st.markdown(f'<h3>{exercise["phrase"]}</h3>', unsafe_allow_html=True)
            st.markdown(f'<i>{exercise["traduction"]}</i>', unsafe_allow_html=True)

            # Champ de réponse
            user_answer = st.text_input('Votre réponse (complétez les blancs) :', key=f'in_de_{current_question_index}')

            if st.button('Vérifier', key="btn_verify_de"):
                st.session_state.answered_de = True

            if st.session_state.answered_de:
                if user_answer.strip().lower() == exercise['reponse'].strip().lower():
                    st.success('Richtig! Correct !')
                else:
                    st.error(f'Incorrect. La bonne réponse est : **{exercise["reponse"]}**')
                    st.info(f'**Règle :** {exercise["regle"]}')
                
                if st.button('Suivant ➡️', key="btn_next_de"):
                    st.session_state.q_idx_de.pop(0)
                    st.session_state.answered_de = False
                    st.rerun()