import sys
from base64 import b64encode as be
import requests
import urllib.parse
import json
import datetime
import re

from md5gen import md5Generator


owner = 'your_username'
repo = 'the_repo_name_you_just_created'  # your image repository name
path = 'path/'+datetime.date.today().strftime('%y-%m-%d')  # /repo_name/path/xxx.jpg
token = 'dont leak it!!!'  # you access token
baseUrl = 'https://gitee.com/api/v5/repos'  # api format
message = 'add a pic'  # commit message
repoUrl = 'http://gitee.com/'+owner+'/'+repo+'blob/master/'+path
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8'
}


def getSuffix(fileDir):
    res = re.search('\..*', fileDir).span()
    if res is None:
        return '.jpg'
    else:
        return fileDir[res[0]:res[1]]


def urlGenerator(baseUrl, owner, repo, path, pictureName):
    return baseUrl+'/'+owner+'/'+repo+'/contents/'+path+'/'+pictureName


def main():
    params = []
    for p in sys.argv:
        params.append(urllib.parse.unquote(p, 'utf8'))

    params.__delitem__(0)

    for file in params:
        try:
            with open(file, 'rb') as f:
                # pic -> base64
                # postdata format -
                # {
                #   'access_token': token,'content':base64,'message':'...'
                # }
                # must have this fields
                #
                fileStream=f.read()
                picContent = be(fileStream)
                data = {
                    'access_token': token,
                    'content': picContent,
                    'message': message
                }
                """ print('request body:\naccess_token:%s message:%s' %
                    (data['access_token'], data['message'])) """
                picName = md5Generator(fileStream)+getSuffix(file)  # generate file name by md5
                # postUrl - https://gitee.com/api/v5/repos/{owner}/{repo}/contents/{path}/filename.xxx
                url = urlGenerator(baseUrl=baseUrl, owner=owner,
                                   repo=repo, path=path, pictureName=picName)
                #print('url is ', url)
                res = requests.post(url, data)
                responseBody = json.loads(res.text)  # parse json to object
                if res.status_code == 201 or res.status_code == 200:
                    print(responseBody['content']['download_url'])
                elif responseBody['message'] == 'A file with this name already exists':
                    # the fucking gitee will send 400 bad request and don't send anything(even existing file's url) if 
                    # the file had been existed
                    print('https://gitee.com/'+owner+'/'+repo +
                          '/'+'raw/master/'+path+'/'+picName)
                f.close()
        except:
            print('fuck,what happend? 💩')


if __name__ == '__main__':
    main()
