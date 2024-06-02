"""This module provides the API endpoints for the interactor via Flask. This serves
as the controller layer for the RSS reader application.

Defined API endpoints:
 - GET / : Get a list of channels and stories up to the story limit (default: 5).
 - POST /channels/ : Add a channel to be tracked.
 - DELETE /channels/ : Delete a channel from being tracked.
 - PUT /storyCap/ : Set a new story limit to be displayed for each channel.
"""
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from interactor import Interactor, build_RSS
from sqliteDAO import SQLiteDAO

app = Flask(__name__)
CORS(app)

DAO = SQLiteDAO("./tests/test.db")
urls = DAO.get_urls()
interactor = Interactor(DAO, build_RSS(urls), 5)


@app.route('/')
def main():
    """TODO:"""
    interactor.build_channels()
    return jsonify([channel.serialize() for channel in interactor.channels])


@app.post('/channels/')
def add_channel():
    """TODO:"""
    data = request.form
    interactor.add_channel(data["name"], data["url"])
    interactor.build_channels()
    return Response("Add channel", status=201)


@app.delete('/channels/')
def remove_channel():
    """TODO:"""
    name = request.data.decode("utf-8")
    if interactor.remove_channel(name):
        interactor.build_channels()
        return Response(f"Deleted channel {name}", status=204)
    else:
        return Response(f"Failed to track channel {name}", status=400)


@app.put('/storyCap/')
def set_max_stories():
    """TODO:"""
    interactor.max_stories = int(request.form["num"])
    interactor.build_channels()
    return Response(status=200)


if __name__ == '__main__':
    app.run(debug=True)
