### Setup
```
pip install fastapi uvicorn pandas
```
Mettre les 3 csv users.csv, actions.csv, books.csv dans un dossier data à la racine du repo. 

Executer le script generate_pseudos.py dans utils pour ajouter des username fictifs à tous les users.

### Run

```
uvicorn main:app --reload
```
