# models/character_relationships.py
from transformers import pipeline

# Initialiser le modèle pour l'extraction des relations
relationship_extractor = pipeline('ner', aggregation_strategy='simple')

def extract_character_relationships(script):
    sections = script.split('\n\n')
    relationships = []
    
    for section in sections:
        entities = relationship_extractor(section)
        relationships.append({
            'section': section,
            'relationships': [entity['entity_group'] for entity in entities]
        })
    
    return relationships
