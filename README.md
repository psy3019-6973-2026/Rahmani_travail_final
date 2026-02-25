# Rahmani_travail_final

# Travail final: Brainbeats: Classifying Music Genre with fMRI Connectivity

## Description du projet:

Ce projet s’inscrit dans la continuité du travail réalisé à partir du dataset Music Genre Neuroimaging Dataset (OpenNeuro ds003720).

Cette étude vise à comprendre comment le cerveau humain représente différentes catégories musicales lors de l’écoute passive de musique. Les données ont été acquises par IRMf chez cinq participants ayant écouté 540 extraits musicaux appartenant à 10 genres distincts (blues, classique, country, disco, hiphop, jazz, metal, pop, reggae, rock).

Les travaux des chercheurs (Nakai, Koide-Majima, and Nishimoto (2021)) suggèrent que des régions auditives, notamment le cortex temporal supérieur (STG), jouent un rôle clé dans la représentation des genres musicaux. L’objectif général est d’examiner dans quelle mesure l’activité cérébrale permet de prédire le genre musical écouté à l’aide de méthodes d’apprentissage automatique.

## Pourquoi j'ai choisi ce projet?

Ce projet correspond directement à mes intérêts de recherche, qui portent sur la perception musicale de différentes population (personnes ayant une dyslexie et athlètes commotionnés) et l'effet de la musique sur le cerveau

## Les tâches que j'ai décidé de réaliser

- Tâche 1: Reproductibilité complète du notebook
   * Exécution complète du notebook original à partir d'un notebook vierge
   * Identification et documentation des erreurs ou incompatibilités
   * Vérification de la cohérence des résultats obtenus avec ceux rapportés par l'étudiant
   * Création et automatisation d'un environnement virtuel (requirements.txt)

- Tâche 2: Extension multi-sujets
  L’analyse initiale portait uniquement sur le participant sub-005.

  Je vais adapter le notebook afin d’appliquer l'analyse aux cinq participants (sub-001 à sub-005).

  Cette tâche comprend :
   * Vérifier si les fichier event files sont complètes et que l'analyse peut être fait sur tous les sujets
   * Identification des incohérences éventuelles entre sujets
     
- Tâche 3: Intégration des données prétraité voxel-wise (.npy)
  En plus des données brutes, des matrices voxel-wise prétraitées sont disponibles au format .npy. Je vais:
  * Adapter le notebook de l'étudiant pour analyser les données pré traités de tous les participants
  * Comparer les matrices générées avec celles obtenues via le pipeline basé sur les données brutes
  * Vérifier la cohérence des résultats avec ceux rapportés dans les travaux publiés
  * Documenter les différences potentielles liées au preprocessing
