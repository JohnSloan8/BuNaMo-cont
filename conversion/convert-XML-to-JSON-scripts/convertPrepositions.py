import xml.etree.ElementTree as ET
import copy
import os
import json

preposition_XML_filenames = os.listdir('../BuNaMo/preposition')

def main():

    default_preposition_objects = {}
    preposition_variations_objects = []

    count = 1
    for fname in preposition_XML_filenames:
        print(str(count) + ' ')
        object_from_one_file = parse_one_xml_file('../BuNaMo/preposition/' + fname)
        default = object_from_one_file[0].pop('default')
        default_preposition_objects[default] = object_from_one_file[0]
        preposition_variations_objects.extend(object_from_one_file[1])
        count += 1

    with open('../converted-JSON-data/prepositions/prepositions_default.json', 'w') as outfile:
        json.dump(default_preposition_objects, outfile, ensure_ascii=False)

    with open('../converted-JSON-data/prepositions/prepositions.json', 'w') as outfile:
        json.dump(preposition_variations_objects, outfile, ensure_ascii=False)

def parse_one_xml_file(filename):
    mytree = ET.parse(filename)
    root = mytree.getroot()

    default_json_object = copy.deepcopy(root.attrib)
    json_variations = []
    for el in root:       
        el_json = {'default': default_json_object['default']}
        for item in el.items():
            if item[0] == 'default':
                el_json['type'] = "preposition"
                el_json['word'] = item[1]
                el_json['person'] = el.tag[:3].lower()
                if len(el.tag) > 3:
                    el_json['gender'] = el.tag[3:].lower()

                default_json_object[el.tag] = item[1]
            else:
                el_json[item[0]] = item[1]
        json_variations.append(el_json)

    # print('default_json_object:', default_json_object)
    # print('json_variations:', json_variations)
    return [default_json_object, json_variations]

if __name__ == "__main__":
    main()
# parse_one_xml_file('../BuNaMo/preposition/um_prep.xml')
