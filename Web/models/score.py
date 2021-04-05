from datetime import datetime

class Score:
    """ Simple class to represent a score in a game """

    def __init__(self, name, score):
        """ Initializes private attributes

        Args:
            name (str): name of the player (cannot be empty)
            score (int): score of the player (cannot be negative)
        
        Raises:
            ValueError: name is empty or not string, score is not integer or negative
        """

        if type(name) is not str or not name:
            raise ValueError("Invalid name.")
        if type(score) is not int or score < 0:
            raise ValueError("Invalid score.")

        self._name = name
        self._score = score
    
        # set time
        now = datetime.now()
        self._date = now.strftime("%Y-%m-%d")
        self._time = now.strftime("%H:%M:%S")
      
        
    @property
    def name(self):
        """ Provides the name property

        Returns:
            str: instance.name
        """
        return self._name
        
    @property
    def score(self):
        """ Provides score value

        Returns:
            int: instance.score
        """
        return self._score

    @property
    def __dict__(self):
        """ Provides a dictionary representation of score instance

        Returns:
            dict: { name : score }
        """
        score_dict = dict(
            name=self._name,
            score=self._score,
            date=self._date,
            time=self._time
        )
        return score_dict
    
    def __str__(self):
        """ Provides a string representation of score instance

        Returns:
            str: 'Score: Name (Score)'
        """
        return F"Score: {self.name} ({self.score})"
    
    def __gt__(self, other):
        """ Score comparison function

        Args:
            other (obj): a Score instance

        Returns:
            bool: if self is greater than other
        """
        if not other.score >= self.score:
            return True

    def set_time_and_date(self, time, date):
        """Overwrite time and date properties. Only do this when readind from Json files
        and recreating Score instances.

        Args:
            time (String): %H:%M:%S
            date (String): "%Y-%m-%d"
        """
        self._time = time
        self._date = date