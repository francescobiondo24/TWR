import streamlit as st
import pandas as pd


st.title("Torre di controllo da remoto")

# definisco alcune compagnie aeree operanti a Linate
airlines= ["aer lingus", "aerflot", "air berlin", "air canada", "air france",
           "alitalia", "etihad", "iberia", "klm"]

st.markdown("#### in assenza di object detecting selezionare la compagnia aerea")
select_airline= st.selectbox('AIRLINE',airlines)
select_day= st.sidebar.selectbox('GIORNO', ('Monday','Tuesday','Wednesday','Thursday',
                                             'Friday'))

departures= pd.read_csv('orari partenze.csv', sep =';')
st.write(departures)

@st.cache
def destination_fly(departures):
    for i in range(len(departures['AIRLINE'])):
        if departures.loc[i]['AIRLINE'] == select_airline and departures.loc[i]['DAY'] == select_day:
            destination_airport= departures.loc[i]['DESTINATION']
            n_fly= departures.loc[i]['N_FLY']
            hour= departures.loc[i]['HOUR']


    return destination_airport, n_fly, hour

destination= destination_fly(departures)
st.write("FLY TABEL", destination)

st.markdown("## PIANIFICAZIONE VOLO")
st.markdown("### Condizioni meteo e servizi di aeroporto")
# condizioni meteo
meteo= st.sidebar.selectbox('METEOROLOGICAL CONDITIONS', ('Sun', 'Rain', 'Snow', 'Hail', 'Drizzle', 'Fog', 'Cloud',
                                                    'Wind', 'Strong wind', 'Storm'))

anti_icing= st.sidebar.selectbox('DE/ANTI-ICING and DE SNOWING', ('Yes', 'No'))
operazioni= pd.read_csv("servizi di aeroporto.csv", sep=';')
st.write(operazioni)

def icing(operazioni):
    if operazioni.loc[0]['AVVIENE1'] == anti_icing:
        procedimento1= operazioni.loc[0]['STEPS']
    if operazioni.loc[0]['AVVIENE2'] == anti_icing:
        procedimento1= operazioni.loc[0]['OPPOSTO']

    return procedimento1

op= icing(operazioni)
st.write(op)

def snow(operazioni):
    if operazioni.loc[0]['AVVIENE1'] == anti_icing and meteo == 'Snow':
        procedimento= operazioni.loc[0]['AZIONI']
    else:
        pass

    return procedimento

op1= snow(operazioni)
st.write(op1)







st.markdown("### AEROMOBILE AL SUOLO")
