Analyse inspirée du script de Xuan Chen (CC0 1.0-  Creative Commons Zero v1.0 Universal) Utilisation commerciale autorisée, Modification libre, Distribution sans restriction, Utilisation privée
Données : Nakai, Koide-Majima, and Nishimoto (2022). Music genre neuroimaging dataset. Data in Brief. 40, 107675. https://doi.org/10.1016/j.dib.2021.107675


Télécharger les données brutes:

# 1. Active l'environnement
conda activate project-env

# 2. Clone le dataset OpenNeuro
datalad clone https://github.com/OpenNeuroDatasets/ds003720.git sourcedata/ds003720

# 3. Récupère les fichiers (~46GB)
cd sourcedata/ds003720
datalad get .
cd ../..

