import random
import pandas as pd

# Listes étendues de prénoms et de noms
first_names = [
    "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack",
    "Kathy", "Liam", "Mona", "Nina", "Oscar", "Paul", "Quincy", "Rose", "Sam", "Tina",
    "Uma", "Vince", "Wendy", "Xander", "Yara", "Zane", "Oliver", "Lucas", "Emma", "Ava",
    "Sophia", "Isabella", "Mia", "Amelia", "Harper", "Evelyn", "Abigail", "Emily", "Ella",
    "Madison", "Scarlett", "Victoria", "Aria", "Grace", "Chloe", "Camila", "Penelope",
    "Riley", "Layla", "Lillian"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez",
    "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor",
    "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez",
    "Clark", "Lewis", "Robinson", "Walker", "Young", "Allen", "King", "Wright", "Scott",
    "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson", "Baker", "Hall",
    "Rivera", "Campbell", "Mitchell", "Carter", "Roberts"
]


def mix_names(first_name, last_name):
    # Take the first half of the first name and the second half of the last name
    first_half_first = first_name[:len(first_name) // 2]
    second_half_last = last_name[len(last_name) // 2:]

    # Combine them
    mixed_name1 = first_half_first + second_half_last

    # Take the first half of the last name and the second half of the first name
    first_half_last = last_name[:len(last_name) // 2]
    second_half_first = first_name[len(first_name) // 2:]

    # Combine them
    mixed_name2 = first_half_last + second_half_first

    return random.choice([mixed_name1, mixed_name2])


def generate_username():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    mixed_name = mix_names(first_name, last_name)
    number = random.randint(1000, 9999)
    username = f"{mixed_name}{number}"
    return username


def generate_unique_usernames(count):
    usernames = set()
    while len(usernames) < count:
        usernames.add(generate_username())
    return list(usernames)

def add_usernames_to_csv(file_path):
    # Lire le fichier CSV
    df = pd.read_csv(file_path)

    # Générer autant de pseudos que de lignes dans le CSV
    usernames = generate_unique_usernames(len(df))

    # Ajouter la nouvelle colonne 'username' en deuxième position
    df.insert(1, 'username', usernames)

    # Sauvegarder le fichier CSV modifié
    df.to_csv(file_path, index=False)

if __name__ == "__main__":

    # Chemin vers le fichier CSV
    file_path = '../data/users.csv'

    # Ajouter les pseudos au CSV
    add_usernames_to_csv(file_path)