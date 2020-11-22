from instapy import InstaPy
#creating session uisng password and email id
session = InstaPy(username="waseem.ali404",
                  password="Junglebook2@").login()
# for running the bot with out browser gui use this one
#session = InstaPy(username='test', password='test', headless_browser=True)
#setting the session to like 100 post randomly,  setting unfollow to false
session.like_by_tags(['Karachi', 'Lahore','Islamabad','Modeling','showbiz','lifestyle','tourism '], amount=20)
#dont like posts with such tags
session.set_dont_like(["naked", "nsfw"])
#like posts from new feed also
session.like_by_feed(amount=100, randomize=False, unfollow=False, interact=False)
#incase you wnat the bot to follow some accounts
#session.set_do_follow(enabled=True, percentage=10, times=2)
#session.set_relationship_bounds(enabled=True, max_followers=8500)
#setting comment percentage to 80 persent
session.set_do_comment(True, percentage=80)
#comments are picked up form this array
session.set_comments(["Nice!", "stunning!", "Beautiful :heart_eyes:"])
# setting the limit of the bot , so the peak like in an hour should not exceed the
#limit , otherwise instagram will know and block the account
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
#ending the session
session.end()