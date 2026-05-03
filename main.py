import argparse
import os
import json
from model_loader import ModelLoader
from pipeline import VocPipeline

def main():
    parser = argparse.ArgumentParser(description="OCR Japonais vers Decks Flashcards")
    parser.add_argument("--in_dir", required=True, help="Dossier contenant les images")
    parser.add_argument("--out", default="deck.apkg", help="Chemin de sortie")
    parser.add_argument("--autocorrect", action="store_true", default=False)

    args = parser.parse_args()

    loader = ModelLoader()
    pipeline = VocPipeline(loader)
    
    all_vocab = []
    valid_extensions = ('.jpg', '.jpeg', '.png')
    image_files = sorted([f for f in os.listdir(args.in_dir) if f.lower().endswith(valid_extensions)])

    if not image_files:
        print("Aucune image trouvée dans le dossier.")
        return

    print(f"--- Début du traitement de {len(image_files)} images ---")

    for img in image_files:
        print(f"Analyse de {img}...")
        path = os.path.join(args.in_dir, img)
        try:
            res = pipeline.extract_vocab(path, args.autocorrect)
            print(res)
            all_vocab.extend(res)
        except Exception as e:
            print(f"Erreur lors de l'analyse de {img}: {e}")


    pipeline.save_to_apkg(all_vocab, args.out)

    print(f"\nFinito, {len(all_vocab)} mots extraits.")
    print(f"Fichier sauvegardé sous : {args.out}")

if __name__ == "__main__":
    main()