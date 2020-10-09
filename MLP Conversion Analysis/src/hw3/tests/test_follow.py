import unittest
import pandas as pd 

from .. follow import followOnComments
from ..cleanData import cleanData

class test_follow(unittest.TestCase):

    def test_follow1(self):
        test_data = {"title": [],"writer": [],"pony": [],"dialog":[]}
        df = pd.DataFrame(test_data)
        true={'twilight': {'applejack': '0','rarity': '0','pinkie': '0','rainbow': '0','fluttershy': '0','other':'0'},
        'applejack': {'twilight': '0','rarity': '0','pinkie': '0','rainbow': '0','fluttershy': '0','other':'0'},
        'rarity': {'twilight': '0','applejack': '0','pinkie': '0','rainbow': '0','fluttershy': '0','other':'0'},
        'pinkie': {'twilight': '0','applejack': '0','rarity': '0','rainbow': '0','fluttershy': '0','other':'0'},
        'rainbow': {'twilight': '0','applejack': '0','rarity': '0','pinkie': '0','fluttershy': '0','other':'0'},
        'fluttershy': {'twilight': '0','applejack': '0','rarity': '0','pinkie': '0','rainbow': '0','other':'0'}}
        
       
        values=followOnComments(df)
        #print(values)
        self.assertEqual(values,true)

    def test_follow2(self):
        test_data = {"title": ['ep01','ep01','ep02'],
                            "writer": ['w1','w1','w2'],
                            "pony": ['Applejack','Twilight Sparkle','Applejack'],
                            "dialog":['Fluttershy hello','hello world','You are so pretty']}
        df = pd.DataFrame(test_data)
        true={'twilight': {'applejack': '1.0','rarity': '0.0','pinkie': '0.0','rainbow': '0.0','fluttershy': '0.0','other':'0.0'},
        'applejack': {'twilight': '0','rarity': '0','pinkie': '0','rainbow': '0','fluttershy': '0','other':'0'},
        'rarity': {'twilight': '0','applejack': '0','pinkie': '0','rainbow': '0','fluttershy': '0','other':'0'},
        'pinkie': {'twilight': '0','applejack': '0','rarity': '0','rainbow': '0','fluttershy': '0','other':'0'},
        'rainbow': {'twilight': '0','applejack': '0','rarity': '0','pinkie': '0','fluttershy': '0','other':'0'},
        'fluttershy': {'twilight': '0','applejack': '0','rarity': '0','pinkie': '0','rainbow': '0','other':'0'}}
        
       
        values=followOnComments(df)
        #print(values)
        self.assertEqual(values,true)

    def test_follow3(self):
        test_data = {"title": ['ep01','ep01','ep01','ep01','ep01','ep01'],
                            "writer": ['w1','w1','w2','w3','w4','w4'],
                            "pony": ['Applejack','Twilight Sparkle','Rainbow Dash','Twilight Sparkle','Rarity','Twilight Sparkle'],
                            "dialog":['Fluttershy hello','hello world','You are so pretty','Thank you','emmmmm','hehe']}
        df = pd.DataFrame(test_data)
        
        true = {'twilight': {'applejack': '0.33','rarity': '0.33','pinkie': '0.0','rainbow': '0.33','fluttershy': '0.0','other': '0.0'},
        'applejack': {'twilight': '0','rarity': '0','pinkie': '0','rainbow': '0','fluttershy': '0','other': '0'},
        'rarity': {'twilight': '1.0','applejack': '0.0','pinkie': '0.0','rainbow': '0.0','fluttershy': '0.0','other': '0.0'},
        'pinkie': {'twilight': '0','applejack': '0','rarity': '0','rainbow': '0','fluttershy': '0','other': '0'},
        'rainbow': {'twilight': '1.0','applejack': '0.0','rarity': '0.0','pinkie': '0.0','fluttershy': '0.0','other': '0.0'},
        'fluttershy': {'twilight': '0','applejack': '0','rarity': '0','pinkie': '0','rainbow': '0','other': '0'}}
       
        values=followOnComments(df)
        #print(values)
        self.assertEqual(values,true)

    def test_follow4(self):
        test_data = test_data = {"title": ['ep00','ep01','ep01','ep01','ep01','ep01','ep01','ep01'],
                            "writer": ['w1','w1','w2','w3','w4','w4','w5','w6'],
                            "pony": ['cnjs','Twilight Sparkle','Rainbow Dash','Twilight Sparkle','abc','Fluttershy','Twilight Sparkle','Pinkie Pie'],
                            "dialog":['Fluttershy hello','hello world','You are so pretty','Thank you','emmmmm','hehe','hey twilight','hows going']}
        df = pd.DataFrame(test_data)
        true={'twilight': {'applejack': '0.0','rarity': '0.0','pinkie': '0.0','rainbow': '0.5','fluttershy': '0.5','other': '0.0'},
        'applejack': {'twilight': '0','rarity': '0','pinkie': '0','rainbow': '0','fluttershy': '0','other': '0'},
        'rarity': {'twilight': '0','applejack': '0','pinkie': '0','rainbow': '0','fluttershy': '0','other': '0'},
        'pinkie': {'twilight': '1.0','applejack': '0.0','rarity': '0.0','rainbow': '0.0','fluttershy': '0.0','other': '0.0'},
        'rainbow': {'twilight': '1.0','applejack': '0.0','rarity': '0.0','pinkie': '0.0','fluttershy': '0.0','other': '0.0'},
        'fluttershy': {'twilight': '0.0','applejack': '0.0','rarity': '0.0','pinkie': '0.0','rainbow': '0.0','other': '1.0'}}
        
       
        values=followOnComments(df)
        #print(values)
        self.assertEqual(values,true)

