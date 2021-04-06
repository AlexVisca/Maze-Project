import json
from models.score import Score

class ScoreManager:
    """ Class collects and manages score instances """
    def __init__(self):
        """ Initialises a dict to hold score instances

        format: { "name1": score_instance1 , "name2": score_instance2 }
        """
        self.read_from_json()
        
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
        self.write_to_json() #rewrite the whole json file
    
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
        
        # Sort the list of dictionaries by the value of the score
        sorted_list = sorted(list_scores, key=lambda k: k['score'])
        return sorted_list

    ###########################Persistence#####################################
    
    def write_to_json(self):
        """rewrite the json file with self._scores. it is packed to put it in json 
        friendly format
        """
        with open('scores.json', 'w') as file:
            scores = self.pack()
            json.dump(scores, file, ensure_ascii=False, indent=3)
    
    def read_from_json(self):
        """Read the scores from score.json, unpack them into the cprrect format and 
        save self._scores for internal use
        """
        try:
            with open('scores.json', 'r+') as file:
                scores = json.load(file)
                self._scores = self.unpack(scores)
        except:
            self._scores = dict()
    
    def pack(self):
        """ We cannot save a score instance in json. This method takes self._scores which has 
        score_instances and returns a dictionary where the score instances are all in dict format
        instead of objects


        Returns:
            [type]: [description]
        """
        _dict = dict()
        for name, score_obj in self._scores.items():
            _dict[name] = score_obj.__dict__
        return _dict
    
    def unpack(self, _dict):
        """The opposite of pack. Give a dictionary version of the scores, it converts it to
        a version that has Score instances

        Args:
            _dict (dict): the scores in dictionary format as retrieved from json file

        Returns:
            dict: dict with score instances
        """
        _json = dict()
        for name, score_as_dict in _dict.items():
            score = score_as_dict['score']
            score_obj = Score(name, score)
            # overwrite the score objects date and time
            time = score_as_dict['time']
            date = score_as_dict['date']
            score_obj.set_time_and_date(time, date)
            _json[name] = score_obj
        return _json