Le capteur est interrogé toutes les 0.5 secondes. Si un mouvement est détecté, le capteur envoie un signal à la carte qui met le pin relais (GPIO27) sur niveau haut(HIGH), ce qui active la pompe. Après 0.005 secondes, le pin relais (GPIO27) est remis sur niveau bas(LOW), ce qui arrête la pompe. Après une temporisation de 10 secondes(pour laisser souffler le processeur), on refait la même manoeuvre et ainsi de suite.

Prérequis :
1. Avoir un Raspberry avec une distribution Linux (« Raspbian » de préférence) installée.
2. Si vous n’avez pas de module « gpiozero », installez-le en tapant la ligne suivante dans votre console:
pip install gpiozero
3. Assurez-vous que la librairie Rpi est installée et que vos composants sont bien connectés au Raspberry comme décrit précédemment.
4. Créer un fichier d’extension .py (par exemple: diy.py) et mettez-y le code ci-haut, puis sauver le fichier.

Comment exécuter le code
En mode console, tapez la ligne suivante pour lancer le programme : python diy.py

