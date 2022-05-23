import markdown

with open('templates/history1.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

with open('history1.html', 'w') as f:
    f.write(html)
