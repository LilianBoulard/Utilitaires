# coding: utf-8

"""
Cet utilitaire copie les fichiers avec certaines extensions d'un dossier à un autre.
"""

import os, shutil

# Source et destination. Inclure "\\" à la fin.
src = "C:\\Temp\\Source\\"
dst = "C:\\Temp\\Destination\\"

# Copie les fichiers qui ont une des extensions suivantes.
acceptedExt = ["pdf"]


# ----------------------------------


print("Copie...")

# Passe à travers tous les dossiers de la source et récupère :
# root : chemin complet du dossier (racine comprise)
# subdirs : liste contenant tous les dossiers trouvés dans le dossier actuellement analysé
# files : liste contenant tous les fichiers trouvés dans le dossier actuellement analysé
for root, subdirs, files in os.walk(src):
    dstPath = root[len(src)::]
    # Pour chaque fichier "file" dans la liste "files"
    for file in files:
        # Divise le nom du fichier en utilisant ".", puis sélectionne le dernier item de la liste générée, qui est donc l'extension, et vérifie si elle fait partie de la liste acceptedExt
        if file.split(".")[-1:][0] in acceptedExt:
            # Si le dossier destination n'existe pas
            if not os.path.exists(os.path.join(dst, dstPath)):
                # Le créé
                os.makedirs(os.path.join(dst, dstPath))
            # Copie le fichier de la source à la destination.
            shutil.copy2(os.path.join(root, file), os.path.join(dst, dstPath))

input("Terminée. Appuyez sur entrée pour fermer le programme...")
