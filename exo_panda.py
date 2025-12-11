"""
Ce script charge et affiche des données d'employés à partir de fichiers CSV.
Il effectue les opérations suivantes :
1. Charge les données des employés à partir d'un fichier CSV et définit la première colonne comme index.
2. Charge les données des départements à partir d'un autre fichier CSV.
3. Calcule une colonne indiquant si chaque employé est adulte (âge > 18).
4. Trie les employés par salaire de manière décroissante.
5. Fusionne les données des employés avec celles des départements en ajoutant le responsable de chaque département.
6. Calcule si chaque employé est surpayé par rapport à la moyenne de son département.
7. Sauvegarde les données finales dans un fichier Excel et les affiche dans la console.
"""

import pandas as pd

# Charger le fichier employees
data = pd.read_csv("employees_sample.csv", index_col=0)

# Charger le fichier departments_with_heads et merger sur "department"
depts = pd.read_csv("departments_with_heads.csv")

# Calculs existants
data["is adult"] = data["age"] > 18
data = data.sort_values("salary", ascending=False)

# Merge : ajout de head_of_department (left pour garder tous les employés)
data = pd.merge(data.reset_index(), depts, on="department", how="left").set_index("name")

# Calculer la moyenne de salaire par département
avg_salary_by_dept = data.groupby("department")["salary"].transform("mean")

# Déterminer si l'employé est surpayé (salaire > moyenne du département)
data["overpayed"] = data["salary"] > avg_salary_by_dept

# Options d'affichage
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Sauvegarde et affichage
data.to_excel("data.xlsx", index=True)
print(data)