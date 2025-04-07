import sys
import requests
from smartfunc import backend
from strip_tags import strip_tags


@backend("openrouter/openai/gpt-4o-mini")
def generate_summary(text: str):
    """Generate a summary of the following text: {{ text }}"""
    pass


def fetch_hn_post(id: int):
    url = f"https://news.ycombinator.com/item?id={id}"
    resp = requests.get(url)
    return resp.text


html = fetch_hn_post(sys.argv[1])
text = strip_tags(html)
resp = generate_summary(text)
print(resp)
