import imgkit

options = {"xvfb": ""}
imgkit.from_file("index.html", "screenshot.jpg", options=options)
