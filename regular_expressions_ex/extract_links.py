import re

pattern = r"(?P<url>(?P<sub_domain>www)\.(?P<domain>[A-Za-z0-9]+(\-[A-Za-z0-9]+)*)(?P<domain_extension>(\.[a-z]+)+))"
valid_urls = []

text = input()
while text != "":
    matches = re.finditer(pattern, text)

    for match in matches:
        valid_urls.append(match.group("url"))

    text = input()

for url in valid_urls:
    print(url)