# Api key : 6e0215a35b9f4485b5b6c203ccd6befa

import requests
from pprint import pprint


class NewsFeed:

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = f"https://newsapi.org/v2/everything?q={self.interest}&from={self.from_date}&to={self.to_date}&sortBy=popularity&apiKey" \
              f"=6e0215a35b9f4485b5b6c203ccd6befa "

        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n" + "\n"

        return email_body



