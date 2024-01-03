import xml.etree.ElementTree as ET, os


# Function for reading the Extended_Modelmatching.txt
def lese_flugzeuge(dateiname):
    flugzeuge = {}
    with open(dateiname, 'r') as file:
        for line in file:
            split_line = line.strip().split()
            if len(split_line) == 2:
                flugzeug, ersatz = split_line
                if flugzeug not in flugzeuge:
                    flugzeuge[flugzeug] = []
                flugzeuge[flugzeug].append(ersatz)
    return flugzeuge


                            # Path to the .txt
flugzeuge = lese_flugzeuge('Extended_Modelmatching.txt')

# Reads data from the .vmr
with open('input.vmr', 'r') as file:
    data = file.read()

root = ET.fromstring(data)

# Here he writes the externaloutput.vmr
with open('externaloutput.vmr', 'w') as file:
    file.write('<?xml version="1.0" encoding="utf-8"?>\n')
    file.write('<ModelMatchRuleSet>\n')

    for model_match_rule in root.iter('ModelMatchRule'):
        type_code = model_match_rule.get('TypeCode')
        if type_code in flugzeuge:
            for replacement in flugzeuge[type_code]:
                print(f'plane({type_code}) found') # Debugging out
                model_match_rule.set('TypeCode', replacement)
                new_data = ET.tostring(model_match_rule, encoding='utf-8').decode('utf-8')
                new_data = new_data.rstrip()
                file.write('\t' + new_data + '\n')

    file.write('</ModelMatchRuleSet>')
