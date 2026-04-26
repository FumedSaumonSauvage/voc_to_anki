import json
import base64
import time
from prompt_loader import get_full_prompt

class VocPipeline:
    def __init__(self, model_loader):
        self.loader = model_loader

    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def extract_vocab(self, image_path, language="JP", autocorrect=False):
        base64_image = self.encode_image(image_path)
        system_prompt = get_full_prompt(autocorrect=autocorrect, language=language) # loader smart

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

    def model_to_flash_deck(self, data, name):
        timestamp = str(int(time.time() * 1000))
        deck_id = 1
        
        card_list = []
        for index, item in enumerate(data):
            card_list.append({
                "id": index + 1,
                "deckId": deck_id,
                "ordinal": index,
                "question": item.get("mot_original", ""),
                "questionImage": "",
                "questionVoice": "",
                "answer": f"{item.get('lecture', '')} - {item.get('traduction', '')}",
                "answerImage": "",
                "answerVoice": "",
                "isReversibleQA": False,
                "isReversed": False
            })

        return [
            {
                "serialVersionUID": -8121772616636313000,
                "deck": {
                    "id": deck_id,
                    "name": name,
                    "createdDateTime": timestamp,
                    "updatedDateTime": timestamp
                },
                "cardList": card_list
            }
        ]

    def model_to_anki(self, data, name):
        anki_lines = []
        for item in data:
            front = f"{item['mot_original']} [{item.get('lecture', '')}]"
            back = item['traduction']
            anki_lines.append(f"{front};{back}")
        return "\n".join(anki_lines)