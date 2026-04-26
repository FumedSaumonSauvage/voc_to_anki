import argparse
import os
import json
from model_loader import ModelLoader
from pipeline import VocPipeline

def main():
    parser = argparse.ArgumentParser(description="OCR Japonais vers Decks Flashcards")
    parser.add_argument("--in_dir", required=True, help="Dossier contenant les images")
    parser.add_argument("--type", choices=["flashdeck", "anki"], required=True)
    parser.add_argument("--out", required=True, help="Chemin de sortie")
    parser.add_argument("--language", default="JP")
    parser.add_argument("--autocorrect", action="store_true", default=False)
    parser.add_argument("--name", default="Mots Japonais")

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
            res = pipeline.extract_vocab(path, args.language, args.autocorrect)
            all_vocab.extend(res)
        except Exception as e:
            print(f"Erreur lors de l'analyse de {img}: {e}")

    # Conversion finale
    if args.type == "flashdeck":
        final_output = pipeline.model_to_flash_deck(all_vocab, args.name)
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(final_output, f, ensure_ascii=False, indent=2)
    else:
        final_output = pipeline.model_to_anki(all_vocab, args.name)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(final_output)

    print(f"\nSuccès ! {len(all_vocab)} mots extraits.")
    print(f"Fichier sauvegardé sous : {args.out}")

if __name__ == "__main__":
    main()