import requests

def main():
    response = requests.get("https://api.github.com")
    print(response.json())

if __name__ == "__main__":
    main()