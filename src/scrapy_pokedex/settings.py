# Scrapy settings for scrapy_pokedex project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from typing import Dict

# Custom config entries
SPIDER = "pokedex_list"
ENABLE_DEBUG: bool = False
MAX_ROWS: int | None = 50
DEFAULT_OUTPUT: bool = False

# Scrapy settings
BOT_NAME = "scrapy_pokedex"
SPIDER_MODULES: list[str] = ["scrapy_pokedex.spiders"]
NEWSPIDER_MODULE = "scrapy_pokedex.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "scrapy_pokedex (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 10
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES: Dict[str, int | None] = {
    "scrapy_pokedex.middlewares.ScrapyPokedexSpiderMiddleware": 543,
}

# User-Agent randomization
RANDOM_UA_PER_PROXY = True
RANDOM_UA_TYPE = "random"
RANDOM_UA_SAME_OS_FAMILY = False

# Proxy randomization
PROXY_LIST = "proxies.txt"
# Proxy mode
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and assign it to every requests
# 2 = Put a custom proxy to use in the settings
PROXY_MODE = 0
# Retry many times since proxies often fail
RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES: Dict[str, int | None] = {
    "scrapy_pokedex.middlewares.ScrapyPokedexDownloaderMiddleware": 543,
    "scrapy_user_agents.middlewares.RandomUserAgentMiddleware": 400,
    "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 110,
    "scrapy_proxies.RandomProxy": 100,
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": 90,
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS: Dict[str, int | None] = {
    "scrapy.extensions.telnet.TelnetConsole": None,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES: Dict[str, int | None] = {
    "scrapy_pokedex.pipelines.ScrapyPokedexPipeline": 300,
    "scrapy.pipelines.files.FilesPipeline": 200,
    "scrapy.pipelines.images.ImagesPipeline": 100,
}

# Media pipeline settings
FILES_STORE = "./scrapy_pokedex/data/output/files"
FILES_EXPIRES = 90

IMAGES_STORE = "./scrapy_pokedex/data/output/images"
IMAGES_EXPIRES = 90
IMAGES_THUMBS = {
    "small": (50, 50),
    "big": (270, 270),
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 0.5
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 60 * 15
HTTPCACHE_DIR = "httpcache"
HTTPCACHE_IGNORE_HTTP_CODES: list[str | int] = []
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Enable and configure logging
# See https://docs.scrapy.org/en/latest/topics/logging.html
LOG_ENABLED = False

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
