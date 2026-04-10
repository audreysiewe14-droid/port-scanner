# Port Scanner

Un scanner de ports simple construit en Python from scratch.

## Description

C'est un outil de reconnaissance reseau qui scanne les 1024 premiers ports d'une machine cible et affiche les ports ouverts avec leur service associe.

## Technologies

-Python 3
-Module socket
-Module sys
-Module datetime

##Installation

\bash
git clone https://github.com/audreysiewe14-droid/port-scanner.git
cd port_scanner
\

##Utilisation

\bash
python3 port_scanner.py <adresse_ip>
\

###Exemple
\bash
python3 port_scanner.py 127.0.0.1
\

##Resultat attendu

\
Scan de 127.0.0.1
Debut:14:32:10
------------------------------
[+]Port 631 Ouvert -> ipp
------------------------------
Fin:14:34:25
Duree:0:02:15

Scan termine!
\

##Avertissement
Cet outil est destine uniquement a des fins educatives.
Nejamais scanner des machines  sans autorisation explicite.

##Auteure
**Audrey** --Etudiante en L2 informatique,future experte en cybersecurite 
