from controllers.score_manager import ScoreManager
from models.score import Score
import pytest


def test_score_manager():
    score_manager = ScoreManager()
    # create new score with the worst possible score so we
    # know it will be at the end of the sorted score list
    score = Score("Alex", 1001)
    # add the score
    score_manager.add_score(score)
    # get the list of scores (sorted)
    scores_list = score_manager.get_scores()
    # get the last item in the list (worst score)
    retrieved_score = scores_list[-1]
    # confirm that the name and score is the same as the score we created
    assert retrieved_score['name'] == score.name and retrieved_score['score'] == score.score