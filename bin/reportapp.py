import requests


def main():
    choice = input("[R]eport weather or [s]ee reports? Or E[x]it? ")
    while choice:
        if choice.lower().strip() == 'r':
            report_event()
        elif choice.lower().strip() == 's':
            see_events()
        elif choice.lower().strip() == 'x':
            print("Exiting...")
            exit(0)
        else:
            print(f"Don't know what to do with {choice}.")

        choice = input("[R]eport weather or [s]ee reports? Or E[x]it? ")


def report_event():
    desc = input("What is happening now? ")
    city = input("What city? ")
    data = {
        "description": desc,
        "location": {
            "city": city,
            "state": "TX"
        }
    }

    url = "http://127.0.0.1:8000/api/reports"
    resp = requests.post(url, json=data)
    resp.raise_for_status()

    result = resp.json()
    print(f"Reported new event: {result.get('id')}")


def see_events():
    url = "http://127.0.0.1:8000/api/reports"
    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()

    for r in data:
        print(f"{r.get('location').get('city')} status: {r.get('description')}")


if __name__ == '__main__':
    main()
