# app.py
import streamlit as st
import requests  # For currency conversion
from modules.conversions import (
    convert_length,
    convert_temperature,
    convert_weight,
    convert_volume,
    convert_area,
    convert_speed,
    convert_time,
    convert_pressure,
    convert_energy,
    convert_power,
    convert_data,
    convert_frequency,
    convert_angle,
)

st.set_page_config(page_title="Unit Converter", page_icon="📏")


# Modern CSS Styling
st.markdown(
    """
    <style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 20px;
        color: #ffffff;
    }
    h1 {
        color: #917bc1;
        text-align: center;
        margin-bottom: 20px;
    }
    .stSelectbox, .stNumberInput, .stButton {
        width: 100%;
        margin-bottom: 15px;
    }
    .stButton > button {
        background-color: #917bc1;
        color: #ffffff;
        width: 100%;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #FF4B4B;
        color: #ffffff;
    }
    .stButton > button:active {
        background-color: #FF4B4B;
        color: #ffffff;
    }
    .stTextInput>div>div>input:focus-visible,
    .stNumberInput>div>div>input:focus-visible,
    select:focus-visible {
        outline: 2px solid #917bc1;
        outline-offset: 2px;
    }

    .stSpinner {
        text-align: center;
        margin-top: 20px;
    }
    .result-container {
        margin-top: 20px;
        padding: 15px;
        background-color: #282828;
        border-radius: 5px;
        text-align: center;
    }
    .result {
        font-size: 1.1em;
        font-weight: 600;
        color: #b45fab;
        display: inline-block;
        padding: 2px 6px;
        background-color: #4a4a4a;
        border-radius: 5px;
        margin-left: 5px;
    }
    .stTextInput>div>div>input {
        background-color: #282828;
        color: #ffffff;
        border: 1px solid #555;
    }
    .stNumberInput>div>div>input {
        background-color: #282828;
        color: #ffffff;
        border: 1px solid #555;
    }
    select {
        background-color: #282828;
        color: #ffffff;
        border: 1px solid #555;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Unit Converter")


conversion_type = st.selectbox("Select Conversion Type: ", ["Temperature", "Length", "Weight", "Volume", "Area", "Speed", "Time", "Pressure", "Energy", "Power", "Data", "Frequency", "Angle", "Currency"])

value = st.number_input("Enter Your Value: ", 1)

unit_mappings = {
    "Length": {"Centimeter": "cm", "meter": "m", "kilometer": "km", "inch": "in", "Feet": "ft", "Yard": "yd", "Mile": "mile"},
    "Temperature": {"Celsius": "°C", "Fahrenheit": "°F", "Kelvin": "K"},
    "Weight": {"Gram": "g", "Kilogram": "kg", "Pound": "lb", "Ounce": "oz"},
    "Volume": {"Milliliter": "ml", "Liter": "l", "Gallon": "gal", "Quart": "qt", "Pint": "pt", "Cup": "cup", "Fluid Ounce": "fl oz"},
    "Area": {"Square Meter": "sq m", "Square Kilometer": "sq km", "Square Foot": "sq ft", "Square Yard": "sq yd", "Square Mile": "sq mile", "Acre": "acre", "Hectare": "hectare"},
    "Speed": {"Meters per Second": "m/s", "Kilometers per Hour": "km/h", "Miles per Hour": "mile/h", "Knot": "knot"},
    "Time": {"Second": "sec", "Minute": "min", "Hour": "hr", "Day": "day", "Week": "week", "Month": "month", "Year": "year"},
    "Pressure": {"Pascal": "Pa", "Hectopascal": "hPa", "Kilopascal": "kPa", "Megapascal": "MPa", "Bar": "bar", "Torr": "torr", "Pound per Square Inch": "psi", "Kip per Square Inch": "ksi"},
    "Energy": {"Joule": "J", "Kilojoule": "kJ", "Calorie": "cal", "Kilocalorie": "kcal", "Watt-hour": "Wh", "Kilowatt-hour": "kWh", "Megawatt-hour": "MWh", "Gigawatt-hour": "GWh"},
    "Power": {"Watt": "W", "Kilowatt": "kW", "Megawatt": "MW", "Gigawatt": "GW", "Horsepower": "hp"},
    "Data": {"Bit": "bit", "Byte": "byte", "Kilobyte": "kb", "Megabyte": "Mb", "Gigabyte": "Gb", "Terabyte": "Tb", "Petabyte": "Pb", "Exabyte": "Eb"},
    "Frequency": {"Hertz": "Hz", "Kilohertz": "kHz", "Megahertz": "MHz", "Gigahertz": "GHz", "Terahertz": "THz"},
    "Angle": {"Degree": "deg", "Radian": "rad", "Gradian": "grad"},
    "Currency": {"USD": "USD", "EUR": "EUR", "GBP": "GBP", "INR": "INR", "AUD": "AUD", "CAD": "CAD", "SGD": "SGD", "JPY": "JPY", "CNY": "CNY", "AED": "AED", "SAR": "SAR", "QAR": "QAR", "MYR": "MYR", "NZD": "NZD", "ZAR": "ZAR", "PKR": "PKR"}
}

if conversion_type in unit_mappings:
    unit_from_options = list(unit_mappings[conversion_type].keys())
    unit_from_display = st.selectbox("Select Your Unit From: ", unit_from_options)
    unit_to_options = list(unit_mappings[conversion_type].keys())
    unit_to_display = st.selectbox("Select Your Unit To: ", unit_to_options)
    unit_from = unit_mappings[conversion_type][unit_from_display]
    unit_to = unit_mappings[conversion_type][unit_to_display]

    if st.button("Convert"):
        with st.spinner(f"Converting {value} {unit_from_display} to {unit_to_display}..."):
            if conversion_type == "Length":
                result = convert_length(value, unit_from, unit_to)
            elif conversion_type == "Temperature":
                result = convert_temperature(value, unit_from, unit_to)
            elif conversion_type == "Weight":
                result = convert_weight(value, unit_from, unit_to)
            elif conversion_type == "Volume":
                result = convert_volume(value, unit_from, unit_to)
            elif conversion_type == "Area":
                result = convert_area(value, unit_from, unit_to)
            elif conversion_type == "Speed":
                result = convert_speed(value, unit_from, unit_to)
            elif conversion_type == "Time":
                result = convert_time(value, unit_from, unit_to)
            elif conversion_type == "Pressure":
                result = convert_pressure(value, unit_from, unit_to)
            elif conversion_type == "Energy":
                result = convert_energy(value, unit_from, unit_to)
            elif conversion_type == "Power":
                result = convert_power(value, unit_from, unit_to)
            elif conversion_type == "Data":
                result = convert_data(value, unit_from, unit_to)
            elif conversion_type == "Frequency":
                result = convert_frequency(value, unit_from, unit_to)
            elif conversion_type == "Angle":
                result = convert_angle(value, unit_from, unit_to)
            elif conversion_type == "Currency":
                # Currency conversion using API
                api_url = f"https://api.exchangerate-api.com/v4/latest/{unit_from}"
                try:
                    response = requests.get(api_url, timeout=10)
                    response.raise_for_status()
                    data = response.json()
                    rate = data["rates"][unit_to]
                    result = value * rate
                except requests.exceptions.RequestException as e:
                    st.error(f"Error fetching currency data: {e}")
                    result = None

            else:
                result = None

            if result is not None:
                st.subheader("Result:")
                st.markdown(f'<div class="result-container"> <strong>{value} {unit_from}</strong> is Equal to <span class="result">{result} {unit_to}</span></div>', unsafe_allow_html=True)
            else:
                st.write("Conversion not supported or invalid units.")

else:
    st.write("Please select a valid conversion type.")