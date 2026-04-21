Analyse inspirée du script de Xuan Chen (CC0 1.0-  Creative Commons Zero v1.0 Universal) Utilisation commerciale autorisée, Modification libre, Distribution sans restriction, Utilisation privée
Données : Nakai et al. (2023), OpenNeuro ds003720
Pipeline : airoh-pipeline/airoh-template

Télécharger les données brutes:

# 1. Active l'environnement
conda activate project-env

# 2. Clone le dataset OpenNeuro
datalad clone https://github.com/OpenNeuroDatasets/ds003720.git sourcedata/ds003720

# 3. Récupère les fichiers (~46GB)
cd sourcedata/ds003720
datalad get .
cd ../..

