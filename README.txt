##Test Technique
**************
Le script est détaillé au niveau du fichier test.ipynb
******
1) Lecture des 4 fichiers CSV.

2) Insertion dans la base de données Postgresql.

3)Groupper les donnés du fichier "Partner.csv" afin d'avoir le nombre des partenaires et le nombre des vendeurs pour chaque partenaire.

4)Calculer le nombre des vendeurs inactifs, sachant que la definition d'un vendeur inactif est celui qui posséde ni de crédit ni de débit au niveau du fichier balance.csv .

5)Afficher les partenaires qui ont des vendeurs inactifs.

6) Calculer le nombre des vendeurs actifs, rappelant qu'un vendeur actif a au moins un crédit ou un débit.

7) afficher le nombre des vendeurs actifs pour chaque partenaire.

8) Calculer le nombre des transactions efféctuées par chaque partenaire.

9) calculer le nombre des transactions effecuées par chaque vendeur.

10) Calculer le nombre des transactions efféctuées par chaque partenaire périodiquement (toute la période/par moi/par semaine).

11) afficher le meuilleur partenaire pour chaque période.

12) Calculer la moyenne des transactions pour chaque période.

13) Calculer la moyenne des transactions par jour.

14) Calcler la moyenne générale des transactions.

15) Calculer le nombre des transactions effectuées par date.

*****

La artie de visualisation

GRAPHIQUE 1: Tableau affiche le nombre des transactions total par chaque partenaire.
GRAPHIQUE 2: (en haut à droite) tableau qui montre nombre des transactions effectués par chaque vendeurs avec chaque partenaire. Ceci permet de visualiser la meilleure combinaison partenaire-vendeur.
GRAPHIQUE 3: (en bas à gauche) Graphique de Serie temporelle montre l'activité des partenaires ainsi que la plage de temps.
GRAPHIQUE 4: (en bas à droite) Graphique de Serie temporelle montre la moyenne d'activité des partenaires ainsi que la plage de temps.
GRAPHIQUE 5: (en bas) Graphique à secturs montre les statistiques globals.
