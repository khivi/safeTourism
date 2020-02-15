#!/usr/bin/python3

import google_news
import analysis
import upload_file
#import test_model

def main(location):

  status = google_news.google_news_main(location)
  if status == 'error':
    stat = {'error':'Error in get_news.py'}
    return stat
  #test_model.test_model_main()
  upload_file.upload_to_bucket("headlines.txt", "./headlines.txt", "max12345")
  analysis_response = analysis.analysis_main()
  return analysis_response
