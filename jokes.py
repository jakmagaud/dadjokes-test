import requests
import argparse
import time

ENDPOINT = "https://icanhazdadjoke.com/"

def joke_lookup_search(num_jokes, search_term):
    headers = {"Accept": "application/json", "User-Agent": "dadjokes-test (https://github.com/jakmagaud/dadjokes-test)"}
    for i in range(num_jokes):
        response = requests.get(url=ENDPOINT + "/search", headers=headers, params={"term": search_term})
        if response.status_code == 200:
            results = response.json()["results"]
            return results


def joke_lookup_random(num_jokes):
    headers = {"Accept": "application/json", "User-Agent": "dadjokes-test (https://github.com/jakmagaud/dadjokes-test)"}

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
    
    if args.search:
        results = joke_lookup_search(num_jokes=args.num_jokes, search_term=args.search)
        joke_index = 0

    end_time = time.time() + 60
    while time.time() < end_time:
        if args.search:
            for i in range(args.num_jokes):
                if joke_index < len(results):
                    print(results[joke_index]["joke"])
                    joke_index += 1
                else:
                    print("We're all out of jokes on that topic!")
                    exit()
        else:
            joke_lookup_random(num_jokes=args.num_jokes)
        time.sleep(15)