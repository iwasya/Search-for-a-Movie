from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def get_movie_info(api_key, movie_title):
    base_url = "http://www.omdbapi.com/"
    params = {
        'apikey': api_key,
        't': movie_title
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    movie_info = None
    if request.method == 'POST':
        api_key = "4cb49ca4"  # Ganti dengan API key Anda
        movie_title = request.form['movie_title']
        movie_info = get_movie_info(api_key, movie_title)
    return render_template('index.html', movie_info=movie_info)

if __name__ == '__main__':
    app.run(debug=True)
