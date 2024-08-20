### Unzip any file (7zip, rar, zip)

# Etape 1: Installer les dépendances nécessaires

Assurez-vous d'avoir Python 3 installé. Ensuite, installez les bibliothèques requises :

```
pip install py7zr patool tk
```

# Etape 2: Construire l'executable avec PyInstaller

```
pyinstaller --onefile --windowed unzipper.py
```
--onefile : Crée un seul fichier exécutable.
--windowed : Empêche l'ouverture d'une console lorsque vous exécutez le programme.

# Etape 3: rendez-vous dans le fichier /dist pour trouver l'executable et l'utiliser

```
cd dist
explorer .
/*puis double cliquez sur unzipper - ou */

.\unzipper.exe
```


