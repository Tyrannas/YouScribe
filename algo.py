import os

import pandas as pd

DS = None

class DataStore:
    def __init__(self, data_path="/data"):
        # Chargement des CSV dans des DataFrames
        self.users = pd.read_csv(os.path.join(data_path, 'users.csv'))
        self.books = pd.read_csv(os.path.join(data_path, 'books.csv'))
        self.actions = pd.read_csv(os.path.join(data_path, 'actions.csv'))

def init_data(data_path):
    global DS
    DS = DataStore(data_path)
    return DS

def recommend(user=None, book=None):
    if not user and not book:
        raise ValueError("Either one or both user and book must be provided")
    return [{"name": "Lord of the Rings", "confidence": 0.78, "reasons": ["You also liked The Hobbit", "It's top 10 in Fantasy"]}]