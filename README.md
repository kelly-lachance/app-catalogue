# Catalogue de livres

Applications Streamlit pour explorer un petit catalogue de 19 livres de poésie : prix, note sur 5 et stock disponible.


## Les trois applications

| Fichier | Ce qu'il fait |
| --- | --- |
| `app.py` | **Explorateur** : filtre les livres, affiche des indicateurs et les classements. |
| `dashboard.py` | **Tableau de bord** : les mêmes filtres, avec des graphiques interactifs. |
| `graphiques.py` | **Galerie de graphiques - tests** : un même jeu de données affiché avec Streamlit, Matplotlib et Plotly. |

### `app.py` : l'explorateur

- Filtres dans la barre latérale : note minimale, prix maximum (en GBP) et recherche dans le titre.
- Indicateurs sur la sélection : nombre de livres, prix moyen, note moyenne, stock moyen.
- Les 5 livres les mieux notés et les 5 moins chers.
- Les données brutes dans une section repliable.

### `dashboard.py` : le tableau de bord

Les filtres de la barre latérale s'appliquent à tous les graphiques.

- **Distribution d'une variable** : un histogramme dont on choisit la variable (note, prix ou stock).
- **Livres par note** : à afficher en barres ou en secteurs.
- **Prix et note** : un nuage de points où chaque point est un livre, sa taille indiquant le stock. On n'y observe pas de lien entre le prix et la note.

### `graphiques.py` : la galerie

Le même catalogue représenté de plusieurs façons : graphiques natifs de Streamlit (`st.bar_chart`, `st.scatter_chart`), histogramme Matplotlib et graphiques Plotly interactifs (nuage de points, stock par livre).

## Lancer une application

Depuis le dossier du projet :

```bash
pip install -r requirements.txt
streamlit run app.py
```

Pour lancer les autres applications, remplacez `app.py` par `dashboard.py` ou `graphiques.py`. L'application s'ouvre dans votre navigateur, par défaut sur http://localhost:8501.

> Lancez la commande depuis le dossier du projet : les scripts lisent les données avec le chemin relatif `data/livres_poetry.csv`.

## Organisation du projet

```
app-catalogue/
├── app.py               # explorateur
├── dashboard.py         # tableau de bord
├── graphiques.py        # galerie de graphiques
├── data/
│   └── livres_poetry.csv
└── requirements.txt
```

## Les données

`data/livres_poetry.csv` contient une ligne par livre :

| Colonne | Contenu |
| --- | --- |
| `titre` | titre du livre |
| `categorie` | catégorie (ici toujours « Poetry ») |
| `prix_gbp` | prix en livres sterling |
| `note` | note de 1 à 5 |
| `stock` | nombre d'exemplaires disponibles |
| `upc` | code produit unique |

## Technologies

Python, Streamlit, pandas, Matplotlib, Plotly.

![alt text](<Capture d'écran 2026-11-13 110135.png>)
![alt text](<Capture d'écran 2026-11-16 164548.png>)