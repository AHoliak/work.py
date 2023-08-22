data = '''{
    audioBoxSerialNumber = AA0001;
    energyValues = (
        "-19.88488",
        "-19.94069",
        "-27.40622",
        ...
        "-63.01849"
    );
    input = "Mic 4";
    output = Right;
    serialNumber = H1CHL8HX0360;
    source = "HighVoltageEarbudTest_PreCal.wav";
}'''

# Remove unwanted characters from the string
data = data.replace('{', '').replace('}', '').replace(';', '').replace('\n', '').replace(' ', '')

# Split the string by the '=' character
key_value_pairs = data.split('=')

# Extract the key-value pairs of interest
energy_values = key_value_pairs[2][1:-1].split(',')
energy_values = [value.strip('"') for value in energy_values]

# Extract the serial number
serial_number = key_value_pairs[4].strip()

# Create a dictionary
dictionary = {'serialNumber': serial_number, 'energyValues': energy_values}

print(dictionary)

