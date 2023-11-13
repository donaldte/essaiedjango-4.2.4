from essaiedjango.celery import app
from .models import Cours 

@app.task 
def add(x, y):
    return x + y

@app.task
def create_cours_for_testing():

    for i in range(500):
        Cours.objects.create(nom=f"Francais {i}", description="Cours de francais")

    return 'done' 


@app.task
def my_periodic_task():
    return 'bonjour tous monde'    