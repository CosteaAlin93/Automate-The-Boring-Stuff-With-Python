import bs4, requests

def getAmazonPrice(producUrl):
    res = requests.get(producUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elements = soup.select('html.doc-desktop body div.main-container-outer div.main-container-inner div#main-container.main-container section.page-section.page-section-light div.container div.row div.col-sm-5.col-md-7.col-lg-7 div.product-highlights-wrapper div.row div.col-sm-12.col-md-6.col-lg-5 form.main-product-form div.product-highlight.product-page-pricing div div.d-inline-flex.justify-space-between.w-100 div.pricing-block.has-installments p.product-new-price')
    return elements[0].text.strip()

price = getAmazonPrice('https://www.emag.ro/trotineta-electrica-xiaomi-mi-pro-2-putere-motor-300-w-autonomie-45-km-viteza-maxima-25-km-h-negru-fbc4025gl/pd/D94003MBM/?ref=hdr-favorite_products')
print('The price is ' + price)