from collections import defaultdict
class Twitter:

    followMap: dict
    tweetMap: dict
    time: int

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # plan: get the last 10 tweets from every followed user + self
        # which is O(n)
        # then sort for O(nlogn)
        users = set(self.followMap[userId])
        users.add(userId)
        all_tweets = []

        for user in users:
            all_tweets.extend(self.tweetMap[user][-10:])
        
        all_tweets = sorted(all_tweets, reverse=True)
        res = [tweet[1] for tweet in all_tweets[:10]]
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
