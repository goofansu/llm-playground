import sys
from smartfunc import backend


@backend("openrouter/openai/gpt-4o-mini")
def translate_to_zh(text: str):
    """Translate given text to Chinese: {{ text }}"""
    pass


@backend("openrouter/google/gemini-2.0-flash-001")
def translate_to_en(text: str):
    """Translate given text to English: {{ text }}"""
    pass


text_in_zh = translate_to_zh(sys.argv[1])
print(text_in_zh)

text_in_en = translate_to_en(text_in_zh)
print(text_in_en)
