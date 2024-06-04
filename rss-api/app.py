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

DAO = SQLiteDAO("channels.db")
urls = DAO.get_urls()
interactor = Interactor(DAO, build_RSS(urls), 5)


@app.route('/')
def main():
    """Responds to a GET request by returning the list of tracked channels and their stories. This rebuilds the stories
    in the tracked channels, and returns a serialised JSON array of the channels and their respective stories.
    """
    interactor.build_channels()
    return jsonify([channel.serialize() for channel in interactor.channels])


@app.post('/channels/')
def add_channel():
    """Responds to a POST request attempting to start tracking a channel.

    Requires
        - Parameters "name", "url". The name must not match any currently tracked channels, and the url must be a valid
          link to an RSS document.
    Returns
        - On success, a Response with status 201 and a message detailing that the channel has been added. On
          failure, a Response with status 400 and a message detailing the failure.
    """
    data = request.form
    if interactor.add_channel(data["name"], data["url"]):
        interactor.build_channels()
        return Response(f"Added channel {data['name']}", status=201)
    else:
        return Response(f"Failed to track channel {data['name']}", status=400)


@app.delete('/channels/')
def remove_channel():
    """Responds to a DELETE request attempting to stop tracking a channel.

    Requies
        - A API request with the name of the channel to be deleted as the body.
    Returns
        - On success, a Response with status 204 and a message detailing the deletion. On failure, a Response with
          status 400 and a message detailing the failure to delete.
    """
    name = request.data.decode("utf-8")
    if interactor.remove_channel(name):
        interactor.build_channels()
        return Response(f"Deleted channel {name}", status=204)
    else:
        return Response(f"Failed to untrack channel {name}", status=400)


@app.put('/storyCap/')
def set_max_stories():
    """Respond to a PUT request setting a new max story limit.

    Requires
        - Parameter "num": The new value of the story limit, which must be an integer.
    Returns
        - a Response with status 200.
    """
    interactor.max_stories = int(request.form["num"])
    interactor.build_channels()
    return Response(status=200)


if __name__ == '__main__':
    app.run(debug=True)
