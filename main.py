import yagmail
import pandas
from news import NewsFeed
import datetime
import time

while True:
    if datetime.datetime.now().hour == 8:
        df = pandas.read_excel('xyz.xlsx')

        for index, row in df.iterrows():
            today=datetime.datetime.now().strftime('%Y-%m%d')
            yesterday=(datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m%d')
            newsfeed= NewsFeed(interest=row['interest'], from_date=yesterday, to_date=today)
            email= yagmail.SMTP(user="abhayk2570@gmail.com", password="clsuciqazpmlymmo")
            email.send(to=row['email'],
                       subject=f"Your {row['interest']} news for today",
                       contents=f"Hi {row['name']}\n See what's on about {row['interest']} today {newsfeed.get()} \n")
    time.sleep(60)
