import pandas
from bs4 import BeautifulSoup as bs
import requests
try:
    page=requests.get("https://weather.com/en-IN/weather/tenday/l/2046056f0dc98f950f1ff8c2d24b310cd867622757ab20c8afe5bb3e7e1c3f9b")
    soup=bs(page.content,'lxml')
    table=soup.find("table",class_="twc-table")
    daily_forecast=soup.find(id="main-DailyForecast-1bbda948-59cc-4040-9a36-d9c1ed37a806")
    tabledata_10days=daily_forecast.find_all("tr",class_="clickable closed")
    Row_data=[] #list to store row data
    print("Get Temp. upto 15 days of Lalkuan Haldwani")
    choice=int(input("Select in range day 1 uto day 15 :"))
    if choice<1 or choice>15:
        print("enter valid day")
    for day in range(choice): 
        day1_day=tabledata_10days[day].find("span",class_="date-time").text
        day1_date=tabledata_10days[day].find("span",class_="day-detail clearfix").text.split()
        day1_date="-".join(day1_date)# formatted date
        day1_description=tabledata_10days[day].find("td",class_="description").span.text
        day1_temp=tabledata_10days[day].find("td",class_="temp").div.text.split("°")
        day1_temp=day1_temp[0]+"°"+"C"+"/"+day1_temp[1]+"°"+"C"#modified temperature 
        day1_precip=tabledata_10days[day].find("td",class_="precip").div.text
        day1_wind=tabledata_10days[day].find("td",class_="wind").span.text
        day1_humidity=tabledata_10days[day].find("td",class_="humidity").span.text
        Row_data.append([day1_date+" ",day1_temp,day1_precip+"  ",day1_wind+"  ",day1_humidity+"   "])
    Index=[i for i in range(1,choice+1)] # replace default index in the dataframe
    #creating table using dataframe
    data=pandas.DataFrame(Row_data,index=Index,columns=['DAY-MONTH','HIGH/LOW','PRECIP','WIND(dir/speed)','HUMIDITY'])
    print(data)
    print('Do you want to create a CSV file.')
    feed=input("Enter yes/no :")
    if feed=="yes":
        data.to_csv("weather.csv")
        print("csv created successfully")
except:
    print("Please connect to Internet...")