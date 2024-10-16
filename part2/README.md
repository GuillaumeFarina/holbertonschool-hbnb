# HBnB Application

## Aperçu du projet

L'application **HBnB** est une application Python modulaire qui suit les meilleures pratiques de développement pour les couches de Présentation, Logique Métier et Persistance. Elle est développée avec **Flask** pour le côté web et utilise un dépôt en mémoire pour le stockage temporaire des données, qui sera remplacé par une base de données plus tard dans le projet.

Ce projet met également en œuvre le modèle de conception **Facade** pour simplifier les interactions entre ces couches.

## Structure du projet

L'organisation du projet est modulaire pour permettre une meilleure maintenabilité et évolutivité. Voici la structure des répertoires :

```
hbnb/
├── app/
│   ├── __init__.py                # Initialise l'application Flask
│   ├── api/
│   │   ├── __init__.py            # Initialise les endpoints de l'API
│   │   ├── v1/
│   │       ├── __init__.py        # Version 1 de l'API
│   │       ├── users.py           # Endpoints pour les utilisateurs
│   │       ├── places.py          # Endpoints pour les lieux
│   │       ├── reviews.py         # Endpoints pour les avis
│   │       ├── amenities.py       # Endpoints pour les commodités
│   ├── models/
│   │   ├── __init__.py            # Initialise les modèles de données
│   │   ├── user.py                # Modèle de données pour les utilisateurs
│   │   ├── place.py               # Modèle de données pour les lieux
│   │   ├── review.py              # Modèle de données pour les avis
│   │   ├── amenity.py             # Modèle de données pour les commodités
│   ├── services/
│   │   ├── __init__.py            # Initialise les services
│   │   ├── facade.py              # Implémente le modèle de conception Facade
│   ├── persistence/
│       ├── __init__.py            # Initialise la couche de persistance
│       ├── repository.py          # Dépôt en mémoire pour le stockage des objets
├── run.py                         # Point d'entrée pour exécuter l'application Flask
├── config.py                      # Configuration de l'application
├── requirements.txt               # Liste des dépendances du projet
├── README.md                      # Ce fichier
```

## Instructions pour exécuter l'application

### Prérequis

- **Python 3.x** doit être installé sur votre machine.
- Les packages listés dans `requirements.txt` doivent être installés.

### Étapes d'installation

1. **Clonez le projet depuis GitHub** :

   ```bash
   git clone https://github.com/holbertonschool-hbnb.git
   cd holbertonschool-hbnb/part2
   ```

2. **Installez les dépendances** : Exécutez la commande suivante pour installer les packages nécessaires à partir du fichier `requirements.txt` :

   ```bash
   pip install -r requirements.txt
   ```

3. **Exécutez l'application Flask** : Une fois que tout est installé, lancez l'application avec :

   ```bash
   python3 run.py
   ```

L'application sera accessible à l'adresse [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Description des fichiers importants

- **`run.py`** : Le fichier principal pour démarrer l'application Flask.
- **`config.py`** : Fichier de configuration pour définir les paramètres globaux et les clés de sécurité.
- **`app/`** : Contient tous les modules de l'application, organisés en différentes couches (API, modèles, services, persistance).
- **`app/api/`** : Gère les points de terminaison de l'API pour la version actuelle.
- **`app/models/`** : Contient les classes de la logique métier comme `User`, `Place`, `Review`, etc.
- **`app/services/`** : Contient le modèle de conception Facade pour coordonner les interactions entre les différentes couches.
- **`app/persistence/`** : Contient un dépôt en mémoire pour le stockage des objets. Ce dépôt sera remplacé par une base de données dans une partie ultérieure du projet.

## Dépendances

Le fichier `requirements.txt` contient les packages suivants :

- **flask**
- **flask-restx**

Installez-les en exécutant la commande :

```bash
pip install -r requirements.txt
```

## À venir

Dans les futures parties du projet, la couche de persistance actuelle (en mémoire) sera remplacée par une solution basée sur une base de données à l'aide de **SQLAlchemy**. L'API sera également enrichie avec des fonctionnalités supplémentaires.
