from datetime import datetime
import webbrowser
import requests
#corpus
greet_message=["hii","hello","hey there","hey","hi there"]
date_msg=["date","tell me date","date today"]
time_msg=["time","tell me time","time right now"]
news_msg = ["news", "tell me news", "latest news", "headlines"]
weather_msg=["weather","tell me weather","current weather"]
#google_msg=["open google","google"]
def get_location():
    response=requests.get("http://ip-api.com/json/")
    data=response.json()
    city=data.get("city","unknown location")
    country=data.get("country","unknown country")
    return city,country
def weather():
    api_key="685a36633e35a8063810b83612d70449"
    city=input("Enter city name: ")
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data=requests.get(url).json()
    if data.get("cod")!="404":
        main=data["main"]
        temperature=main["temp"]
        humidity=main["humidity"]
        weather_desc=data["weather"][0]["description"]
        return f"Temperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {weather_desc}"
    else:
        return "City Not Found"
def get_news():
    api_key = "pub_2abe8aae109d4c01bab6df399795f5c2"
    url = f"https://newsdata.io/api/1/news?apikey={api_key}&q=india&language=en"
    data = requests.get(url).json()
    articles=data['articles']
    totals=len(articles)
    for i in range(totals):
        title=articles[i]['title']
        link=articles[i]['link']
        print(f"{i+1}. {title}\nRead more: {link}\n")
    # results = data.get("results", [])
    # if not results:
    #     return None, None
    # title = results[0]["title"]
    # link = results[0]["link"]
    # return title, link

chat=True
while(chat):
    msg=input("Enter your message: ").lower()
    if msg in greet_message:
        print("hello")
    elif msg in date_msg:
        print(datetime.now().date())
    elif msg in time_msg:
        curr_time=datetime.now().time()
        print(curr_time.strftime("%I:%M:%S"))
    elif msg=="bye":
        print("bye")
        chat=False
    elif "open" in msg:
        site=msg.split("open ")[-1]
        url=f"https://www.{site}.com"
        webbrowser.open(url)
    elif msg=="location":
        print(get_location())
    elif msg in news_msg:
        title, link = get_news()
        print("Headline:", title)
        print("Opening full article in browser...")
        webbrowser.open(link)
    elif msg in weather_msg:
        print(weather())
    else:
        print("i don't understand")