import os
import shutil
from collections import Counter

if __name__ == "__main__":
    
    # Chercher les noms des fichiers dans un dossier
    f = []
    for (dirpath, dirnames, filenames) in os.walk(r"path"):
        f.append(filenames)
        break
    print(f[0])
    files = f[0]
    
    # Chercher le ".truc" d'un fichier
    types = []
    
    for i in range(len(files)):
        for j in range(len(files[i])):
            if files[i][j] == ".":
                types.append(files[i][j:])
    print(types)
    
    # Créer nouveau fichier
    # save_path = r"C:\Users\moham\OneDrive\Bureau\Nouveau dossier"
    # name_of_file = input("What is the name of the file: ")
    # completeName = os.path.join(save_path, name_of_file+".txt") 
    # file1 = open(completeName, "w")
    
    # Créer un nouveau dossier
    # os.makedirs(r"path")
    
    count = Counter(types)
    
    try:
        for i in count.keys():
            fo = fr"path\{i}"
            os.makedirs(fo)
    except:
        print('nop')
    try:
        for j in range(len(files)):
            if types[j] == ".py":
                shutil.move(r"path\.py")
    except:
        print("uw")
