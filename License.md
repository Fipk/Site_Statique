# Convertisseur MD en HTML

Pour pouvoir utiliser ce convertisseur vous aurez besoin de:
* Markdown2
* Argparse

Pour les installer rentrez:
* **Markdown2 :** `pip install markdown2`
* **Argparse :** `pip install argparse`

Ensuite clonez ce repository puis allez dans le fichier cloné.

Puis dans votre invité de commande rentrez:

`python main.py -i fichier_a_convertir.md -o nom_du_fichier_converti.html`

ou

`python main.py --input fichier_a_convertir.md --output nom_du_fichier_converti.html`

Le -i ou --input va permettre d'ouvrir le fichier à convertir et -o ou --output va permettre de choisir le fichier ou sera conservé les changements.

Toutefois vous pouvez aussi rajouter des options supplémentaires comme cela:

`python index.py -i fichier_a_convertir.md -o nom_du_fichier_converti.html -a`

Le -a va permettre de traduire en allemand le fichier.
Pour plus d'options vous pouvez aussi tapez:

`python index.py -h`

## Licence
BSD 3-Clause License