import xml.etree.ElementTree as ET
import copy
import os
import json

adjective_XML_filenames = os.listdir('../BuNaMo/adjective')

def main():

    default_adjective_objects = {}
    adjective_variations_objects = []

    count = 1
    for fname in adjective_XML_filenames:
        print(f"{count}: {fname}\n")
        object_from_one_file = parse_one_xml_file('../BuNaMo/adjective/' + fname)
        default = object_from_one_file[0].pop('default')
        default_adjective_objects[default] = object_from_one_file[0]
        adjective_variations_objects.extend(object_from_one_file[1])
        count += 1

    with open('../converted-JSON-data/adjectives/adjectives_default.json', 'w') as outfile:
        json.dump(default_adjective_objects, outfile, ensure_ascii=False)

    with open('../converted-JSON-data/adjectives/adjectives.json', 'w') as outfile:
        json.dump(adjective_variations_objects, outfile, ensure_ascii=False)

def parse_one_xml_file(filename):
    mytree = ET.parse(filename)
    root = mytree.getroot()

    default_json_object = copy.deepcopy(root.attrib)
    json_variations = []
    for el in root:       
        el_json = {'default': default_json_object['default']}
        for item in el.items():
            if item[0] == 'default':
                el_json['type'] = "adjective"
                el_json['word'] = item[1]
                if el.tag == 'graded':
                    el_json['graded'] = True
                else:
                    el_json['graded'] = False
                    el_json['number'] = el.tag[:2].lower()
                    el_json['case'] = el.tag[2:5].lower()
                    if len(el.tag) > 5:
                        el_json['gender'] = el.tag[5:].lower()

                default_json_object[el.tag] = item[1]
            else:
                el_json[item[0]] = item[1]
        json_variations.append(el_json)

    # print('default_json_object', default_json_object)
    # print('json_variations', json_variations)
    return [default_json_object, json_variations]

if __name__ == "__main__":
    main()
# parse_one_xml_file('../BuNaMo/adjective/ábalta_adj3.xml')
