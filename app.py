import streamlit as st

# Funciones de conversión directamente definidas
def celsius_a_kelvin(gradCelsius):
    return gradCelsius + 273.15

def kelvin_a_celsius(gradKelvin):
    return gradKelvin - 273.15

def celsius_a_fahrenheit(gradCelsius):
    return (gradCelsius * 9.0 / 5.0) + 32.0

def fahrenheit_a_celsius(gradFahrenheit):
    return (gradFahrenheit - 32.0) * 5.0 / 9.0

def fahrenheit_a_kelvin(gradFahrenheit):
    gradCelsius = fahrenheit_a_celsius(gradFahrenheit)
    return celsius_a_kelvin(gradCelsius)

def kelvin_a_fahrenheit(gradKelvin):
    gradCelsius = kelvin_a_celsius(gradKelvin)
    return celsius_a_fahrenheit(gradCelsius)

# Interfaz de Streamlit
st.title("Conversor de Escalas Termométricas")

# Entrada de temperatura
temperatura_str = st.text_input("Introduce la temperatura:", value="0")

try:
    temperatura = float(temperatura_str)
except ValueError:
    st.error("Por favor, introduce un valor numérico válido.")
    temperatura = None

# Selección de escalas
escala_origen = st.selectbox("Selecciona la escala de origen:", ("Celsius", "Fahrenheit", "Kelvin"))
escala_destino = st.selectbox("Selecciona la escala de destino:", ("Celsius", "Fahrenheit", "Kelvin"))

# Conversión y resultados
if st.button("Convertir") and temperatura is not None:
    if escala_origen == "Celsius" and escala_destino == "Fahrenheit":
        resultado = celsius_a_fahrenheit(temperatura)
        st.write(f"{temperatura}° Celsius son {resultado}° Fahrenheit")
    elif escala_origen == "Celsius" and escala_destino == "Kelvin":
        resultado = celsius_a_kelvin(temperatura)
        st.write(f"{temperatura}° Celsius son {resultado} Kelvin")
    elif escala_origen == "Fahrenheit" and escala_destino == "Celsius":
        resultado = fahrenheit_a_celsius(temperatura)
        st.write(f"{temperatura}° Fahrenheit son {resultado}° Celsius")
    elif escala_origen == "Fahrenheit" and escala_destino == "Kelvin":
        resultado = fahrenheit_a_kelvin(temperatura)
        st.write(f"{temperatura}° Fahrenheit son {resultado} Kelvin")
    elif escala_origen == "Kelvin" and escala_destino == "Celsius":
        resultado = kelvin_a_celsius(temperatura)
        st.write(f"{temperatura} Kelvin son {resultado}° Celsius")
    elif escala_origen == "Kelvin" and escala_destino == "Fahrenheit":
        resultado = kelvin_a_fahrenheit(temperatura)
        st.write(f"{temperatura} Kelvin son {resultado}° Fahrenheit")
    else:
        st.write("Por favor selecciona diferentes escalas de origen y destino.")

       
