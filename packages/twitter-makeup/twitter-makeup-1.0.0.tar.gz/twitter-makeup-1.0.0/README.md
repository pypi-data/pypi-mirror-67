# Make up your Twitter Profile! [python package]

Small library to make up your twitter profile, from 🐴 to 🦄 !

Here is a [dedicated docker service](https://github.com/nidup/twitter-makeup-service) including a scheduler to use it directly without any development work.

You can see it live on my [Twitter profile](https://twitter.com/duponico) 🐦

## Examples 🦄

Example                                         | Result
----------------------------------------------- | ------------------------------
Change the banner for the day                   | ![alt text](./data/banner-morning.jpg "Morning banner")
And the night                                   | ![alt text](./data/banner-night.jpg "Night banner")
Change your display name the morning            | Nico ☕
And during the day                              | Nico 💻
And for the night                               | Nico 😴
Change your location when traveling             | Boston
Change your description when attending an event | Currently at #craftconf, let's have a chat 💬

## Install 📦

```
pip install twitter-makeup
```

## Configure 🛠️

Twitter MakeUp allows to programmatically change your profile on your behalf.

To configure it, you need to generate Twitter credentials.

[Follow the Twitter guide (OAuth 1.0a)](https://developer.twitter.com/en/docs/basics/authentication/overview).

## Use it! 🦄

```python
import tweepy
from twitter_makeup import MakeUp

# Configure Tweepy
consumer_key = 'YourKey'
consumer_secret = 'YourSecret'
access_token = 'YourAccessToken'
access_secret = 'YourAccessSecret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

# Make up your profile 🦄
makeup = MakeUp(api)

# Change your banner 
banner_path = 'images/banner-night.jpg'
makeup.change_banner_picture(banner_path)
print('Banner picture has been changed using "'+ banner_path + '" 🦄')

# Change your profile picture
profile_path = 'images/profile-weekend.jpg'
makeup.change_profile_picture(profile_path)
print('Profile picture has been changed using "'+ profile_path + '" 🦄')

# Change your profile name
profile_name = 'Nicolas Dupont ☕'
makeup.change_profile_name(profile_name)
print('Profile name has been changed by "' + profile_name + '" 🦄')

# Change your profile location
profile_location = 'Nantes'
makeup.change_profile_location(profile_location)
print('Profile location has been changed by "' + profile_location + '" 🦄')

# Change your profile description
profile_description = "Co-founder and CPO at @akeneopim\
\n❤️ crafting products to create value for users and businesses\
\n💬 and 📝 about product, engineering, teamwork, learnings"
makeup.change_profile_description(profile_description)
print('Profile description has been changed by "' + profile_description + '" 🦄')
```

## License

[MIT](LICENSE)

## Third party

This library uses the excellent [Tweepy](https://www.tweepy.org/), providing a wrapper around a small subset of Tweepy capabilities.
