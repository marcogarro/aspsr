from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = 'change_this_secret'  # replace with a random secret in production

# Simple in-memory user store
USERS = {
    'admin': 'password'  # username: password
}


@app.route('/', methods=['GET', 'POST'])
def login():
    """Display login form and authenticate user."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in USERS and USERS[username] == password:
            session['user'] = username
            return redirect(url_for('weather'))
        return render_template('login.html', error='Credenziali non valide')
    return render_template('login.html')


def logged_in():
    return 'user' in session


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if not logged_in():
        return redirect(url_for('login'))

    weather_info = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather_info = get_weather(city)
    return render_template('weather.html', weather=weather_info)


def get_weather(city_name):
    """Fetch weather information for a city using the Open-Meteo API."""
    geo_url = (
        'https://geocoding-api.open-meteo.com/v1/search'
        f'?name={city_name}&count=1&language=it&format=json'
    )
    geo_resp = requests.get(geo_url, timeout=10)
    if geo_resp.status_code != 200:
        return {'error': 'Errore nella richiesta geocoding'}

    geo_data = geo_resp.json().get('results')
    if not geo_data:
        return {'error': 'Citta non trovata'}

    lat = geo_data[0]['latitude']
    lon = geo_data[0]['longitude']

    weather_url = (
        'https://api.open-meteo.com/v1/forecast'
        f'?latitude={lat}&longitude={lon}&current_weather=true'
    )
    weather_resp = requests.get(weather_url, timeout=10)
    if weather_resp.status_code != 200:
        return {'error': 'Errore nel recupero del meteo'}

    weather_data = weather_resp.json().get('current_weather', {})
    return {
        'city': geo_data[0]['name'],
        'temperature': weather_data.get('temperature'),
        'windspeed': weather_data.get('windspeed'),
        'weathercode': weather_data.get('weathercode'),
    }


if __name__ == '__main__':
    app.run(debug=True)
