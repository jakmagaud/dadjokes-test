import requests
import argparse
import json

ENDPOINT = "https://icanhazdadjoke.com/"


def joke_lookup(num_jokes, search_term):
    headers = {"Accept": "application/json", "User-Agent": "dadjokes-test (https://github.com/jakmagaud/dadjokes-test)"}
    if search_term:
        print('hi')
    else:
        for i in range(num_jokes):
            response = requests.get(url=ENDPOINT, headers=headers)
            if response.status_code == 200:
                print(response.json()["joke"])

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num-jokes", help="number of jokes in each set", type=int, choices=list(range(1,11)))
    parser.add_argument("-s", "--search", help="search term")
    args = parser.parse_args()

    # set default values if user doesn't specify
    if not args.num_jokes:
        args.num_jokes = 1
            
    joke_lookup(num_jokes=args.num_jokes, search_term=args.search)