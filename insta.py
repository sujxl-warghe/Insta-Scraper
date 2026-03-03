# Import instaloader package
import instaloader

# Creating an Instaloader object
ig = instaloader.Instaloader()

# Taking the Instagram username as input from user
usrname = input("Enter username: ")

# Fetching the details of provided username using Instaloader object
profile = instaloader.Profile.from_username(ig.context, usrname)

# Printing the fetched details
print("Username:", profile.username)
print("Number of Posts Uploaded:", profile.mediacount)
print(profile.username + " is having " + str(profile.followers) + " followers.")
print(profile.username + " is following " + str(profile.followees) + " people")
print("Bio:", profile.biography)

# Downloading profile picture
instaloader.Instaloader().download_profile(
    usrname,
    profile_pic_only=True
)
