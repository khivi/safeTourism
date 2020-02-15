#!/usr/bin/python3

import json
import requests
import os

def analysis_main():
    apiKey = os.environ['GCPAPI']
    URL = "https://language.googleapis.com/v1/documents:analyzeSentiment?key={}".format(apiKey)
    payload = open("request.json")
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    response = requests.post(URL, data=payload, headers=headers)
    json_resp = response.json()
    return json_resp
