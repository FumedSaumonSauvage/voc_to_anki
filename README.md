# Vocabulary list (on paper) in Japanese -> French to Anki & others, using Mistral VLM

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
- `--type`: "flashdeck" (json custom) ou "anki" (un txt à importer, séparateur `;`). Si tu choisis Anki, oublie pas de mettre un fichier .txt en `--out`

Dans ton terminal avec le venv activé:
```
python main.py --in_dir ./photos --type flashdeck --out deck.json --autocorrect --name "Turbo vocab"
```
(choisis tes options)


## Notes

- J'avais mis une option pour changer de langue mais j'ai pas fini et ca sert objectivement à rien
- Pour que ca aille plus vite, compresse tes images (`jpegoptim --size 800k *.jpg` sur linux)


## English version

Options: 
- `--autocorrect`: Auto-corrects words if your Japanese -> French vocabulary list is poorly translated (which is the case for mine). Japanese takes priority.
- `--in_dir`: The directory containing your input images.
- `--out`: The output file path.
- `--type`: "flashdeck" (custom JSON) or "anki" (a .txt file for import, using ; as a separator). If you choose Anki, don't forget to use a .txt extension for the --out file.

Just translate the instructions if you need more