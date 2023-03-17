# Projet-Mastermind
Projet Mastermind

## BITD02
KHIDER Sarah

ANDREUCCI Elise

MEDENECHE Sarah

## URL de dépot du projet 
https://github.com/uvsq22204797/Projet-Mastermind.git

## Objectif du projet
L'objectif de notre projet est de programmer le jeu de plateau Mastermind comportant une interface graphique et un certain nombre de fonctionnalités.

## Les règles à implémenter ( définies par l’inventeur du jeu Mordecai Meirowitz en 1970 ) 
-Il s’agit d’un jeu à 2 joueurs dans lequel un des joueurs choisit un code secret formé de 4 pions de couleur alignés et l’autre joueur doit deviner ce code en au plus 10 essais de code ; un essai consiste à proposer un code et à le comparer au code secret; huit couleurs sont disponibles dans le jeu et
plusieurs pions du code peuvent être de la même couleur ;

-A chaque essai, le joueur qui décode acquiert l’information suivante:

*le nombre de pions bien placés ( mais il ne sait pas lesquels) ; un pion est bien placé s’il a la même couleur que le pion qui est à la même position dans le code secret ;

*et le nombre de pions mal placés; un pion est mal placé s’il a la même couleur qu’un pion du code secret qui n’est pas à une position d’un pion bien placé ; de plus chaque pion du code secret peut compter pour au plus un pion mal placé ;
Cette information peut être matérialisée par deux nombres accolés au code essayé ou bien, comme sur le jeu de plateau, par des petits pions dont le nombre indique en rouge (resp. en blanc) le nombre de pions bien (resp. mal) placés ; vous trouverez un exemple sur la figure ci-dessous ;

-Si le joueur qui décode trouve le code secret en moins de 10 essais alors il gagne, sinon c’est son adversaire qui gagne.

## Travail demandé
Il faut fournir une interface graphique permettant de jouer dans 2 modes différents :
  • mode 2 joueurs : le premier joueur choisit le code secret, puis celui-ci est caché et l’autre joueur doit le trouver ;
  
  • mode 1 joueur : idem sauf que le code secret est choisi au hasard au début du jeu ;
  
  Le choix de l’interface graphique est libre. Vous pouvez vous inspirer de la version plateau du jeu sans que cela soit une obligation.
  Votre programme doit également permettre de :
  
  • sauvegarder une partie en cours puis de la recharger ;
  
  • revenir en arrière(ce qui s’apparente à de la triche!),c’est-à-dire annuler des essais qui ont été faits ;
  
  • proposer une aide fournissant un code compatible avec les informations obtenues aux essais précédents (sans utiliser le code secret !) 






