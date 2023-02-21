from fastapi import FastAPI
import joblib
import surprise

app = FastAPI()

@app.get('/')
def index():
    return {'Sistema de recomendación':'Se necesita usuario y código del programa.'}

#Cargamos el modelo
modelo = joblib.load('sistema_recomendacion.joblib')

@app.get('/prediccion/us/{usuario}/prog/{show}')
def prediccion(usuario:int,show:str):
    score = modelo.predict(usuario,show)[3]
    if score>4:
        return 'El programa '+show+' es muy recomendado para el usuario '+str(usuario)
    elif score>3:
        return 'El programa '+show+' es recomendado para el usuario '+str(usuario)
    elif score>2:
        return 'El programa '+show+' tiene baja recomendación para el usuario '+str(usuario)
    else:
        return 'El programa '+show+' no es recomendadoo para el usuario '+str(usuario)