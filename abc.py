import feedparser

# Fetch the feed with posts mentioning "gpt" and having at least 37 points
feed_url = "https://hnrss.org/newest?q=indie-hackers&points=92"
feed = feedparser.parse(feed_url)

# Extract the link of the latest post
if feed.entries:
    print(feed.entries[0].link)  # Print the link of the latest post