#!/bin/python3 
import instaloader

# creating an Instaloader() object
ig=instaloader.Instaloader()


def grab_info():
   # Taking the instagram username as input from user
    #Fetching the details of provided useraname using instaloder object
    username=input("Enter an IG username: ")

    profile=instaloader.Profile.from_username(ig.context, username)

    # Printing the fetched details and storing the profile pic of that account
    print("Username: ", profile.username)
    print("Number of Posts Uploaded: ", profile.mediacount)
    print(profile.username+" currently has " + str(profile.followers)+' followers.')
    print(profile.username+" is following " + str(profile.followees)+' people')
    print("Bio: ", profile.biography)

    instaloader.Instaloader().download_profile(username,profile_pic_only=True)

grab_info()

