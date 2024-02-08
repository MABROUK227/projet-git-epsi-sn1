
# Demander le nom et le prénom de l'utilisateur
nom = input('Quel est ton nom ?: ')
prenom = input('Quel est ton prénom ?: ')

# Afficher le nom et le prénom de l'utilisateur
print(f"Tu t'appelles {nom} {prenom}")

# Demander l'âge de l'utilisateur et vérifier si c'est un nombre entier
while True:
    age_str = input('Quel est ton âge ?: ')
    if age_str.isdigit():  # Vérifie si l'entrée est un nombre entier
        age = int(age_str)
        break
    else:
        print("Veuillez entrer un nombre entier pour l'âge.")

# Calculer l'année de naissance de l'utilisateur
annee_de_naissance = 2024 - age 

# Afficher l'année de naissance
print(f"Tu es né(e) en {annee_de_naissance}")
