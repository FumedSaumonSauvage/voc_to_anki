import json
import base64
import time
import os
from prompt_loader import get_full_prompt
import pandas as pd
import random
import genanki

class VocPipeline:
    def __init__(self, model_loader):
        self.loader = model_loader

    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def extract_vocab(self, image_path, language="JP", autocorrect=False):
        base64_image = self.encode_image(image_path)
        system_prompt = get_full_prompt(autocorrect=autocorrect, language=language) 

        response = self.loader.client.chat.complete(
            model=self.loader.model_name,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": system_prompt},
                        {"type": "image_url", "image_url": f"data:image/jpeg;base64,{base64_image}"}
                    ]
                }
            ],
            response_format={"type": "json_object"}
        )
        
        res_content = json.loads(response.choices[0].message.content)
        return res_content if isinstance(res_content, list) else res_content.get("vocabulaire", [])

    def save_to_apkg(self, data, output_name="deck.apkg"):
        if not data:
            print("Pas de data en export")
            return

        model_id = random.randrange(1 << 30, 1 << 31) #TODO ajouter une option pour fixer?
        my_model = genanki.Model(
            model_id,
            'Vocab Model',
            fields=[
                {'name': 'Question'},
                {'name': 'Answer'},
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '<div style="font-size: 30px; text-align: center;">{{Question}}</div>',
                    'afmt': '{{FrontSide}}<hr id="answer"><div style="text-align: center;">{{Answer}}</div>',
                },
            ],
            css='.card { font-family: arial; font-size: 20px; text-align: center; color: black; background-color: white; }'
        )

        deck_id = random.randrange(1 << 30, 1 << 31) #TODO ajouter une option pour fixer?
        deck_name = output_name.replace(".apkg", "")
        my_deck = genanki.Deck(deck_id, deck_name)

        for item in data:
            original = item.get("mot_original", "")
            lecture = item.get("lecture", "")
            traduction = item.get("traduction", "")
            
            answer_html = f"<div style='color: #2ecc71; font-size: 25px;'>{lecture}</div><br>{traduction}"
            
            my_note = genanki.Note(
                model=my_model,
                fields=[original, answer_html]
            )
            my_deck.add_note(my_note)

        try:
            genanki.Package(my_deck).write_to_file(output_name)
            print(f"Finito : {output_name} ({len(data)} cartes)")
        except Exception as e:
            print(f"Erreur package : {e}")