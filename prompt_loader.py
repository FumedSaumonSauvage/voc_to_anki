from prompt import BASE_PROMPT, AUTOCORRECT_INSTRUCTION

def get_full_prompt(autocorrect=False, language="JP"): # TODO fix le langage pas implementé dans le prompt
    # cook le prompt final
    prompt = BASE_PROMPT
    
    if autocorrect:
        prompt += AUTOCORRECT_INSTRUCTION
    
    prompt += f"\nLanguage cible pour la traduction : {language}"
    
    return prompt