from data.link import datalink
from empresas.ads import ads

empresas = {}

for key, values in datalink.items():
    page = values['page']
    link = values['link']
    template = values['template']


    if key == 'empresa2':
        compani = ads(page, template)
  
    
    empresas[key] = {
        'page': page,
        'rout': link,
        'template': template,
        'compani': ads(page, template)
    }
