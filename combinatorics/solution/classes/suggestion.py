from itertools import combinations, permutations
from collections import namedtuple

class Suggestion(object):
    '''
    Object that takes in input and number k, 
    provides suggestion
    '''
    def __init__(self, actual, target, data = {}):
        assert len(data) != 0, "No data provided"
        assert actual > 0, "No actual budget provided"
        assert target > 0, "No target budget provided"
        assert target < actual, "No budget adjustment required"
        self.data = data 
        self.actual = actual
        self.target = target

    def _find_combinations(self, k=0):
        return list(combinations(self.data.keys(), k))

    def suggestion(self, combination = None):
        assert combination <= len(self.data), "NUmber of combinations cannot be more than length of dataset"
        z = []
        if combination is None:
            k = len(self.data)
            for i in range(1,len(self.data)+1):
                z.extend(self._find_combinations(i))
        else:
            z = self._find_combinations(combination)

        t = float("inf")

        returntuple = namedtuple('returntuple', 'Name Value')
        
        sumoftuples = t
        for indx, i in enumerate(z):
            returnlist = []
            if sum(i) >= self.actual - self.target:
                sumoftuples = min(sumoftuples, sum(i))
                for elem in i:
                    t = returntuple(Name=self.data[elem], Value=elem)
                    returnlist.append(t)
                
                yield returnlist

if __name__ == 'main':
    Suggestion()