import xml.etree.ElementTree as ET
import copy
import os
import json

all_noun_objects = []

def main():
    noun_XML_filenames = os.listdir('../BuNaMo/noun')

    for fname in noun_XML_filenames:
        print('parsing ', fname)
        objects_from_one_file = parse_one_xml_file('../BuNaMo/noun/' + fname)
        all_noun_objects.extend(objects_from_one_file)

    with open('./nouns.json', 'w') as outfile:
        json.dump(all_noun_objects, outfile, ensure_ascii=False)

def parse_one_xml_file(filename):
    mytree = ET.parse(filename)
    root = mytree.getroot()
    json_objects = []
    for el in root:
        json_object = copy.deepcopy(root.attrib)
        for item in el.items():
            if item[0] == "default":
                json_object["word"] = item[1]
            else:
                json_object[item[0]] = item[1]

        json_object["number"] = el.tag[:2]
        json_object["case"] = el.tag[2:].lower()
        json_objects.append(json_object)
    
    return json_objects

if __name__ == "__main__":
    main()
