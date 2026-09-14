from collections import defaultdict, deque
import heapq

class Twitter:

    followMap: dict
    tweetMap: dict
    time: int

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # plan: get the last 10 tweets from every followed user + self
        # which is O(n)
        # then sort for O(nlogn)
        users = set(self.followMap[userId])
        users.add(userId)
        max_heap = []
        for user in users:
            tweets = self.tweetMap[user]
            if tweets:
                idx = len(tweets) - 1
                time, tweet_id = tweets[idx]
                heapq.heappush(max_heap, (-time, tweet_id, user, idx - 1))

        feed = []
        while max_heap and len(feed) < 10:
            neg_time, tweet_id, user, next_idx = heapq.heappop(max_heap)
            feed.append(tweet_id)
            if next_idx >= 0:
                t, tid = self.tweetMap[user][next_idx]
                heapq.heappush(max_heap, (-t, tid, user, next_idx - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
