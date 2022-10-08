import smartpy as sp

class PhraseKeeper(sp.Contract):
    def __init__(self, initialPhrase):
        self.init(phrase = initialPhrase)
    @sp.entry_point
    def setPhrase(self, params):
        self.data.phrase = params

@sp.add_test(name = "Initial Test")
def test():
    scenario = sp.testScenario()
    scenario.h1("Initial String")
    
    c1 = PhraseKeeper("Let's Test")
    scenario += c1
    scenario.h2("Update String")
    scenario += c1.setPhrase("Test Success")