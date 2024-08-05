from flask import Blueprint, request, jsonify
from .utils import collect_weather_data, get_weather_data
import asyncio

main = Blueprint('main', __name__)


@main.route('/weather', methods=['POST'])
def post_weather():
    data = request.get_json()
    user_defined_id = data['user_defined_id']
    city_ids = data['city_ids']

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(collect_weather_data(user_defined_id, city_ids))

    return jsonify({'status': 'Data collection started'}), 202


@main.route('/weather/<user_defined_id>', methods=['GET'])
def get_weather(user_defined_id):
    data = get_weather_data(user_defined_id)
    if data:
        return jsonify(data), 200
    return jsonify({'error': 'Data not found'}), 404
