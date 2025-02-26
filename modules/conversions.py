def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "cm": {"m": 0.01, "km": 0.00001, "in": 0.393701, "ft": 0.0328084, "yd": 0.0109361, "mile": 0.00000621371},
        "m": {"cm": 100, "km": 0.001, "in": 39.3701, "ft": 3.28084, "yd": 1.09361, "mile": 0.000621371},
        "km": {"cm": 100000, "m": 1000, "in": 39370.1, "ft": 3280.84, "yd": 1093.61, "mile": 0.621371},
        "in": {"cm": 2.54, "m": 0.0254, "km": 0.0000254, "ft": 0.0833333, "yd": 0.0277778, "mile": 0.0000157828},
        "ft": {"cm": 30.48, "m": 0.3048, "km": 0.0003048, "in": 12, "yd": 0.333333, "mile": 0.000189394},
        "yd": {"cm": 91.44, "m": 0.9144, "km": 0.0009144, "in": 36, "ft": 3, "mile": 0.000568182},
        "mile": {"cm": 160934, "m": 1609.34, "km": 1.60934, "in": 63360, "ft": 5280, "yd": 1760},
    }
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        return value * conversion_factors[from_unit][to_unit]
    else:
        return None

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "°C":
        if to_unit == "°F":
            return (value * 9/5) + 32
        elif to_unit == "K":
            return value + 273.15
    elif from_unit == "°F":
        if to_unit == "°C":
            return (value - 32) * 5/9
        elif to_unit == "K":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "K":
        if to_unit == "°C":
            return value - 273.15
        elif to_unit == "°F":
            return (value - 273.15) * 9/5 + 32
    return None

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "g": {"kg": 0.001, "lb": 0.00220462, "oz": 0.035274},
        "kg": {"g": 1000, "lb": 2.20462, "oz": 35.274},
        "lb": {"g": 453.592, "kg": 0.453592, "oz": 16},
        "oz": {"g": 28.3495, "kg": 0.0283495, "lb": 0.0625},
    }
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        return value * conversion_factors[from_unit][to_unit]
    else:
        return None

def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        "ml": {"l": 0.001, "gal": 0.000264172, "qt": 0.00105669, "pt": 0.00211338, "cup": 0.00422675, "fl oz": 0.033814},
        "l": {"ml": 1000, "gal": 0.264172, "qt": 1.05669, "pt": 2.11338, "cup": 4.22675, "fl oz": 33.814},
        "gal": {"ml": 3785.41, "l": 3.78541, "qt": 4, "pt": 8, "cup": 16, "fl oz": 128},
        "qt": {"ml": 946.353, "l": 0.946353, "gal": 0.25, "pt": 2, "cup": 4, "fl oz": 32},
        "pt": {"ml": 473.176, "l": 0.473176, "gal": 0.125, "qt": 0.5, "cup": 2, "fl oz": 16},
        "cup": {"ml": 236.588, "l": 0.236588, "gal": 0.0625, "qt": 0.25, "pt": 0.5, "fl oz": 8},
        "fl oz": {"ml": 29.5735, "l": 0.0295735, "gal": 0.0078125, "qt": 0.03125, "pt": 0.0625, "cup": 0.125},
    }
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        return value * conversion_factors[from_unit][to_unit]
    else:
        return None

def convert_area(value, from_unit, to_unit):
    conversion_factors = {
        "sq m": {"sq km": 0.000001, "sq ft": 10.7639, "sq yd": 1.19599, "sq mile": 3.86102e-7, "acre": 0.000247105, "hectare": 0.0001},
        "sq km": {"sq m": 1000000, "sq ft": 10763910.42, "sq yd": 1195990.05, "sq mile": 0.386102, "acre": 247.105, "hectare": 100},
        "sq ft": {"sq m": 0.092903, "sq km": 9.2903e-8, "sq yd": 0.111111, "sq mile": 3.587e-8, "acre": 2.2957e-5, "hectare": 9.2903e-6},
        "sq yd": {"sq m": 0.836127, "sq km": 8.3613e-7, "sq ft": 9, "sq mile": 3.2283e-7, "acre": 0.000206612, "hectare": 8.3613e-5},
        "sq mile": {"sq m": 2589988.11, "sq km": 2.58999, "sq ft": 27878399.5, "sq yd": 3097600, "acre": 640, "hectare": 258.999},
        "acre": {"sq m": 4046.86, "sq km": 0.00404686, "sq ft": 43560, "sq yd": 4840, "sq mile": 0.0015625, "hectare": 0.404686},
        "hectare": {"sq m": 10000, "sq km": 0.01, "sq ft": 107639.10, "sq yd": 11959.9, "sq mile": 0.00386102, "acre": 2.47105},
    }
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        return value * conversion_factors[from_unit][to_unit]
    else:
        return None

def convert_speed(value, from_unit, to_unit):
    conversion_factors = {
        "m/s": {"km/h": 3.6, "mile/h": 2.23694, "knot": 1.94384},
        "km/h": {"m/s": 0.277778, "mile/h": 0.621371, "knot": 0.539957},
        "mile/h": {"m/s": 0.44704, "km/h": 1.60934, "knot": 0.868976},
        "knot": {"m/s": 0.514444, "km/h": 1.852, "mile/h": 1.15078},
    }
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        return value * conversion_factors[from_unit][to_unit]
    else:
        return None

def convert_time(value, from_unit, to_unit):
    conversion_factors = {
        "sec": {"min": 1/60, "hr": 1/3600, "day": 1/86400, "week": 1/604800, "month": 1/2628000, "year": 1/31536000},
        "min": {"sec": 60, "hr": 1/60, "day": 1/1440, "week": 1/10080, "month": 1/43800, "year": 1/525600},
        "hr": {"sec": 3600, "min": 60, "day": 1/24, "week": 1/168, "month": 1/730, "year": 1/8760},
        "day": {"sec": 86400, "min": 1440, "hr": 24, "week": 1/7, "month": 1/30.4167, "year": 1/365},
        "week": {"sec": 604800, "min": 10080, "hr": 168, "day": 7, "month": 1/4.34524, "year": 1/52.1429},
        "month": {"sec": 2628000, "min": 43800, "hr": 730, "day": 30.4167, "week": 4.34524, "year": 1/12},
        "year": {"sec": 31536000, "min": 525600, "hr": 8760, "day": 365, "week": 52.1429, "month": 12},
    }
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        return value * conversion_factors[from_unit][to_unit]
    else:
        return None

def convert_pressure(value, from_unit, to_unit):
    conversion_factors = {
        "Pa": {"hPa": 0.01, "kPa": 0.001, "MPa": 1e-6, "bar": 1e-5, "torr": 0.00750062, "psi": 0.000145038, "ksi": 1.45038e-7},
        "hPa": {"Pa": 100, "kPa": 0.1, "MPa": 1e-5, "bar": 0.001, "torr": 0.750062, "psi": 0.0145038, "ksi": 1.45038e-6},
        "kPa": {"Pa": 1000, "hPa": 10, "MPa": 0.001, "bar": 0.01, "torr": 7.50062, "psi": 0.145038, "ksi": 1.45038e-5},
        "MPa": {"Pa": 1000000, "hPa": 10000, "kPa": 1000, "bar": 10, "torr": 7500.62, "psi": 145.038, "ksi": 0.000145038},
        "bar": {"Pa": 100000, "hPa": 1000, "kPa": 100, "MPa": 0.1, "torr": 750.062, "psi": 14.5038, "ksi": 0.000145038},
        "torr": {"Pa": 133.322, "hPa": 1.33322, "kPa": 0.133322, "MPa": 1.33322e-4, "bar": 0.00133322, "psi": 0.0193368, "ksi": 1.93368e-6},
        "psi": {"Pa": 6894.76, "hPa": 68.9476, "kPa": 6.89476, "MPa": 0.00689476, "bar": 0.0689476, "torr": 51.7149, "ksi": 0.001},
        "ksi": {"Pa": 6894757, "hPa": 68947.6, "kPa": 6894.76, "MPa": 6.89476, "bar": 68.9476, "torr": 51714.9, "psi": 1000},
    }
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        return value * conversion_factors[from_unit][to_unit]
    else:
        return None

def convert_energy(value, from_unit, to_unit):
    conversion_factors = {
        "J": {"kJ": 0.001, "cal": 0.239006, "kcal": 0.000239006, "Wh": 0.000277778, "kWh": 2.77778e-7, "MWh": 2.77778e-10, "GWh": 2.77778e-13},
        "kJ": {"J": 1000, "cal": 239.006, "kcal": 0.239006, "Wh": 0.277778, "kWh": 0.000277778, "MWh": 2.77778e-7, "GWh": 2.77778e-10},
        "cal": {"J": 4.1868, "kJ": 0.0041868, "kcal": 0.001, "Wh": 0.001163, "kWh": 1.163e-6, "MWh": 1.163e-9, "GWh": 1.163e-12},
        "kcal": {"J": 4186.8, "kJ": 4.1868, "cal": 1000, "Wh": 1.163, "kWh": 0.001163, "MWh": 1.163e-6, "GWh": 1.163e-9},
        "Wh": {"J": 3600, "kJ": 3.6, "cal": 860.421, "kcal": 0.860421, "kWh": 0.001, "MWh": 1e-6, "GWh": 1e-9},
        "kWh": {"J": 3600000, "kJ": 3600, "cal": 860421, "kcal": 860.421, "Wh": 1000, "MWh": 0.001, "GWh": 1e-6},
        "MWh": {"J": 3600000000, "kJ": 3600000, "cal": 860421000, "kcal": 860421, "Wh": 1000000, "kWh": 1000, "GWh": 0.001},
        "GWh": {"J": 3600000000000, "kJ": 3600000000, "cal": 860421000000, "kcal": 860421000, "Wh": 1000000000, "kWh": 1000000, "MWh": 1000},
    }
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        return value * conversion_factors[from_unit][to_unit]
    else:
        return None

def convert_power(value, from_unit, to_unit):
    conversion_factors = {
        "W": {"kW": 0.001, "MW": 1e-6, "GW": 1e-9, "hp": 0.00134102},
        "kW": {"W": 1000, "MW": 0.001, "GW": 1e-6, "hp": 1.34102},
        "MW": {"W": 1000000, "kW": 1000, "GW": 0.001, "hp": 1341.02},
        "GW": {"W": 1000000000, "kW": 1000000, "MW": 1000, "hp": 1341020},
        "hp": {"W": 745.7, "kW": 0.7457, "MW": 0.0007457, "GW": 7.457e-7},
    }
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        return value * conversion_factors[from_unit][to_unit]
    else:
        return None

def convert_data(value, from_unit, to_unit):
    conversion_factors = {
        "bit": {"byte": 1/8, "kb": 1/8000, "Mb": 1/8000000, "Gb": 1/8000000000, "Tb": 1/8e+12, "Pb": 1/8e+15, "Eb": 1/8e+18},
        "byte": {"bit": 8, "kb": 1/1000, "Mb": 1/1000000, "Gb": 1/1000000000, "Tb": 1/1e+12, "Pb": 1/1e+15, "Eb": 1/1e+18},
        "kb": {"bit": 8000, "byte": 1000, "Mb": 1/1000, "Gb": 1/1000000, "Tb": 1/1e+9, "Pb": 1/1e+12, "Eb": 1/1e+15},
        "Mb": {"bit": 8000000, "byte": 1000000, "kb": 1000, "Gb": 1/1000, "Tb": 1/1e+6, "Pb": 1/1e+9, "Eb": 1/1e+12},
        "Gb": {"bit": 8000000000, "byte": 1000000000, "kb": 1000000, "Mb": 1000, "Tb": 1/1000, "Pb": 1/1e+6, "Eb": 1/1e+9},
        "Tb": {"bit": 8e+12, "byte": 1e+12, "kb": 1e+9, "Mb": 1e+6, "Gb": 1000, "Pb": 1/1000, "Eb": 1/1e+6},
        "Pb": {"bit": 8e+15, "byte": 1e+15, "kb": 1e+12, "Mb": 1e+9, "Gb": 1e+6, "Tb": 1000, "Eb": 1/1000},
        "Eb": {"bit": 8e+18, "byte": 1e+18, "kb": 1e+15, "Mb": 1e+12, "Gb": 1e+9, "Tb": 1e+6, "Pb": 1000},
    }
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        return value * conversion_factors[from_unit][to_unit]
    else:
        return None

def convert_frequency(value, from_unit, to_unit):
    conversion_factors = {
        "Hz": {"kHz": 0.001, "MHz": 1e-6, "GHz": 1e-9, "THz": 1e-12},
        "kHz": {"Hz": 1000, "MHz": 0.001, "GHz": 1e-6, "THz": 1e-9},
        "MHz": {"Hz": 1000000, "kHz": 1000, "GHz": 0.001, "THz": 1e-6},
        "GHz": {"Hz": 1000000000, "kHz": 1000000, "MHz": 1000, "THz": 0.001},
        "THz": {"Hz": 1000000000000, "kHz": 1000000000, "MHz": 1000000, "GHz": 1000},
    }
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
         return value * conversion_factors[from_unit][to_unit]
    else:
        return None

def convert_angle(value, from_unit, to_unit):
    conversion_factors = {
        "deg": {"rad": 0.0174533, "grad": 1.11111},
        "rad": {"deg": 57.2958, "grad": 63.662},
        "grad": {"deg": 0.9, "rad": 0.015708},
    }
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        return value * conversion_factors[from_unit][to_unit]
    else:
        return None