import json
import requests
import os


def post_request(json_data, url):
    with open('request.json', 'w') as outfile:
        json.dump(json_data, outfile, indent=4)
    payload = open("request.json")
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    response = requests.post(url, data=payload, headers=headers)
    return response

def create_response_main():
    apiKey = os.environ['GCPAPI']
    URL = "https://language.googleapis.com/v1/documents:analyzeSentiment?key={}".format(apiKey)
    lines = [line.rstrip('\n') for line in open('./headlines.txt')]
    json_data = {'document': {'type': 'PLAIN_TEXT', 'content': 'PAYLOAD'}, 'encodingType': 'UTF8'}
    score = 0
    for r in range(len(lines)):
    #for r in range(1):
        json_data['document']['content'] = lines[r]
        #print(json_data)
        response = post_request(json_data, URL)
        #print(response.json)
        json_resp = json.loads(response.content)
        #print(json_resp)
        score = score + json_resp['documentSentiment']['score']
        #print('Score: {} TScore: {}'.format(json_resp['documentSentiment']['score'], score))
        with open('gcp_reply.json', 'a') as outfile:
            json.dump(json_resp, outfile, indent=4)
        print('.',end=''),
    print("Completed")
    avgScore = score / len(lines)
    print('Average Score: {}'.format(avgScore))
