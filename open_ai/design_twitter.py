# https://leetcode.com/problems/design-twitter/

from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> list of (time, tweetId)
        self.following = defaultdict(set)    # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

    # Could also merge k sorted lists...
    def getNewsFeed(self, userId: int) -> List[int]:
        # include the user's own tweets plus everyone they follow
        users = self.following[userId] | {userId}
        candidates = []

        for uid in users:
            candidates += self.tweets[uid][-10:]
        
        # 10 most recent by timestamp
        top = heapq.nlargest(10, candidates, key=lambda t: t[0])

        result = []
        for tweet in top:
            result.append(tweet[1])

        return result

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
