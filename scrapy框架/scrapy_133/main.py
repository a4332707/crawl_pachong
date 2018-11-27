#配置命令行信息
from scrapy import  cmdline #使用cmdline模块配置运行信息
# cmdline.execute(['scrapy','crawl','bd'])
# cmdline.execute('scrapy crawl bd'.split())
# cmdline.execute('scrapy crawl zl'.split())
# cmdline.execute('scrapy crawl zph'.split())
# cmdline.execute('scrapy crawl headers'.split())
# cmdline.execute('scrapy crawl proxy'.split())
# cmdline.execute('scrapy crawl wb'.split())
cmdline.execute('scrapy crawl lagouwang'.split())



