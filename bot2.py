import praw
import time
import re
cn_string=re.compile('chicken nugget', re.I)
trump_string=re.compile(' trump ', re.I)
reddit = praw.Reddit(client_id="T4d76_k_xajueg",
                     client_secret="7N4RtEPAhdcJ8cpPvxDGbxLi_ZercA",
                     password="ydaRiTs84!",
                     user_agent="testbot by u/churchofbabyyoda420",
                     username="churchofbabyyoda420")
reddit_user = reddit.user.me()
selftext_count = 0
notext_count = 0
while True:
    post=True
    print("******************************************************************************************************************************************************")
    subreddit = reddit.subreddit("all")
    try:
        for submission in subreddit.stream.submissions():
            #print('Subreddit:',submission.subreddit)
            if submission.subreddit.over18:
                try:
                    f = open("nsfw.log", "r")
                    known_nsfw = f.read()
                except:
                    print("Could not open file")
                finally:
                    f.close()
                if str(submission.subreddit) not in known_nsfw:
                    f = open("nsfw.log","a")
                    f.write(str(submission.subreddit))
                    f.write("\n")
                    f.close()
            if submission.selftext:
                #print('Self Text:', submission.selftext)
                selftext_count = selftext_count + 1
            else:
                notext_count = notext_count + 1
            if (cn_string.search(submission.selftext) or cn_string.search(submission.title)):
                submission.reply("Fan of chicken nuggets I am.  Herh herh herh.")
                print("Nuggets:",submission.permalink)
            if (trump_string.search(submission.selftext) or trump_string.search(submission.title)):
                submission.reply("The dark side clouds everything. Impossible to see the light, the future is.")
                print("Trump", submission.permalink)
            if selftext_count % 100 == 0 or notext_count % 100 == 0:
                print("Self-Text:",selftext_count)
                print("No-text:",notext_count)
    except KeyboardInterrupt as e:
        print("Stopping due to KeyboardInterrupt")
        print(e)
        exit(0)
    except BaseException as e:
        print("Something went wrong, continuing")
        print(str(e.__doc__))
