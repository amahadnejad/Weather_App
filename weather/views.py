import requests
from django.shortcuts import render
from django.conf import settings


def get_weather(request):
    city = request.GET.get('city', 'New York')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHER_API_KEY}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data = {'error': 'City not found or API limit exceeded'}
    except requests.exceptions.RequestException as e:
        weather_data = {'error': f'Error fetching data: {str(e)}'}

    return render(request, 'weather/weather.html', {'weather_data': weather_data})
