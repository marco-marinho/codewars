class User:
    
    ranks = {-8: 0, -7:1, -6:2, -5:3, -4:4, -3:5, -2:6, -1:7, 1:8, 2:9,
            3:10, 4:11, 5:12, 6:13, 7:14, 8:15}
    
    def __init__(self):
        self.rank = -8
        self.progress = 0
       
    def inc_progress(self, rank):
        diff = User.ranks[rank]-User.ranks[self.rank]
        if diff<=-2:
            return
        elif diff == -1:
            self.progress += 1  
        elif diff == 0:
            self.progress += 3
        else:
            self.progress += 10 * diff * diff
        self.update_rank()
      
    def update_rank(self):
        while self.progress >= 100 and self.rank < 8:
            if self.rank == -1: 
                self.rank = 1
            else:
                self.rank += 1
            self.progress -= 100   
        if self.rank == 8:
            self.progress = 0