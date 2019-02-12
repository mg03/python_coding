import unittest, os, sys
# sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath(sys.path[0]) + '/../')
from classes.suggestion import *

class SuggestionTest(unittest.TestCase):
    '''
    Test for suggestion
    '''
    def __init__(self, testname, args):
        super(SuggestionTest, self).__init__(testname)
        self._args = args

    def setUp(self):
        print("setUp")
        print("data is {}").format(self._args[0])
        print("actual is {}").format(self._args[1])
        print("target is {}").format(self._args[2])
        print("cnt is {}").format(self._args[3])
        print("price combinations is {}").format(self._args[4])
        print("item and price combinations are {}").format(self._args[5])

    def test_find_combinations(self):
        """Does combination list have required entries?"""
        z = Suggestion(self._args[1], self._args[2], self._args[0])
        returnedlist = z._find_combinations(len(self._args[0]))
        self.failIf(returnedlist != self._args[4])

    def test_suggestions(self):
        z = Suggestion(self._args[1], self._args[2], self._args[0])
        for m in z.suggestion(len(self._args[0])):
            self.failIf(set(m) != set(self._args[5]))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    input = []
    input.append({55: 'item1', 100: 'item2' })  
    input.append(1050)
    input.append(1000)
    input.append(2)
    input.append([(100,55)])
    returntuple = namedtuple('returntuple', 'Name Value')
    suite.addTest(SuggestionTest('test_find_combinations', input))

    t = []
    t.append(returntuple(Name='item1', Value=55))
    t.append(returntuple(Name='item2', Value=100))
    input.append(t)

    suite.addTest(SuggestionTest('test_suggestions', input))

    unittest.TextTestRunner(verbosity=2).run(suite)