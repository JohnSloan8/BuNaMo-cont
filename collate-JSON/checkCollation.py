import json

def main():
    with open("./wordObjectDictionary.json") as json_file:
        data = json.load(json_file)

    print('data:', data['mé'])
    print('data:', data['thú'])

if __name__ == "__main__":
    main()
