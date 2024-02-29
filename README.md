Manuel d'utilisation - Outil de Génération de Profils d'Altitude à partir de Fichiers GPX
Cet outil vous permet de générer un profil d'altitude à partir d'un fichier GPX contenant des données GPS d'un parcours. Le profil d'altitude sera représenté sous forme d'image PNG.

Installation: 
- Installer Python 
- Installer les bibliotèques "Matplotlib", "NumPy" et "gpxpy" et les modules "geopy" et "scipy" ("pip install" puis nom de la bibliothèque dans Powershell)
- Pour avoir un aperçu des logs, le script peut être lancé dans VisualStudio Code (il faudra alors aussi installer l'addon python et python debugging).


Paramètres Réglables:
L'outil dispose de plusieurs paramètres que vous pouvez ajuster selon vos préférences pour personnaliser le profil d'altitude généré.

1. gpx_file_path (obligatoire)
Description : Chemin vers le fichier GPX contenant les données GPS du parcours.
Emplacement : Ligne 9 du fichier GPX2profil.py.
Exemple : gpx_file_path = "path/vers/votre/fichier.gpx"
2. fill_color (optionnel)
Description : Couleur de remplissage du profil d'altitude. Vous pouvez spécifier une couleur en utilisant son code hexadécimal.
Emplacement : Ligne 34 du fichier GPX2profil.py.
Valeur par défaut : '#FFFFFF' (blanc).
Exemple : fill_color = '#00FF00' (vert).
3. smooth_factor (optionnel)
Description : Facteur de lissage du profil d'altitude. Plus la valeur est élevée, plus le profil sera lissé.
Emplacement : Ligne 35 du fichier GPX2profil.py.
Valeur par défaut : 90.
Exemple : smooth_factor = 50.
4. flatten_factor (optionnel)
Description : Facteur d'aplatissement vertical du profil d'altitude. Une valeur proche de 1 donnera un profil plus plat, tandis qu'une valeur plus proche de 0 donnera un profil plus élevé.
Emplacement : Ligne 36 du fichier GPX2profil.py.
Valeur par défaut : 0.7.
Exemple : flatten_factor = 0.5.
5. top_margin (optionnel)
Description : Marge supérieure du profil d'altitude. Permet de laisser de l'espace au-dessus du profil.
Emplacement : Ligne 37 du fichier GPX2profil.py.
Valeur par défaut : 30 pixels.
Exemple : top_margin = 50.
Utilisation
Assurez-vous d'avoir Python et les bibliothèques Matplotlib, NumPy et gpxpy installées sur votre système.
Placez le fichier GPX contenant les données GPS du parcours dans le même répertoire que le fichier GPX2profil.py.
Ouvrez le fichier GPX2profil.py dans un éditeur de texte.
Réglez les paramètres souhaités en fonction de vos préférences en modifiant les valeurs correspondantes (lignes 34 à 37).
Enregistrez les modifications apportées au fichier GPX2profil.py.
Exécutez le script GPX2profil.py en ligne de commande ou via un environnement Python.
Le profil d'altitude sera généré sous forme d'image PNG dans le même répertoire que le fichier GPX2profil.py.
Assurez-vous d'avoir le fichier GPX correctement formaté avec les données GPS de votre parcours. Vous pouvez également ajuster les paramètres pour obtenir le profil d'altitude souhaité.

Avertissements:
Assurez-vous que les bibliothèques Matplotlib, NumPy et gpxpy sont installées avant d'exécuter le script.
Vérifiez que le fichier GPX est correctement formaté et contient les données GPS du parcours.
Les commentaires dans le fichier GPX doivent contenir les mots "départ" et "réel" pour identifier le point de départ du parcours.
