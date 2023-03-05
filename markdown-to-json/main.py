import pycob as cob
import markdown
import html_to_json
import json

def home(server_request: cob.Request) -> cob.Page:
    page = cob.Page("Markdown to JSON")

    page.add_header("Markdown to JSON")

    with page.add_card() as card:
        card.add_header("Paste your Markdown Here", size=2)
        with card.add_form(method="POST") as form:
            form.add_formtextarea("Markdown", "markdown", "Enter Markdown here")
            form.add_formsubmit("Convert")
    
    markdown_param = server_request.params("markdown")

    if not markdown_param or markdown_param == "":
        return page
    
    page.add_divider()

    html_str = markdown.markdown(markdown_param)
    json_str = json.dumps(html_to_json.convert(html_str), indent=4)

    page.add_header("JSON Output")
    page.add_codeeditor(json_str, language="json")

    page.add_divider()

    page.add_header("Source Code For This Page")
    page.add_link("View on GitHub", "https://github.com/pycob/prototypes/blob/main/markdown-to-html/")
    page.add_emgithub("https://github.com/pycob/prototypes/blob/main/markdown-to-html/main.py")

    return page

app = cob.App("Markdown to JSON")

app.register_function(home)

server = app.run()