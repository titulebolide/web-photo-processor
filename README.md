# Script de préparation des photos pour le site de l'AP

## Installation
Il y a besoin de librairies python à installer via pip:

```bash
python3 -m pip install -r requirements.txt
```

## Utilisation
```bash
./preparePhoto.py --source DOSSIER_SOURCES --target DOSSIER_OU_EXPORTER
```
Crée dans le `DOSSIER_OU_EXPORTER` deux dossiers : `zips` et `photos`.
(Si ce dossier n'existe pas, il sera créé)
Il suffira ensuite de copier leur contenu dans les dossiers du même nom dans `/data` sur `ap-storage`

## Remarques
Les photos origniales doivent avoir leur noms formatés de la façon suivante:

`loginfrankiz&lerestedunom.jpg`

(Le nom doit commencer avec le login frankiz et le login frankiz doit être terminé par une esperluette)

*En pratique, on peut utiliser l'esperluette comme un séparateur de champs, e.g.: `franck.pacard&11-12-202&2.jpg`. Mais c'est libre à vous d'en faire ce que vous voulez.*

Laissez les noms des fichiers contenus dans le dossier `zips` et `photos` inchangés!
Le login frankiz présent au début du nom de fichier est utilisé par le site.

## Si jamais
```bash
./preparePhoto.py --help
```
