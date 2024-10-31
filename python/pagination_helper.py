class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.count = len(collection)
        self.pages = len(collection) // items_per_page
        self.items_per_page = items_per_page
        if (rest := len(collection) % items_per_page) != 0:
            self.pages += 1
            self.rest = rest
        else:
            self.rest = self.items_per_page

    def item_count(self):
        return self.count

    def page_count(self):
        return self.pages

    def page_item_count(self, page_index):
        if (page_index + 1) > self.pages or page_index < 0:
            return -1
        if (page_index + 1) < self.pages:
            return self.items_per_page
        else:
            return self.rest

    def page_index(self, item_index):
        if item_index + 1 > self.count or item_index < 0:
            return -1
        return ((item_index + self.items_per_page) // self.items_per_page) - 1
