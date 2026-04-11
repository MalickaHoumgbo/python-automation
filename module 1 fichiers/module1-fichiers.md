# Module 1 — Manipulation de fichiers automatique
> `os` · `pathlib` · `shutil`

---

## 1. Pourquoi ces outils ?

En contexte data, tu vas souvent recevoir des fichiers bruts (CSV, JSON, Excel) à organiser, déplacer, renommer ou vérifier avant même de les analyser. Faire ça manuellement est lent, risqué et non reproductible.

Ces trois bibliothèques te permettent d'écrire un script qui fait ce travail à ta place, de manière fiable et automatique.

---

## 2. Les 3 bibliothèques

| Bibliothèque | Rôle | Priorité |
|---|---|---|
| `os` | Interagir avec le système (ancienne méthode) | Secondaire |
| `pathlib` | Manipuler les chemins de fichiers (méthode moderne) | **Principale** |
| `shutil` | Copier, déplacer, supprimer des fichiers | Complémentaire |

> **Règle d'or** : utilise `pathlib` en priorité. `os` reste utile pour certaines opérations système. `shutil` prend le relais pour les actions physiques sur les fichiers.

---

## 3. Cours — `pathlib`

### Importer et créer un chemin

```python
from pathlib import Path

# Définir un chemin
dossier = Path("data/raw")

# Chemin absolu (depuis la racine du système)
dossier_absolu = Path("/home/malicka/projets/data/raw")
```

### Opérations essentielles

```python
from pathlib import Path

dossier = Path("data/raw")

# Vérifier si un fichier ou dossier existe
dossier.exists()          # True ou False

# Créer un dossier (et ses parents si nécessaire)
dossier.mkdir(parents=True, exist_ok=True)

# Lister tous les fichiers d'un dossier
for fichier in dossier.iterdir():
    print(fichier)

# Filtrer par extension
for csv in dossier.glob("*.csv"):
    print(csv)

# Accéder au nom, suffixe, parent
p = Path("data/raw/coffee_sales.csv")
p.name        # 'coffee_sales.csv'
p.stem        # 'coffee_sales'
p.suffix      # '.csv'
p.parent      # data/raw
```

### Construire un nouveau chemin

```python
dossier = Path("data")
fichier = dossier / "raw" / "coffee_sales.csv"
# Résultat : data/raw/coffee_sales.csv
```

> L'opérateur `/` sur des objets `Path` construit des chemins proprement,
> sans concaténation de chaînes risquée.

---

## 4. Cours — `shutil`

```python
import shutil
from pathlib import Path

source = Path("data/raw/coffee_sales.csv")
destination = Path("data/processed/coffee_sales.csv")

# Copier un fichier
shutil.copy(source, destination)

# Déplacer un fichier
shutil.move(source, destination)

# Supprimer un dossier entier (attention : irréversible)
shutil.rmtree(Path("data/temp"))
```

---

## 5. Cours — `os` (compléments utiles)

```python
import os

# Lister les fichiers d'un dossier (ancienne méthode)
os.listdir("data/raw")

# Renommer un fichier
os.rename("data/raw/old_name.csv", "data/raw/new_name.csv")

# Supprimer un fichier
os.remove("data/raw/fichier_inutile.csv")

# Obtenir le répertoire courant
os.getcwd()
```

---

## 6. Cas pratique — Organisateur de datasets

**Contexte** : tu as un dossier `downloads/` qui contient des fichiers mélangés (CSV, JSON, Excel). Tu veux les trier automatiquement dans des sous-dossiers par extension.

```python
from pathlib import Path
import shutil

# --- Configuration ---
source = Path("downloads")
destination_base = Path("data/sorted")

# Mapping extension → dossier cible
categories = {
    ".csv": "csv",
    ".json": "json",
    ".xlsx": "excel"
}

# --- Script ---
for fichier in source.iterdir():
    if fichier.is_file():
        extension = fichier.suffix.lower()
        
        if extension in categories:
            dossier_cible = destination_base / categories[extension]
            dossier_cible.mkdir(parents=True, exist_ok=True)
            
            shutil.move(fichier, dossier_cible / fichier.name)
            print(f"Déplacé : {fichier.name} → {dossier_cible}")
        else:
            print(f"Extension non reconnue : {fichier.name}")
```

**Ce que fait ce script ligne par ligne :**
1. Il parcourt tous les fichiers du dossier `downloads/`
2. Pour chaque fichier, il lit l'extension
3. Il crée le sous-dossier cible si nécessaire
4. Il déplace le fichier au bon endroit
5. Il affiche un log de ce qu'il a fait

---

## 7. Exercices

### Exercice 1 — Exploration (facile)
Écris un script qui :
1. Crée un dossier `test_module1/` dans ton répertoire courant
2. Liste tous les fichiers `.csv` présents dans ton dossier `data/`
3. Affiche pour chacun : son nom, son extension, son dossier parent

---

### Exercice 2 — Renommage automatique (intermédiaire)
Tu as des fichiers nommés de façon incohérente :
```
Coffee Sales 2023.csv
coffee_sales_2023.csv
COFFEE-SALES-2023.csv
```
Écris un script qui renomme tous les CSV d'un dossier en **snake_case minuscule** automatiquement.

*Indice : `.stem`, `.suffix`, `.rename()`, et la méthode `.lower().replace(" ", "_")`*

---

### Exercice 3 — Cas réel sur tes datasets (avancé)
En t'inspirant du cas pratique ci-dessus, écris un script adapté à ton repo `data-foundations-month1` :
1. Parcours le dossier `datasets/`
2. Crée un fichier `inventaire.txt` qui liste tous les fichiers présents avec leur taille en Ko
3. Déplace les fichiers de plus de 1 Mo dans un sous-dossier `datasets/large/`

*Indice : `.stat().st_size` retourne la taille en octets*

---

## 8. Réflexion (framework personnel)

```markdown
### Ce que j'ai fait
...

### Pourquoi
...

### Ce que ça m'a appris
...
```

---

## 9. À retenir

| Opération | Code |
|---|---|
| Créer un dossier | `Path("dossier").mkdir(parents=True, exist_ok=True)` |
| Lister les CSV | `Path("dossier").glob("*.csv")` |
| Déplacer un fichier | `shutil.move(source, destination)` |
| Copier un fichier | `shutil.copy(source, destination)` |
| Nom du fichier | `Path("fichier.csv").stem` |
| Extension | `Path("fichier.csv").suffix` |

---

*Module suivant → Module 2 : Traitements pandas automatisés*
