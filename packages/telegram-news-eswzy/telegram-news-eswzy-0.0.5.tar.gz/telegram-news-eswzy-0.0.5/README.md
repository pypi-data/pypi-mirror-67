# Telegram-news

Python program package for automatically fetching news and pushing by telegram bot.

# Simple Start

First of all, install telegram_news:
```shell script
pip install telegram_news
```

In a Python file, write:

```python
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
db = Session(bind=engine.connect())
url = "https://en.wikinews.org/wiki/Main_Page"
np = NewsPostman(listURLs=[url, ], sendList=["@your_channel_name", ], db=db)
ie = 

```

Then, you will get messages like this in your channel or group:

>**Bangladesh reports five new deaths due to COVID-19, a daily highest**
>
>Yesterday, [Bangladesh](https://en.wikinews.org/wiki/Bangladesh) has confirmed five new deaths due to [COVID-19](https://en.wikinews.org/wiki/COVID-19) on the day. This is the highest number of fatalities in a day due to the virus. As of yesterday, Bangladesh's [Institute of Epidemiology, Disease Control and Research](https://en.wikipedia.org/wiki/Institute_of_Epidemiology,_Disease_Control_and_Research) (IEDCR) reported the number of recorded infected cases included 114 active cases and 33 recovered cases who were staying home. A total of 17 deaths have been recorded.
>
>In an online news briefing, the director of IEDCR, Dr [Meerjady Sabrina Flora](https://en.wikipedia.org/wiki/Meerjady_Sabrina_Flora)
>
>A hospital official told Anadolu Agency, a local news outlet, that one of the deceased was Jalal Saifur Rahman, a director of Bengali Anti-Corruption Commission, who was cared for at the Kuwait Maitree Hospital.
>
>On Saturday, in an online video announcement, Bangladeshi Road Transport and Bridges Minister Obaidul Quader said public transport would be shut down for longer than initially planned, until this coming Saturday. This public transport shutdown had initially started on March 26 and was planned to end on Saturday, April 4. Transport of essential goods -- medical, fuel and food -- was still allowed.
>
>The first recorded incidents of COVID-19 infection in Bangladesh were on March 8, in two people who returned from Italy and also the wife of one of them. As of March 19, these three had already recovered.
>
>Wednesday, April 8, 2020 ["[COVID-19 Confirmed Patients](http://119.40.84.187/surveillance/)" — [IEDCR](https://en.wikipedia.org/wiki/IEDCR) ] [[Full text]](https://en.wikinews.org/wiki/Bangladesh_reports_five_new_deaths_due_to_COVID-19,_a_daily_highest?dpl_id=2891328)