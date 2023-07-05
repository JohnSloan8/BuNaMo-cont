import xml.etree.ElementTree as ET
import copy
import os
import json

possessive_XML_filenames = os.listdir('../BuNaMo/possessive')

def main():

    default_possessive_objects = {}
    possessive_variations_objects = []

    count = 1
    for fname in possessive_XML_filenames:
        print(str(count) + ' ')
        object_from_one_file = parse_one_xml_file('../BuNaMo/possessive/' + fname)
        default = object_from_one_file[0].pop('default')
        default_possessive_objects[default] = object_from_one_file[0]
        possessive_variations_objects.extend(object_from_one_file[1])
        count += 1

    with open('../converted-JSON-data/possessives/possessives_default.json', 'w') as outfile:
        json.dump(default_possessive_objects, outfile, ensure_ascii=False)

    with open('../converted-JSON-data/possessives/possessives.json', 'w') as outfile:
        json.dump(possessive_variations_objects, outfile, ensure_ascii=False)

def parse_one_xml_file(filename):
    mytree = ET.parse(filename)
    root = mytree.getroot()

    default_json_object = copy.deepcopy(root.attrib)
    json_variations = []
    for el in root:       
        el_json = {'default': default_json_object['default']}
        
        if 'fem' in filename:
            el_json['gender'] = 'fem'
            el_json['number'] = 'sg'
        elif 'masc' in filename:
            el_json['gender'] = 'masc'
            el_json['number'] = 'sg'
        elif 'pl' in filename or 'ár'in filename or 'bhur' in filename:
            el_json['number'] = 'pl'
        else:
            el_json['number'] = 'sg'

        for item in el.items():
            el_json['type'] = "possessive"
            el_json['word'] = item[1]
            el_json['form'] = el.tag.lower()
            default_json_object[el.tag] = item[1]
        json_variations.append(el_json)

    # print('default_json_object:', default_json_object)
    # print('json_variations:', json_variations)
    return [default_json_object, json_variations]

if __name__ == "__main__":
    main()
# parse_one_xml_file('../BuNaMo/possessive/bhur_poss.xml')
