#models/emotion detector

from transformers import pipeline
from typing import List, Dict, Union

class EmotionDetector:
    def __init__(self):
        """
        Initialise le détecteur d'émotions en chargeant le modèle d'analyse des sentiments.
        """
        self.emotion_detector = pipeline('sentiment-analysis')

    def detect_emotions(self, script: str) -> List[Dict[str, Union[str, List[Dict[str, str]]]]]:
        """
        Détecte les émotions dans un script divisé en scènes.

        Args:
            script (str): Le script à analyser.

        Returns:
            List[Dict]: Une liste de dictionnaires contenant les scènes et leurs émotions détectées.
        """
        if not script:
            raise ValueError("Le script ne peut pas être vide.")

        scenes = script.split('\n\n')
        emotion_results = []
        for scene in scenes:
            try:
                emotions = self.emotion_detector(scene)
                emotion_results.append({
                    'scene': scene,
                    'emotions': emotions
                })
            except Exception as e:
                emotion_results.append({
                    'scene': scene,
                    'error': str(e)
                })
        return emotion_results
