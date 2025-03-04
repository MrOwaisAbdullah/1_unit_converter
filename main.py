import streamlit as st
import requests
from modules.ai_integration import get_ai_conversions
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
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="ConvertIQ: Unit Converter", page_icon="📏")


# CSS Styling
st.markdown(
    """
    <style>

        :root {
        --primary-color-rgb: 145, 123, 193; /* RGB values of #917bc1 */
        --shadow-color: 0,0,0;
    }
    [data-theme="dark"] {
        --shadow-color: 255,255,255;
        --primary-color-rgb: 161, 138, 214; /* Lighter tint for dark mode */
    }

    [data-theme="light"] {
        --shadow-color: 0,0,0;
    }

    .stButton > button {
        background-color: #917bc1;
        width: 100%;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #FF4B4B;
    }

    .stButton > button,
    .stButton > button:hover,
    .stButton > button:active,
    .stButton > button:focus {
        color: #ffffff !important;
    }

    .result-container {
        margin-top: 20px;
        padding: 25px;
        background: rgba(var(--primary-color-rgb), 0.08); /* Semi-transparent primary color */
        border-radius: 12px;
        text-align: center;
        box-shadow: 
            0 4px 12px rgba(var(--shadow-color), 0.15),
            0 0 0 2px rgba(var(--primary-color-rgb), 0.15); /* Inner glow effect */
        color: var(--text-color);
        border: 3px solid rgba(var(--primary-color-rgb), 0.3); /* Thicker semi-transparent border */
        transition: all 0.3s ease;
    }

    .result {
        font-size: 1.2em;
        font-weight: 800;
        color: var(--primary-color);
        display: inline-block;
        padding: 4px 12px;
        border-radius: 8px;
        margin-left: 10px;
        background-color: rgba(var(--primary-color-rgb), 0.15);
        text-shadow: 0 2px 4px rgba(var(--shadow-color), 0.1);
    }

    /* AI explanation text */
    .result-container div[style*="color: #cccccc"] {
        color: var(--text-color) !important;
        opacity: 0.9;
        line-height: 1.6;
        padding: 12px;
        font-size: 0.95em;
        background: rgba(var(--primary-color-rgb), 0.05);
        border-radius: 6px;
        margin-top: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# Heading and description
st.markdown(
    "<h1 style='text-align: center;'>📏 ConvertIQ: Unit Converter</h1>",
    unsafe_allow_html=True
    )
st.markdown(
    "<p style='text-align: center;'>Convert any unit with ease, precision, and AI-powered insights—all in one smart, user-friendly tool</p>",
    unsafe_allow_html=True
    )

# Session state tracking for conversion type
if 'prev_conversion_type' not in st.session_state:
    st.session_state.prev_conversion_type = None

# Sidebar
with st.sidebar:
    st.header("Conversion Settings")
    new_conversion_type = st.selectbox(
        "Select Conversion Type:",
        ["Temperature", "Length", "Weight", "Volume", "Area", "Speed", "Time",
         "Pressure", "Energy", "Power", "Data", "Frequency", "Angle", "Currency"]
    )

    # My Details
    st.markdown("---")
    st.markdown("### Made with ❤️ by **Owais Abdullah**")
    st.markdown("**LinkedIn:** [@mrowaisabdullah](https://www.linkedin.com/in/mrowaisabdullah/)")

    # Clear results if conversion type changes
    if new_conversion_type != st.session_state.prev_conversion_type:
        st.session_state.standard_result = None
        st.session_state.ai_result = None
        st.session_state.prev_conversion_type = new_conversion_type
        
conversion_type = new_conversion_type

# Main content
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
    col1 , col2 = st.columns(2)
    with col1:
        unit_from_options = list(unit_mappings[conversion_type].keys())
        unit_from_display = st.selectbox("Select Your Unit From: ", unit_from_options)
        unit_from = unit_mappings[conversion_type][unit_from_display]
    with col2:
        unit_to_options = list(unit_mappings[conversion_type].keys())
        unit_to_display = st.selectbox("Select Your Unit To: ", unit_to_options, index=1)
        unit_to = unit_mappings[conversion_type][unit_to_display]

    standard_conv = st.button("Convert")

    ai_conv = st.button("Convert with AI 🔮")

    # Initialize session state for results
    if 'standard_result' not in st.session_state:
        st.session_state.standard_result = None
    if 'ai_result' not in st.session_state:
        st.session_state.ai_result = None

    # Handle standard conversion
    if standard_conv:
        with st.spinner(f"Converting {value} {unit_from_display} to {unit_to_display}..."):
            # Standard conversion logic
            if conversion_type == "Currency":
                exchange_api = os.getenv("EXCHANGE_RATE_API")
                api_url = f"{exchange_api}/{unit_from}"
                try:
                    response = requests.get(api_url, timeout=10)
                    response.raise_for_status()
                    data = response.json()
                    rate = data["rates"][unit_to]
                    result = value * rate
                    result = result.toFixed(2)
                except requests.exceptions.RequestException as e:
                    st.error(f"Error fetching currency data: {e}")
            else:
                # Conversion functions
                conversion_functions = {
                    "Length": convert_length,
                    "Temperature": convert_temperature,
                    "Weight": convert_weight,
                    "Volume": convert_volume,
                    "Area": convert_area,
                    "Speed": convert_speed,
                    "Time": convert_time,
                    "Pressure": convert_pressure,
                    "Energy": convert_energy,
                    "Power": convert_power,
                    "Data": convert_data,
                    "Frequency": convert_frequency,
                    "Angle": convert_angle
                }
                result = conversion_functions[conversion_type](value, unit_from, unit_to)

            st.session_state.standard_result = result

    # Handle AI conversion
    if ai_conv:
        with st.spinner("Generating AI-powered conversion..."):
            try:
                if conversion_type == "Currency":
                    exchange_api = os.getenv("EXCHANGE_RATE_API")
                    api_url = f"{exchange_api}/{unit_from}"
                    try:
                        response = requests.get(api_url, timeout=10)
                        response.raise_for_status()
                        data = response.json()
                        rate = data["rates"][unit_to]
                        ai_response = get_ai_conversions(conversion_type, unit_from, value, unit_to, realtime_rate=rate)
                        
                        # Parse response
                        if "|" in ai_response:
                            ai_value, explanation = ai_response.split("|", 1)
                            ai_result = float(ai_value.strip())
                        else:
                            ai_result = float(ai_response.split()[0])
                            explanation = " ".join(ai_response.split()[1:])
                        
                        st.session_state.ai_result = (ai_result, explanation)
                        
                    except (requests.exceptions.RequestException, KeyError, ValueError) as e:
                        st.error(f"Error in currency conversion: {e}")
                        ai_response = get_ai_conversions(conversion_type, unit_from, value, unit_to)
                        try:
                            if "|" in ai_response:
                                ai_value, explanation = ai_response.split("|", 1)
                                ai_result = float(ai_value.strip())
                            else:
                                ai_result = float(ai_response.split()[0])
                                explanation = " ".join(ai_response.split()[1:])
                            st.session_state.ai_result = (ai_result, explanation)
                        except (ValueError, IndexError) as parse_error:
                            st.error(f"Error parsing AI response: {str(parse_error)}")
                            st.session_state.ai_result = ("N/A", ai_response)

                else:  # Handle non-currency conversions
                    ai_response = get_ai_conversions(conversion_type, unit_from, value, unit_to)
                    try:
                        if "|" in ai_response:
                            ai_value, explanation = ai_response.split("|", 1)
                            ai_result = float(ai_value.strip())
                        else:
                            ai_result = float(ai_response.split()[0])
                            explanation = " ".join(ai_response.split()[1:])
                        st.session_state.ai_result = (ai_result, explanation)
                    except (ValueError, IndexError) as e:
                        st.error(f"Error parsing AI response: {str(e)}")
                        st.session_state.ai_result = ("N/A", ai_response)

            except (requests.exceptions.RequestException, ValueError, IndexError) as main_error:
                st.error(f"AI Conversion Failed: {str(main_error)}")
                st.session_state.ai_result = ("Error", "Could not generate conversion")

    # Showing both results if available
    if st.session_state.standard_result is not None:
        st.subheader("Standard Conversion Result:")
        st.markdown(f'''
            <div class="result-container">
                <strong>{value} {unit_from}</strong> &nbsp;is equal to 
                <span class="result">{st.session_state.standard_result} {unit_to}</span>
            </div>
        ''', unsafe_allow_html=True)

    if st.session_state.ai_result is not None:
        if st.session_state.standard_result is not None:
            st.markdown('<div class="result-separator"></div>', unsafe_allow_html=True)
        ai_result, ai_response = st.session_state.ai_result
        st.subheader("AI Conversion Result:")
        st.markdown(f'''
            <div class="result-container ">
                <div style="margin-bottom: 10px; border-bottom: 1px solid #444; padding-bottom: 10px;">
                    <strong>{value} {unit_from}</strong> → 
                    <span class="result">{ai_result} {unit_to}</span>
                </div>
                    <div style="font-size: 0.9em;">{ai_response}</div>
            </div>
        ''', unsafe_allow_html=True)

else:
    st.write("Please select a valid conversion type.")
