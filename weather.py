import requests

def get_weather_forecast():
    # Connecting to weather api
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Santiago,chile&units=metric&appid=dc2f73149dc51fa8419b1f0fa54ed035'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    # Parsing JSON
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    # Creating forecast string and recomendations for the day
    forecast = 'The forecast for today is '
    forecast += description + ' with high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min))

    recomendation = ', so you should use'

    if  5 < temp_min <= 20:
        recomendation += ' some regular clothes, good weather.'
    elif temp_min > 20:
        recomendation += ' only some light clothes.'
    elif temp_min > 30:
        recomendation += ' only a swimwear and some flip-flop sandals...'
    elif temp_min < 5:
        recomendation += ' a very good jacket, maybe a polar bear...'
    else:
        recomendation += ' something appropriate for this strange weather.'

    forecast = forecast + '\n' + recomendation

    return forecast
