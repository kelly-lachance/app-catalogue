import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

comptes = {
    "usernames": {
        "utilisateur": {
            "name": "utilisateur",
            "password": "utilisateurMDP",
            "email": "utilisateur@exemple.fr",
            "failed_login_attempts": 0,   # géré automatiquement
            "logged_in": False,           # géré automatiquement
            "roles": ["utilisateur"],
        },
        "root": {
            "name": "root",
            "password": "rootMDP",
            "email": "admin@exemple.fr",
            "failed_login_attempts": 0,
            "logged_in": False,
            "roles": ["administrateur"],
        },
    }
}

authenticator = Authenticate(
    comptes,                                             # les comptes
    "nom_du_cookie",                                     # le nom du cookie, un texte au choix
    "une-cle-secrete-longue-d-au-moins-32-caracteres",   # la clé qui signe le cookie
    30,                                                  # le nombre de jours avant que le cookie expire
)

authenticator.login(fields={"Form name": "Connexion", "Username": "Nom d'utilisateur",
                            "Password": "Mot de passe", "Login": "Se connecter"})

if st.session_state["authentication_status"]:

    with st.sidebar : 
        st.title(f"Bienvenue {st.session_state['name']} !")
        authenticator.logout("Déconnexion", "sidebar")
        selection = option_menu(
         menu_title = None,
            options = ["Connexion","Accueil", "Photos"],
        )

    if selection == "Accueil" : 
        st.title("Bienvenue sur la page d'accueil !")

    elif selection =="Photos" : 
        st.title("Bienvenue sur mon album photo")

        photos = [
            ("Un chat", "https://static.streamlit.io/examples/cat.jpg"),
            ("Un chien", "https://static.streamlit.io/examples/dog.jpg"),
            ("Un hibou", "https://static.streamlit.io/examples/owl.jpg"),
            ("Chat tigré", "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg"),
            ("Chat qui regarde", "https://upload.wikimedia.org/wikipedia/commons/4/4d/Cat_November_2010-1a.jpg"),
            ("Chaton", "https://upload.wikimedia.org/wikipedia/commons/b/bb/Kittyply_edit1.jpg"),
        ]

        for i in range (0, len(photos),3) : 
            colonnes = st.columns(3)
            for colonne, (titre,url) in zip(colonnes, photos[i:i+3]) : 
                with colonne : 
                    st.header(titre)
                    st.image(url)


elif st.session_state["authentication_status"] is False:
    st.error("Le nom d'utilisateur ou le mot de passe est incorrect.")

elif st.session_state["authentication_status"] is None:
    st.warning("Les champs nom d'utilisateur et mot de passe doivent être remplis.")

