import xml.etree.ElementTree as ET
import copy
import os
import json

noun_XML_filenames = os.listdir('../../BuNaMo/noun')

def main():

    default_noun_objects = {}
    noun_variations_objects = []

    count = 1
    for fname in noun_XML_filenames:
        print(str(count) + ' ')
        object_from_one_file = parse_one_xml_file('../../BuNaMo/noun/' + fname)
        # default_noun_objects.append(object_from_one_file[0])
        default = object_from_one_file[0].pop('default')
        default_noun_objects[default] = object_from_one_file[0]
        noun_variations_objects.extend(object_from_one_file[1])
        count += 1

    with open('./default_nouns.json', 'w') as outfile:
        json.dump(default_noun_objects, outfile, ensure_ascii=False)

    with open('./noun_variations.json', 'w') as outfile:
        json.dump(noun_variations_objects, outfile, ensure_ascii=False)

def parse_one_xml_file(filename):
    mytree = ET.parse(filename)
    root = mytree.getroot()

    default_json_object = copy.deepcopy(root.attrib)
    json_variations = []
    for el in root:       
        el_json = {'default': default_json_object['default']}
        for item in el.items():
            if item[0] == 'default':
                el_json['word'] = item[1]
                el_json['number'] = el.tag[:2].lower()
                el_json['case'] = el.tag[2:].lower()
                default_json_object[el.tag] = item[1]
            else:
                el_json[item[0]] = item[1]
        json_variations.append(el_json)

    return [default_json_object, json_variations]

if __name__ == "__main__":
    main()
    # parse_one_xml_file('../../BuNaMo/noun/abacas_masc.xml')
