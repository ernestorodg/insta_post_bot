# Instagram bot using Instapy

from instapy import InstaPy

def get_login():
	login_file = open('user.txt','r') 
	login = login_file.readline().split(':')
	user = login[0]
	password = login[1][0:-1]
	login_file.close()
	return (user, password)

user, password = get_login()

session = InstaPy(username=user, password=password)
session.login()

# Giving likes by hashtags
session.like_by_tags(["bmw", "mercedes"], amount=5)
# Avoid some hashtags
session.set_dont_like(["naked", "nsfw"])
# Follow a percentage from the liked fotos
session.set_do_follow(True, percentage=50)
# Set a comment to half of the liked fotos
session.set_do_comment(True, percentage=50)
# List with comments
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])

session.end()
