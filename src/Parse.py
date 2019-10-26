from bs4 import BeautifulSoup
import requests


class Parse:

    def __init__(self, url):
        self.soup = BeautifulSoup(requests.get(url).content, 'html5lib')

    def generate_webpage(self):
        list_of_output = self.soup.find_all(["h1", "p", "noscript"])
        title = ""
        html_script = ""
        start_tag, end_tag = self.__template()
        html_script += start_tag
        for output in list_of_output:
            if output.name == "h1" or output.name == "p":
                if output.name == "h1" and title == "":
                    title = str(output.text).strip()
                html_script += output.prettify()
            elif output.name == "noscript":
                html_script += output.find("img").prettify()
        html_script += end_tag
        return title, html_script

    def generate_webpage2(self):
        return "abc",self.soup.prettify()

    def __template(self):
        start_template = """<!DOCTYPE html>
        <html>
<head>
<title>Free Medium</title>
<style>
h1 {
	margin-right: 150px;
	margin-left: 80px;
}
p {
	margin-right: 150px;
	margin-left: 80px;
}
img {
	display: block;
    max-height:70%;
    max-width:70%;
    height:auto;
    width:auto;
	margin-left: auto;
	margin-right: auto;
}
</style>
</head>
<body>"""
        end_template = """</body>
</html>"""

        return start_template, end_template
