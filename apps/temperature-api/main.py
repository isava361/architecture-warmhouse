import random
from datetime import datetime, timezone
from flask import Flask, jsonify, request

# Создаем экземпляр Flask-приложения
app = Flask(__name__)

def generate_fake_temperature_data(sensor_id=None, location=None):
    """
    Генерирует словарь с фейковыми данными о температуре,
    соответствующий структуре TemperatureResponse в Go.
    """
    if not location:
        location = f"Room-{sensor_id}" if sensor_id else "Unknown Location"

    if not sensor_id:
        sensor_id = str(random.randint(1, 999))

    return {
        "value": round(random.uniform(18.0, 25.5), 2),
        "unit": "Celsius",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "location": location,
        "status": "ok",
        "sensor_id": sensor_id,
        "sensor_type": "temperature",
        "description": f"Simulated temperature sensor for {location}."
    }

@app.route('/temperature/<string:sensor_id>', methods=['GET'])
def get_temperature_by_id(sensor_id):
    """
    Эндпоинт для получения температуры по ID датчика.
    Имитирует GET /temperature/{sensor_id}
    """
    print(f"Request received for sensor_id: {sensor_id}")

    data = generate_fake_temperature_data(sensor_id=sensor_id)

    return jsonify(data)

@app.route('/temperature', methods=['GET'])
def get_temperature_by_location():
    """
    Эндпоинт для получения температуры по местоположению (query parameter).
    Имитирует GET /temperature?location={location}
    """
    location = request.args.get('location')
    if not location:
        return jsonify({"error": "Location parameter is required"}), 400

    print(f"Request received for location: {location}")

    data = generate_fake_temperature_data(location=location)

    return jsonify(data)

@app.route('/')
def index():
    """Просто приветственная страница, чтобы проверить, что сервер работает."""
    return "<h1>Temperature API Simulator is running</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
