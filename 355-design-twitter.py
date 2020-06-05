# 355. Design Twitter

# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and 
# is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. 
# Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.
# Example:

# Twitter twitter = new Twitter();

# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);

# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);

# // User 1 follows user 2.
# twitter.follow(1, 2);

# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);

# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.getNewsFeed(1);

# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);

# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);


class Tweet:
    # static variable
    timestamp = 0

    def __init__(self, tid, time):
        self.id = tid
        self.time = time
        self.next = None

class User:
    def __init__(self, uid):
        self.id = uid
        self.following = set()
        self.head_tweet = None
        # follow myself
        self.follow(uid)

    def follow(self, uid):
        self.following.add(uid)

    def unfollow(self, uid):
        # 不可以取关自己
        if uid != self.id and uid in self.following:
            self.following.remove(uid)

    def post(self, tid):
        tweet = Tweet(tid, Tweet.timestamp)
        Tweet.timestamp += 1
        # 将新建的推文插入链表头
        # 越靠前的推文 time 值越大
        tweet.next = self.head_tweet
        self.head_tweet = tweet

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users_dic = {}
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.users_dic:
            self.users_dic[userId] = User(userId)

        user = self.users_dic[userId]
        user.post(tweetId)

    # merge k sorted list
    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. 
        Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        result = []
        if userId not in self.users_dic:
            return result
        # 关注列表的用户 Id
        heap = []
        for i, uid in enumerate(self.users_dic[userId].following):
            head_tweet = self.users_dic[uid].head_tweet
            if head_tweet:
                heapq.heappush(heap, (-head_tweet.time, head_tweet))
        while heap:
            if len(result) == 10:
                break
            time, tweet = heapq.heappop(heap)
            result.append(tweet.id)
            if tweet.next:
                next_tweet = tweet.next
                heapq.heappush(heap, (-next_tweet.time, next_tweet))
        return result

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        # 若 followee 不存在，则新建
        if followerId not in self.users_dic:
            self.users_dic[followerId] = User(followerId)
        # 若 follower 不存在，则新建
        if followeeId not in self.users_dic:
            self.users_dic[followeeId] = User(followeeId)

        follower = self.users_dic[followerId]
        follower.follow(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return

        if followerId not in self.users_dic:
            self.users_dic[followerId] = User(followerId)

        if followeeId not in self.users_dic:
            self.users_dic[followeeId] = User(followeeId)

        follower = self.users_dic[followerId]
        follower.unfollow(followeeId)