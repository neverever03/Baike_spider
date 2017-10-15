class UrlManager(object):
    def __init__(self):
        self.new_urls = set()#待爬取
        self.old_urls = set()#已爬取

    # 1向管理器中添加url
    def add_new_url(self, url):
        if url is None:
            return
        # 当url既不在待爬取url列表中也不在已爬取的列表中时，则将其添加到新的url——set()集合中
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 2判断是否还有待爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    #3批量添加
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)


    #4获取待爬取的url
    def get_new_url(self):
        #获取并移除
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url