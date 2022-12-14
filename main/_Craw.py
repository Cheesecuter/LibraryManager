import requests
import re
import time
import csv
import _FrozenDir
import _Database


class Craw:
    def __init__(self, db):
        self._db = db
        self.srcPath = _FrozenDir.app_path()+r'\\src'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
        }
        pass

    def _craw(self):
        self.bookNo = 1
        for it in range(1, 5):
            try:
                self._crawPages(it)
                time.sleep(1)
            except Exception as e:
                pass

    def _crawPages(self, pageNum):
        _url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-" + \
            str(pageNum)
        response = requests.get(_url, headers=self.headers)
        response.encoding = 'gbk'
        csvPath = self.srcPath+r'\\books.csv'
        pageContent = response.text
        pageContent.encode().decode
        obj = re.compile(
            r'.*?<div class="name">.*?<a href=".*?"'
            r'.*?target="_blank".*?title="(?P<bookName>.*?)">'
            r'.*?<div class="publisher_info">'
            r'.*?title="(?P<authorName>.*?)"'
            r'.*?<div class="publisher_info">'
            r'.*?<span>(?P<publishDate>.*?)</span>&nbsp;'
            r'.*?target="_blank">(?P<publisher>.*?)</a></div>'
            r'.*?<div class="price">'
            r'.*?<span class="price_r">&yen;(?P<price>.*?)</span>', re.S
        )
        result = obj.finditer(pageContent)
        f = open(csvPath, mode="a", encoding="UTF-8-SIG")
        csvWtriter = csv.writer(f)
        for it in result:
            print("----------------------------------------------")
            print(it.group("bookName"))
            print(it.group("authorName"))
            print(it.group("publishDate"))
            print(it.group("publisher"))
            print(it.group("price"))
            dic = it.groupdict()
            print(type(dic))
            csvWtriter.writerow(dic.values())
            self._db._InitBooksData(str('%06d' % self.bookNo),
                                    it.group("bookName"),
                                    it.group("authorName"),
                                    it.group("publisher"),
                                    it.group("publishDate"),
                                    it.group("price"))
            self.bookNo = self.bookNo+1
        f.close()
