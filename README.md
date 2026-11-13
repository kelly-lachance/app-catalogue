# Catalogue de livres

Application Streamlit pour explorer un catalogue de livres de poésie (fichier `data/livres_poetry.csv`).

## Ce que fait l'application

- **Filtrer** les livres depuis la barre latérale : note minimale, prix maximum (en GBP) et recherche dans le titre.
- **Afficher** les livres retenus avec quelques indicateurs : nombre de livres, prix moyen, note moyenne et stock moyen.
- **Classer** la sélection : les 5 livres les mieux notés et les 5 moins chers.
- **Consulter** les données brutes complètes dans une section repliable.

## Lancer l'application

Depuis le dossier du projet :

```bash
pip install -r requirements.txt
streamlit run app.py
```

L'application s'ouvre ensuite dans votre navigateur (par défaut sur http://localhost:8501).
<img width="1901" height="902" alt="image" src="https://github.com/user-attachments/assets/41178b16-d813-4df5-b3c3-9e2fe034e40f" />