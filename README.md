
# Projet Django : Gestion de Produits, Fournisseurs et Commandes

Bienvenue dans notre projet Django 

## Sommaire
- [Introduction](#introduction)
- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation et Lancement de l'Application](#installation-et-lancement-de-lapplication)
- [Guide d'Utilisation](#guide-dutilisation)
- [Liens et Ressources](#liens-et-ressources)

## Introduction

Ce projet a été développé dans le cadre d'un projet universitaire pour fournir une solution de gestion de produits avec la prise en charge des fournisseurs et des commandes. Il inclut des fonctionnalités permettant de :
- Lier des fournisseurs aux produits.
- Enregistrer et gérer des commandes.
Le projet utilise Django comme framework backend et est conçu pour être facilement extensible avec des fonctionnalités d'administration.

## Fonctionnalités

Voici un aperçu des fonctionnalités principales de ce projet :

1. **Gestion des Produits** : Création, mise à jour et affichage détaillé des produits. Chaque produit peut être associé à plusieurs fournisseurs avec des prix spécifiques.
2. **Gestion des Fournisseurs** : Création et mise à jour des informations des fournisseurs.
3. **Stock et Prix des Produits** : Association de chaque produit à des fournisseurs avec les prix spécifiques HT et TTC, ainsi que les niveaux de stock.
4. **Gestion des Commandes** : 
5. **Fonctionnalités d'Administration** : Interface d'administration Django personnalisée pour la gestion rapide des produits, fournisseurs et commandes.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- **Python** (version 3.13 ou supérieure)
- **Django** (version mentionnée dans `requirements.txt`)
- **npm** et **Node.js** pour installer les dépendances frontend

## Installation et Lancement de l'Application

Suivez ces étapes pour configurer et exécuter le projet en local :

1. Créer un venv :
   ```bash
   virtualenv venv
   source venv/bin/activate
   ```

2. Installez les dépendances Python :
   ```bash
   pip install -r requirements.txt
   ```

3. Installez les dépendances frontend :
   ```bash
   npm add bootstrap jquery-slim @popperjs/core
   ```

4. Exécutez les migrations de la base de données :
   ```bash
   python3 manage.py migrate
   ```

5. Créez un superutilisateur pour accéder à l'interface d'administration :
   ```bash
   python manage.py createsuperuser
   ```

6. Lancez le serveur :
   ```bash
   python manage.py runserver
   ```

7. Ouvrez votre navigateur et accédez à [http://127.0.0.1:8000](http://127.0.0.1:8000) pour explorer l'application !

## Guide d'Utilisation

1. **Connexion à l'Administration** : Rendez-vous sur `/admin` et connectez-vous avec le compte superutilisateur.
2. **Ajout de Produits et de Fournisseurs** :
   - Dans l'interface d'administration, accédez aux sections "Produits" et "Fournisseurs" pour ajouter, modifier ou supprimer des entrées.
3. **Gestion des Commandes** :
   - Accédez à la section "Commandes" pour créer une commande. Ajoutez des produits, spécifiez les quantités et suivez le statut.
4. **Suivi des Stocks** :
   - Lorsqu'une commande passe à l'état "Reçue", le stock de chaque produit est automatiquement mis à jour.
5. **Recherche Avancée** :
   - Utilisez la barre de recherche de la page des produits pour trouver rapidement un élément par nom, code ou attribut.

## Liens et Ressources

- **Vidéo de démonstration** : [Lien YouTube](https://youtu.be/8UTay169WdA) pour une présentation détaillée de l'application et de ses fonctionnalités.

---

Excusez nous pour le retard.