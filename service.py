import json
import operator
import requests
import time
from ibm_watson import VisualRecognitionV3 , ApiException
from credentials import food2fork 
from credentials import watson
from credentials import edamam


# Takes in a ibm watson dict and scrubs it for 
# irrelevent classifiers
# ----------------------------------------------
def scrubKeywords(results): 
    badWords = set(['fruit', 'vegetable', 'food', 'accessory fruit', 'Delicious', 'root vegetable', 'citrus'])
    results = sorted(results,reverse=True, key = lambda i: i['score'])
    words = []
    for i in results: 
        if i['class'] not in badWords: 
            words.append(i['class'])
    return words


# takes in a image url and returns a scrubbed and sorted
# list of image classifiers
# ----------------------------------------------
def findClassifiers(image_pathname): 
    visual_recognition = VisualRecognitionV3('2018-03-19',iam_apikey= watson.key)

    base = '/Users/scrochet/Downloads/'
    url = str(base + image_pathname)

    classifier_ids = ["food"]
    classes_result = dict()
    time.sleep(.5)
    try: 
        # classes_result = visual_recognition.classify(url=url,classifier_ids=classifier_ids).get_result()
        with open(("{}".format(url)), 'rb') as images_file:
            classes_result = visual_recognition.classify(
                images_file,
                threshold='0.6',
                classifier_ids=classifier_ids).get_result()
            print(classes_result)
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
        return False

    results = []
    for i in classes_result["images"][0]["classifiers"][0]["classes"]: 
        results.append(i)

    results = scrubKeywords(results)
    
    return results

def f2fsearchRecipes(keyword): 
    url_string = "https://www.food2fork.com/api/search?key={}&q={}".format(food2fork.api_key,keyword)
    r = requests.get(url_string)
    return r.json()

def edemamSearchRecipes(keyword_list): 
    if len(keyword_list) == 0: 
        return False
    
    query = ""
    for i in range(0,len(keyword_list),1):
        # if this is the last keyword in the list
        if i == len(keyword_list) - 1: 
            query = query + keyword_list[i]
        
        else: 
            query = query + keyword_list[i] + " and "

    url_string = "https://api.edamam.com/search?q={}&app_id={}&app_key={}&diet={}".format(query, edamam.api_id, edamam.api_key,"balanced")
    r = requests.get(url_string)
    return r.json()
