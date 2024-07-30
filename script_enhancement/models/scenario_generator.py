# models/scenario_generator.py
from transformers import pipeline

# Initialiser le modèle pour la génération de texte
generator = pipeline('text-generation', model='gpt2')

def generate_scenario(template, context):
    prompt = template.format(context=context)
    generated_scenario = generator(prompt, max_length=500, num_return_sequences=1)
    return generated_scenario[0]['generated_text']
