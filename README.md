# Travail final: Brainbeats: Classifying Music Genre with fMRI Connectivity

## Description du projet:

Ce projet s’inscrit dans la continuité du travail réalisé à partir du dataset Music Genre Neuroimaging Dataset (OpenNeuro ds003720).

Cette étude cherche à comprendre comment le cerveau code les genres musicaux pendant une simple écoute, sans tâche. Cinq participants ont écouté 540 extraits de 10 genres (blues, classical, country, disco, hiphop, jazz, metal, pop, reggae, rock) pendant l’IRMf.​

Les auteurs montrent que certaines régions auditives, surtout le gyrus temporal supérieur latéral (LSTG) et le sulcus de Heschl (HS), répondent différemment selon le genre, ce qui forme une sorte de “carte” des genres dans le cortex auditif. Par exemple, les patterns d’activation pour classical et jazz se ressemblent, tout comme ceux pour rock et metal, alors que d’autres genres comme blues ou hiphop sont plus distincts.
<img width="417" height="353" alt="image" src="https://github.com/user-attachments/assets/5bc18ad5-0cbd-4140-8526-79807e211678" />

Ils ont aussi utilisé un modèle appelé modulation-transfer function (MTF): ce modèle décrit chaque extrait musical en termes de “textures sonores”, c’est‑à‑dire comment l’énergie du son fluctue dans le temps (modulations rapides ou lentes, liées au rythme) et en fréquence (modulations fines ou grossières, liées au timbre). Ils ont trouvé que le modèle MTF prédit bien quel voxel est sensible aux modulations acoustiques typiques de ce genre.

<img width="400" height="400" alt="Image article" src="https://github.com/user-attachments/assets/da89a23d-c120-4557-93a2-4a46ea193bee" />

L’étudiant ayant repris le projet a également observé, à partir de sa matrice de confusion, que certains genres ressortaient davantage que d’autres. Il a utilisé un modèle différent de celui de Nakai et al., basé sur un atlas Schaefer 100 ROI, des matrices de connectivité ROI‑ROI et un classifieur Random Forest, pour étudier la structure de connectivité cérébrale associée aux genres musicaux.
<img width="400" height="400" alt="Image étudiant" src="https://github.com/user-attachments/assets/91ce8a12-2f8c-4b86-af11-12103fc7510f" />


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

