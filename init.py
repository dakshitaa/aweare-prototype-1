import smartpy as sp

import geocoder
import datetime

home_add = geocoder.ip('me')
#initilalise - user id, tag id, home geolocation
#record: timestamp of verification 
# + boolean (geolocation of verification != home geolocation)
# query NFT level

class GeoTag(sp.Contract):
    def __init__(self):
        self.init(home_loc = [0,0], curr_loc = [0,0], userID = 0, tagID = 0, curr_time = str(datetime.datetime.now().time()))

    @sp.entry_point
    def setHomeAdd(self, loc):
        self.data.home_loc = loc
        self.data.curr_loc = loc
        self.data.curr_time = str(datetime.datetime.now().time())
        self.data.tagID += 1
        self.data.userID += 1
    
    @sp.entry_point
    def setNewTag(self, loc):
        # sp.verify(loc != home_loc)
        self.data.curr_loc = loc
        self.data.curr_time = str(datetime.datetime.now().time())
        self.data.tagID += 1

@sp.add_test(name = "Test Contract")
def test():
    scenario = sp.test_scenario()
    scenario.h1("Initial GeoTag")
    
    c1 = GeoTag()
    scenario += c1
    scenario.h2("Update Home Address (Initial Registration)")
    scenario += c1.setHomeAdd([107, 120])
    scenario.h2("First Tag")
    scenario += c1.setNewTag([103, 99])