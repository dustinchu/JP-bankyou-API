from bs4 import BeautifulSoup
import requests
from utf.jpUnicode import Japanese
import json



class NewsBodyPlayUrlModel():
    def getPlayUrl(pageUrl):
        r = requests.get("https://www3.nhk.or.jp/news/easy/"+pageUrl+"/"+pageUrl+".html")
        if r.status_code != 200:
            return {'message': 'Html get !=200 error '}, 404
        r.encoding = 'utf-8'
        # print(r.text)
        soup = BeautifulSoup(r.text, "lxml")
        # print(soup)
        # 字串判斷使用
        isJp = 0
        # 寸內容
        bodyStr = ""

        for post in soup.find_all("article", "article-main"):
            # print(post)
            for body in post.find_all("div", "article-main__body article-body"):
                for bodyText in body.strings:
                    if bodyText != "\n":
                        # 將字串分割
                        if Japanese.is_japanese(bodyText):
                            # 是漢字的話漢字後面加上&
                            bodyStr += bodyText + "&"
                            isJp = 1
                        else:
                            # 如果上一筆是漢字isJp=1  結束要加上空白
                            if isJp == 1:
                                isJp = 0
                                bodyStr += bodyText + " "
                            # 如果isJp=0 代表前面沒漢字　不需要加空白　不=0的話 代表前面有漢字 將is存成2
                            else:
                                bodyStr += bodyText + " "

        return {'bodyText': bodyStr}

