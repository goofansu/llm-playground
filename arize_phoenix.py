import litellm
import os

os.environ["PHOENIX_COLLECTOR_HTTP_ENDPOINT"] = "http://localhost:6006/v1/traces"

# set arize as a callback, litellm will send the data to arize
litellm.callbacks = ["arize_phoenix"]

# openai call
response = litellm.completion(
    model="openrouter/openai/gpt-4o", messages=[{"role": "user", "content": "hello"}]
)

print(response)
