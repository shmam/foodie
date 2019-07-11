import json
import operator
from watson_developer_cloud import VisualRecognitionV3
from credentials import key 


def scrubKeywords(results): 
    badWords = set(['fruit', 'vegetable', 'food', 'accessory fruit'])
    results = sorted(results,reverse=True, key = lambda i: i['score'])
    words = []
    for i in results: 
        if i['class'] not in badWords: 
            words.append(i['class'])

    return words



visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey= key)

url = 'https://images-na.ssl-images-amazon.com/images/I/918YNa3bAaL._SL1500_.jpg'
classifier_ids = ["food"]

classes_result = visual_recognition.classify(url=url,classifier_ids=classifier_ids).get_result()

results = []
for i in classes_result["images"][0]["classifiers"][0]["classes"]: 
    results.append(i)

results = scrubKeywords(results)


print(results)


