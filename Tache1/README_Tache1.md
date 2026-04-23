Analyse inspirée du script de Xuan Chen (CC0 1.0-  Creative Commons Zero v1.0 Universal) Utilisation commerciale autorisée, Modification libre, Distribution sans restriction, Utilisation privée
Données : Nakai, Koide-Majima, and Nishimoto (2022). Music genre neuroimaging dataset. Data in Brief. 40, 107675. https://doi.org/10.1016/j.dib.2021.107675


Étapes pour télécharger les données brutes:

# 1. Créer l'environnement virtuel
conda env create -f brainbeats_env

# 2. Active l'environnement
conda activate brainbeats-env

# 3. Clone le dataset OpenNeuro
datalad clone https://github.com/OpenNeuroDatasets/ds003720.git sourcedata/ds003720

# 4. Récupère les fichiers (~46GB)
cd sourcedata/ds003720
datalad get .
cd ../..

# Ordre pour exécuter les notebooks
- brainbeats_analysis_pca_diyaa
- brainbeats_sub005_allruns_diyaa
- brainbeats_visualization_diyaa

