import requests

def random_qoutes():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    response = requests.get(url)
    data = response.json()

    # Validation, if not working Api
    if data.get("success") and "data" in data:
        quotes_data = data["data"]
        author = quotes_data["author"]
        content = quotes_data["content"]
        return author, content
    else:
        raise Exception("Failed to fetech data")


def main():
    try:
        auther, quotes = random_qoutes()
        print("*" * 100)
        print("Random Quotes:")
        print(f"Auther: {auther}\nQuote: {quotes}")
        print("*" * 100)

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()