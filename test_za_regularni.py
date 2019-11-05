import re
import requests

vzorec = (
    r'<div class="table-row">\n\s*<div class="table-cell t-rank">\n\s*(?P<mesto>.*?)\n\s*</div>\n\s*<div '
    r'class="table-cell t-name"><a href=".*?">\n\s*(?P<ime>.*?)</a></div>\n\s*<div class="table-cell active '
    r't-nw">\n\s*(?P<premozenje>.*?)\n\s*</div>\n\s*<div class="table-cell t-lcd \w*">\n\s*'
    r'(?P<zadnja_sprememba>.*?)\n\s*</div>\n\s*<!-- <div class="table-cell t-lcp \w*">'
    r'(?P<zadnja_sprememba_procenti>.*?)</div> -->\n\s*<div class="table-cell t-ycd \w*">\n\s*'
    r'(?P<letna_sprememba>.*?)\n\s*</div>\n\s*<!-- <div class="table-cell t-ycp \w*">'
    r'(?P<letna_sprememba_procent>.*?)</div> -->\n\s*<div class="table-cell t-country">\n\s*(?P<drzava>.*?)'
    r'\n\s*</div>\n\s*<div class="table-cell t-industry">\n\s*(?P<podrocje>.*?)\n\s*</div>\n\s*</div>'
)

zadetki = []
counter = 0

with open(f"/Users/nik/Desktop/programiranje_1_projektna_naloga/nalozena_stran_rocno/rocno_shranjen_html.html", encoding='utf-8') as file:
    vsebina = file.read()

for zadetek in re.finditer(vzorec, vsebina):
    zadetki.append(zadetek.groupdict())
    counter += 1

print(counter)