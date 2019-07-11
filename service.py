import json
import operator
import requests
from watson_developer_cloud import VisualRecognitionV3
from credentials.food2fork import * 
from credentials.watson import * 


# Takes in a ibm watson dict and scrubs it for 
# irrelevent classifiers
# ----------------------------------------------
def scrubKeywords(results): 
    badWords = set(['fruit', 'vegetable', 'food', 'accessory fruit', 'Delicious'])
    results = sorted(results,reverse=True, key = lambda i: i['score'])
    words = []
    for i in results: 
        if i['class'] not in badWords: 
            words.append(i['class'])
    return words


# takes in a image url and returns a scrubbed and sorted
# list of image classifiers
# ----------------------------------------------
def findClassifiers(image_url): 
    visual_recognition = VisualRecognitionV3('2018-03-19',iam_apikey= key)

    url = image_url
    classifier_ids = ["food"]

    classes_result = visual_recognition.classify(url=url,classifier_ids=classifier_ids).get_result()

    results = []
    for i in classes_result["images"][0]["classifiers"][0]["classes"]: 
        results.append(i)

    results = scrubKeywords(results)
    
    return results

def searchRecipes(keyword): 
    recipelist = []
    url_string = "https://www.food2fork.com/api/search?key={}&q={}".format(api_key,keyword)
    r = requests.get(url_string)
    return r.json()