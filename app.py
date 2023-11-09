from flask import Flask, render_template, request
import requests
app = Flask(__name__)
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"
headers = {
  'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
  'x-rapidapi-key': "78842da2a9msh458c79623a82694p14831bjsn4ef8ef042c12",
  }
random_joke = "food/jokes/random"
random_trivia = "food/trivia/random"
find = "recipes/findByIngredients"
randomFind = "recipes/random"


@app.route('/')
def search_page():
  joke_response = str(requests.request("GET", url + random_joke, headers=headers).json()['text'])
  trivia_response = str(requests.request("GET", url + random_trivia, headers=headers).json()['text'])
  return render_template('search.html', joke=joke_response, trivia=trivia_response)
  

if __name__ == '__main__':
  app.run()