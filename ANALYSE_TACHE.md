# Analyse des matrices de corrélation de la tâche 1, 2 et 3:

Pour la tâche 1, le modèle a été construit en utilisant les données de test du participant #5 à la fois comme données d’entraînement et comme données de test. Cette approche ne permet pas une évaluation valide de la capacité de généralisation du modèle. Même si le Random Forest est relativement robuste au surapprentissage, ce type de biais compromet fortement l’interprétation des performances.

La matrice de confusion montre néanmoins que le modèle ne parvient pas à identifier des patrons discriminants entre les genres musicaux. Les confusions observées (pop–métal, métal–classique, jazz–blues) suggèrent que les signaux extraits à partir de l’atlas de Schaefer (2018) ne permettent pas de distinguer clairement les catégories. Cela peut indiquer que les régions définies par cet atlas, ne sont pas suffisamment spécifiques aux caractéristiques auditives ou musicales nécessaires pour la classification des genres.

Dans la tâche 2, le modèle a été entraîné sur les données d’entraînement de l’ensemble des participants, puis évalué sur des données de test indépendantes. Les résultats montrent une exactitude globale de 10,8 %, avec des variations interindividuelles allant de 7 % à 12 % (sub-001 : 7,3 %, sub-002 : 10,2 %, sub-003 : 12,2 %, sub-004 : 7,9 % et sub-005 : 7,9 %).

<img width="1135" height="1157" alt="cm_sub-001" src="https://github.com/user-attachments/assets/4ab80d88-22ba-4889-a131-f6fc648d7986" />
<img width="1115" height="1157" alt="cm_sub-002" src="https://github.com/user-attachments/assets/a83a8ae5-10af-4d74-bbb6-122f53a267c8" />
<img width="1135" height="1157" alt="cm_sub-003" src="https://github.com/user-attachments/assets/b19fa1ef-c344-48ac-bb8a-79cbc2c7abbf" />
<img width="1115" height="1157" alt="cm_sub-004" src="https://github.com/user-attachments/assets/2ece4bc8-4ad8-49df-9f3b-6744df23326c" />
<img width="1115" height="1157" alt="cm_sub-005" src="https://github.com/user-attachments/assets/79791713-b4f0-42e6-98bf-b1444b888b2d" />


Ces performances, proches du hasard, confiment que les patterns d’activation extraits via l’atlas de Schaefer ne contiennent pas suffisamment d’information discriminante pour permettre au modèle de différencier les genres musicaux. Cela pourrait s’expliquer par le fait que cet atlas, bien adapté à l’étude de réseaux fonctionnels à grande échelle, manque de résolution ou de spécificité dans les régions auditives fines (par exemple, le gyrus inférieur temporal et le gyrus temporal supérieur), qui sont cruciales pour le traitement des caractéristiques musicales.

Dans la tâche 3, l’utilisation de données prétraitées n’a pas permis d’améliorer l’exactitude globale (toujours 10,8 %), bien que certaines améliorations individuelles soient observées (sub-001 : 14,6 %, sub-002 : 12,1 %). Cette légère amélioration suggère que le prétraitement peut renforcer certains signaux individuels, mais qu’il ne compense pas les limites liées à la représentation des données elle-même. Le problème ne semble pas uniquement lié au bruit ou à la qualité des données, mais plutôt à la pertinence des régions définies par l’atlas pour la tâche étudiée.

Dans l’ensemble, les résultats indiquent que le modèle présente une capacité prédictive très limitée. Au-delà du choix du modèle, ces résultats mettent surtout en évidence l’importance du choix de l’atlas. L’atlas de Schaefer (2018), bien qu’optimal pour l’étude de la connectivité fonctionnelle à grande échelle, pourrait ne pas être le plus adapté pour des analyses fines liées à la perception auditive ou musicale. Il serait donc pertinent d’explorer d’autres atlas plus spécialisés dans les régions auditives (par exemple, un atlas Destrieux ou Harvard-Oxford) ou d’augmenter la résolution des données afin de mieux identifier les signaux neuronaux spécifiques aux genres musicaux.
