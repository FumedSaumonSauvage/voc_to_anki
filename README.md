# Vocabulary list (on paper) in Japanese -> French to Anki apkg, using Mistral VLM

(English below)

## Instructions pour Pab

### Cree ta clef API Mistral

Tu vas sur la [console Mistral](https://console.mistral.ai/) (fais toi un compte) puis dans `API Keys` et `Generate a new key`. Faudra sans doute que tu drop un numéro de CB pour la facturation, me rappelle plus trop de comment ca marche. Bref, donne ta clef à personne.

### Pull le code et remplis les params

**Si tu as un souci avec ces instructions demande à ChatGPT et il te dira comment faire, j'ai rien testé sous Windows**

Renmomme le fichier `.env.template` en `.env` et colle ta clef API créée juste avant.

Ouvre ton terminal et crée toi un environnement virtuel à la racine du dossier, ce sera plus propre: 
```bash
python -m venv .venv
```
Ensuite: 
- Sous linux: `source .venv/bin/activate`
- Sous Windows: `.venv\Scripts\activate`

Puis:
```bash
pip install -r requirements.txt
```

### run le code

Options:
- `--autocorrect`: autocorrige les mots si ta liste de vocabulaire jap -> francais est mal traduite (c'est le cas de la mienne). Le jap a alors la priorité.
- `--in_dir`: le dossier avec tes images en input
- `--out`: le fichier output

Dans ton terminal avec le venv activé:
```
python main.py --in_dir ./test_images --out deck.apkg --autocorrect
```
(choisis tes options)


## Notes

- J'avais mis une option pour changer de langue mais j'ai pas fini et ca sert objectivement à rien
- Pour que ca aille plus vite, compresse tes images (`jpegoptim --size 800k *.jpg` sur linux)
- L'ID de deck est généré aléatoirement donc on peut pas maj les decks


## English version

Options: 
- `--autocorrect`: Auto-corrects words if your Japanese -> French vocabulary list is poorly translated (which is the case for mine). Japanese takes priority.
- `--in_dir`: The directory containing your input images.
- `--out`: The output apkg file path.

Just translate the instructions if you need more