from flask import Flask, request, jsonify
import requests 

app = Flask(__name__)

THINGSPEAK_URL = "https://api.thingspeak.com/channels/2982389/feeds.json?api_key=50ESVIOZ8T8K3Y4K&results=100"

@app.route('/')
def home():
    return "Bem-vindo a api de consulta de buscas FindMyPet!"

@app.route('/find', methods=['GET'])
def find():
    try:
        animal_id = request.args.get('id')
        
        if not animal_id:
            return jsonify({'error': 'Parâmetro "id" é obrigatório'}), 400

        response = requests.get(THINGSPEAK_URL)
        response.raise_for_status() 
        
        data = response.json()
        feeds = data.get('feeds', [])
        
        animal = None
        for feed in feeds:
            if feed.get('field4') == animal_id:
                animal = {
                    'entry_id': feed['entry_id'],
                    'created_at': feed['created_at'],
                    'latitude': feed['field1'],
                    'longitude': feed['field2'],
                    'status': feed['field3'],
                    'animal_id': feed['field4']
                }
                break
        
        if animal:
            return jsonify(animal)
        else:
            return jsonify({'error': f'Animal com ID {animal_id} não encontrado'}), 404

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Erro na conexão com ThingSpeak: {str(e)}'}), 502
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)