import praw

# authenticate
reddit = praw.Reddit(
    client_id="clientID",
    client_secret="clientSecret",
    password="lastpass",
    user_agent="can be anything",
    username="username",
)

# make sure it's us
print(reddit.user.me())

newpost = reddit.subreddit("subreddit").submit("subreddit text")