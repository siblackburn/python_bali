from typing Iterable, Tuple
import queue


class CrawlerItem:

    def __init__(self, url, depth):
        self.url = url
        self.depth = depth


class Crawler:

    def __init__(self, initial_url, max_depth):
        self.initial_url = initial_url
        self.max_depth = max_depth
    
    def crawl(self) -> Iterable[Tuple[str, str]]:
        results = list()

        processing_queue = queue.Queue()
        processing_queue.put(CrawlerItem(self.initial_url, 1))
        while not processing_queue.empty() > 0:
            item = processing_queue.get()
            url = item.url

            if item.depth < self.max_depth:
                # PROCESS CURRENT ITEM
                # DOWNLOAD THE PAGE
                # GET NEW LINKS
                new_links = [...]
                for link in new_links:
                    results.append((url,link))


                    processing_queue.put(CrawlerItem(link, item.depth + 1))



        return results


def my_method():
    if ...
        return 0
