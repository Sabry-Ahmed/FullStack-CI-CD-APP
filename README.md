
# Projet FullStack CI/CD

Ce projet FullStack CI/CD est une application simple comprenant un backend et un frontend. Il utilise Docker et Docker Compose pour faciliter le déploiement et la gestion des dépendances.

[![Backend Testing](https://github.com/Sabry-Ahmed/FullStack-CI-CD-APP/actions/workflows/Backend.yml/badge.svg)](https://github.com/Sabry-Ahmed/FullStack-CI-CD-APP/actions/workflows/Backend.yml)
[![Docker Build Backend Image](https://github.com/Sabry-Ahmed/FullStack-CI-CD-APP/actions/workflows/Backend_docker.yml/badge.svg)](https://github.com/Sabry-Ahmed/FullStack-CI-CD-APP/actions/workflows/Backend_docker.yml)
[![Docker Build Frontend Image](https://github.com/Sabry-Ahmed/FullStack-CI-CD-APP/actions/workflows/Build_frontend_image.yml/badge.svg)](https://github.com/Sabry-Ahmed/FullStack-CI-CD-APP/actions/workflows/Build_frontend_image.yml)
[![Frontend Testing](https://github.com/Sabry-Ahmed/FullStack-CI-CD-APP/actions/workflows/Front_test.yml/badge.svg)](https://github.com/Sabry-Ahmed/FullStack-CI-CD-APP/actions/workflows/Front_test.yml)



## Structure du Projet

### Backend

Le dossier `Backend` contient le code du backend de l'application. Voici une brève description des fichiers :

- **Dockerfile:** Le fichier Docker pour construire l'image du backend.
- **app.py:** Le code principal du backend avec des méthodes pour gérer les requêtes.
- **init.sql:** Un script SQL d'initialisation pour configurer la base de données.
- **requirements.txt:** Les dépendances Python du backend.
- **test_app.py:** Des tests unitaires pour le backend.

### Frontend

Le dossier `Frontend` contient le code du frontend de l'application. Voici une brève description des fichiers :

- **Dockerfile:** Le fichier Docker pour construire l'image du frontend.
- **streamlit_app.py:** Le code principal du frontend basé sur Streamlit.
- **requirements.txt:** Les dépendances Python du frontend.
- **test_streamlit_app.py:** Des tests unitaires pour le frontend.

### docker-compose.yaml

Le fichier `docker-compose.yaml` définit les services et la configuration nécessaire pour exécuter l'application avec Docker Compose. Il configure les services backend, frontend, et une base de données PostgreSQL.

## Construire et Exécuter le Projet

Suivez ces étapes pour construire et exécuter le projet :

1. Assurez-vous d'avoir Docker et Docker Compose installés sur votre machine.

2. Clonez le projet depuis le référentiel Git.

   ```bash
   git clone git@github.com:Sabry-Ahmed/FullStack-CI-CD-APP.git
   cd FullStack-CI-CD-APP
   ```

3. Dans le dossier racine du projet, exécutez la commande suivante pour construire les images Docker.

   ```bash
   docker-compose build
   ```

4. Ensuite, exécutez la commande suivante pour démarrer les services.

   ```bash
   docker-compose up
   ```
   
##Capture d'écran du Build Docker-Compose
![Build](/test.png "Build")

## Démo du Projet
![ScreenRecording2024-02-01at22 34 20-ezgif com-optimize](https://github.com/Sabry-Ahmed/FullStack-CI-CD-APP/assets/67513897/aef3339c-9d6c-4292-ba58-99519b6269a2)

5. Ouvrez votre navigateur et accédez à [http://localhost:5001](http://localhost:5001) pour voir l'API.
6. Ouvrez votre navigateur et accédez à [http://0.0.0.0:8501](http://0.0.0.0:8501) pour voir l'interface utilisateur du frontend.
L'application est maintenant opérationnelle, avec le backend exposé sur le port 5001 et le frontend sur le port 8501.

## Endpoints du Backend

- **GET /api/data:** Récupère des données depuis la base de données.
- **POST /api/insert:** Insère de nouvelles données dans la base de données.
- **POST /api/delete:** Supprime des données de la base de données.
