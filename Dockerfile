# Étape 1 : image de base
FROM python:3.12-slim

# Étape 2 : définir le dossier de travail
WORKDIR /app

# Étape 3 : copier les fichiers
COPY app/ app/
COPY app/requirements.txt .

# Étape 4 : installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : exposer le port et démarrer l’app
EXPOSE 5000
CMD ["python", "app/app.py"]
