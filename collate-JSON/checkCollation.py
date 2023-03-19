import json

def main():
    with open("./wordObjectDictionary.json") as json_file:
        data = json.load(json_file)

    print('data:', data['umainn'])

if __name__ == "__main__":
    main()
