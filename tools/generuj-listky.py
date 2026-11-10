import html
import os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '')
e=lambda s: html.escape(s, quote=True)
SMALL=('0,04 l, malý za polovic','0.04 l, small one at half price')
DAILY=('dle denní nabídky','daily offer')
# kategorie: (cs, en, podtitulek(cs,en)|None, [(cs_nazev, en_nazev, (cs_pozn,en_pozn)|None, cena)])
NAPOJE=[
 ('Pivo','Beer',None,[
  ('Plzeň 12°','Pilsner Urquell 12°',('0,3 l','0.3 l'),47),
  ('Plzeň 12°','Pilsner Urquell 12°',('0,5 l','0.5 l'),67),
  ('Plzeň 12° šnyt','Pilsner Urquell 12° šnyt',('0,3 l','0.3 l, Czech pour with a thick head of foam'),47),
  ('Plzeň 12° mlíko','Pilsner Urquell 12° mlíko',('0,3 l','0.3 l, Czech pour of almost pure foam'),47),
  ('Radegast 10°','Radegast 10°',('0,3 l','0.3 l'),35),
  ('Radegast 10°','Radegast 10°',('0,5 l','0.5 l'),55),
  ('Kosmix dry stout 12°','Kosmix dry stout 12°',('0,3 l','0.3 l'),65),
  ('Kosmix dry stout 12°','Kosmix dry stout 12°',('0,5 l','0.5 l'),85),
  ('Kosmix speciál','Kosmix special',('0,3 l, dle denní nabídky','0.3 l, daily offer'),69),
  ('Kosmix speciál','Kosmix special',('0,5 l, dle denní nabídky','0.5 l, daily offer'),89),
  ('Birell Pomelo & Grep','Birell Pomelo & Grapefruit',('0,3 l','0.3 l, non-alcoholic'),39),
  ('Birell Pomelo & Grep','Birell Pomelo & Grapefruit',('0,5 l','0.5 l, non-alcoholic'),59)]),
 ('Víno','Wine',None,[
  ('Pinot Gris','Pinot Gris',('0,1 l','0.1 l'),65),
  ('Pinot Gris','Pinot Gris',('0,75 l, 12 % alc., suché, moravské zemské víno 2025, vinařství U Vrbů','0.75 l, 12% ABV, dry, Moravian regional wine 2025, U Vrbů winery'),440),
  ('Sauvignon blanc','Sauvignon blanc',('0,7 l, 12 % alc., suché, moravské zemské víno 2024, vinařství Nepraš','0.7 l, 12% ABV, dry, Moravian regional wine 2024, Nepraš winery'),590),
  ('Savrie','Savrie',('0,7 l, 11,5 % alc., suché, moravské zemské víno 2023, vinařství Nepraš','0.7 l, 11.5% ABV, dry, Moravian regional wine 2023, Nepraš winery'),550),
  ('Primitivo Sole Mio','Primitivo Sole Mio',('0,1 l','0.1 l'),60),
  ('Primitivo Sole Mio','Primitivo Sole Mio',('0,7 l, 14 % alc., Itálie','0.7 l, 14% ABV, Italy'),390),
  ('Primitivo di Manduria','Primitivo di Manduria',('0,7 l, 15 % alc., Itálie','0.7 l, 15% ABV, Italy'),490),
  ('Dal Bello','Dal Bello',('0,1 l','0.1 l'),49),
  ('Dal Bello','Dal Bello',('0,75 l, 11 % alc., spumante, Carta Gialla cuvée extra dry, Treviso','0.75 l, 11% ABV, spumante, Carta Gialla cuvée extra dry, Treviso'),340)]),
 ('Prosecco','Prosecco',None,[
  ('Dal Bello','Dal Bello',('0,75 l, 11 % alc., spumante, millesimato, DOC, Treviso, Brut','0.75 l, 11% ABV, spumante, millesimato, DOC, Treviso, Brut'),450)]),
 ('Míchané drinky','Mixed drinks',None,[
  ('Aperol Spritz','Aperol Spritz',('0,25 l','0.25 l'),139),
  ('Hugo Spritz','Hugo Spritz',('0,25 l','0.25 l'),139),
  ('Limoncello Spritz','Limoncello Spritz',('0,25 l','0.25 l'),149)]),
 ('Nealko','Soft drinks',None,[
  ('Točená Malinovka','Draught raspberry soda',('0,3 l','0.3 l'),39),
  ('Točená Malinovka','Draught raspberry soda',('0,5 l','0.5 l'),59),
  ('Fritz Kola','Fritz Kola',('0,33 l','0.33 l'),75),
  ('Fritz Třešeň','Fritz Cherry',('0,33 l','0.33 l'),75),
  ('Fritz Anjola','Fritz Anjola',('0,33 l, ananasovo-limetová','0.33 l, pineapple & lime'),85),
  ('Fentimans tonic','Fentimans tonic',('0,2 l','0.2 l'),79),
  ('Fentimans rose','Fentimans rose',('0,2 l','0.2 l'),79),
  ('Džbán vody s citrónem','Jug of water with lemon',('0,5 l','0.5 l'),20),
  ('Džbán vody s citrónem','Jug of water with lemon',('1 l','1 l'),40)]),
 ('Káva','Coffee',None,[
  ('Espresso','Espresso',None,49),('Doppio','Doppio',None,79),
  ('Americano','Americano',None,59),('Turek','Turkish-style coffee',None,69)]),
 ('Vodka','Vodka',SMALL,[('Zoladkowa De Luxe','Zoladkowa De Luxe',None,59),('Pravda','Pravda',None,75)]),
 ('Rum','Rum',SMALL,[('Heffron 5y','Heffron 5y',None,59),('Malteco 10y','Malteco 10y',None,89),('A.H. Riise XO Reserva','A.H. Riise XO Reserva',None,149)]),
 ('Gin','Gin',SMALL,[("Gordon's","Gordon's",None,69),("Gordon's Pink","Gordon's Pink",None,69)]),
 ('Whisky','Whisky',SMALL,[('Stará Myslivecká Reserva','Stará Myslivecká Reserva',None,65),('Glenfiddich 12y','Glenfiddich 12y',None,129),('Laphroaig 10y','Laphroaig 10y',None,149)]),
 ('Likéry','Liqueurs',SMALL,[
  ('Fernet Stock','Fernet Stock',None,55),('Bartida Zelená','Bartida Zelená (herbal)',None,55),('Bartida Hruška','Bartida pear',None,65),
  ('Ratafia Mandlička','Ratafia almond',None,79),('Ratafia Višnička','Ratafia sour cherry',None,79),('Ratafia Jeřabinka','Ratafia rowanberry',None,79)]),
 ('Destiláty','Fruit brandy',SMALL,[('Bartida Slivovice','Bartida plum brandy (slivovice)',None,89)]),
]
JIDLA=[
 ('K pivu doporučujeme','Goes well with beer',None,[
  ('Cyrilovy pekařské tyčky solené',"Cyril's salted bakery sticks",None,45),
  ('Cyrilovy brambůrky',"Cyril's crisps",('solené nebo hořčicové','salted or mustard'),59),
  ('Pikantní utopenec se zelím','Spicy pickled sausage (utopenec) with cabbage',None,109),
  ('Domácí paštika','Homemade pâté',DAILY,119),
  ('Pivní sláma s dipem','Crispy beer straws with dip',None,89)]),
 ('Obložené chleby','Open sandwiches',('na vyžádání i půlka krajíce za poloviční cenu','half a slice available on request at half price'),[
  ('Se škvarkovou pomazánkou','With pork crackling spread',None,89),
  ('S pikantní masovou pomazánkou','With spicy meat spread',None,89),
  ('S tvarůžkovou pomazánkou','With Olomouc tvarůžky cheese spread',None,99),
  ('S roastbeefem','With roast beef',None,159)]),
 ('Teplá kuchyně','Hot dishes',('ke všem pokrmům podáváme pečivo z řemeslné pekárny Klásek','all dishes are served with bread from the Klásek artisan bakery'),[
  ('Hovězí guláš s pečivem','Beef goulash with bread',None,189),
  ('Domácí burger','Homemade burger',DAILY,189),
  ('Bůček Podzemi s limetkovou mayo a pečivem','Podzemi pork belly with lime mayo and bread',None,179)]),
 ('K vínu doporučujeme','Goes well with wine',None,[
  ('Řecké olivy v misce','Greek olives in a bowl',('zelené s česnekem a citrónem, Kalamata nebo speciální pečené olivy','green with garlic and lemon, Kalamata or special roasted olives'),89),
  ('Řecké olivy s domácí focaccií a olivovým olejem','Greek olives with homemade focaccia and olive oil',('zelené s česnekem a citrónem, Kalamata nebo speciální pečené olivy','green with garlic and lemon, Kalamata or special roasted olives'),109),
  ('Mix nakládaných sýrů','Marinated cheese selection',('pro 2 osoby, gouda, hermelín, čedar, sušená rajčata, olivy, česnek','for 2 people, gouda, Hermelín, cheddar, sun-dried tomatoes, olives, garlic'),189),
  ('Salát Caprese s focaccií','Caprese salad with focaccia',None,189),
  ('Domácí plněná focaccia','Homemade filled focaccia',DAILY,189)]),
]
def t(tag,cls,cs,en,extra=''):
    en_attr=f' data-en="{e(en)}"' if en!=cs else ''
    return f'<{tag} class="{cls}"{en_attr}{extra}>{e(cs)}</{tag}>'

NAV='''<header class="nav" id="top">
  <div class="wrap nav__inner">
    <a href="index.html" class="logo"><img src="img/logo.png" alt="" class="logo__img"><span class="logo__text">Pub Podzemi</span></a>
    <nav class="nav__links">
      <a href="jidelni-listek.html" data-en="Food"{food}>Jídlo</a>
      <a href="napojovy-listek.html" data-en="Drinks"{drinks}>Nápoje</a>
      <a href="index.html#galerie" data-en="Gallery">Galerie</a>
      <a href="index.html#o-nas" data-en="About us">O nás</a>
      <a href="index.html#kontakt" data-en="Contact">Kontakt</a>
    </nav>
    <div class="nav__right">
      <div class="lang" role="group" aria-label="Jazyk" data-en-aria-label="Language">
        <button type="button" class="lang__btn" data-lang="cs">CZ</button>
        <button type="button" class="lang__btn" data-lang="en">EN</button>
      </div>
      <a href="tel:+420602211362" class="btn btn--small btn--reserve js-reserve" data-en="Book a table">Rezervace</a>
      <button type="button" class="nav__toggle" aria-label="Otevřít menu" data-en-aria-label="Open menu" aria-expanded="false">☰</button>
    </div>
  </div>
</header>'''

def page(fn,title,lead,data,active,note):
    cats=[]
    for cs,en,sub,items in data:
        rows=[]
        for ncs,nen,nt,p in items:
            note_html=t('span','item__note',nt[0],nt[1]) if nt else ''
            rows.append(f'''
          <li class="item"><span class="item__main">{t('span','item__name',ncs,nen)}{note_html}</span><span class="item__dots" aria-hidden="true"></span>{t('span','item__price',f'{p} Kč',f'CZK {p}')}</li>''')
        sub_html=t('p','cat__sub',sub[0],sub[1]) if sub else ''
        cats.append(f'''
      <section class="cat">
        {t('h2','cat__title',cs,en)}{sub_html}
        <ul class="items">{''.join(rows)}
        </ul>
      </section>''')
    cur=' aria-current="page"'
    nav=NAV.format(food=cur if active=='jidla' else '', drinks=cur if active=='napoje' else '')
    tab=lambda href,cs,en,key: f'<a href="{href}" class="tabs__tab{" is-active" if key==active else ""}" data-en="{en}"{cur if key==active else ""}>{cs}</a>'
    out=f'''<!doctype html>
<html lang="cs">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title data-en="{e(title[1])} – Pub Podzemi">{e(title[0])} – Pub Podzemi</title>
  <meta name="description" content="{e(title[0])} pivnice Pub Podzemi, Údolní 222/5, Brno." data-en-content="{e(title[1])} of Pub Podzemi, Údolní 222/5, Brno.">
  <link rel="icon" href="img/logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Big+Shoulders+Display:wght@600;800&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css?v=20">
</head>
<body>

{nav}

<main class="listek">
  <div class="wrap">
    <a href="index.html" class="back" data-en="Back to the home page">Zpět na hlavní stránku</a>
    {t('h1','listek__title',title[0],title[1])}
    {t('p','listek__lead',lead[0],lead[1])}
    <nav class="tabs" aria-label="Lístky" data-en-aria-label="Menus">
      {tab("jidelni-listek.html","Jídelní lístek","Food menu","jidla")}
      {tab("napojovy-listek.html","Nápojový lístek","Drinks menu","napoje")}
    </nav>
    <div class="listek__grid">{''.join(cats)}
    </div>
    {t('p','listek__note',note[0],note[1])}
  </div>
</main>

<footer class="footer">
  <div class="wrap footer__inner">
    <span class="logo"><img src="img/logo.png" alt="" class="logo__img"><span class="logo__text">Pub Podzemi</span></span>
    <span data-en="Operator: Podnebi s.r.o., Company ID 04577949, Údolní 222/5, 602 00 Brno">Provozovatel: Podnebi s.r.o., IČ 04577949, Údolní 222/5, 602 00 Brno</span>
    <span>© <span class="year"></span></span>
  </div>
</footer>

<script src="main.js?v=20"></script>
</body>
</html>
'''
    open(R+fn,'w').write(out)

page('napojovy-listek.html',('Nápojový lístek','Drinks menu'),
     ('Na čepu Plzeň, Radegast a speciály z pivovaru Kosmix. K tomu vína, Prosecco, drinky i nealko.',
      'On tap: Pilsner Urquell, Radegast and specials from the Kosmix brewery. Plus wines, Prosecco, cocktails and soft drinks.'),
     NAPOJE,'napoje',('Ceny jsou uvedeny v Kč.','Prices are in Czech crowns (CZK).'))
page('jidelni-listek.html',('Jídelní lístek','Food menu'),
     ('Poctivé jídlo k pivu i k vínu. Pečivo z řemeslné pekárny Klásek.',
      'Honest food to go with beer and wine. Bread from the Klásek artisan bakery.'),
     JIDLA,'jidla',('Ceny jsou uvedeny v Kč. Alergeny na vyžádání u obsluhy.','Prices are in Czech crowns (CZK). Ask our staff for allergen information.'))
print('ok')
