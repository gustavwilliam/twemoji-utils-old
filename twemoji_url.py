BASE_URL = "https://github.com/twitter/twemoji/blob/master/assets/svg/"


def get_hex(emoji: str) -> str:
    return hex(ord(emoji))[2:]


if __name__ == "__main__":
    emoji = input("> ")
    hex = get_hex(emoji)
    url = f"{BASE_URL}{hex}.svg"
    print(url)

