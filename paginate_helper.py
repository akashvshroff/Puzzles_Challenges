class PaginationHelper:

    def __init__(self, collection, items_per_page):
        # The constructor takes in an array of items and a integer indicating
        # how many items fit within a single page
        self.arr = collection
        self.per_page = items_per_page
        self.num_items = len(collection)
        self.num_p, self.rem = divmod(self.num_items, self.per_page)

    def item_count(self):
        # returns the number of items within the entire collection
        return self.num_items

    def page_count(self):
        # returns the number of pages
        return self.num_p + 1

    def page_item_count(self, page_index):
        # returns the number of items on the current page. page_index is zero based
        # this method should return -1 for page_index values that are out of range
        if not 0 <= page_index <= self.num_p:
            return -1
        if page_index == self.num_p:
            return self.rem
        return self.per_page

    def page_index(self, item_index):
        # determines what page an item is on. Zero based indexes.
        # this method should return -1 for item_index values that are out of range
        if not 0 <= item_index < self.num_items:
            return -1
        return item_index//self.per_page
