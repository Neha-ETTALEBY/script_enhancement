#models/dialogue_improvement
from transformers import pipeline
from typing import Dict

class DialogueImprover:
    def __init__(self):
        """
        Initialise l'améliorateur de dialogues en chargeant le modèle de génération de texte.
        """
        self.dialogue_generator = pipeline('text-generation', model='gpt2')

    def improve_dialogue(self, dialogue: str) -> Dict[str, str]:
        """
        Améliore un dialogue donné.

        Args:
            dialogue (str): Le dialogue à améliorer.

        Returns:
            Dict: Un dictionnaire contenant le dialogue amélioré ou un message d'erreur.
        """
        if not dialogue:
            raise ValueError("Le dialogue ne peut pas être vide.")

        try:
            improved = self.dialogue_generator(dialogue, max_length=150, num_return_sequences=1)
            return {'improved_dialogue': improved[0]['generated_text']}
        except Exception as e:
            return {'error': str(e)}
