

class ScoreManager:
    """ Class collects and manages score instances """
    def __init__(self):
        """ Initialises a dict to hold score instances

        format: { "name1": score_instance1 , "name2": score_instance2 }
        """
        self._scores = dict()

    @property
    def scores(self):
        """ Returns values in self_scores as a list

        Returns:
            list: of score instances
        """
        return list(self._scores.values())

    def add_score(self, new_score):
        """ Adds a new score instance to self._scores

        Args:
            key: score name property
            new_score (obj): score instance
        """
        self._scores[new_score.name] = new_score
    
    def remove_score(self, score_name):
        """ Removes a score from self._scores

        Args:
            score_name (str): the name string
        """
        if score_name in self._scores:
            del self._scores[score_name]

    def __len__(self):
        """ Returns the length of self._scores

        Returns:
            int: integer length of self._scores
        """
        return len(self._scores)
    
    def get_scores(self):
        """ Provides dictionary representations of score instances

        Returns:
            list: of dicts
        """
        list_scores = list()
        for item in self._scores.values():
            score_dict = item.__dict__
            list_scores.append(score_dict)
        sorted_list = sorted(list_scores, key=lambda k: k['score'])
        return sorted_list
