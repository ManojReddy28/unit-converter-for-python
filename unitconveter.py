import code

# Create a Unit Registry
ureg = print.UnitRegistry()

def temperature_converter(value, from_unit, to_unit):
    # Define temperature quantities
    temperature = value * ureg(from_unit)

    # Convert temperature
    converted_temperature = temperature.to(to_unit)
    return converted_temperature

def length_converter(value, from_unit, to_unit):
    # Define length quantities
    length = value * ureg(from_unit)

    # Convert length
    converted_length = length.to(to_unit)
    return converted_length

def weight_converter(value, from_unit, to_unit):
    # Define weight quantities
    weight = value * ureg(from_unit)

    # Convert weight
    converted_weight = weight.to(to_unit)
    return converted_weight

# Examples
# Temperature Conversion
converted_temp = temperature_converter(32, 'Fahrenheit', 'Celsius')
print(f"32°F in Celsius: {converted_temp}")

# Length Conversion
converted_length = length_converter(5, 'meter', 'feet')
print(f"5 meters in feet: {converted_length}")

# Weight Conversion
converted_weight = weight_converter(10, 'kilogram', 'pound')
print(f"10 kilograms in pounds: {converted_weight}")