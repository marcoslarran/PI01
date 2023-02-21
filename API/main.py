from fastapi import FastAPI
import pandas as pd
import numpy as np

app = FastAPI()

@app.get('/')
def index():
    return {'Aplicacion de películas':'4 funciones disponibles.'}

plataformas_API = pd.read_csv('https://drive.google.com/uc?id=1s0vrf_ZjUUy2zZD6-W7w0LymCoxGzEmO')

def maxDuracion(dataframe,anio,tipo_dur):
    if tipo_dur.find('eas')!=-1:
        tipo_dur = 'seasons'
    else:
        tipo_dur = 'min'
    cond1 = dataframe['release_year']==anio
    cond2 = dataframe['duration.type']==tipo_dur
    df_filtrado = dataframe[cond1 & cond2]
    #return {'Año':anio,'Tipo de duracion':tipo_dur}
    return {'Película de mayor duracion':
            df_filtrado[df_filtrado['duration.int']==df_filtrado['duration.int'].max()]['title'].values[0]}

@app.get('/get_max_duration/year/{year}/platform/{platform}/dur/{duration_type}')
def get_max_duration(year:int, platform:str, duration_type:str):
    platform = platform.casefold()
    if platform.find('net') != -1:
        return maxDuracion(plataformas_API[plataformas_API['show_id'].str.contains('ns')],year,duration_type)
    elif platform.find('hul') != -1:
        return maxDuracion(plataformas_API[plataformas_API['show_id'].str.contains('hs')],year,duration_type)
    elif platform.find('disn') != -1:
        return maxDuracion(plataformas_API[plataformas_API['show_id'].str.contains('ds')],year,duration_type)
    elif platform.find('amaz') != -1:
        return maxDuracion(plataformas_API[plataformas_API['show_id'].str.contains('as')],year,duration_type)

def puntajes(dataframe,anio,puntaje):
    cond1 = dataframe['release_year']==anio
    cond2 = dataframe['rating']>=puntaje
    df_filtrado = dataframe[cond1 & cond2]
    return {'Cantidad de películas con puntaje promedio mayor o igual a '+str(puntaje):df_filtrado.shape[0]}

@app.get('/get_score_count/platform/{platform}/score/{scored}/year/{year}')
def get_score_count(platform:str, scored:float, year:int):
    platform = platform.casefold()
    if platform.find('net') != -1:
        return puntajes(plataformas_API[plataformas_API['show_id'].str.contains('ns')],year,scored)
    elif platform.find('hul') != -1:
        return puntajes(plataformas_API[plataformas_API['show_id'].str.contains('hs')],year,scored)
    elif platform.find('disn') != -1:
        return puntajes(plataformas_API[plataformas_API['show_id'].str.contains('ds')],year,scored)
    elif platform.find('amaz') != -1:
        return puntajes(plataformas_API[plataformas_API['show_id'].str.contains('as')],year,scored)

@app.get('/get_count_platform/{platform}')
def get_count_platform(platform:str):
    platform = platform.casefold()
    if platform.find('net') != -1:
        return {'Cantidad de películas':plataformas_API[plataformas_API['show_id'].str.contains('ns')].shape[0]}
    elif platform.find('hul') != -1:
        return {'Cantidad de películas':plataformas_API[plataformas_API['show_id'].str.contains('hs')].shape[0]}
    elif platform.find('disn') != -1:
        return {'Cantidad de películas':plataformas_API[plataformas_API['show_id'].str.contains('ds')].shape[0]}
    elif platform.find('amaz') != -1:
        return {'Cantidad de películas':plataformas_API[plataformas_API['show_id'].str.contains('as')].shape[0]}

def actorMayorPresencia(dataframe,anio):
    actores = []
    cast = dataframe[dataframe['release_year']==anio]['cast']
    for i in cast:
        try:
            if i.find(',')!=-1:
                for act in i.split(','):
                    actores.append(act.strip().title())
            else:
                actores.append(i.strip().title())
        except:
            pass
    return {'Actor con mayor presencia ':max(set(actores),key=actores.count)}

@app.get('/get_actor/platform/{platform}/year/{year}')
def get_actor(platform:str, year:int):
    platform = platform.casefold()
    if platform.find('net') != -1:
        return actorMayorPresencia(plataformas_API[plataformas_API['show_id'].str.contains('ns')],year)
    elif platform.find('hul') != -1:
        return actorMayorPresencia(plataformas_API[plataformas_API['show_id'].str.contains('hs')],year)
    elif platform.find('disn') != -1:
        return actorMayorPresencia(plataformas_API[plataformas_API['show_id'].str.contains('ds')],year)
    elif platform.find('amaz') != -1:
        return actorMayorPresencia(plataformas_API[plataformas_API['show_id'].str.contains('as')],year)