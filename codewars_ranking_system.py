class User():
    def __init__(self):
        self.ranks = [i for i in range(-8, 9) if i != 0]
        self.progress = 0
        self.rank = -8
        self.curr = self.ranks.index(self.rank)
        self.completed = None

    def inc_progress(self, r):
        self.curr = self.ranks.index(self.rank)
        self.completed = self.ranks.index(r)
        if not self.completed - self.curr <= -2:
            self.calculate_progress()

    def calculate_progress(self):
        diff = self.completed - self.curr
        if not diff:
            self.progress += 3
        elif diff == -1:
            self.progress += 1
        else:
            self.progress += 10 * diff * diff
        if self.progress >= 100:
            self.progress_made()

    def progress_made(self):
        rank_up, rem = divmod(self.progress, 100)
        self.curr += rank_up
        self.rank = self.ranks[self.curr]
        self.progress = rem
