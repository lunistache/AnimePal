# Utilisez l'image Python 3.8
FROM python:3.8-slim-buster

# Définissez le répertoire de travail dans l'image
WORKDIR /

# Copiez les fichiers de votre application dans l'image
COPY requirements.txt .
COPY app.py .
COPY model.pkl . 
COPY tfidf_vectorizer.pkl . 
COPY . .
COPY static static/

# Installez les dépendances de l'application
RUN pip install --no-cache-dir -r requirements.txt

# Définissez l'environnement de production
ENV FLASK_ENV=production

# Exposez le port de l'application
EXPOSE 5000

# Démarrez l'application Flask
CMD ["flask", "run", "--host=0.0.0.0"]

