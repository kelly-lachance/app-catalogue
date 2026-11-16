import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

FICHIER = "data/livres_poetry.csv"
#Etape 1
@st.cache_data
def charger_donnees(chemin) : 
    return pd.read_csv(chemin)

df = charger_donnees(FICHIER)

st.set_page_config(page_title="Catalogue", page_icon = "U+1F4DA", layout="wide")

st.title("Catalogue de livres")

#Etape 2
with st.sidebar : 
    st.header("Filtres")
    note_mini = st.slider("Note minimale", 1,5,1)
    prix_max = st.slider("Prix maximum", 0.0, 60.0, 60.0)
    recherche = st.text_input("Le titre contient")

gauche, droite = st.columns(2)
with gauche:
    variables = {"note" : "Note", "prix_gbp" : "Prix (GBP)", "stock" : "Stock"}
    var_x = st.selectbox("Variable en abscisse", list(variables), format_func=lambda col: variables[col])
    libelle = variables[var_x]
    st.subheader(f"Comment se distribue la variable {libelle} ?")
    fig, ax = plt.subplots(figsize=(8,4))
    ax.hist(df[var_x], bins=10, color="#4C72B0", edgecolor="white")
    ax.set_xlabel(f"{libelle}")
    ax.set_ylabel("Nombre de livres")
    ax.set_title(f"Distribution de {var_x} du catalogue")
    
    st.pyplot(fig)
    if libelle =="Note" : 
        st.caption("Plus de la moitier des livres ont une note entre 4 et 5")
    elif libelle =="Prix (GBP)" : 
        st.caption("La motier des livres du catalogue ont un prix qui se situe entre 10 et 50 GBP")
    else : 
        st.caption("40% des livres ont un stock inférieur à 3")

with droite:
    type_graphique = st.radio("Type de graphique", ["Barres", "Secteurs"], horizontal=True)
    par_note=df["note"].value_counts().sort_index().rename_axis("note").reset_index(name="nombre")
    st.subheader("combien de livres par note ?")
    if type_graphique == "Barres" : 
        graphique = px.bar(par_note, x="note", y="nombre", labels={"note" : "Note", "nombre" : "Nombre de livres"})
    else : 
        graphique = px.pie(par_note, names="note", values="nombre")
    
    st.plotly_chart(graphique)

st.subheader("le prix et la note vont-ils ensemble ?")
fig = px.scatter(
    df,
    x="prix_gbp",
    y="note",
    size="stock",
    hover_name="titre",
    labels={"prix_gbp" : "Prix (GBP)", "note" : "Note sur 5"},
    title = "Chaque point est un livre",
)
st.plotly_chart(fig, use_container_width=True)
st.caption("Il ne semble pas y avoir de correlation entre le prix et la note d'un livre")
