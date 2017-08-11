'''
Python 3 program to send a SMS with the current weather details from the location specified from the user.
'''
import pyowm
from twilio.rest import Client

# Setup Twilio to send me SMS regarding tomorrow's weather in San Jose, CA
accountSID = 'Your SID goes here'
authToken = 'Your authentication token goes here'
twilioCli = Client(accountSID, authToken)
my_number = '+1 Your phone number goes here'
twilio_number = '+1 Your twilio phone number goes here'

# API key for OWM
owm = pyowm.OWM('Your API key goes here')


place = input("Please enter the location to get weather details (Ex. san jose, ca): \n")
forecast = owm.daily_forecast(place)
tomorrow = pyowm.timeutils.tomorrow()
sunny = forecast.will_be_sunny_at(tomorrow)

if sunny:
    print("It will be sunny tomorrow!")
else:
    print("No sunshine tomorrow!")

# Search for current weather at the location you've specified
observation = owm.weather_at_place(place)
w = observation.get_weather()
#print(w)

# Weather details
#print(w.get_wind()['speed']) # Wind speed

# Print the temp
temperature = w.get_temperature('fahrenheit')['temp']
print(w.get_detailed_status())
#print(w.get_humidity())


current_weather = 'The current temparature is {} degrees fahrenheit in {}'.format(temperature, place)
current_weather = str(current_weather)
print(current_weather)
message = twilioCli.messages.create(body=current_weather, from_=twilio_number, to=my_number)



