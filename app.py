import streamlit as st

def bereken_tempo(wattage, gewicht):
    constante = 17.33
    tempo_min_per_km = (constante * gewicht) / wattage
    minuten = int(tempo_min_per_km)
    seconden = (tempo_min_per_km - minuten) * 60
    return f"{minuten} minuten en {seconden:.0f} seconden per kilometer"

st.title('Bereken je Tempo')
st.write('Vul je gewicht en wattage in om je hardlooptempo te berekenen.')

gewicht = st.number_input('Voer je gewicht in (in kg):', min_value=0.0, value=65.0, step=0.1)
wattage = st.number_input('Voer het wattage in:', min_value=0.0, value=236.0, step=0.1)

if st.button('Bereken Tempo'):
    tempo = bereken_tempo(wattage, gewicht)
    st.success(f"Het tempo is {tempo}.")
