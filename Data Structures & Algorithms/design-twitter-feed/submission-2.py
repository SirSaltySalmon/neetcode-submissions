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
        heap_tweets = []

        for user in users:
            tweets_to_attempt = self.tweetMap[user][-10:]
            for tweet in tweets_to_attempt:
                if len(heap_tweets) < 10:
                    heapq.heappush(heap_tweets, tweet)
                else:
                    heapq.heappushpop(heap_tweets, tweet)

        res = deque()
        while heap_tweets:
            tweet = heapq.heappop(heap_tweets)
            res.appendleft(tweet[1])

        return list(res)

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
