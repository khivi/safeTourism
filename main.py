import get_news
import create_response

location = input("Enter your Destination: ")
get_news.get_news_main(location)
create_response.create_response_main()