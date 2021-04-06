import pygame

class Score:
    def __init__(self):
        self._name = "GUEST" # default name
        self._score = 1000 # default score
        # to calculate score
        self._start_time = pygame.time.get_ticks()/1000 # in seconds
        self._end_time = None
    
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
    
    def get_start_time(self):
        return self._start_time
    
    def end_timer(self):
        self._end_time = pygame.time.get_ticks()/1000
        time_taken = self._end_time - self._start_time
        self._score = round(time_taken, 1)
        
        
        