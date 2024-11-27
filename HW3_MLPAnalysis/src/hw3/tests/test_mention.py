import unittest
import pandas as pd 

from ..mentions import gen_mentions
from ..cleanData import cleanData

class MentionTestCase(unittest.TestCase):

    def test_mention1(self):
        test_data = {"title": [],"writer": [],"pony": [],"dialog":[]}
        df = pd.DataFrame(test_data)
        true={'twilight': {'applejack': '0','rarity': '0','pinkie': '0','rainbow': '0','fluttershy': '0'},
        'applejack': {'twilight': '0','rarity': '0','pinkie': '0','rainbow': '0','fluttershy': '0'},
        'rarity': {'twilight': '0','applejack': '0','pinkie': '0','rainbow': '0','fluttershy': '0'},
        'pinkie': {'twilight': '0','applejack': '0','rarity': '0','rainbow': '0','fluttershy': '0'},
        'rainbow': {'twilight': '0','applejack': '0','rarity': '0','pinkie': '0','fluttershy': '0'},
        'fluttershy': {'twilight': '0','applejack': '0','rarity': '0','pinkie': '0','rainbow': '0'}}
        
       
        values=gen_mentions(df)
        print(values)
        self.assertEqual(values,true)

  
    def test_mention2(self):
        test_data = {"title": ['ep01','ep01','ep01','ep01'],
                            "writer": ['w1','w1','w1','w1'],
                            "pony": ['Twilight Sparkle','Rainbow Dash', 'Fluttershy','Twilight Sparkle'],
                            "dialog":['Fluttershy','Rarity','Twilight Sparkle','Rainbow Dash is the best pony ever']}
        df = pd.DataFrame(test_data)
        #clean_test=cleanData(df)
        true={'twilight': {'applejack': '0.0','rarity': '0.0','pinkie': '0.0','rainbow': '0.5','fluttershy': '0.5'},
        'applejack': {'twilight': '0','rarity': '0','pinkie': '0','rainbow': '0','fluttershy': '0'},
        'rarity': {'twilight': '0','applejack': '0','pinkie': '0','rainbow': '0','fluttershy': '0'},
        'pinkie': {'twilight': '0','applejack': '0','rarity': '0','rainbow': '0','fluttershy': '0'},
        'rainbow': {'twilight': '0.0','applejack': '0.0','rarity': '1.0','pinkie': '0.0','fluttershy': '0.0'},
        'fluttershy': {'twilight': '1.0','applejack': '0.0','rarity': '0.0','pinkie': '0.0','rainbow': '0.0'}}
        values=gen_mentions(df)
        print(values)
        self.assertEqual(values,true)
    
    def test_mention3(self):
        test_data = {"title": ['ep01','ep01'],
                            "writer": ['w1','w1'],
                            "pony": ['Twilight Sparkle','Twilight Sparkle'],
                            "dialog":['Fluttershy Rarity!Rarit!rarity','pinkie Pie Pinkie Pie Pie']}
        df = pd.DataFrame(test_data)
        #clean_test=cleanData(df)
        true={'twilight': {'applejack': '0.0','rarity': '0.2','pinkie': '0.6','rainbow': '0.0','fluttershy': '0.2'},
        'applejack': {'twilight': '0','rarity': '0','pinkie': '0','rainbow': '0','fluttershy': '0'},
        'rarity': {'twilight': '0','applejack': '0','pinkie': '0','rainbow': '0','fluttershy': '0'},
        'pinkie': {'twilight': '0','applejack': '0','rarity': '0','rainbow': '0','fluttershy': '0'},
        'rainbow': {'twilight': '0','applejack': '0','rarity': '0','pinkie': '0','fluttershy': '0'},
        'fluttershy': {'twilight': '0','applejack': '0','rarity': '0','pinkie': '0','rainbow': '0'}}
        values=gen_mentions(df)
        print(values)
        self.assertEqual(values,true)

   
  