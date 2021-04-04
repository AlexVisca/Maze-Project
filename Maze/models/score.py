class Score:
    def __init__(self):
        self._name = "GUEST" # default name
        self._score = 100 # default score
    
    def __dict__(self):
        """ Provides a dictionary representation of score instance

        Returns:
            dict: { name : score }
        """
        score_dict = dict(
            name=self._name,
            score=self._score
        )
        return score_dict
    
    def set_name(self, name):
        self._name = name
    
    def set_score(self, score):
        self._score = score
    
    def get_name(self):
        return self._name
    
    def get_score(self):
        return self._score
        
        
        