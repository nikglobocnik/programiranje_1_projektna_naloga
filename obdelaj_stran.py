import re
import orodja

vrstica = re.compile(
    r'<div class="table-row">.*?</div>\n\s*</div>',
    flags=re.DOTALL
)

podatki_vrstica = re.compile(
    r'<div class="table-row">\n\s*<div class="table-cell t-rank">\n\s*(?P<mesto>.*?)\n\s*</div>\n\s*<div '
    r'class="table-cell t-name"><a href=".*?">\n\s*(?P<ime>.*?)</a></div>\n\s*<div class="table-cell active '
    r't-nw">\n\s*(?P<premozenje>.*?)\n\s*</div>\n\s*<div class="table-cell t-lcd \w*">\n\s*'
    r'(?P<zadnja_sprememba>.*?)\n\s*</div>\n\s*<!-- <div class="table-cell t-lcp \w*">'
    r'(?P<zadnja_sprememba_procenti>.*?)</div> -->\n\s*<div class="table-cell t-ycd \w*">\n\s*'
    r'(?P<letna_sprememba>.*?)\n\s*</div>\n\s*<!-- <div class="table-cell t-ycp \w*">'
    r'(?P<letna_sprememba_procenti>.*?)</div> -->\n\s*<div class="table-cell t-country">\n\s*(?P<drzava>.*?)'
    r'\n\s*</div>\n\s*<div class="table-cell t-industry">\n\s*(?P<podrocje>.*?)\n\s*</div>\n\s*</div>',
    flags=re.DOTALL
)

def spremeni(string):
    '''Funkcija primerno spremeni nize.'''
    for znak in string:
        if znak == '+':
            string = string.replace('+', '')
        elif znak == '-':
            string = string
        elif znak == '$':
            string = string.replace('$', '')
    if string.endswith('B'):
        string = string.replace('B', '')
        string = int(float(string) * 10**9)
    elif string.endswith('M'):
        string = string.replace('M', '')
        string = int(float(string) * 10**6)
    elif string.endswith('k'):
        string = string.replace('k', '') 
        string = int(float(string) * 10**3)  
    elif string.endswith('%'):
        string = string.replace('%', '') 
        string = float(string)
    return string
        


def podatki_v_vrstici(vrst): 
    '''Funkcija iz podatkov v vrsticah naredi slovar glede na dana gesla.'''
    if podatki_vrstica.search(vrst) == None:
        return
    else:
        seznam_gesel = ['premozenje', 'zadnja_sprememba', 'zadnja_sprememba_procenti', 'letna_sprememba', 'letna_sprememba_procenti']
        podatki_vrstice = podatki_vrstica.search(vrst).groupdict()
        for geslo in seznam_gesel:
            podatki_vrstice[geslo] = spremeni(podatki_vrstice[geslo])
        return podatki_vrstice


def vrstice_na_spletni_strani(ime_datoteke):
    vsebina = orodja.vsebina_datoteke(ime_datoteke)
    for row in vrstica.finditer(vsebina):
        yield podatki_v_vrstici(row.group(0))

def nalozi_strani():
    url = ('https://www.bloomberg.com//billionaires/')
    ime_datoteke = (f'/Users/nik/programiranje_1_projektna_naloga/nalozena_stran_rocno/rocno_shranjen_html.html')
    orodja.shrani_spletno_stran(url, ime_datoteke, vsili_prenos=False)

spl_str = (f'/Users/nik/programiranje_1_projektna_naloga/nalozena_stran_rocno/rocno_shranjen_html.html')

# Zgoraj spletno stran definiramo drugače, kot naloženo, ker se pojavi težava pri zajemu spletne strani.

vse_vrstice = []
def zdruzi_vrstice():
    for vrstica in vrstice_na_spletni_strani(spl_str):
        vse_vrstice.append(vrstica)


def ustvari_json():
    orodja.zapisi_json(vse_vrstice, "/Users/nik/programiranje_1_projektna_naloga/obdelani_podatki/podatki.json")

imena_polj = ['mesto', 'ime', 'premozenje', 'zadnja_sprememba', 'zadnja_sprememba_procenti', 'letna_sprememba', 'letna_sprememba_procenti', 'drzava', 'podrocje']

def ustvari_csv():
    orodja.zapisi_csv(vse_vrstice, imena_polj, "/Users/nik/programiranje_1_projektna_naloga/obdelani_podatki/podatki.csv")


nalozi_strani()
zdruzi_vrstice()
ustvari_json()
ustvari_csv()
