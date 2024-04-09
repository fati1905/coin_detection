# coin_detection
<p>Ce projet vise à développer un programme capable de détecter et d'identifier des pièces de monnaie en euros à partir d'une image. La nécessité de ce projet découle de la volonté d'automatiser le comptage de la monnaie, facilitant ainsi la tâche dans divers scénarios tels que le tri de pièces collectées ou l'assistance dans des environnements de vente.</p>

## Pour Commencer

Ces instructions vous guideront à travers l'installation et la configuration nécessaires pour exécuter le projet sur votre machine locale. Suivez ces étapes simples pour mettre en place le projet.

### Prérequis

Avant de commencer, assurez-vous d'avoir Python installé sur votre système. Ce projet a été testé avec Python 3.8, mais il devrait être compatible avec d'autres versions de Python 3. Assurez-vous également d'avoir `pip` disponible pour installer des dépendances.

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
python main.py
```


## La base de données:
<p>La base de données comprend 92 images de pièces de monnaie capturées par les étudiants du Master 1 VMI (Vision et Machine Intelligente) à Paris Cité, dans le cadre du projet du module "Introduction à l'analyse d'images". Ces images représentent des pièces de 2 euros, 1 euro, 50 centimes, 20 centimes, 10 centimes, 2 centimes et 1 centime, prises avec des smartphones ordinaires et sur divers arrière-plans. Cette diversité constitue l'un des principaux défis de ce projet.</p>
<p>Ci-dessous, vous trouverez un échantillon de quelques images extraites de notre base de données.</p>

![image](https://github.com/fati1905/coin_detection/assets/81489719/2ee0de51-bddd-4536-938a-2090caf84f20)

![image](https://github.com/fati1905/coin_detection/assets/81489719/a4d7d8ca-252a-48b8-a63e-29a86a0209ba)

<p>Notre base de données est accompagnée d'un fichier Excel, représenté dans l'image ci-dessous, qui contient les nomenclatures des images, le nombre de pièces dans chaque image ainsi que la valeur totale des pièces. Ce fichier est essentiel pour évaluer ultérieurement les performances de notre programme.</p>

![image](https://github.com/fati1905/coin_detection/assets/81489719/08640781-03e9-4dce-a6ee-33e630e0f713)

## Description du Modèle
Ce modèle est construit en utilisant Keras, une bibliothèque de deep learning haut niveau qui permet de construire et d'entraîner des modèles de réseaux de neurones de manière intuitive et rapide. 
### Architecture du Modèle
Le modèle utilise une architecture de réseau de neurones convolutifs (CNN, Convolutional Neural Network), bien adaptée à la reconnaissance d'images. Voici les composants clés de l'architecture :

#### Couche Conv2D: 
Deux couches convolutionnelles avec respectivement 32 et 64 filtres de taille 5x5, utilisant la fonction d'activation ReLU. Ces couches sont conçues pour extraire des caractéristiques des images.
#### Couche MaxPooling2D:
Deux couches de pooling max avec une fenêtre de 2x2 suivent chaque couche convolutionnelle pour réduire la dimensionnalité tout en préservant les caractéristiques importantes.
#### Couche Flatten: 
Convertit les matrices de caractéristiques en un vecteur unique, facilitant la transition entre les couches convolutives et les couches denses.
#### Couche Dense: 
Une couche dense avec 1000 unités et la fonction d'activation ReLU, suivie d'une couche de sortie avec 8 unités (correspondant aux 8 classes de pièces de monnaie) et la fonction d'activation softmax pour la classification multiclasse.
### Entraînement du Modèle
Le modèle est compilé avec la fonction de perte categorical_crossentropy, optimisé par Adam, et évalué en utilisant la précision (accuracy) comme métrique.
L'entraînement se fait sur des données divisées en un ensemble d'entraînement et un ensemble de test, avec une normalisation des pixels entre 0 et 1 pour améliorer l'efficacité de l'entraînement.
Le modèle est entraîné pour 10 époques avec un batch size de 256 et une division de validation de 30% sur l'ensemble d'entraînement pour surveiller et prévenir le surajustement.

### Résultats et Visualisation
Après l'entraînement, le modèle est évalué sur l'ensemble de test pour déterminer sa précision.
Deux graphiques sont générés pour visualiser la précision et la perte du modèle au fil des époques, offrant un aperçu de l'apprentissage et de l'amélioration du modèle au fil du temps.
Ce modèle offre une base solide pour la classification d'images de pièces de monnaie européennes, avec un potentiel d'amélioration et d'ajustement selon les besoins spécifiques du projet.

## Contributeurs:
Ce projet a été réalisé grâce à la contribution des membres suivants :</p>
    <ul>
        <li><strong>Fatima BEN KADOUR</strong></li>
        <li><strong>Tilelli BEKTACHE</strong></li>
        <li><strong>Sabine BELAID</strong></li>
        <li><strong>Marwa RIZI</strong></li>
    </ul>
