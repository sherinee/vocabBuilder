import json
import random
def main():
    #random number
    randomId =str(random.randint(1, 54000))
    print(randomId)
    with open('wordsDictionary.json') as data_file:
        data = json.load(data_file)
        for key, value in data.items():
            if key == randomId:
                print(data[key]['Word'])
                print(data[key]['Meaning'])

if __name__ == "__main__":
    main()
