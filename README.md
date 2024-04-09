# coin_detection
<p>Ce projet vise à développer un programme capable de détecter et d'identifier des pièces de monnaie en euros à partir d'une image. La nécessité de ce projet découle de la volonté d'automatiser le comptage de la monnaie, facilitant ainsi la tâche dans divers scénarios tels que le tri de pièces collectées ou l'assistance dans des environnements de vente.</p>

## Pour Commencer

Ces instructions vous guideront à travers l'installation et la configuration nécessaires pour exécuter le projet sur votre machine locale. Suivez ces étapes simples pour mettre en place le projet.

### Prérequis

Avant de commencer, assurez-vous d'avoir Python installé sur votre système. Ce projet a été testé avec Python 3.8, mais il devrait être compatible avec d'autres versions de Python 3. Assurez-vous également d'avoir `pip` disponible pour installer des dépendances.
Bibliotheques utilisées:
- os
- OpenCV
- numpy
- matplotlib.pyplot
- keras
  

### Installation

1. **Cloner le dépôt**

   Ouvrez un terminal et clonez le dépôt GitHub en utilisant la commande suivante :

   ```sh
   git clone https://github.com/fati1905/coin_detection
   cd coin_detection
   ```
### Exécution

Pour exécuter le programme principal, utilisez la commande suivante dans le terminal :

```sh
createmodel.py #pour creer le modele
python main.py #pour l'executer
```


## La base de données:
<p>La base de données comprend 92 images de pièces de monnaie capturées par les étudiants du Master 1 VMI (Vision et Machine Intelligente) à Paris Cité, dans le cadre du projet du module "Introduction à l'analyse d'images". Ces images représentent des pièces de 2 euros, 1 euro, 50 centimes, 20 centimes, 10 centimes, 2 centimes et 1 centime, prises avec des smartphones ordinaires et sur divers arrière-plans. Cette diversité constitue l'un des principaux défis de ce projet.</p>
<p>Ci-dessous, vous trouverez un échantillon de quelques images extraites de notre base de données.</p>

![image](https://github.com/fati1905/coin_detection/assets/81489719/2ee0de51-bddd-4536-938a-2090caf84f20)

![image](https://github.com/fati1905/coin_detection/assets/81489719/a4d7d8ca-252a-48b8-a63e-29a86a0209ba)

<p>Notre base de données est accompagnée d'un fichier Excel, représenté dans l'image ci-dessous, qui contient les nomenclatures des images, le nombre de pièces dans chaque image ainsi que la valeur totale des pièces. Ce fichier est essentiel pour évaluer ultérieurement les performances de notre programme.</p>

![image](https://github.com/fati1905/coin_detection/assets/81489719/08640781-03e9-4dce-a6ee-33e630e0f713)

## Description du Modèle 

### Prétraitement des Images
Les images sont d'abord converties en système BGR pour l'utilisation avec la bibliothèque OpenCV. Nous appliquons ensuite une binarisation pour simplifier la détection des contours en accentuant ces derniers, ce qui permet une meilleure distinction entre les pièces et l'arrière-plan. Après la détection de contours, nous filtrons ceux-ci en fonction de leur taille et aire pour réduire le bruit et isoler les régions d'intérêt correspondant aux pièces. Cette étape préparatoire est cruciale pour la réussite de la classification ultérieure.

### Méthode de Classification
Le cœur de notre système repose sur l'utilisation de réseaux de neurones convolutionnels (CNN), reconnus pour leur efficacité dans le traitement d'images. Les CNN ont la capacité de découvrir et d'extraire des caractéristiques pertinentes des données, même celles qui ne sont pas immédiatement évidentes. En raison de similitudes dans les caractéristiques physiques des pièces de monnaie, telles que le diamètre, la couleur, et les inscriptions, le CNN se révèle être un choix judicieux pour notre objectif de classification.

### Évaluation du Modèle
L'évaluation de notre modèle se fait au cours de son entraînement, en surveillant à la fois l'exactitude générale et la perte, ainsi que l'exactitude et la perte de validation. Cette approche nous permet d'ajuster le modèle pour optimiser ses performances.

### Résultats et Observations
Les résultats varient en fonction des images testées, mettant en lumière certaines limitations de notre approche, telles que la difficulté à distinguer des pièces avec des caractéristiques très similaires ou des problèmes liés à l'orientation et au chevauchement des pièces. Cependant, notre modèle montre des performances prometteuses, en particulier avec des pièces de valeurs plus élevées.
<img width="410" alt="Capture d'écran 2024-04-09 174318" src="https://github.com/fati1905/coin_detection/assets/152429992/1b53c47f-7086-4829-90e9-2809e534e60d">
<img width="409" alt="Capture d'écran 2024-04-09 174427" src="https://github.com/fati1905/coin_detection/assets/152429992/e63644c5-5837-4b29-8623-47acd5934cac">
<img width="407" alt="Capture d'écran 2024-04-09 174646" src="https://github.com/fati1905/coin_detection/assets/152429992/62c68169-00a1-4ab2-8b74-91b62ddb6621">
<img width="389" alt="Capture d'écran 2024-04-09 174718" src="https://github.com/fati1905/coin_detection/assets/152429992/9a68bd2d-9cfd-4cc7-a389-0a20315bbee3">
<img width="384" alt="Capture d'écran 2024-04-09 174744" src="https://github.com/fati1905/coin_detection/assets/152429992/6806e82b-9e6e-4603-a54c-9accb2ecdfc7">

### Conclusion
Notre système de détection de pièces de monnaie démontre le potentiel des CNN pour automatiser le comptage de monnaies dans des images. Bien que des défis subsistent, en particulier en ce qui concerne la gestion du bruit de fond et des variations dans l'apparence des pièces, les résultats sont encourageants. Des travaux futurs pourront explorer des améliorations du prétraitement et l'utilisation de modèles CNN pré-entraînés pour améliorer davantage la précision de la classification.

## Contributeurs:
Ce projet a été réalisé grâce à la contribution des membres suivants :</p>
    <ul>
        <li><strong>Fatima BEN KADOUR</strong></li>
        <li><strong>Tilelli BEKTACHE</strong></li>
        <li><strong>Sabine BELAID</strong></li>
        <li><strong>Marwa RIZI</strong></li>
    </ul>
