import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

FICHIER = "data/livres_poetry.csv"

st.set_page_config(page_title="Graphiques", layout="wide")

@st.cache_data
def charger_donnees(chemin) : 
    return pd.read_csv(chemin)

df = charger_donnees(FICHIER)

note_mini = st.sidebar.slider("Note minimale", 1,5,1)
selection=df[df["note"]>=note_mini]

if len(selection) ==0:
    st.warning("Aucun livre ne correspond.")
    st.stop()

    
fig = px.histogram(
    selection,
    x="prix_gbp",
    nbins=10,
    labels={"prix_gbp" : "Prix (GBP)"},
    title = f"{len(selection)} livres notes {note_mini} ou plus",
)
st.plotly_chart(fig,use_container_width=True)

st.title("Visualiser le catalogue")
st.write(df.head())

st.subheader("Nombre de livres par note")
par_note = df["note"].value_counts().sort_index()
st.bar_chart(par_note)

st.subheader("Prix et note, livre par livre")
st.scatter_chart(df, x="prix_gbp", y="note", size="stock")

st.subheader("Repartition des prix")
fig, ax = plt.subplots(figsize=(8,4))
ax.hist(df["prix_gbp"], bins=10, color = "#4C72B0", edgecolor = "white")
ax.set_xlabel("Prix (GBP)")
ax.set_ylabel("Nombre de livres")
ax.set_title("Distribution des prix du catalogue")

st.pyplot(fig)

st.subheader("Prix et note, en interactif")
fig = px.scatter(
    df,
    x="prix_gbp",
    y="note",
    size = "stock", 
    hover_name="titre",
    labels = {"prix_gbp" : "Prix (GBP)", "note" : "Note sur 5"},
    title = "Chaque point est un livre"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Stock par livre")

fig = px.bar (
    df.sort_values("stock", ascending=False), 
    x="titre",
    y="stock",
    color="note",
    labels={"titre" : "", "stock" : "Exemplaires", "note" : "Note"},  
)
fig.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig,use_container_width=True)