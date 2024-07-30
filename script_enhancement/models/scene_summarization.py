#models/scene_summarization

from transformers import pipeline
from typing import Dict

class SceneSummarizer:
    def __init__(self):
        """
        Initialise le résumeur de scènes en chargeant le modèle de résumé.
        """
        self.summarizer = pipeline('summarization')

    def summarize_scene(self, scene: str) -> Dict[str, str]:
        """
        Résume une scène donnée.

        Args:
            scene (str): La scène à résumer.

        Returns:
            Dict: Un dictionnaire contenant le résumé de la scène ou un message d'erreur.
        """
        if not scene:
            raise ValueError("La scène ne peut pas être vide.")

        try:
            summary = self.summarizer(scene, max_length=150, min_length=50, do_sample=False)
            return {'summary': summary[0]['summary_text']}
        except Exception as e:
            return {'error': str(e)}
