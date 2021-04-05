# API
from flask import Flask, request, render_template
from controllers.score_manager import ScoreManager
from models.score import Score

app = Flask(__name__)
score_manager = ScoreManager()

@app.route('/')
def display_scores():
    return render_template("scores.html", score_list=score_manager.get_scores())

@app.route('/api/list')  # -- Default method 'GET'
def list_all_scores():
    """ Returns a dictionary of scores

    Returns:
        dict: score dicts
    """
    return {"scores": score_manager.get_scores()}

@app.route('/api/new', methods=['PUT'])
def add_new_score():
    """ Adds a score to the server

    Returns:
        str: HTTP status code
    """
    try:
        # -- Get the JSON data of the request, containing a new object to add

        data = request.get_json()
        new_score = Score(data['name'], int(data['score']))
        score_manager.add_score(new_score)
        
        return '', 204
    
    except:  # This is the correct syntax
        return "Error", 400

@app.route('/api/list', methods=['DELETE'])
def delete_score():
    """ Removes a score or scores from the server

    Returns:
        str: HTTP status code
    """
    try:
        # -- Get the JSON data of the request, containing a new object to remove
        data = request.get_json()
        score_manager.remove_score(data['name'])

        return '', 204
    except:
        return "Error", 400


if __name__ == "__main__":
    app.run(debug=True)
