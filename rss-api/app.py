from flask import Flask, jsonify, request
import json
from interactor import Interactor, build_RSS
from sqliteDAO import SQLiteDAO

app = Flask(__name__)

DAO = SQLiteDAO("./tests/test.db")
urls = DAO.get_urls()
interactor = Interactor(DAO, build_RSS(urls), 5)


@app.route('/')
def main():
    interactor.build_channels()
    channels = [channel.serialize() for channel in interactor.channels]
    return jsonify(channels=channels)


@app.get('/channels/')
def get_channels():
    interactor.build_channels()
    return jsonify(num_tracked=len(interactor.channels),
                   channels=[channel.serialize() for channel in interactor.channels])


@app.post('/channels/')
def add_channel():
    json_data = request.json
    data = json.load(json_data)
    return interactor.add_channel(data["name"], data["url"])


@app.delete('/channels/')
def remove_channel():
    json_data = request.json
    data = json.load(json_data)
    return interactor.remove_channel(data["name"], data["url"])


@app.put('/storyCap/')
def set_max_stories():
    json_data = request.json
    data = json.load(json_data)
    interactor.max_stories = data["num"]


if __name__ == '__main__':
    app.run()
