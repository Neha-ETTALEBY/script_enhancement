from flask import Flask, request, jsonify
from models.emotion_detection import EmotionDetector
from models.dialogue_improvement import DialogueImprover
from models.scenario_generator import generate_scenario
from models.scene_summarization import SceneSummarizer
from models.character_relationships import extract_character_relationships


app = Flask(__name__)

# Initialiser les classes
emotion_detector = EmotionDetector()
dialogue_improver = DialogueImprover()
scene_summarizer = SceneSummarizer()

@app.route('/detect_emotions', methods=['POST'])
def detect_emotions_endpoint():
    """
    Endpoint pour détecter les émotions dans un script.
    """
    try:
        data = request.get_json()
        script = data.get('script', '')
        if not script:
            return jsonify({'error': 'No script provided'}), 400
        emotions = emotion_detector.detect_emotions(script)
        return jsonify(emotions)
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@app.route('/improve_dialogue', methods=['POST'])
def improve_dialogue_endpoint():
    """
    Endpoint pour améliorer un dialogue.
    """
    try:
        data = request.get_json()
        dialogue = data.get('dialogue', '')
        if not dialogue:
            return jsonify({'error': 'No dialogue provided'}), 400
        improved_dialogue = dialogue_improver.improve_dialogue(dialogue)
        return jsonify(improved_dialogue)
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@app.route('/summarize_scene', methods=['POST'])
def summarize_scene_endpoint():
    """
    Endpoint pour résumer une scène.
    """
    try:
        data = request.get_json()
        scene = data.get('scene', '')
        if not scene:
            return jsonify({'error': 'No scene provided'}), 400
        summary = scene_summarizer.summarize_scene(scene)
        return jsonify(summary)
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500
    
@app.route('/generate_scenario', methods=['POST'])
def generate_scenario_endpoint():
    data = request.json
    template = data.get('template')
    context = data.get('context')
    
    if not template or not context:
        return jsonify({'error': 'Missing required fields: template and context'}), 400
    
    scenario = generate_scenario(template, context)
    return jsonify({'scenario': scenario})



@app.route('/extract_character_relationships', methods=['POST'])
def extract_character_relationships_endpoint():
    script = request.json['script']
    relationships = extract_character_relationships(script)
    return jsonify(relationships)
if __name__ == '__main__':
    app.run(debug=True)
