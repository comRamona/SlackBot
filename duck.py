import unirest
import re
import duckduckgo


def findImage(img=""):
    key=""
    theurl="https://duckduckgo-duckduckgo-zero-click-info.p.mashape.com/?callback=process_duckduckgo&format=json&no_html=1&no_redirect=1&q=%s&skip_disambig=1" % (img)
    response = unirest.get(theurl,
      headers={
        "X-Mashape-Key": key,
        "Accept": "application/json"
      }
    )
    response_text=response.body
    p=re.compile(r'(Image\":\")(.*)(\",\"ImageIsLogo)')
    m=p.search(response_text)
    res=m.group(2)
    if len(res)<2:
        p=re.compile(r'(http[^\"]*((\.png)|(\.jpg)))')
        m=p.search(response_text)
        if(m!=None):
            res=m.group()
        else:
            r=duckduckgo.query(img)
            if r.related and hasattr(r.related[0],'text'):
                            res=r.related[0].text
            elif r.results and hasattr(r.results[0],'text'):
                       res=r.results[0].text
            else:
                res=duckduckgo.get_zci(img)

    return res
