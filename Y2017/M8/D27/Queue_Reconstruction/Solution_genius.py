# Runtime: 118ms
# Reference: https://discuss.leetcode.com/topic/60981/explanation-of-the-neat-sort-insert-solution
def reconstructQueue(self, people):
    people.sort(key=lambda h, k: (-h, k))
    queue = []
    for p in people:
        queue.insert(p[1], p)
    return queue