# Catalogue 

Applications Streamlit pour explorer un petit catalogue de 19 livres de poésie : prix, note sur 5 et stock disponible. Le dépôt contient aussi une application de test avec page de connexion et album photo.


## Les quatre applications

| Fichier | Ce qu'il fait |
| --- | --- |
| `app.py` | **Explorateur** : filtre les livres, affiche des indicateurs et les classements. |
| `dashboard.py` | **Tableau de bord** : les mêmes filtres, avec des graphiques interactifs. |
| `graphiques.py` | **Galerie de graphiques - tests** : un même jeu de données affiché avec Streamlit, Matplotlib et Plotly. |
| `test.py` | **Connexion et album photo - tests** : une page de connexion qui donne accès à une page d'accueil et à un album photo. |

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

### `test.py` : connexion et album photo

- Une page de connexion gérée avec Streamlit Authenticator. Les comptes sont écrits dans le script, avec pour chacun `name`, `password`, `email`, `failed_login_attempts`, `logged_in` et `roles`.
- Une fois connecté, la barre latérale affiche « Bienvenue *nom* », un bouton Déconnexion et un menu (Accueil, Photos).
- L'album affiche les photos trois par ligne.

Comptes de test :

| Nom d'utilisateur | Mot de passe |
| --- | --- |
| `utilisateur` | `utilisateurMDP` |
| `root` | `rootMDP` |

> Ces comptes servent uniquement au test : ne réutilisez jamais ces mots de passe ailleurs.

## Lancer une application

Depuis le dossier du projet :

```bash
pip install -r requirements.txt
streamlit run app.py
```

Pour lancer les autres applications, remplacez `app.py` par `dashboard.py`, `graphiques.py` ou `album.py`. L'application s'ouvre dans votre navigateur, par défaut sur http://localhost:8501.

> Lancez la commande depuis le dossier du projet : les scripts lisent les données avec le chemin relatif `data/livres_poetry.csv`.

## Déployer sur Streamlit Community Cloud

1. Poussez le dépôt sur GitHub, avec le fichier `requirements.txt` à la racine.
2. Sur [share.streamlit.io](https://share.streamlit.io), connectez-vous avec votre compte GitHub, puis cliquez sur **Create app**.
3. Choisissez le dépôt, la branche (`main`) et le fichier principal de l'application à déployer (par exemple `album.py`).
4. Cliquez sur **Deploy**. L'application est mise en ligne avec une URL publique, et se met à jour à chaque `git push`.

Chaque application se déploie séparément : pour en mettre plusieurs en ligne, recommencez l'étape 2 en changeant de fichier principal.

Contenu de `requirements.txt` :

```
streamlit
pandas
matplotlib
plotly
streamlit-authenticator
streamlit-option-menu
```

## Organisation du projet

```
app-catalogue/
├── app.py               # explorateur
├── dashboard.py         # tableau de bord
├── graphiques.py        # galerie de graphiques
├── album.py             # connexion et album photo
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

Python, Streamlit, pandas, Matplotlib, Plotly, Streamlit Authenticator, streamlit-option-menu.

![alt text](<Capture d'écran 2026-11-13 110135.png>)
![alt text](<Capture d'écran 2026-11-16 164548.png>)