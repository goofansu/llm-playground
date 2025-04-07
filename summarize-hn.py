import requests
import gradio as gr
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


def process(id: int) -> str:
    html = fetch_hn_post(id)
    text = strip_tags(html)
    resp = generate_summary(text)
    return resp


# Create a Gradio interface
with gr.Blocks() as demo:
    # Add a title to the interface
    gr.Markdown("# Summarize Hacker News")

    # Create an input component for the integer
    with gr.Row():
        number_input = gr.Number(label="Hacker News ID", precision=0)

    # Create a button for submission
    with gr.Row():
        submit_btn = gr.Button("Submit")

    # Create an output text component
    with gr.Row():
        output_text = gr.Textbox(label="Result")

    # Set up the submission action
    submit_btn.click(fn=process, inputs=[number_input], outputs=[output_text])

# Launch the app
if __name__ == "__main__":
    demo.launch()
