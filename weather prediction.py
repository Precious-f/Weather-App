import calendar
print("~o~o~o~o~ Nigerian Weather Prediction ~o~o~o~o~")

userInput= None
my_list= ("a","b","c","d")
while userInput not in my_list:
    #To get user's input 
    userInput = input("suggested questions:\nWhat is the weather like today ? -A \nwhat is the percentage of rainfall this month? -B\nWhat is the percentage of sunshine this month? -C\nIs it going to be a rainy day? -D\n-> ").lower()
#error handling
while True:
    try:
        y = int(input("Enter Year : "))
        if y == 0 :
            print("Invalid input! year should not be less than 1,Please enter a valid year")
        else:  
          break

    except ValueError:
        print("Invalid input!\nPlease enter a valid Year.")
max_month=12
min_month = 1
while True:
    try:
        m=int(input("Enter month in figure (e.g for Jan enter 1): ".format(max_month)))
        if m > max_month:
            print("Invalid input! month should not be greater than {}".format(max_month))
        elif m < min_month:
            print("Invalid input! month should not be less than {}".format(max_month))
        else:    
          break
    except ValueError:
        print("Invalid input!!! please enter a valid integer.")
       

print("")
c = calendar.TextCalendar(calendar.SUNDAY)

# Print the calendar for the current month
str = c.formatmonth(y, m, 0, 0)
print(str)
#error handling incase the the user inputs a number greater than 31

thirties = [4, 9, 6, 11]

max_date=31
min_date = 1

if m in thirties:
    max_date = 30
elif m == 2:
    max_date = 28


if y%4 == 0 and (y%100 != 0 or y%400 == 0):
    if m == 2:
        max_date = 29

while True:
    try:
        d=int(input("Enter date: ".format(max_date)))
        print("")
        if d > max_date:
            print("Invalid input! date should not be greater than {}".format(max_date))
        elif d < min_date:
            print("Invalid input! date should not be less than {}".format(min_date))
        else:    
          break
    except ValueError:
        print("Invalid input!!! please enter a valid integer.")


r=int(input("Enter your geopolitical zones:\n North Central - 1\n North West - 2\n North East - 3\n South East - 4\n South-South - 5\n South West - 6\n -> "))

match userInput:
    case "a":
    
        if m ==1 and r== 1:
            print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
        elif m == 2 and r==1:
            print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
        elif m ==3 and r==1:
            print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
        elif m ==4 and r==1:
            print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
        elif m ==5 and r==1:
            print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
        elif m ==6 and r==1:
            print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
        elif m == 7 and r== 1:
            print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
        elif m == 8 and r== 1:
            print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
        elif m == 9 and r== 1:
            print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
        elif m == 10 and r== 1:
            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
        elif m == 11 and r== 1:
            print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
        elif m == 12 and r== 1:
            print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
    
    
        elif m == 1 and r== 2:
            print("The average temperature ranges between 30°C and 86°F. \nThe temperature will be cooler at night at approximately 13°C(55°F)\nStaying hydrated is advisable. \n")
        elif m == 2 and r==2:
            print("The average maximum daytime temperatures is around 34°C (93°F). \nNighttime temperatures generally drop to 16°C (61F). \nIt is going to be a very  hot day, so wear light and breathable clothes to stay comfortable and also stay hydrated🌞\nIts going to be very cold at night so make sure to wear the appropriate cloth.")
        elif m ==3 and r==2:
            print("Average High Temperature: Around 34°C (93°F). \nAverage Low Temperature at Night: Approximately 16°C (61°F).\nSunshine: Expect around 8 hours of sunshine today\nso protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm and stay hydrated all day🌞🔥 ")
        elif m ==4 and r==2:
            print("The average temperature today is 39°C or 100°F ,therefore it is most likely a sunny day although there is no expection of raifall. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool.\n At nighttime the temperature of approximately 73°F (23°C) . It's the warmest month of the year, ")
        elif m ==5 and r==2:
            print("Average daytime Temperature : Around 39°C (102°F).\n Average Night Temperature: It drops to 26°C (79°F)\nIts going to be a cloudy Day ☁️")
        elif m ==6 and r==2:
            print("The high temperature hovers around 34°C (93.2°F), while we expect rainfall  which will provides refreshing showers . \nSo, expect sultry weather with occasional thunderstorms and rain! ☀️🌧️")       
        elif m == 7 and r== 2:
            print("The average high temperature hovers around 92°F (33.3°C), while the nights remain warm at approximately 76°F (24.4°C). \nExpect thunderstorms and rain.🌦️")      
        elif m == 8 and r== 2:
            print("The average daytime temperature is 27°C (84°F), expect  rainfall\n nighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
        elif m == 9 and r== 2:
            print("Expect daytime temperatures ranging from 75°F to 95°F (24°C to 35°C). \nIt's advisable to stay hydrated, as the heat can be intense. 🌡️☀️")
        elif m == 10 and r== 2:
            print("There woud be very high temperatures, during the day, temperatures often hover around 35°C (95°F), but as evening approaches, \nthere's a noticeable cool-down, with temperatures gently dropping to a more temperate 21°C (70°F) . \nIt's advisable to stay hydrated and seek shade during the hot afternoons! ☀️🌧️")   
        elif m == 11 and r== 2:
            print("Daytime average temperatures can reach 34°C (93°F) . \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F).\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
        elif m == 12 and r== 2:
            print("The average temperatures range between 60°F and 89°F (15.6°C to 31.7°C).\nThe days is would hot, while nights are very cold . Rainy days are rare during December . So, stay hydrated! ☀️🌡️")


        elif m == 1 and r== 3:
            print("High Temperature: Around 92°F (33.3°C)\nLow Temperature: Approximately 74°F (23.3°C)\nOverall, Today offers pleasant conditions for outdoor exploration! 🌞🌡️")
        elif m == 2 and r==3:
            print("High Temperature: Around 92°F (33.3°C)\nHigh Temperature: Around 92°F (33.3°C) \nITs a sunny day so ensure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
        elif m ==3 and r==3:
            print("high temperatures increasing from 97°F to 100°F (36.1°C to 37.8°C). \nNights are warmer too, with lows ranging from 66°F to 72°F (18.9°C to 22.2°C). \nExpect a gentle breeze and mostly clear to partly cloudy skies . \nIt's a great time to explore, but stay hydrated! ☀️🌡️")
        elif m ==4 and r==3:
            print("High Temperatures:The average high temperature occurs around 100°F.\nLow Temperatures: The average low temperature is 75°F\n Cloud cover: Its going to be cloudy.")
        elif m ==5 and r==3:
            print("Sunrise: At 5:57 AM\nSunset: Around 6:38 PM\nAverage High Temperature: Around 93°F (33.9°C)\nAverage Low Temperature: Approximately 75°F (23.9°C).")
        elif m ==6 and r==3:
            print("Sunrise: At 6:01 AM.\nSunset:Around 6:44pm\nAverage High Temperature: Around 87°F (30.6°C)\nRainfall: Expecation a rainfall today.")
        elif m == 7 and r== 3:
            print("Average High Temperature: Still hot at around 31.8°C (89.2°F).\nAverage Low Temperature: Approximately 22.3°C (72.1°F).\nRainfall: Its a rainy day so indoors activies are advised")
        elif m == 8 and r== 3:
            print("High temperatures are around 83°F, rarely falling below 79°F or exceeding 89°F\nLow temperatures hover around 69°F, rarely falling below 67°F or exceeding 71°F . August is a time of transition, so pack an umbrella and embrace the lush greenery! ☔🌡️")
        elif m == 9 and r== 3:
            print("Sunrise: At 6:01 AM\nSunset: Around 6:44 PM \nAverage High Temperature: Around 90°F (32.2°C).\nAverage Low Temperature: Approximately 66°F (18.9°C).")
        elif m == 10 and r== 3:
            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
        elif m == 11 and r== 3:
            print(" Average High Temperature: Around 91°F (32.8°C).\nAverage High Temperature: Around 91°F (32.8°C).\nSunshine: Expect around 9.1 hours of sunshine today.\nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
        elif m == 12 and r== 3:
            print("We  would experience a relatively cooler temperatures, with daytime highs ranging from 92°F to 96°F (31.7°C to 33.8°C). Nighttime temperatures drops, reaching around 57°F (15.5°C).")
                    


        elif m == 1 and r== 4:
            print("Today we will experience warm temperatures with an average high of 86°F (30°C) and a low of 76°F (24.4°C).\nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.🌞")
        elif m == 2 and r==4:
            print("Today we will experience warm temperatures. \nHigh temperatures hover around 87°F (30.6°C), rarely falling below 82°F (27.8°C) or exceeding 91°F (32.8°C) . \nLow temperatures increase slightly from 67°F (19.4°C) to 71°F (21.7°C) 1. \nExpect favorable sunlight hours and a jovial, warm atmosphere.☀️")
        elif m ==3 and r==4:
            print("Today we will experience a very warm and muggy weather. \nAverage highs reach 88°F (31°C), while lows settle around 74°F (23°C). 🌞")
        elif m ==4 and r==4:
            print("Today we will experience a very high temperature with daytime highs around 34°C (94°F) and nighttime lows dropping to 24°C. \nBe prepared for the heat by wearing light, breathable fabrics and staying hydrated. 🌞🔥")
        elif m ==5 and r==4:
            print("Today we will experience a very high temperatures with daytime highs around 33°C (91°F) and nighttime lows cooling down to about 24°C \nKeep in mind that these are average temperatures, and some days can be even warmer. 🌞\n It may rain today, keep that in mind also.🌧️")
        elif m ==6 and r==4:
            print("Today we will experience a warm weather with average temperatures ranging between 31°C (87.8°F) and 23°C (73.4°F). \nIt's a hot day, and you can expect cloudy conditions and a  rainfall. \nThe average daily high temperature hovers around 85°F (29.4°C), while the low temperature stays at approximately 74°F (23.3°C). \nIf you are going to be outdoors pack light clothing and an umbrella! 🌦️🌡️")
        elif m == 7 and r== 4:
            print("Today's weather is partly sunny with an average high temperature around 82°F (28°C) and a low temperature of approximately 75°F (24°C). \nThe average humidity is around 89%, and the wind blows at 5 mph from the west direction. \nKeep in mind that there's a chance of thunderstorms accompanied, so it's a good idea to stay prepared! 🌦️⚡")
        elif m == 8 and r== 4:
            print("Today we will experience a very warm weather with average high temperatures around 83°F (28°C) and low temperatures of approximately 72°F (22°C). \nExpect daytime temperatures around 30°C, while nighttime temperatures can drop to 23°C . \nThis month typically offers some of the year's milder temperatures . 🌞🌧️")
        elif m == 9 and r== 4:
            print("Today we will experience partly sunny weather with an average high temperature around 88°F (31°C) and a low temperature of approximately 75°F (24°C).\nThe humidity is around 89%, and the wind blows at 5 mph from the west direction. \nExpect warm and comfortable evenings ! ☀️🌧️")
        elif m == 10 and r== 4:
            print("Today we will experience partly sunny weather with an average high temperature around 88°F (31°C) and a low temperature of approximately 75°F (24°C). \nThe humidity is around 89%, and the wind blows at 5 mph from the west direction . \nExpect warm days and comfortable evenings during this month! ☀️🌧️")
        elif m == 11 and r== 4:
            print("Today we will experience a delightful climate with an average high temperature around 33°C (92°F) and a low temperature of approximately 22°C (72°F) . \nThis month is characterized by partly cloudy skies and the possibility of a thunderstorm . \nExpect long daylight hours with around 7.3 hours of sunshine daily, making it one of the sunniest months in the year . 🌦️⚡")
        elif m == 12 and r== 4:
            print("Today we will experience relatively cooler weather, akin to winter. \nDaytime temperatures settle within a range of 31.7°C (89.1°F) to 33.8°C (92.8°F)\nNight temperatures drop to their annual nadir at 15.5°C (59.9°F) . \nIf you'd like more detailed daily forecasts, you can check here.")



        elif m == 1 and r== 5:
            print("Daytime Temperatures: Ranging from 25°C (77°F) to 30°C (86°F).\nNighttime Temperatures: Dropping to around 20°C (68°F).\nThe harmattan season brings dry and relatively cool conditions, making it a pleasant time to visit. \nRemember to stay hydrated, especially given the warm temperatures! 🌞🌴")
        elif m == 2 and r==5:
            print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
        elif m ==3 and r==5:
            print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
        elif m ==4 and r==5:
            print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
        elif m ==5 and r==5:
            print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
        elif m ==6 and r==5:
            print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
        elif m == 7 and r== 5:
            print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
        elif m == 8 and r== 5:
            print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
        elif m == 9 and r== 5:
            print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
        elif m == 10 and r== 5:
            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
        elif m == 11 and r== 5:
            print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
        elif m == 12 and r== 5:
            print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
        


        elif m == 1 and r== 6:
            print("Today we will experience cool and wet weather. \nThe average high temperature hovers around 9°C (48°F), while the average low temperature drops to approximately 3°C (37°F) . \nIt's advisable to dress warmly and carry an umbrella or raincoat, as rain is common during this month. 🌧️🧥")
        elif m == 2 and r==6:
            print("Today we will experience a moderate climate. \nThe average high temperature reaches 93°F (34°C). \nThe average low temperature remains around 71°F (22°C) . \nExpect warm day and comfortable night . 🌞🌙")
        elif m ==3 and r==6:
            print("Today we will experience a pleasant climate. \nThe average high temperature reaches 87°F (31°C). \nWhile the average low temperature remains around 75°F (24°C). \nExpect warm days and comfortable nights during this month. 🌞🌙")
        elif m ==4 and r==6:
            print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
        elif m ==5 and r==6:
            print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
        elif m ==6 and r==6:
            print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
        elif m == 7 and r== 6:
            print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
        elif m == 8 and r== 6:
            print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
        elif m == 9 and r== 6:
            print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
        elif m == 10 and r== 6:
            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
        elif m == 11 and r== 6:
            print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
        elif m == 12 and r== 6:
            print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥\n")
        
    #print("NB: The weather precidition ")                                                              
            
    case "b":
        
        if m ==1 and r== 1:
            print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
        elif m == 2 and r==1:
            print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
        elif m ==3 and r==1:
            print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
        elif m ==4 and r==1:
            print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
        elif m ==5 and r==1:
            print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
        elif m ==6 and r==1:
            print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
        elif m == 7 and r== 1:
            print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
        elif m == 8 and r== 1:
            print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
        elif m == 9 and r== 1:
            print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
        elif m == 10 and r== 1:
            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
        elif m == 11 and r== 1:
            print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
        elif m == 12 and r== 1:
            print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
    
    
        elif m == 1 and r== 2:
            print("The average temperature ranges between 30°C and 86°F. \nThe temperature will be cooler at night at approximately 13°C(55°F)\nStaying hydrated is advisable. \n")
        elif m == 2 and r==2:
            print("The average maximum daytime temperatures is around 34°C (93°F). \nNighttime temperatures generally drop to 16°C (61F). \nIt is going to be a very  hot day, so wear light and breathable clothes to stay comfortable and also stay hydrated🌞\nIts going to be very cold at night so make sure to wear the appropriate cloth.")
        elif m ==3 and r==2:
            print("Average High Temperature: Around 34°C (93°F). \nAverage Low Temperature at Night: Approximately 16°C (61°F).\nSunshine: Expect around 8 hours of sunshine today\nso protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm and stay hydrated all day🌞🔥 ")
        elif m ==4 and r==2:
            print("The average temperature today is 39°C or 100°F ,therefore it is most likely a sunny day although there is no expection of raifall. \nEnsure you wear breathable materials like cotton, linen, and jersey. \\nLight-colored fabrics help reflect heat and keep you cool.\nAt nighttime the temperature of approximately 73°F (23°C) . It's the warmest month of the year, so  ")
        elif m ==5 and r==2:
            print("Average daytime Temperature : Around 39°C (102°F).\n Average Night Temperature: It drops to 26°C (79°F)\nIts going to be a cloudy Day ☁️")
        elif m ==6 and r==2:
            print("The high temperature hovers around 34°C (93.2°F), while we expect rainfall  which will provides refreshing showers . \nSo, expect sultry weather with occasional thunderstorms and rain! ☀️🌧️")       
        elif m == 7 and r== 2:
            print("The average high temperature hovers around 92°F (33.3°C), while the nights remain warm at approximately 76°F (24.4°C). \nExpect thunderstorms and rain.🌦️")      
        elif m == 8 and r== 2:
            print("The average daytime temperature is 27°C (84°F), expect  rainfall\n nighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
        elif m == 9 and r== 2:
            print("Expect daytime temperatures ranging from 75°F to 95°F (24°C to 35°C). \nIt's advisable to stay hydrated, as the heat can be intense. 🌡️☀️")
        elif m == 10 and r== 2:
            print("There woud be very high temperatures, during the day, temperatures often hover around 35°C (95°F), but as evening approaches, \nthere's a noticeable cool-down, with temperatures gently dropping to a more temperate 21°C (70°F) . \nIt's advisable to stay hydrated and seek shade during the hot afternoons! ☀️🌧️")   
        elif m == 11 and r== 2:
            print("Daytime average temperatures can reach 34°C (93°F) . \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F).\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
        elif m == 12 and r== 2:
            print("The average temperatures range between 60°F and 89°F (15.6°C to 31.7°C).\nThe days is would hot, while nights are very cold . Rainy days are rare during December . So, stay hydrated! ☀️🌡️")


        elif m == 1 and r== 3:
            print("High Temperature: Around 92°F (33.3°C)\nLow Temperature: Approximately 74°F (23.3°C)\nOverall, Today offers pleasant conditions for outdoor exploration! 🌞🌡️")
        elif m == 2 and r==3:
            print("High Temperature: Around 92°F (33.3°C)\nHigh Temperature: Around 92°F (33.3°C) \nITs a sunny day so ensure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
        elif m ==3 and r==3:
            print("high temperatures increasing from 97°F to 100°F (36.1°C to 37.8°C). \nNights are warmer too, with lows ranging from 66°F to 72°F (18.9°C to 22.2°C). \nExpect a gentle breeze and mostly clear to partly cloudy skies . \nIt's a great time to explore, but stay hydrated! ☀️🌡️")
        elif m ==4 and r==3:
            print("High Temperatures:The average high temperature occurs around 100°F.\nLow Temperatures: The average low temperature is 75°F\n Cloud cover: Its going to be cloudy.")
        elif m ==5 and r==3:
            print("Sunrise: At 5:57 AM\nSunset: Around 6:38 PM\nAverage High Temperature: Around 93°F (33.9°C)\nAverage Low Temperature: Approximately 75°F (23.9°C).")
        elif m ==6 and r==3:
            print("Sunrise: At 6:01 AM.\nSunset:Around 6:44pm\nAverage High Temperature: Around 87°F (30.6°C)\nRainfall: Expecation a rainfall today.")
        elif m == 7 and r== 3:
            print("Average High Temperature: Still hot at around 31.8°C (89.2°F).\nAverage Low Temperature: Approximately 22.3°C (72.1°F).\nRainfall: Its a rainy day so indoors activies are advised")
        elif m == 8 and r== 3:
            print("High temperatures are around 83°F, rarely falling below 79°F or exceeding 89°F\nLow temperatures hover around 69°F, rarely falling below 67°F or exceeding 71°F . August is a time of transition, so pack an umbrella and embrace the lush greenery! ☔🌡️")
        elif m == 9 and r== 3:
            print("Sunrise: At 6:01 AM\nSunset: Around 6:44 PM \nAverage High Temperature: Around 90°F (32.2°C).\nAverage Low Temperature: Approximately 66°F (18.9°C).")
        elif m == 10 and r== 3:
            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
        elif m == 11 and r== 3:
            print(" Average High Temperature: Around 91°F (32.8°C).\nAverage High Temperature: Around 91°F (32.8°C).\nSunshine: Expect around 9.1 hours of sunshine today.\nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
        elif m == 12 and r== 3:
            print("We  would experience a relatively cooler temperatures, with daytime highs ranging from 92°F to 96°F (31.7°C to 33.8°C). Nighttime temperatures drops, reaching around 57°F (15.5°C).")
                    


        elif m == 1 and r== 4:
            print("Today we will experience warm temperatures with an average high of 86°F (30°C) and a low of 76°F (24.4°C).\nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.🌞")
        elif m == 2 and r==4:
            print("Today we will experience warm temperatures. \nHigh temperatures hover around 87°F (30.6°C), rarely falling below 82°F (27.8°C) or exceeding 91°F (32.8°C) . \nLow temperatures increase slightly from 67°F (19.4°C) to 71°F (21.7°C) 1. \nExpect favorable sunlight hours and a jovial, warm atmosphere.☀️")
        elif m ==3 and r==4:
            print("Today we will experience a very warm and muggy weather. \nAverage highs reach 88°F (31°C), while lows settle around 74°F (23°C). 🌞")
        elif m ==4 and r==4:
            print("Today we will experience a very high temperature with daytime highs around 34°C (94°F) and nighttime lows dropping to 24°C. \nBe prepared for the heat by wearing light, breathable fabrics and staying hydrated. 🌞🔥")
        elif m ==5 and r==4:
            print("Today we will experience a very high temperatures with daytime highs around 33°C (91°F) and nighttime lows cooling down to about 24°C \nKeep in mind that these are average temperatures, and some days can be even warmer. 🌞\n It may rain today, keep that in mind also.🌧️")
        elif m ==6 and r==4:
            print("Today we will experience a warm weather with average temperatures ranging between 31°C (87.8°F) and 23°C (73.4°F). \nIt's a hot day, and you can expect cloudy conditions and a  rainfall. \nThe average daily high temperature hovers around 85°F (29.4°C), while the low temperature stays at approximately 74°F (23.3°C). \nIf you are going to be outdoors pack light clothing and an umbrella! 🌦️🌡️")
        elif m == 7 and r== 4:
            print("Today's weather is partly sunny with an average high temperature around 82°F (28°C) and a low temperature of approximately 75°F (24°C). \nThe average humidity is around 89%, and the wind blows at 5 mph from the west direction. \nKeep in mind that there's a chance of thunderstorms accompanied, so it's a good idea to stay prepared! 🌦️⚡")
        elif m == 8 and r== 4:
            print("Today we will experience a very warm weather with average high temperatures around 83°F (28°C) and low temperatures of approximately 72°F (22°C). \nExpect daytime temperatures around 30°C, while nighttime temperatures can drop to 23°C . \nThis month typically offers some of the year's milder temperatures . 🌞🌧️")
        elif m == 9 and r== 4:
            print("Today we will experience partly sunny weather with an average high temperature around 88°F (31°C) and a low temperature of approximately 75°F (24°C).\nThe humidity is around 89%, and the wind blows at 5 mph from the west direction. \nExpect warm and comfortable evenings ! ☀️🌧️")
        elif m == 10 and r== 4:
            print("Today we will experience partly sunny weather with an average high temperature around 88°F (31°C) and a low temperature of approximately 75°F (24°C). \nThe humidity is around 89%, and the wind blows at 5 mph from the west direction . \nExpect warm days and comfortable evenings during this month! ☀️🌧️")
        elif m == 11 and r== 4:
            print("Today we will experience a delightful climate with an average high temperature around 33°C (92°F) and a low temperature of approximately 22°C (72°F) . \nThis month is characterized by partly cloudy skies and the possibility of a thunderstorm . \nExpect long daylight hours with around 7.3 hours of sunshine daily, making it one of the sunniest months in the year . 🌦️⚡")
        elif m == 12 and r== 4:
            print("Today we will experience relatively cooler weather, akin to winter. \nDaytime temperatures settle within a range of 31.7°C (89.1°F) to 33.8°C (92.8°F)\nNight temperatures drop to their annual nadir at 15.5°C (59.9°F) . \nIf you'd like more detailed daily forecasts, you can check here.")



        elif m == 1 and r== 5:
            print("")
        elif m == 2 and r==5:
            print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
        elif m ==3 and r==5:
            print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
        elif m ==4 and r==5:
            print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
        elif m ==5 and r==5:
            print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
        elif m ==6 and r==5:
            print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
        elif m == 7 and r== 5:
            print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
        elif m == 8 and r== 5:
            print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
        elif m == 9 and r== 5:
            print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
        elif m == 10 and r== 5:
            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
        elif m == 11 and r== 5:
            print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
        elif m == 12 and r== 5:
            print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
        

        elif m == 1 and r== 6:
            print("In January, the south-west region typically receives about 141.58 millimeters (5.57 inches) of precipitation \nwith 224.18 rainy days (approximately 61.42% of the time). \nIt's a relatively wet month, so be prepared for rain. ☔🌧️")
        elif m == 2 and r==6:
            print("In February, the south-west region typically receives about 141.58 millimeters (5.57 inches) of precipitation \nwith 224.18 rainy days (approximately 61.42% of the time). \nIt's a relatively wet month, so be prepared for rain. ☔🌧️")
        elif m == 3 and r==6:
            print("In March, the south-west region typically receives about 141.58 millimeters (5.57 inches) of precipitation \nwith 224.18 rainy days (approximately 61.42% of the time). \nIt's a relatively wet month, so be prepared for rain. ☔🌧️")
        elif m ==4 and r==6:
            print("In April, the south-west region typically receives about 4.75 inches (120.7 mm) of rainfall during the month.\n The percentage of rainfall is 59% this month \nIt's a relatively wet period, so be prepared for rain. ☔🌧️")
        elif m ==5 and r==6:
            print("In May, the south-west region typically receives approximately 4.39 inches (111.5 mm) of precipitation \nwith 40% of the days experiencing rainy weather. \nIt's advisable to carry an umbrella or raincoat during your visit! ☔🌧️")
        elif m ==6 and r==6:
            print("In June, the south-west region experiences heavy rainfall, \nwith an average of approximately 313 mm for the month. \nThis marks the year's heaviest rainfall, and intense rain showers are frequent. \nBe prepared with appropriate rain gear to stay dry! ☔🌧️")
        elif m == 7 and r== 6:
            print("In July, the south-west region typically receives around 14.4 inches (366 mm) of precipitation, \nwith 70% of the days experiencing rainy weather. \nIt's a wet month, \nso be prepared with an umbrella or raincoat if you're in Lagos! ☔🌧️")
        elif m == 8 and r== 6:
            print("In August, the south-west region typically experiences high rainfall, averaging around 146 mm for the month. \nThis translates to approximately 12 rainy days. \nWhile the daytime temperatures hover around 28°C (82°F), \nevenings cool down to a more temperate 24°C (75°F). \nThe area enjoys about 110 hours of sunshine, \nmaking it neither too gloomy nor overly bright. \nIf you're planning a visit, consider airy clothing and bring a raincoat just in case! ☔🌞")
        elif m == 9 and r== 6:
            print("In September, the south-west region typically experiences heavy rainfall, \naveraging around 201 mm for the month. \nApproximately 13 days of rainfall are expected, with daytime temperatures hovering around 28°C (83°F) and nights cooling down to about 24°C (75°F). \nThe area enjoys a balanced 116 hours of sunlight, ensuring it's neither too overcast nor too sunny. \nIf you're planning a visit, consider airy clothing and bring a raincoat just in case! ☔🌞")
        elif m == 10 and r== 6:
            print("In October, the south-west region typically receives moderate rainfall, \naveraging around 66 mm for the month . \nRain is expected on roughly 12 days. \nThe city usually sees around 170 hours of sunlight, \nindicating a moderately sunny period. \nWhile daytime temperatures settle at around 29°C (85°F), \nevenings drop to approximately 25°C (77°F)\nIt's essential to be prepared for such heat. \nWearing light, breathable fabrics and protecting yourself from the sun's intensity with hats or shades can make a difference.☔🌞")
        elif m == 11 and r== 6:
            print("In November, the south-west region typically experiences moderate rainfall, \naveraging around 85 mm for the month. \nTypically, around 5 days of rainfall are expected. \nThe area enjoys a balanced 188 hours of sunlight, \nensuring it's neither too overcast nor too sunny. \nIf you're inclined towards comfortable temperatures and drier conditions, \n Dress in lightweight and breathable outfits to handle the warmth, \nand don't forget your raincoat for occasional showers! ☔🌞")
        elif m == 12 and r== 6:
            print("In December, the south-west region generally experiences very high temperatures during the day, \nsettling around 31°C (87°F). \nHowever, evenings bring relief as temperatures drop to approximately 26°C (79°F). \nIt's advisable to wear appropriate clothing to handle the warmth.\n\nAs for rainfall, the south-west region typically receives moderate precipitation, \naveraging around 40 mm (1.57 inches) for the month. Rain is expected on roughly 2 days. \nWith approximately 193 hours of sunshine, most days are sunny, giving the area a pleasant and vibrant feel. \nDecember is a great time to visit if you prefer dry days with pleasant temperatures. 🌞☔")



    case "c":
        
        if m ==1 and r== 1:
            print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
        elif m == 2 and r==1:
            print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
        elif m ==3 and r==1:
            print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
        elif m ==4 and r==1:
            print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
        elif m ==5 and r==1:
            print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
        elif m ==6 and r==1:
            print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
        elif m == 7 and r== 1:
            print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
        elif m == 8 and r== 1:
            print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
        elif m == 9 and r== 1:
            print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
        elif m == 10 and r== 1:
            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
        elif m == 11 and r== 1:
            print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
        elif m == 12 and r== 1:
            print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
    
    
        elif m == 1 and r== 2:
            print("The average temperature ranges between 30°C and 86°F. \nThe temperature will be cooler at night at approximately 13°C(55°F)\nStaying hydrated is advisable. \n")
        elif m == 2 and r==2:
            print("The average maximum daytime temperatures is around 34°C (93°F). \nNighttime temperatures generally drop to 16°C (61F). \nIt is going to be a very  hot day, so wear light and breathable clothes to stay comfortable and also stay hydrated🌞\nIts going to be very cold at night so make sure to wear the appropriate cloth.")
        elif m ==3 and r==2:
            print("Average High Temperature: Around 34°C (93°F). \nAverage Low Temperature at Night: Approximately 16°C (61°F).\nSunshine: Expect around 8 hours of sunshine today\nso protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm and stay hydrated all day🌞🔥 ")
        elif m ==4 and r==2:
            print("The average temperature today is 39°C or 100°F ,therefore it is most likely a sunny day although there is no expection of raifall. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool.\nAt nighttime the temperature of approximately 73°F (23°C) . It's the warmest month of the year, so  ")
        elif m ==5 and r==2:
            print("Average daytime Temperature : Around 39°C (102°F).\n Average Night Temperature: It drops to 26°C (79°F)\nIts going to be a cloudy Day ☁️")
        elif m ==6 and r==2:
            print("The high temperature hovers around 34°C (93.2°F), while we expect rainfall  which will provides refreshing showers . \nSo, expect sultry weather with occasional thunderstorms and rain! ☀️🌧️")       
        elif m == 7 and r== 2:
            print("The average high temperature hovers around 92°F (33.3°C), while the nights remain warm at approximately 76°F (24.4°C). \nExpect thunderstorms and rain.🌦️")      
        elif m == 8 and r== 2:
            print("The average daytime temperature is 27°C (84°F), expect  rainfall\n nighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
        elif m == 9 and r== 2:
            print("Expect daytime temperatures ranging from 75°F to 95°F (24°C to 35°C). \nIt's advisable to stay hydrated, as the heat can be intense. 🌡️☀️")
        elif m == 10 and r== 2:
            print("There woud be very high temperatures, during the day, temperatures often hover around 35°C (95°F), but as evening approaches, \nthere's a noticeable cool-down, with temperatures gently dropping to a more temperate 21°C (70°F) . \nIt's advisable to stay hydrated and seek shade during the hot afternoons! ☀️🌧️")   
        elif m == 11 and r== 2:
            print("Daytime average temperatures can reach 34°C (93°F) . \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F).\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
        elif m == 12 and r== 2:
            print("The average temperatures range between 60°F and 89°F (15.6°C to 31.7°C).\nThe days is would hot, while nights are very cold . Rainy days are rare during December . So, stay hydrated! ☀️🌡️")


        elif m == 1 and r== 3:
            print("High Temperature: Around 92°F (33.3°C)\nLow Temperature: Approximately 74°F (23.3°C)\nOverall, Today offers pleasant conditions for outdoor exploration! 🌞🌡️")
        elif m == 2 and r==3:
            print("High Temperature: Around 92°F (33.3°C)\nHigh Temperature: Around 92°F (33.3°C) \nITs a sunny day so ensure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
        elif m ==3 and r==3:
            print("high temperatures increasing from 97°F to 100°F (36.1°C to 37.8°C). \nNights are warmer too, with lows ranging from 66°F to 72°F (18.9°C to 22.2°C). \nExpect a gentle breeze and mostly clear to partly cloudy skies . \nIt's a great time to explore, but stay hydrated! ☀️🌡️")
        elif m ==4 and r==3:
            print("High Temperatures:The average high temperature occurs around 100°F.\nLow Temperatures: The average low temperature is 75°F\n Cloud cover: Its going to be cloudy.")
        elif m ==5 and r==3:
            print("Sunrise: At 5:57 AM\nSunset: Around 6:38 PM\nAverage High Temperature: Around 93°F (33.9°C)\nAverage Low Temperature: Approximately 75°F (23.9°C).")
        elif m ==6 and r==3:
            print("Sunrise: At 6:01 AM.\nSunset:Around 6:44pm\nAverage High Temperature: Around 87°F (30.6°C)\nRainfall: Expecation a rainfall today.")
        elif m == 7 and r== 3:
            print("Average High Temperature: Still hot at around 31.8°C (89.2°F).\nAverage Low Temperature: Approximately 22.3°C (72.1°F).\nRainfall: Its a rainy day so indoors activies are advised")
        elif m == 8 and r== 3:
            print("High temperatures are around 83°F, rarely falling below 79°F or exceeding 89°F\nLow temperatures hover around 69°F, rarely falling below 67°F or exceeding 71°F . August is a time of transition, so pack an umbrella and embrace the lush greenery! ☔🌡️")
        elif m == 9 and r== 3:
            print("Sunrise: At 6:01 AM\nSunset: Around 6:44 PM \nAverage High Temperature: Around 90°F (32.2°C).\nAverage Low Temperature: Approximately 66°F (18.9°C).")
        elif m == 10 and r== 3:
            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
        elif m == 11 and r== 3:
            print(" Average High Temperature: Around 91°F (32.8°C).\nAverage High Temperature: Around 91°F (32.8°C).\nSunshine: Expect around 9.1 hours of sunshine today.\nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
        elif m == 12 and r== 3:
            print("We  would experience a relatively cooler temperatures, with daytime highs ranging from 92°F to 96°F (31.7°C to 33.8°C). Nighttime temperatures drops, reaching around 57°F (15.5°C).")
                    

        elif m == 1 and r== 4:
            print("Today we will experience warm temperatures with an average high of 86°F (30°C) and a low of 76°F (24.4°C).\nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.🌞")
        elif m == 2 and r==4:
            print("Today we will experience warm temperatures. \nHigh temperatures hover around 87°F (30.6°C), rarely falling below 82°F (27.8°C) or exceeding 91°F (32.8°C) . \nLow temperatures increase slightly from 67°F (19.4°C) to 71°F (21.7°C) 1. \nExpect favorable sunlight hours and a jovial, warm atmosphere.☀️")
        elif m ==3 and r==4:
            print("Today we will experience a very warm and muggy weather. \nAverage highs reach 88°F (31°C), while lows settle around 74°F (23°C). 🌞")
        elif m ==4 and r==4:
            print("Today we will experience a very high temperature with daytime highs around 34°C (94°F) and nighttime lows dropping to 24°C. \nBe prepared for the heat by wearing light, breathable fabrics and staying hydrated. 🌞🔥")
        elif m ==5 and r==4:
            print("Today we will experience a very high temperatures with daytime highs around 33°C (91°F) and nighttime lows cooling down to about 24°C \nKeep in mind that these are average temperatures, and some days can be even warmer. 🌞\n It may rain today, keep that in mind also.🌧️")
        elif m ==6 and r==4:
            print("Today we will experience a warm weather with average temperatures ranging between 31°C (87.8°F) and 23°C (73.4°F). \nIt's a hot day, and you can expect cloudy conditions and a  rainfall. \nThe average daily high temperature hovers around 85°F (29.4°C), while the low temperature stays at approximately 74°F (23.3°C). \nIf you are going to be outdoors pack light clothing and an umbrella! 🌦️🌡️")
        elif m == 7 and r== 4:
            print("Today's weather is partly sunny with an average high temperature around 82°F (28°C) and a low temperature of approximately 75°F (24°C). \nThe average humidity is around 89%, and the wind blows at 5 mph from the west direction. \nKeep in mind that there's a chance of thunderstorms accompanied, so it's a good idea to stay prepared! 🌦️⚡")
        elif m == 8 and r== 4:
            print("Today we will experience a very warm weather with average high temperatures around 83°F (28°C) and low temperatures of approximately 72°F (22°C). \nExpect daytime temperatures around 30°C, while nighttime temperatures can drop to 23°C . \nThis month typically offers some of the year's milder temperatures . 🌞🌧️")
        elif m == 9 and r== 4:
            print("Today we will experience partly sunny weather with an average high temperature around 88°F (31°C) and a low temperature of approximately 75°F (24°C).\nThe humidity is around 89%, and the wind blows at 5 mph from the west direction. \nExpect warm and comfortable evenings ! ☀️🌧️")
        elif m == 10 and r== 4:
            print("Today we will experience partly sunny weather with an average high temperature around 88°F (31°C) and a low temperature of approximately 75°F (24°C). \nThe humidity is around 89%, and the wind blows at 5 mph from the west direction . \nExpect warm days and comfortable evenings during this month! ☀️🌧️")
        elif m == 11 and r== 4:
            print("Today we will experience a delightful climate with an average high temperature around 33°C (92°F) and a low temperature of approximately 22°C (72°F) . \nThis month is characterized by partly cloudy skies and the possibility of a thunderstorm . \nExpect long daylight hours with around 7.3 hours of sunshine daily, making it one of the sunniest months in the year . 🌦️⚡")
        elif m == 12 and r== 4:
            print("Today we will experience relatively cooler weather, akin to winter. \nDaytime temperatures settle within a range of 31.7°C (89.1°F) to 33.8°C (92.8°F)\nNight temperatures drop to their annual nadir at 15.5°C (59.9°F) . \nIf you'd like more detailed daily forecasts, you can check here.")


        elif m == 1 and r== 5:
            print("")
        elif m == 2 and r==5:
            print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
        elif m ==3 and r==5:
            print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
        elif m ==4 and r==5:
            print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
        elif m ==5 and r==5:
            print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
        elif m ==6 and r==5:
            print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
        elif m == 7 and r== 5:
            print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
        elif m == 8 and r== 5:
            print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
        elif m == 9 and r== 5:
            print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
        elif m == 10 and r== 5:
            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
        elif m == 11 and r== 5:
            print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
        elif m == 12 and r== 5:
            print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
        


        elif m == 1 and r== 6:
            print("In January, south-west region typically enjoys 163 hours of sunlight, \nwhich accounts for approximately 50.5% of the available daylight hours. \nIt's a moderately sunny month, with occasional periods of cloudy or overcast skies. \nIf you're planning a visit, consider wearing airy clothing and enjoy the pleasant weather! 🌞")
        elif m == 2 and r==6:
            print("In February, south-west region typically enjoys 170 hours of sunlight, \nwhich accounts for approximately 56.7% of the available daylight hours. \nIt's quite sunny, with occasional periods of cloudy or overcast skies. \nIf you're planning a visit, consider wearing airy clothing and enjoy the pleasant weather! 🌞")
        elif m == 3 and r==6:
            print("In March, the south-west region typically receives about 141.58 millimeters (5.57 inches) of precipitation \nwith 224.18 rainy days (approximately 61.42% of the time). \nIt's a relatively wet month, so be prepared for rain. ☔🌧️")
        elif m ==4 and r==6:
            print("In April, the south-west region typically receives about 4.75 inches (120.7 mm) of rainfall during the month.\n The percentage of rainfall is 59% this month \nIt's a relatively wet period, so be prepared for rain. ☔🌧️")
        elif m ==5 and r==6:
            print("In May, the south-west region typically receives approximately 4.39 inches (111.5 mm) of precipitation \nwith 40% of the days experiencing rainy weather. \nIt's advisable to carry an umbrella or raincoat during your visit! ☔🌧️")
        elif m ==6 and r==6:
            print("In June, the south-west region experiences heavy rainfall, \nwith an average of approximately 313 mm for the month. \nThis marks the year's heaviest rainfall, and intense rain showers are frequent. \nBe prepared with appropriate rain gear to stay dry! ☔🌧️")
        elif m == 7 and r== 6:
            print("In July, the south-west region typically receives around 14.4 inches (366 mm) of precipitation, \nwith 70% of the days experiencing rainy weather. \nIt's a wet month, \nso be prepared with an umbrella or raincoat if you're in Lagos! ☔🌧️")
        elif m == 8 and r== 6:
            print("In August, the south-west region typically experiences high rainfall, averaging around 146 mm for the month. \nThis translates to approximately 12 rainy days. \nWhile the daytime temperatures hover around 28°C (82°F), \nevenings cool down to a more temperate 24°C (75°F). \nThe area enjoys about 110 hours of sunshine, \nmaking it neither too gloomy nor overly bright. \nIf you're planning a visit, consider airy clothing and bring a raincoat just in case! ☔🌞")
        elif m == 9 and r== 6:
            print("In September, the south-west region typically experiences heavy rainfall, \naveraging around 201 mm for the month. \nApproximately 13 days of rainfall are expected, with daytime temperatures hovering around 28°C (83°F) and nights cooling down to about 24°C (75°F). \nThe area enjoys a balanced 116 hours of sunlight, ensuring it's neither too overcast nor too sunny. \nIf you're planning a visit, consider airy clothing and bring a raincoat just in case! ☔🌞")
        elif m == 10 and r== 6:
            print("In October, the south-west region typically receives moderate rainfall, \naveraging around 66 mm for the month . \nRain is expected on roughly 12 days. \nThe city usually sees around 170 hours of sunlight, \nindicating a moderately sunny period. \nWhile daytime temperatures settle at around 29°C (85°F), \nevenings drop to approximately 25°C (77°F)\nIt's essential to be prepared for such heat. \nWearing light, breathable fabrics and protecting yourself from the sun's intensity with hats or shades can make a difference.☔🌞")
        elif m == 11 and r== 6:
            print("In November, the south-west region typically experiences moderate rainfall, \naveraging around 85 mm for the month. \nTypically, around 5 days of rainfall are expected. \nThe area enjoys a balanced 188 hours of sunlight, \nensuring it's neither too overcast nor too sunny. \nIf you're inclined towards comfortable temperatures and drier conditions, \n Dress in lightweight and breathable outfits to handle the warmth, \nand don't forget your raincoat for occasional showers! ☔🌞")
        elif m == 12 and r== 6:
            print("In December, the south-west region generally experiences very high temperatures during the day, \nsettling around 31°C (87°F). \nHowever, evenings bring relief as temperatures drop to approximately 26°C (79°F). \nIt's advisable to wear appropriate clothing to handle the warmth.\n\nAs for rainfall, the south-west region typically receives moderate precipitation, \naveraging around 40 mm (1.57 inches) for the month. Rain is expected on roughly 2 days. \nWith approximately 193 hours of sunshine, most days are sunny, giving the area a pleasant and vibrant feel. \nDecember is a great time to visit if you prefer dry days with pleasant temperatures. 🌞☔")




    case "d":
        
        if m ==1 and r== 1:
            print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
        elif m == 2 and r==1:
            print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
        elif m ==3 and r==1:
            print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
        elif m ==4 and r==1:
            print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
        elif m ==5 and r==1:
            print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
        elif m ==6 and r==1:
            print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
        elif m == 7 and r== 1:
            print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
        elif m == 8 and r== 1:
            print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
        elif m == 9 and r== 1:
            print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
        elif m == 10 and r== 1:
            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
        elif m == 11 and r== 1:
            print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
        elif m == 12 and r== 1:
            print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
    
    
        elif m == 1 and r== 2:
            print("The average temperature ranges between 30°C and 86°F. \nThe temperature will be cooler at night at approximately 13°C(55°F)\nStaying hydrated is advisable. \n")
        elif m == 2 and r==2:
            print("The average maximum daytime temperatures is around 34°C (93°F). \nNighttime temperatures generally drop to 16°C (61F). \nIt is going to be a very  hot day, so wear light and breathable clothes to stay comfortable and also stay hydrated🌞\nIts going to be very cold at night so make sure to wear the appropriate cloth.")
        elif m ==3 and r==2:
            print("Average High Temperature: Around 34°C (93°F). \nAverage Low Temperature at Night: Approximately 16°C (61°F).\nSunshine: Expect around 8 hours of sunshine today\nso protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm and stay hydrated all day🌞🔥 ")
        elif m ==4 and r==2:
            print("The average temperature today is 39°C or 100°F ,therefore it is most likely a sunny day although there is no expection of raifall. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool.\nAt nighttime the temperature of approximately 73°F (23°C) . It's the warmest month of the year, so  ")
        elif m ==5 and r==2:
            print("Average daytime Temperature : Around 39°C (102°F).\n Average Night Temperature: It drops to 26°C (79°F)\nIts going to be a cloudy Day ☁️")
        elif m ==6 and r==2:
            print("The high temperature hovers around 34°C (93.2°F), while we expect rainfall  which will provides refreshing showers . \nSo, expect sultry weather with occasional thunderstorms and rain! ☀️🌧️")       
        elif m == 7 and r== 2:
            print("The average high temperature hovers around 92°F (33.3°C), while the nights remain warm at approximately 76°F (24.4°C). \nExpect thunderstorms and rain.🌦️")      
        elif m == 8 and r== 2:
            print("The average daytime temperature is 27°C (84°F), expect  rainfall\n nighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
        elif m == 9 and r== 2:
            print("Expect daytime temperatures ranging from 75°F to 95°F (24°C to 35°C). \nIt's advisable to stay hydrated, as the heat can be intense. 🌡️☀️")
        elif m == 10 and r== 2:
            print("There woud be very high temperatures, during the day, temperatures often hover around 35°C (95°F), but as evening approaches, \nthere's a noticeable cool-down, with temperatures gently dropping to a more temperate 21°C (70°F) . \nIt's advisable to stay hydrated and seek shade during the hot afternoons! ☀️🌧️")   
        elif m == 11 and r== 2:
            print("Daytime average temperatures can reach 34°C (93°F) . \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F).\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
        elif m == 12 and r== 2:
            print("The average temperatures range between 60°F and 89°F (15.6°C to 31.7°C).\nThe days is would hot, while nights are very cold . Rainy days are rare during December . So, stay hydrated! ☀️🌡️")


        elif m == 1 and r== 3:
            print("High Temperature: Around 92°F (33.3°C)\nLow Temperature: Approximately 74°F (23.3°C)\nOverall, Today offers pleasant conditions for outdoor exploration! 🌞🌡️")
        elif m == 2 and r==3:
            print("High Temperature: Around 92°F (33.3°C)\nHigh Temperature: Around 92°F (33.3°C) \nITs a sunny day so ensure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
        elif m ==3 and r==3:
            print("high temperatures increasing from 97°F to 100°F (36.1°C to 37.8°C). \nNights are warmer too, with lows ranging from 66°F to 72°F (18.9°C to 22.2°C). \nExpect a gentle breeze and mostly clear to partly cloudy skies . \nIt's a great time to explore, but stay hydrated! ☀️🌡️")
        elif m ==4 and r==3:
            print("High Temperatures:The average high temperature occurs around 100°F.\nLow Temperatures: The average low temperature is 75°F\n Cloud cover: Its going to be cloudy.")
        elif m ==5 and r==3:
            print("Sunrise: At 5:57 AM\nSunset: Around 6:38 PM\nAverage High Temperature: Around 93°F (33.9°C)\nAverage Low Temperature: Approximately 75°F (23.9°C).")
        elif m ==6 and r==3:
            print("Sunrise: At 6:01 AM.\nSunset:Around 6:44pm\nAverage High Temperature: Around 87°F (30.6°C)\nRainfall: Expecation a rainfall today.")
        elif m == 7 and r== 3:
            print("Average High Temperature: Still hot at around 31.8°C (89.2°F).\nAverage Low Temperature: Approximately 22.3°C (72.1°F).\nRainfall: Its a rainy day so indoors activies are advised")
        elif m == 8 and r== 3:
            print("High temperatures are around 83°F, rarely falling below 79°F or exceeding 89°F\nLow temperatures hover around 69°F, rarely falling below 67°F or exceeding 71°F . August is a time of transition, so pack an umbrella and embrace the lush greenery! ☔🌡️")
        elif m == 9 and r== 3:
            print("Sunrise: At 6:01 AM\nSunset: Around 6:44 PM \nAverage High Temperature: Around 90°F (32.2°C).\nAverage Low Temperature: Approximately 66°F (18.9°C).")
        elif m == 10 and r== 3:
            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
        elif m == 11 and r== 3:
            print(" Average High Temperature: Around 91°F (32.8°C).\nAverage High Temperature: Around 91°F (32.8°C).\nSunshine: Expect around 9.1 hours of sunshine today.\nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
        elif m == 12 and r== 3:
            print("We  would experience a relatively cooler temperatures, with daytime highs ranging from 92°F to 96°F (31.7°C to 33.8°C). Nighttime temperatures drops, reaching around 57°F (15.5°C).")
                    


        elif m == 1 and r== 4:
            print("Today we will experience warm temperatures with an average high of 86°F (30°C) and a low of 76°F (24.4°C).\nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.🌞")
        elif m == 2 and r==4:
            print("Today we will experience warm temperatures. \nHigh temperatures hover around 87°F (30.6°C), rarely falling below 82°F (27.8°C) or exceeding 91°F (32.8°C) . \nLow temperatures increase slightly from 67°F (19.4°C) to 71°F (21.7°C) 1. \nExpect favorable sunlight hours and a jovial, warm atmosphere.☀️")
        elif m ==3 and r==4:
            print("Today we will experience a very warm and muggy weather. \nAverage highs reach 88°F (31°C), while lows settle around 74°F (23°C). 🌞")
        elif m ==4 and r==4:
            print("Today we will experience a very high temperature with daytime highs around 34°C (94°F) and nighttime lows dropping to 24°C. \nBe prepared for the heat by wearing light, breathable fabrics and staying hydrated. 🌞🔥")
        elif m ==5 and r==4:
            print("Today we will experience a very high temperatures with daytime highs around 33°C (91°F) and nighttime lows cooling down to about 24°C \nKeep in mind that these are average temperatures, and some days can be even warmer. 🌞\n It may rain today, keep that in mind also.🌧️")
        elif m ==6 and r==4:
            print("Today we will experience a warm weather with average temperatures ranging between 31°C (87.8°F) and 23°C (73.4°F). \nIt's a hot day, and you can expect cloudy conditions and a  rainfall. \nThe average daily high temperature hovers around 85°F (29.4°C), while the low temperature stays at approximately 74°F (23.3°C). \nIf you are going to be outdoors pack light clothing and an umbrella! 🌦️🌡️")
        elif m == 7 and r== 4:
            print("Today's weather is partly sunny with an average high temperature around 82°F (28°C) and a low temperature of approximately 75°F (24°C). \nThe average humidity is around 89%, and the wind blows at 5 mph from the west direction. \nKeep in mind that there's a chance of thunderstorms accompanied, so it's a good idea to stay prepared! 🌦️⚡")
        elif m == 8 and r== 4:
            print("Today we will experience a very warm weather with average high temperatures around 83°F (28°C) and low temperatures of approximately 72°F (22°C). \nExpect daytime temperatures around 30°C, while nighttime temperatures can drop to 23°C . \nThis month typically offers some of the year's milder temperatures . 🌞🌧️")
        elif m == 9 and r== 4:
            print("Today we will experience partly sunny weather with an average high temperature around 88°F (31°C) and a low temperature of approximately 75°F (24°C).\nThe humidity is around 89%, and the wind blows at 5 mph from the west direction. \nExpect warm and comfortable evenings ! ☀️🌧️")
        elif m == 10 and r== 4:
            print("Today we will experience partly sunny weather with an average high temperature around 88°F (31°C) and a low temperature of approximately 75°F (24°C). \nThe humidity is around 89%, and the wind blows at 5 mph from the west direction . \nExpect warm days and comfortable evenings during this month! ☀️🌧️")
        elif m == 11 and r== 4:
            print("Today we will experience a delightful climate with an average high temperature around 33°C (92°F) and a low temperature of approximately 22°C (72°F) . \nThis month is characterized by partly cloudy skies and the possibility of a thunderstorm . \nExpect long daylight hours with around 7.3 hours of sunshine daily, making it one of the sunniest months in the year . 🌦️⚡")
        elif m == 12 and r== 4:
            print("Today we will experience relatively cooler weather, akin to winter. \nDaytime temperatures settle within a range of 31.7°C (89.1°F) to 33.8°C (92.8°F)\nNight temperatures drop to their annual nadir at 15.5°C (59.9°F) . \nIf you'd like more detailed daily forecasts, you can check here.")



        elif m == 1 and r== 5:
            print("")
        elif m == 2 and r==5:
            print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
        elif m ==3 and r==5:
            print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
        elif m ==4 and r==5:
            print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
        elif m ==5 and r==5:
            print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
        elif m ==6 and r==5:
            print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
        elif m == 7 and r== 5:
            print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
        elif m == 8 and r== 5:
            print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
        elif m == 9 and r== 5:
            print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
        elif m == 10 and r== 5:
            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
        elif m == 11 and r== 5:
            print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
        elif m == 12 and r== 5:
            print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
        


        elif m == 1 and r== 6:
            print("In January, the south-west region typically receives about 141.58 millimeters (5.57 inches) of precipitation \nwith 224.18 rainy days (approximately 61.42% of the time). \nIt's a relatively wet month, so be prepared for rain. ☔🌧️")
        elif m == 2 and r==6:
            print("In February, the south-west region typically receives about 141.58 millimeters (5.57 inches) of precipitation \nwith 224.18 rainy days (approximately 61.42% of the time). \nIt's a relatively wet month, so be prepared for rain. ☔🌧️")
        elif m == 3 and r==6:
            print("In March, the south-west region typically receives about 141.58 millimeters (5.57 inches) of precipitation \nwith 224.18 rainy days (approximately 61.42% of the time). \nIt's a relatively wet month, so be prepared for rain. ☔🌧️")
        elif m ==4 and r==6:
            print("In April, the south-west region typically receives about 4.75 inches (120.7 mm) of rainfall during the month.\n The percentage of rainfall is 59% this month \nIt's a relatively wet period, so be prepared for rain. ☔🌧️")
        elif m ==5 and r==6:
            print("In May, the south-west region typically receives approximately 4.39 inches (111.5 mm) of precipitation \nwith 40% of the days experiencing rainy weather. \nIt's advisable to carry an umbrella or raincoat during your visit! ☔🌧️")
        elif m ==6 and r==6:
            print("In June, the south-west region experiences heavy rainfall, \nwith an average of approximately 313 mm for the month. \nThis marks the year's heaviest rainfall, and intense rain showers are frequent. \nBe prepared with appropriate rain gear to stay dry! ☔🌧️")
        elif m == 7 and r== 6:
            print("In July, the south-west region typically receives around 14.4 inches (366 mm) of precipitation, \nwith 70% of the days experiencing rainy weather. \nIt's a wet month, \nso be prepared with an umbrella or raincoat if you're in Lagos! ☔🌧️")
        elif m == 8 and r== 6:
            print("In August, the south-west region typically experiences high rainfall, averaging around 146 mm for the month. \nThis translates to approximately 12 rainy days. \nWhile the daytime temperatures hover around 28°C (82°F), \nevenings cool down to a more temperate 24°C (75°F). \nThe area enjoys about 110 hours of sunshine, \nmaking it neither too gloomy nor overly bright. \nIf you're planning a visit, consider airy clothing and bring a raincoat just in case! ☔🌞")
        elif m == 9 and r== 6:
            print("In September, the south-west region typically experiences heavy rainfall, \naveraging around 201 mm for the month. \nApproximately 13 days of rainfall are expected, with daytime temperatures hovering around 28°C (83°F) and nights cooling down to about 24°C (75°F). \nThe area enjoys a balanced 116 hours of sunlight, ensuring it's neither too overcast nor too sunny. \nIf you're planning a visit, consider airy clothing and bring a raincoat just in case! ☔🌞")
        elif m == 10 and r== 6:
            print("In October, the south-west region typically receives moderate rainfall, \naveraging around 66 mm for the month . \nRain is expected on roughly 12 days. \nThe city usually sees around 170 hours of sunlight, \nindicating a moderately sunny period. \nWhile daytime temperatures settle at around 29°C (85°F), \nevenings drop to approximately 25°C (77°F)\nIt's essential to be prepared for such heat. \nWearing light, breathable fabrics and protecting yourself from the sun's intensity with hats or shades can make a difference.☔🌞")
        elif m == 11 and r== 6:
            print("In November, the south-west region typically experiences moderate rainfall, \naveraging around 85 mm for the month. \nTypically, around 5 days of rainfall are expected. \nThe area enjoys a balanced 188 hours of sunlight, \nensuring it's neither too overcast nor too sunny. \nIf you're inclined towards comfortable temperatures and drier conditions, \n Dress in lightweight and breathable outfits to handle the warmth, \nand don't forget your raincoat for occasional showers! ☔🌞")
        elif m == 12 and r== 6:
            print("In December, the south-west region generally experiences very high temperatures during the day, \nsettling around 31°C (87°F). \nHowever, evenings bring relief as temperatures drop to approximately 26°C (79°F). \nIt's advisable to wear appropriate clothing to handle the warmth.\n\nAs for rainfall, the south-west region typically receives moderate precipitation, \naveraging around 40 mm (1.57 inches) for the month. Rain is expected on roughly 2 days. \nWith approximately 193 hours of sunshine, most days are sunny, giving the area a pleasant and vibrant feel. \nDecember is a great time to visit if you prefer dry days with pleasant temperatures. 🌞☔")
    
    case _:
        print("ok")


print("\nNB:The information given may not be perfectly accurate!\n")
#yesno=None
#loop=None
#while yesno not in loop:
    #yesno=("yes","no")
toLoop = 0

while toLoop == 0:
    loop = input("\nDo you want to check a weather for somewhere else: (yes?No):\n-> ").lower()
    if loop.lower() == "yes":
        r=int(input("\nEnter your geopolitical zones:\n North Central - 1\n North West - 2\n North East - 3\n South East - 4\n South-South - 5\n South West - 6\n -> "))
        match r :
            case 1:
                State=input("\nEnter your state: \n Benue State - A\n Kogi state - B\n Kwara state - C\n Nasarawa state - D\n Niger state - E\n Plateau state - F\n -> ").lower()  
                if State == "a":
                    if m == 1 :
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4 :
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5:
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8 :
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11 :
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12:
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                            
                if State == "b":

                    if m == 1 :
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4 :
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7 :
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8 :
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                
                if State == "c":

                    if m == 1 :
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2:
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4 :
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7 :
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8 :
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11 :
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                                 
                if State == "d":

                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7 :
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8 :
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10:
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11 :
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
  
                if State == "e":

                    if m == 1 :
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2:
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4 :
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7 :
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8 :
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11 :
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                                
                if State == "f":
                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                                        
            case 2:
                State=input("\nEnter your state:\n Jigawa -A\n Kaduna -B\n Kano -C\n Katsina -D\n Kebbi -E\n Sokoto -F \n Zamfara -G\n -> ").lower()
                if State == "a":
                    if m == 1 :
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4 :
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7 :
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8 :
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11 :
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12:
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")    
                   
                if State == "b":

                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                     
                if State == "c":

                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                     
 
                if State == "d":

                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                     
                
               
                if State == "e":

                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                     
                
                                       
                if State == "f":
                
                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                     
                if State == "g":
                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                            
            case 3:
                State= input("\n Enter your state :\n Adamawa - A \n Bauchi - B \n Borno - C \n Gombe - D \n Taraba - E \n Yobe - F \n -> ").lower()
                if State == "a":
                    if m == 1 :
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4 :
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8 :
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9:
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11 :
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                              
                if State == "b":

                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                                    
                if State == "c":

                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                     
                if State == "d":

                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                     
                if State == "e":

                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                     
                if State == "f":
                
                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                     
            case 4:
                state=("Enter your state:\n Abia -A\n Anambra -B\n Ebonyi -C \n Enugu -D\n Imo -E \n -> ")
                if State=="a":
                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                                
                if State == "b":
                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                                     
                if State == "c":
                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                               
                if State == "d":
                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                                   
                if State == "e":

                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                                     
                if State == "f":
                
                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                                
            case 5:
                State=input("Enter your state :\n Akwa Ibom State -A \n Bayelsa State -B \n Cross River State -C \n Delta State -D\n Edo State -E \n ->").lower()
                list=("a","b","c","d","e")

                while state not in list :
                    if State == "a":
                        if m == 1:
                            print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                        elif m == 2 :
                            print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                        elif m ==3 :
                            print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                        elif m ==4:
                            print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                        elif m ==5 :
                            print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                        elif m ==6 :
                            print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                        elif m == 7:
                            print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                        elif m == 8:
                            print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                        elif m == 9 :
                            print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                        elif m == 10 :
                            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                        elif m == 11:
                            print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                        elif m == 12 :
                            print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                                        
                    if State == "b":

                        if m == 1:
                            print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                        elif m == 2 :
                            print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                        elif m ==3 :
                            print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                        elif m ==4:
                            print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                        elif m ==5 :
                            print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                        elif m ==6 :
                            print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                        elif m == 7:
                            print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                        elif m == 8:
                            print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                        elif m == 9 :
                            print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                        elif m == 10 :
                            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                        elif m == 11:
                            print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                        elif m == 12 :
                            print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                                
                    if State == "c":

                        if m == 1:
                            print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                        elif m == 2 :
                            print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                        elif m ==3 :
                            print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                        elif m ==4:
                            print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                        elif m ==5 :
                            print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                        elif m ==6 :
                            print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                        elif m == 7:
                            print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                        elif m == 8:
                            print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                        elif m == 9 :
                            print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                        elif m == 10 :
                            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                        elif m == 11:
                            print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                        elif m == 12 :
                            print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                                                
                    if State == "d":

                        if m == 1:
                            print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                        elif m == 2 :
                            print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                        elif m ==3 :
                            print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                        elif m ==4:
                            print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                        elif m ==5 :
                            print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                        elif m ==6 :
                            print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                        elif m == 7:
                            print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                        elif m == 8:
                            print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                        elif m == 9 :
                            print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                        elif m == 10 :
                            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                        elif m == 11:
                            print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                        elif m == 12 :
                            print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                        
                    if State == "e":
                        if m == 1:
                            print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                        elif m == 2 :
                            print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                        elif m ==3 :
                            print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                        elif m ==4:
                            print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                        elif m ==5 :
                            print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                        elif m ==6 :
                            print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                        elif m == 7:
                            print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                        elif m == 8:
                            print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                        elif m == 9 :
                            print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                        elif m == 10 :
                            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                        elif m == 11:
                            print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                        elif m == 12 :
                            print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                                
            case 6:
                State=input("Enter your state :\n Lagos -A \n Ogun -B \n Osun -C \n Ondo -D \n Ekiti -E \n -> ").lower()
                if State == "a":
                        if m == 1:
                            print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                        elif m == 2 :
                            print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                        elif m ==3 :
                            print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                        elif m ==4:
                            print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                        elif m ==5 :
                            print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                        elif m ==6 :
                            print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                        elif m == 7:
                            print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                        elif m == 8:
                            print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                        elif m == 9 :
                            print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                        elif m == 10 :
                            print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                        elif m == 11:
                            print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                        elif m == 12 :
                            print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                                            
                if State == "b":

                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                                
                if State == "c":

                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                                                         
                if State == "d":

                    if m == 1:
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2 :
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4:
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7:
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8:
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11:
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12 :
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
                     
                if State == "e":

                    if m == 1 :
                        print("Daytime temperatures typically vary between 20°C (68°F) and 28°C (82.4°F). \nwhile nighttime temperatures can drop to as low as 15°C (59°F).\nThe atmosphere is going to be quite dry, with low humidity, making any breeze feel cooling. \nHowever, the UV index is going to high today, so protection against skin and eye damage is recommended. \nTry to limit exposure between 10 am and 4 pm. 🌞🔥 ")
                    elif m == 2:
                        print("The average temperature today is 30°C or 86°F ,therefore its a sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated.")
                    elif m ==3 :
                        print("March tends to be the warmest month so, the average temperature today is 32°C or 90°F ,therefore its going to be a very sunny day. \nEnsure you wear breathable materials like cotton, linen, and jersey. \nLight-colored fabrics help reflect heat and keep you cool, and stay hydrated. ")
                    elif m ==4 :
                        print("The average temperature today is 28°C or 82°F ,therefore it is most likely a sunny day although there is low expection of raifall too. \nEnsure you wear breathable materials like cotton, linen, and jersey. Light-colored fabrics help reflect heat and keep you cool. ")
                    elif m ==5 :
                        print("Minimum Temperature : Around 23.8°C (75°F).\n Maximum Temperature: Up to 34.1°C (93°F)\nDaily Average: Approximately 29.0°C (84°F)\nRainFall: it is most likely goin to rain today \nKeep cool and stay hydrated during this warm period! 🌞")
                    elif m ==6 :
                        print("The average temperature today is 27°C or 81°F \nExpect thunderstorms, uncommon tornadoes, and hot weather during this time.\nKeep in mind the possibility of heat waves, with temperatures often exceeding 32°C (90°F). ")
                    elif m == 7 :
                        print("The daytime temperature ranging from 28°C to 33°C (82°F to 91°F). \nNighttime temperatures cool down to approximately 20°C to 23°C (68°F to 73°F)1. \nExpect occasional thunderstorms and some rain during this month. \nHowever, be prepared for heat waves, as the average temperature can exceed 31°C (88°F)2. \nIf you're traveling, consider staying hydrated and taking precautions, especially if you have heart conditions. 🌞🌧️🌩️ ")
                    elif m == 8 :
                        print("The average daytime temperature ranges from 21.7°C (71°F) to 29.2°C (85°F), resulting in an average of 25.5°C (78°F)1. \nExpect a little rainfall, which will provide some relief from the heat. \nNighttime temperatures fall between 20°C (68°F) and 23°C (73.4°F)2. 🌞🌧️")
                    elif m == 9 :
                        print("The average daytime temperature reaches around 30.3°C (87°F), while nighttime temperatures fall to approximately 21.9°C (71°F). \nExpect occasional thunderstorms, some rain, and sultry conditions. \nHeat waves are possible, with average temperatures exceeding 30°C (87°F). \nRemember to stay hydrated and take precautions during this time. 🌞🌩️🔥")
                    elif m == 10 :
                        print(" The average daytime temperatures fall between 27°C (80.6°F) and 31°C (87.8°F). \nwhile nighttime temperatures range from 21°C (69.8°F) to 24°C (75.2°F).  \nhumidity levels remain relatively high. \nIf you're planning a trip, be prepared for sultry conditions and consider staying hydrated! 🌞🌧️")
                    elif m == 11 :
                        print(" The average maximum daytime temperatures range from 30°C (86°F) to 37°C (98.6°F) . \nNighttime temperatures generally drop to a range of 21°C (69.8°F) to 26°C (78.8°F) . \nWhile there can be variations, it's advisable to prepare for potential heat by wearing appropriate clothing. \nPrecipitation levels vary across different areas, with almost no rainfall in Kano ")             
                    elif m == 12:
                        print("Daytime temperatures can reach 33°C (91.4°F) to 38°C (100.4°F). \nnighttime temperatures fall to between 16°C (60.8°F) and 20°C (68°F)12.\nExpect the peak of the harmattan , characterized by dry, dusty winds . \nSo ensure to stay hydrated. 🌞🔥")
  
        print("NB:Please note that the weather may not be accurate always")    
                
  
    elif loop == "no":
        print("Have a great day!\n")
        toLoop += 1
        
    else:
        print("Invalid input! Please type yes or no.")
    









