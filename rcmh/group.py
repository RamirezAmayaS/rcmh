import random

class Group:

    def __init__(self,codes,groups):
        self.codes = codes
        self.groups = groups
        self.grouping = self.random_grouping(codes,groups)

    def random_grouping(self,codes,groups):
        grouping = {}
        for code in codes:
            grouping[code] = random.choice(groups)
        return grouping

    def reassign(n):
        keys = random.sample(self.grouping.keys(),n)
        for key in keys:
            candidate_group = random.choice(groups)
            while candidate_group == self.grouping[key]:
                candidate_group = random.choice(groups)
            self.grouping[key] = candidate_group
