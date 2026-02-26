# Travail final: Brainbeats: Classifying Music Genre with fMRI Connectivity

## Description du projet:

Ce projet s’inscrit dans la continuité du travail réalisé à partir du dataset Music Genre Neuroimaging Dataset (OpenNeuro ds003720).

Cette étude vise à comprendre comment le cerveau humain représente différentes catégories musicales lors de l’écoute passive de musique. Les données ont été acquises par IRMf chez cinq participants ayant écouté 540 extraits musicaux appartenant à 10 genres distincts (blues, classique, country, disco, hiphop, jazz, metal, pop, reggae, rock).

Les travaux des chercheurs (Nakai, Koide-Majima, and Nishimoto (2021)) suggèrent que des régions auditives, notamment le cortex temporal supérieur (STG), jouent un rôle clé dans la représentation des genres musicaux. L’objectif général est d’examiner dans quelle mesure l’activité cérébrale permet de prédire le genre musical écouté à l’aide de méthodes d’apprentissage automatique.

## Pourquoi j'ai choisi ce projet?

Ce projet correspond directement à mes intérêts de recherche, qui portent sur la perception musicale de différentes population (personnes ayant une dyslexie et athlètes commotionnés) et l'effet de la musique sur le cerveau

## Les tâches que j'ai décidé de réaliser

- Tâche 1: Reproductibilité complète du notebook
   * Exécution complète des notebook originax brainbeats_analysis_pca_confmat.ipynb et brainbeats_visualization.ipynb à partir d'un notebook vierge
   * Identification et documentation des erreurs ou incompatibilités (versions de librairies, chemins de fichiers, dépendances manquantes)
   * Vérification de la cohérence des résultats (matrices de connectivité, PCA, matrices de confusion) obtenus avec ceux rapportés par l'étudiant
   * Création d'un environnement virtuel adapté au projet (requirements.txt)
   * Automatiser les deux notebook

- Tâche 2: Extension multi-sujets
  L’analyse initiale portait uniquement sur le participant sub-005. Je vais adapter le notebook afin d’appliquer l'analyse aux cinq participants (sub-001 à sub-005).

  Cette tâche comprend :
   * Vérifier pour chaque sujet la présence et la cohérence des fichiers BOLD (*_bold.nii) et des fichiers d’events (*_events.tsv), en documentant les runs manquants, les essais invalides ou les incohérences de structure
   * Combiner tous les fichiers events.tsv des sujets dans un tableau global, vérifié la présence des colonnes essentielles (subject, onset,	duration,	genre, track, start, end), documenté le nombre d’essais par sujet et inspecté les genres présents, afin d’identifier d’éventuels problèmes d’incohérence entre sujets
   * Adapter le notebook d’analyse (prétraitement basé sur l’atlas Schaefer, extraction de connectivité ROI‑ROI, PCA, classification par Random Forest) pour qu’il s’applique à l’ensemble des cinq participants (sub-001 à sub-005)
   * Génération et comparaison des matrices de confusion par sujet pour explorer les confusions de genres les plus fréquentes, ainsi qu’une matrice de confusion moyenne sur l’ensemble des sujets.
     
- Tâche 3: Intégration des données prétraité voxel-wise (.npy)
  En plus des données brutes, des matrices voxel-wise prétraitées sont disponibles au format .npy. Je vais:
  * Adapter le notebook de l'étudiant pour analyser les données pré traités de tous les participants
  * Comparer les matrices générées avec celles obtenues via le notebook basé sur les données brutes (OpenNeuro)
  * Vérifier la cohérence des résultats avec ceux rapportés dans l'article publié
  * Documenter les différences potentielles liées au prétraitement
