import xml.etree.ElementTree as ET
import copy
import os
import json

verb_XML_filenames = os.listdir('../BuNaMo/verb')


def main():

    default_verb_objects = {}
    verb_variations_objects = []
    mood_variations_objects = []
    verbal_noun_objects = []
    verbal_adjective_objects = []

    count = 1
    for fname in verb_XML_filenames:
        print(f"{count}: {fname}\n")
        default_verb, verbal_noun, verbal_adjective, verb_variations, mood_variations = parse_one_xml_file(
            '../BuNaMo/verb/' + fname)
        default = default_verb.pop('default')
        default_verb_objects[default] = default_verb
        verb_variations_objects.extend(verb_variations)
        mood_variations_objects.extend(mood_variations)
        verbal_noun_objects.append(verbal_noun)
        verbal_adjective_objects.append(verbal_adjective)
        count += 1

    with open('../converted-JSON-data/verbs/verbs_default.json', 'w') as outfile:
        json.dump(default_verb_objects, outfile, ensure_ascii=False)

    with open('../converted-JSON-data/verbs/verbs.json', 'w') as outfile:
        json.dump(verb_variations_objects, outfile, ensure_ascii=False)

    with open('../converted-JSON-data/verbs/moods.json', 'w') as outfile:
        json.dump(mood_variations_objects, outfile, ensure_ascii=False)

    with open('../converted-JSON-data/verbs/verbal_nouns.json', 'w') as outfile:
        json.dump(verbal_noun_objects, outfile, ensure_ascii=False)

    with open('../converted-JSON-data/verbs/verbal_adjectives.json', 'w') as outfile:
        json.dump(verbal_adjective_objects, outfile, ensure_ascii=False)


def parse_one_xml_file(filename):
    mytree = ET.parse(filename)
    root = mytree.getroot()

    default_verb = copy.deepcopy(root.attrib)
    verb_variations = []
    mood_variations = []
    verbal_noun = {}
    verbal_adjective = {}

    for el in root:
        # print('el:', el.items())

        verb = {'default': default_verb['default']}
        for item in el.items():
            # print('item:', item)
            if el.tag == "verbalNoun":
                verbal_noun['default'] = default_verb['default']
                verbal_noun['type'] = 'verbal noun'
                if item[0] == 'default':
                    verbal_noun['word'] = item[1]

            elif el.tag == "verbalAdjective":
                verbal_adjective['default'] = default_verb['default']
                if item[0] == 'default':
                    verbal_adjective['word'] = item[1]
                verbal_adjective['type'] = 'verbal adjective'

            elif el.tag == "tenseForm":

                if item[0] == 'default':
                    verb['word'] = item[1]
                else:
                    verb[item[0]] = item[1]
                verb['type'] = 'verb'

            elif el.tag == "moodForm":
                if item[0] == 'default':
                    verb['word'] = item[1]
                else:
                    verb[item[0]] = item[1]
                verb['type'] = 'mood'

        if el.tag == "tenseForm":
            verb_variations.append(verb)

        elif el.tag == "moodForm":
            mood_variations.append(verb)

    # print('default_verb:', default_verb)
    # print('verb_variations:', verb_variations)
    # print('verbal_noun:', verbal_noun)
    # print('verbal_adjective:', verbal_adjective)
    return default_verb, verbal_noun, verbal_adjective, verb_variations, mood_variations


if __name__ == "__main__":
    main()
# parse_one_xml_file('../BuNaMo/verb/abair_verb.xml')
