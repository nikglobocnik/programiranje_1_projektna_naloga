# Najbogatejši zemljani

### Projektna naloga iz analize podatkov pri predmetu Programiranje 1

## Uvod


Analiziral bom 500 najbogatejših zemljanov. Podatke bom pridobil s strani
[Bloomberg](https://www.bloomberg.com//billionaires/). 

Za vsakega predstavnika bom zajel:
* ime in priimek,
* premoženje,
* državo,
* letni prirast premoženja,
* ...

Delovne hipoteze:
* Miljarderji z  največjim prirastom primoženja prihajajo iz razvijajočih se držav. 
* Bogastvo je neenakomerno razporejeno po svetu.
* Največ miljarderjev je Američanov. 
* ...

## Priprava podatkov

V repozitoriju se sedaj v mapi `obdelani_podatki` nahaja CSV datoteka `podatki.csv`. V njej so podatki o 500 najbogatejših zemljanih. Zajel sem podatke o njihovem premoženju, zadnji spremembi premoženja, letni spremembi premoženja, državi izvora in o področju na katerem delujejo.

Podatke sem pridobil z zajemom. Ustrezne skripte pa se nahajajo v datoteki `obdelaj_stran.py`. V pomoč so mi prišle tudi funkcije iz datoteke `orodja.py`, ki smo jih uporabljali pri predavanjih in vajah.

*Opomba*: Pri shranjevanju spletne strani sem naletel na težavo. Spletna stran je zaznala "čudno dejavnost" in funkcija je shranila html datoteko, ki se nahaja v `nalozene_strani/nalozen_html.html`.  V njej opazimo sporočilo **Are you a robot?**
Zato sem spletno stran, ki sem jo analiziral shranih "na roke". Nahaja se v mapi `html_rocno`. Zato je primerno prilagojena tudi koda v datoteki `obdelaj_stran.py`.
