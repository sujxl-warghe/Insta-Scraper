# Instagram Advanced Analyzer
import os
import instaloader
from dotenv import load_dotenv
from collections import Counter

# Load .env file
load_dotenv()

INSTA_USER = os.getenv("INSTA_USERNAME")
INSTA_PASS = os.getenv("INSTA_PASSWORD")

ig = instaloader.Instaloader()

# Login using .env credentials
ig.login(INSTA_USER, INSTA_PASS)

print("=== Instagram Advanced Analyzer ===")
username = input("Enter Instagram Username: ")

try:
    profile = instaloader.Profile.from_username(ig.context, username)

    print("\n--- Profile Info ---")
    print("Username:", profile.username)
    print("Followers:", profile.followers)
    print("Following:", profile.followees)
    print("Posts:", profile.mediacount)
    print("Private:", profile.is_private)
    print("Verified:", profile.is_verified)
    print("Bio:", profile.biography)

    # Analytics
    total_likes = 0
    total_comments = 0
    hashtags = []
    count = 0

    for post in profile.get_posts():
        total_likes += post.likes
        total_comments += post.comments
        if post.caption:
            hashtags.extend([tag for tag in post.caption.split() if tag.startswith("#")])
        count += 1
        if count == 20:
            break

    print("\n--- Analytics (Last 20 Posts) ---")
    print("Avg Likes:", total_likes // count)
    print("Avg Comments:", total_comments // count)

    print("\nTop Hashtags:")
    for tag, freq in Counter(hashtags).most_common(10):
        print(tag, freq)

except Exception as e:
    print("❌ Error:", e)
