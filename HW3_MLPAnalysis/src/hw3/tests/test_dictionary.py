import unittest
import pandas as pd 

from .. dictionary import nonDictionary
from ..cleanData import cleanData

class test_dictionary(unittest.TestCase):

    def test_dictionary1(self):
        test_data = {"title": [],"writer": [],"pony": [],"dialog":[]}
        df = pd.DataFrame(test_data)
        true={'twilight': [],
        'applejack': [],
        'rarity': [],
        'pinkie': [],
        'rainbow': [],
        'fluttershy': []}
        
       
        values=nonDictionary(df,[])
        #print(values)
        self.assertEqual(values,true)

    def test_dictionary2(self):
        test_data = {"title": ['ep01','ep01','ep01','ep01','ep01','ep01'],
                            "writer": ['w1','w1','w2','w3','w4','w4'],
                            "pony": ['Applejack','Twilight Sparkle','Rainbow Dash','Twilight Sparkle','Rarity','Twilight Sparkle'],
                            "dialog":['Fluttershy hello','hello world','You are so pretty','Thank you','emmmmm','hehe']}
        df = pd.DataFrame(test_data)
        true = {'twilight': ['hello', 'world', 'thank', 'you', 'hehe'],
        'applejack': ['fluttershy', 'hello'],
        'rarity': ['emmmmm'],
        'pinkie': [],
        'rainbow': ['you', 'are', 'so', 'pretty'],
        'fluttershy': []}
        
       
        values=nonDictionary(df,[])
        #print(values)
        self.assertEqual(values,true)
    
    def test_dictionary3(self):
        
        test_data = {"title": ['ep01','ep01','ep01','ep01','ep01','ep01'],
                            "writer": ['w1','w1','w2','w3','w4','w4'],
                            "pony": ['Twilight Sparkle','Rarity','Rainbow Dash','Fluttershy','Rarity','Twilight Sparkle'],
                            "dialog":['My name is applejack','hello f f f world','You are so pretty','Thank you','emmmmm','emm']}
        df = pd.DataFrame(test_data)
        true = {'twilight': ['my', 'name', 'is', 'applejack'],
        'applejack': [],
        'rarity': ['hello', 'world', 'emmmmm'],
        'pinkie': [],
        'rainbow': ['you', 'are', 'so', 'pretty'],
        'fluttershy': ['thank', 'you']}
        
       
        values=nonDictionary(df,['f','i','emm'])
        #print(values)
        self.assertEqual(values,true)

