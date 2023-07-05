
import json

word_types = ["verbs", "nouns", "adjectives", "prepositions", "possessives", "pronouns"]
verb_types = ["verbal_adjectives", "verbal_nouns", "moods"]
def main():

    word_object_dictionary = {}

    for word_type in word_types:
        with open(f"../converted-JSON-data/{word_type}/{word_type}.json") as json_file:
            data = json.load(json_file)
            for word_object in data:
                if word_object['word'] in word_object_dictionary:
                    word_object_dictionary[word_object['word']].append(word_object)
                else:
                    word_object_dictionary[word_object['word']] = [word_object]

    for verb_type in verb_types:
        with open(f"../converted-JSON-data/verbs/{verb_type}.json") as json_file:
            data = json.load(json_file)
            for word_object in data:
                if word_object['word'] in word_object_dictionary:
                    word_object_dictionary[word_object['word']].append(word_object)
                else:
                    word_object_dictionary[word_object['word']] = [word_object]

    with open('./wordObjectDictionary.json', 'w') as outfile:
        json.dump(word_object_dictionary, outfile, ensure_ascii=False)

if __name__ == "__main__":
    main()
