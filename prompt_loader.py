from prompt import BASE_PROMPT, AUTOCORRECT_INSTRUCTION

def get_full_prompt(autocorrect=False):
    # cook le prompt final
    prompt = BASE_PROMPT
    
    if autocorrect:
        prompt += AUTOCORRECT_INSTRUCTION
    
    return prompt