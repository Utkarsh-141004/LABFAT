"""
This script demonstrates a simple GET request using the requests library.
"""

import requests

def main():
    """
    Main function to perform a GET request to GitHub's API and print the response.
    """
    response = requests.get("https://api.github.com")
    print(response.json())


if __name__ == "__main__":
    main()
