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
   * Création d'un environnement virtuel adapté au projet (environment.yml)
   * Automatiser les deux notebook- Je vais finalement automatiser le notebook de la tâche 3.
 
    Résultat :
Aucun problème majeur de reproduction n’a été rencontré. Les figures obtenues (PCA, matrices de confusion, matrices de connectivité) sont très similaires à celles rapportées par l’étudiant, ce qui confirme la reproductibilité globale du pipeline.

    Limite identifiée :
Le modèle utilisait les mêmes données pour l’entraînement et le test (sub-005), ce qui introduit un biais important et empêche toute évaluation valide de la généralisation.

- Tâche 2: Extension multi-sujets
  L’analyse initiale portait uniquement sur le participant sub-005. Je vais adapter le notebook afin d’appliquer l'analyse aux cinq participants (sub-001 à sub-005).

  Cette tâche comprend :
   * Vérifier pour chaque sujet la présence et la cohérence des fichiers BOLD (*_bold.nii) et des fichiers d’events (*_events.tsv), en documentant les runs manquants, les essais invalides ou les incohérences de structure
   * Combiner tous les fichiers events.tsv des sujets dans un tableau global, vérifié la présence des colonnes essentielles (subject, onset,	duration,	genre, track, start, end), documenté le nombre d’essais par sujet et inspecté les genres présents, afin d’identifier d’éventuels problèmes d’incohérence entre sujets
   * Adapter le notebook d’analyse (prétraitement basé sur l’atlas Schaefer, extraction de connectivité ROI‑ROI, PCA, classification par Random Forest) pour qu’il s’applique à l’ensemble des cinq participants (sub-001 à sub-005)
   * Génération et comparaison des matrices de confusion par sujet pour explorer les confusions de genres les plus fréquentes, ainsi qu’une matrice de confusion moyenne sur l’ensemble des sujets.

   Résultat :
L’extension s’est faite sans problème technique majeur. Le pipeline est maintenant fonctionnel pour plusieurs sujets.

   Performance :

Exactitude moyenne : 10,8 % (niveau du hasard)
Variabilité interindividuelle : 7 % à 12 %

Cela montre que les patterns de connectivité extraits ne permettent pas de discriminer efficacement les genres musicaux.
     
- Tâche 3: Intégration des données prétraité voxel-wise (.npy).
  En plus des données brutes, des matrices voxel-wise prétraitées sont disponibles au format .npy. Je vais:
  * Adapter le notebook de l'étudiant pour analyser les données pré traités de tous les participants
  * Comparer les matrices générées avec celles obtenues via le notebook basé sur les données brutes (OpenNeuro)
  * Automatiser le notebook
  * Vérifier la cohérence des résultats avec ceux rapportés dans l'article publié
  * Documenter les différences potentielles liées au prétraitement
 
  Difficulté majeure :
L’automatisation du notebook a demandé beaucoup de temps, notamment pour :

gérer les chemins de données
structurer les entrées/sorties
rendre le pipeline réutilisable sans intervention manuelle

  Résultat :

Pipeline automatisé fonctionnel
Résultats globalement similaires à la tâche 2
Légère amélioration pour certains sujets (ex: sub-001)

  Conclusion :
Le prétraitement améliore légèrement le signal, mais ne résout pas le problème principal lié à la représentation des données.
 
# Analyse des matrices de corrélation de la tâche 1, 2 et 3:

Pour la tâche 1, le modèle a été construit en utilisant les données de test du participant #5 à la fois comme données d’entraînement et comme données de test. Cette approche ne permet pas une évaluation valide de la capacité de généralisation du modèle. Même si le Random Forest est relativement robuste au surapprentissage, ce type de biais compromet fortement l’interprétation des performances.

<img width="738" height="748" alt="pca_confmax" src="https://github.com/user-attachments/assets/ebf66ec3-63fc-4b16-9758-5ea6e0061740" />


La matrice de confusion montre néanmoins que le modèle ne parvient pas à identifier des patrons discriminants entre les genres musicaux. Les confusions observées (pop–métal, métal–classique, jazz–blues) suggèrent que les signaux extraits à partir de l’atlas de Schaefer (2018) ne permettent pas de distinguer clairement les catégories. Cela peut indiquer que les régions définies par cet atlas, ne sont pas suffisamment spécifiques aux caractéristiques auditives ou musicales nécessaires pour la classification des genres.

Dans la tâche 2, le modèle a été entraîné sur les données d’entraînement de l’ensemble des participants, puis évalué sur des données de test indépendantes. Les résultats montrent une exactitude globale de 10,8 %, avec des variations interindividuelles allant de 7 % à 12 % (sub-001 : 7,3 %, sub-002 : 10,2 %, sub-003 : 12,2 %, sub-004 : 7,9 % et sub-005 : 7,9 %).

<img width="1135" height="1157" alt="cm_sub-001" src="https://github.com/user-attachments/assets/4ab80d88-22ba-4889-a131-f6fc648d7986" />
<img width="1115" height="1157" alt="cm_sub-002" src="https://github.com/user-attachments/assets/a83a8ae5-10af-4d74-bbb6-122f53a267c8" />
<img width="1135" height="1157" alt="cm_sub-003" src="https://github.com/user-attachments/assets/b19fa1ef-c344-48ac-bb8a-79cbc2c7abbf" />
<img width="1115" height="1157" alt="cm_sub-004" src="https://github.com/user-attachments/assets/2ece4bc8-4ad8-49df-9f3b-6744df23326c" />
<img width="1115" height="1157" alt="cm_sub-005" src="https://github.com/user-attachments/assets/79791713-b4f0-42e6-98bf-b1444b888b2d" />


Ces performances, proches du hasard, confiment que les patterns d’activation extraits via l’atlas de Schaefer ne contiennent pas suffisamment d’information discriminante pour permettre au modèle de différencier les genres musicaux. Cela pourrait s’expliquer par le fait que cet atlas, bien adapté à l’étude de réseaux fonctionnels à grande échelle, manque de résolution ou de spécificité dans les régions auditives fines (par exemple, le gyrus inférieur temporal et le gyrus temporal supérieur), qui sont cruciales pour le traitement des caractéristiques musicales.

Dans la tâche 3, l’utilisation de données prétraitées n’a pas permis d’améliorer l’exactitude globale (toujours 10,8 %), bien que certaines améliorations individuelles soient observées (sub-001 : 14,6 %, sub-002 : 12,1 %). Cette légère amélioration suggère que le prétraitement peut renforcer certains signaux individuels, mais qu’il ne compense pas les limites liées à la représentation des données elle-même. Le problème ne semble pas uniquement lié au bruit ou à la qualité des données, mais plutôt à la pertinence des régions définies par l’atlas pour la tâche étudiée.

<img width="6995" height="4717" alt="DASHBOARD_CM_GTZAN" src="https://github.com/user-attachments/assets/21e129b0-98cd-4aca-abb3-a99ed5578a07" />


Dans l’ensemble, les résultats indiquent que le modèle présente une capacité prédictive très limitée. Au-delà du choix du modèle, ces résultats mettent surtout en évidence l’importance du choix de l’atlas. L’atlas de Schaefer (2018), bien qu’optimal pour l’étude de la connectivité fonctionnelle à grande échelle, pourrait ne pas être le plus adapté pour des analyses fines liées à la perception auditive ou musicale. Il serait donc pertinent d’explorer d’autres atlas plus spécialisés dans les régions auditives (par exemple, un atlas Destrieux ou Harvard-Oxford) ou d’augmenter la résolution des données afin de mieux identifier les signaux neuronaux spécifiques aux genres musicaux.

# Rôle de l’intelligence artificielle dans le projet

La réalisation des trois tâches a été assistée par des outils d’intelligence artificielle, notamment ChatGPT (GPT-5) et Perplexity Pro.

L’IA a joué un rôle important pour le débogage et la compréhension du code. Il m'a aidé a:
* Identifier rapidement les erreurs (chemins, formats de données, dépendances)
* Expliquer le fonctionnement des notebooks et du pipeline
* Aider à la transformation d’un notebook en pipeline reproductible et automatique 

Cependant, toutes les suggestions ont été vérifiées, adaptées et validées avant leur intégration dans le projet.
<img width="170" height="77" alt="image" src="https://github.com/user-attachments/assets/98185aa5-be64-4b19-8db4-05de6fd4f5c7" />
