import random
import copy

class Group:

    def __init__(self,codes,groups,grouping):
        self.codes = codes
        self.groups = groups
        if grouping == None:
            self.grouping = self.random_grouping(codes,groups)
        else:
            self.grouping = grouping

    def random_grouping(self,codes,groups):
        grouping = {}
        for code in codes:
            grouping[code] = random.choice(groups)
        return grouping

    def reassign(self,n):
        grouping = copy.deepcopy(self.grouping)
        keys = random.sample(self.grouping.keys(),n)
        for key in keys:
            candidate_group = random.choice(self.groups)
            while candidate_group == grouping[key]:
                candidate_group = random.choice(self.groups)
            grouping[key] = candidate_group
        return grouping
