from flask import Flask, render_template, request
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import os
#app = Flask(__name__, template_folder='front')
app = Flask(__name__, template_folder=os.getcwd())
app.static_folder = 'static'



# Load the pre-trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the pre-trained TfidfVectorizer
with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input
    title = request.form['title']
    genre = request.form['genre']
    description = request.form['description']
    type = request.form['type']
    producer = request.form['producer']
    studio = request.form['studio']

    # Convert user input to dataframe
    user_input_df = pd.DataFrame({
        "Title": [title],
        "Genre": [genre],
        "synopsis": [description],
        "Type": [type],
        "Producer": [producer],
        "Studio": [studio]
    })

    # Vectorize user input
    user_input_vec = vectorizer.transform(user_input_df.apply(lambda x: " ".join(x), axis=1))

    # Predict rating
    rating = model.predict(user_input_vec)

    # Display the predicted rating
    return render_template('index.html', prediction=f"Predicted rating: {rating[0]:.2f}")

if __name__ == '__main__':
    app.run(debug=True)