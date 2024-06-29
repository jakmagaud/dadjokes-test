import requests
import argparse
import time

ENDPOINT = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json", "User-Agent": "dadjokes-test (https://github.com/jakmagaud/dadjokes-test)"}

# gets all the jokes for a search term and returns it in a list
def joke_lookup_search(num_jokes, search_term):
    for i in range(num_jokes):
        response = requests.get(url=ENDPOINT + "/search", headers=headers, params={"term": search_term})
        if response.status_code == 200:
            results = response.json()["results"]
            return results


# gets a single random joke and prints it
def joke_lookup_random(num_jokes):
    for i in range(num_jokes):
        response = requests.get(url=ENDPOINT, headers=headers)
        if response.status_code == 200:
            print(response.json()["joke"])


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num-jokes", help="number of jokes in each set", type=int, choices=list(range(1,11)))
    parser.add_argument("-s", "--search", help="search term")
    args = parser.parse_args()

    # number of jokes per set defaults to 1 if not specified
    if not args.num_jokes:
        args.num_jokes = 1
    
    # if a search topic is passed in, get all the jokes for that search term
    if args.search:
        results = joke_lookup_search(num_jokes=args.num_jokes, search_term=args.search)
        joke_index = 0

    # loop runs once every 15 seconds for a total of 60 seconds
    end_time = time.time() + 60
    while time.time() < end_time:
        # if there's a search term, just index into the list of search results and print the next joke
        if args.search:
            for i in range(args.num_jokes):
                if joke_index < len(results):
                    print(results[joke_index]["joke"])
                    joke_index += 1
                # if the number of jokes we have to print exceeds the length of the result list, quit
                else:
                    print("We're all out of jokes on that topic!")
                    exit()
        else:
            joke_lookup_random(num_jokes=args.num_jokes)
        time.sleep(15)