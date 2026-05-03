# Vocabulary list (on paper) in Japanese -> French to Anki apkg, using Mistral VLM

(English below)

## Instructions pour Pab

### Cree ta clef API Gemini

Tu vas sur le [google ai studio](https://aistudio.google.com/app/api-keys) puis dans `API Keys` et `Generate a new key`. Faudra sans doute que tu drop un numéro de CB pour la facturation, me rappelle plus trop de comment ca marche. Bref, donne ta clef à personne.

Tu as le droit à 20 requetes par jour gratos sur les models flash au moment où j'ai dev ce truc.

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
- `--in_dir`: le dossier avec tes images jpeg en input
- `--out`: le fichier output
- `--deckid`: un ID de deck optionnel (genre 1234567890) précis pour faire juste des maj de deck (je sais pas si ca marche en vrai selon le client anki)

Dans ton terminal avec le venv activé:
```
python main.py --in_dir ./test_images --out deck.apkg --autocorrect
```
(choisis tes options)


## Notes

- Pour que ca aille plus vite, compresse tes images (`jpegoptim --size 800k *.jpg` sur linux)
- que du jpeg please


## English version

### Create your Gemini API key

Go to Google AI Studio (https://aistudio.google.com/app/api-keys), then under `API Keys` click `Generate a new key`. You will probably need to enter a credit card number for billing; I can’t fully remember how that works. In any case, don’t give your key to anyone.

You get 20 free requests per day on the flash models at the time I wrote this.

### Pull the code and fill the params

**If you have trouble with these instructions ask ChatGPT and it will tell you how to do it — I haven’t tested this on Windows.**

Rename the file `.env.template` to `.env` and paste the API key you created earlier.

Open a terminal and create a virtual environment at the project root to keep things clean:
```bash
python -m venv .venv
```
Then activate it:
- On Linux/macOS: `source .venv/bin/activate`
- On Windows: `.venv\Scripts\activate`

Next:
```bash
pip install -r requirements.txt
```

### Run the code

Options:
- `--autocorrect`: autocorrects words if your Japanese -> French vocabulary list has bad translations (mine does). Japanese will be prioritized when correcting.
- `--in_dir`: the folder containing your input JPEG images
- `--out`: the output file
- `--deckid`: an optional deck ID (e.g., 1234567890) used to update a specific deck (I’m not sure if this actually works depending on the Anki client)

With the venv activated in your terminal:
```
python main.py --in_dir ./test_images --out deck.apkg --autocorrect
```
(choose your options)

## Notes

- To make things faster, compress your images (`jpegoptim --size 800k *.jpg` on Linux).
- JPEG only, please.
