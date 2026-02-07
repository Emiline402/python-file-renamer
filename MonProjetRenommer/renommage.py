import os # pour gérer les fichiers
#____________________________
# Script de renommage de fichiers
#____________________________
# Dossiers cotenant les fichiers
dossier = "test_dossiers"
# verifier si le dossier existe
if not os.path.exists(dossier):
    print(f"Erreur : le doosier '{dossier}' n'hexiste pas" )
    exit()  # Arreter le script
# Lister les fichiers du dossier
fichiers = os.listdir(dossier)
if not fichiers:
    print("Le dossier est vides rien a renommer")
    exit()

print("fichiers trouvés : " , fichiers)

# Demande le nouveaux nom des fichiers
nouveau_nom = input("Quel est le nouveau nom des fichiers ?")

# renommer les fichiers
for index, fichier in enumerate(fichiers):
    extension = os.path.splitext(fichier)[1] # Garder l'extension
    ancien_chemin = os.path.join(dossier, fichier)
    nouveau_chemin = os.path.join(dossier,
f"{nouveau_nom}_{index + 1}{extension}")
    os.rename(ancien_chemin, nouveau_chemin)
    print(f"{fichier}  -> {nouveau_nom}_{index +1}{extension}")

    print("renommage terminer avec succés !")

