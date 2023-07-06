import json

def main():
    with open("./wordObjectDictionary.json") as json_file:
        data = json.load(json_file)

    print('rith:', data['rith'])
    print('thú:', data['thú'])
    print('dúirt:', data['dúirt'])

if __name__ == "__main__":
    main()
