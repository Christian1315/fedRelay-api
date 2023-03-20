# README

## Technologies outside the curriculum

L'API' FedRelay, vise à offrir un service de livraison 100% connecté qui met en relation des agences de livraison et les particuliers.
La cible est : les e-commerçant, les personnes âgées de 18ans - 40ans qui ont une connaissance de l'outil informatique.

## Development Technology

- Django
- Django Rest Framework

## Execution Procedure

Accéder au projet
```bash
$ git clone https://github.com/Innov-Prime/fedrelay-api-v1.git
$ cd api-fedrelay

```
Installer les dépendances
```bash

==== INSATALLATION D\'UN NOUVEL ENVIRONNEMENT DJANGO ============
$ python -m venv env

==== INSATALLATION DE DJANGO ============
$ python -m pip install Django

==== INSATALLATION DES AUTRES DEPENDANCES  ============
$ python install -r requirement.txt 


```
Démarrer le serveur en développement
```bash
==== ACTIVATION DE L\'ENVIRONNEMENT  ============
$ env\Scripts\activate

==== DEMARRAGE REEL DU PROJET ============
$ cd src
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
