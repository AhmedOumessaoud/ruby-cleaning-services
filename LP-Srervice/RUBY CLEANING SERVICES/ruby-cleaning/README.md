# Ruby Cleaning Services — Agadir

Landing page HTML/CSS/JavaScript reprenant le design fourni : vagues bleues, titres en capsules, quatre cartes de services, quatre engagements, parcours en trois étapes, matériel, bandeau WhatsApp et catégories de pied de page.

## Aperçu local

Depuis ce dossier :

```powershell
python -m http.server 8080 --bind 127.0.0.1
```

Ouvrir http://127.0.0.1:8080 et actualiser avec Ctrl+F5.

## Assets et interactions

- Logo officiel fourni conservé dans assets/logo.png.
- Photos extraites du visuel fourni : assets/reference-*.jpg.
- Icônes SVG dessinées dans le HTML selon les motifs du modèle.
- Texte HTML sélectionnable et mise à l'échelle selon la largeur de la page.
- Cartes et catégories ouvrant WhatsApp avec un message adapté.
- Bandeau de contact, téléphone, Instagram et retour en haut fonctionnels.
- Ancienne version conservée dans ruby-cleaning-previous-design.zip à côté du dossier projet.

Le texte commercial reprend le modèle demandé, y compris les mentions « Qualité Garantie » et « Produits Écologiques ». Ces affirmations proviennent du visuel fourni et ne constituent pas une certification indépendante.

## Vérification et publication

python verify.py vérifie les assets, les images et les ancres (Pillow requis uniquement pour cette vérification). node --check js/main.js vérifie la syntaxe JavaScript. Le contrôle visuel par navigateur était indisponible dans cette session.

Aucune installation ni compilation n'est nécessaire pour le site. Publier le contenu de ce dossier sur un hébergement statique HTTPS. Remplacer og:image par une URL absolue sur le domaine final pour le partage social.
