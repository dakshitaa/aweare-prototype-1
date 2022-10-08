import smartpy as sp

import geocoder

home_add = geocoder.ip('me')
#initilalise - user id, tag id, home geolocation
#record: timestamp of verification 
# + boolean (geolocation of verification != home geolocation)
# query NFT level

def getCurrLoc():
    curr_loc = geocoder.ip('me')
class PhraseKeeper(sp.Contract):
    def __init__(self, initialPhrase):
        self.init(phrase = initialPhrase)
    @sp.entry_point
    def setPhrase(self, params):
        self.data.phrase = params

@sp.add_test(name = "Initial Test")
def test():
    scenario = sp.test_scenario()
    scenario.h1("Initial String")
    
    c1 = PhraseKeeper(str(home_add.latlng))
    scenario += c1
    scenario.h2("Update String")
    scenario += c1.setPhrase("Test Success")