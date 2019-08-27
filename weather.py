from bs4 import BeautifulSoup as bs
import requests
page=requests.get("https://weather.com/en-IN/weather/tenday/l/2046056f0dc98f950f1ff8c2d24b310cd867622757ab20c8afe5bb3e7e1c3f9b")
soup=bs(page.content,'lxml')
table=soup.find("table",class_="twc-table")
daily_forecast=soup.find(id="main-DailyForecast-1bbda948-59cc-4040-9a36-d9c1ed37a806")
tabledata_10days=daily_forecast.find_all("tr",class_="clickable closed")
choice=int(input("Press 1 for Today's Temp or 2 for 10 days Temp :"))
if choice==1:
    day1_day=tabledata_10days[0].find("span",class_="date-time").text
    day1_date=tabledata_10days[0].find("span",class_="day-detail clearfix").text.split(" ")
    day1_date="-".join(day1_date)# formatted date
    day1_description=tabledata_10days[0].find("td",class_="description").span.text
    day1_temp=tabledata_10days[0].find("td",class_="temp").div.text.split("°")
    day1_temp=day1_temp[0]+"°"+"C"+"/"+day1_temp[1]+"°"+"C" #formatted temp.
    day1_precip=tabledata_10days[0].find("td",class_="precip").div.text
    day1_wind=tabledata_10days[0].find("td",class_="wind").span.text
    day1_humidity=tabledata_10days[0].find("td",class_="humidity").span.text
    print(day1_day, day1_date, day1_description,day1_temp,day1_precip,day1_wind,day1_humidity)

else:
    for day in range(len(tabledata_10days)):
        day1_day=tabledata_10days[day].find("span",class_="date-time").text
        day1_date=tabledata_10days[day].find("span",class_="day-detail clearfix").text.split()
        day1_date="-".join(day1_date)# formatted date
        day1_description=tabledata_10days[day].find("td",class_="description").span.text
        day1_temp=tabledata_10days[day].find("td",class_="temp").div.text
        day1_temp=day1_temp[0]+"°"+"C"+"/"+day1_temp[1]+"°"+"C"#modified temperature 
        day1_precip=tabledata_10days[day].find("td",class_="precip").div.text
        day1_wind=tabledata_10days[day].find("td",class_="wind").span.text
        day1_humidity=tabledata_10days[day].find("td",class_="humidity").span.text
    print(day1_day, day1_date, day1_description,day1_temp,day1_precip,day1_wind,day1_humidity)
