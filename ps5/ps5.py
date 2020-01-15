# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
            # pubdate = pubdate.astimezone(pytz.timezone('Asia/Taipei'))
            # pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate

    

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """     
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PharseTrigger(Trigger):
    def __init__(self, phrase):
        super().__init__()
        self.phrase = phrase.lower().strip(string.punctuation)      # format phrase

    def evaluate(self, story):
        return super().evaluate(story)

    def is_phrase_in(self, text):
        text = text.lower()       # format text

        for i in string.punctuation:        # replace punctuation with space
            text = text.replace(i, ' ')
        
        text = text.split()       # string to list of words
        words_valid_check = True        # check if every word in phrase is in text list or not

        for i in self.phrase.split():       
            if i in text:
                continue
            else:
                words_valid_check = False
                break

        text = ' '.join(text)     # formatted string of text

        if self.phrase in text and words_valid_check:      # if words in phrase are all valid and are consecutive, trigger
            return True
        else:       # else, don't trigger
            return False

# Problem 3
class TitleTrigger(PharseTrigger):
    def __init__(self, phrase):
        super().__init__(phrase)

    def evaluate(self, story):      # substitute evalute function
        title = story.get_title()       # get title of the NewsStory instance
        return super().is_phrase_in(title)      # check if self.phrase is in title

# Problem 4
class DescriptionTrigger(PharseTrigger):
    def __init__(self, phrase):
        super().__init__(phrase)

    def evaluate(self, story):      # similar to TitleTrigger's evaluate function
        description = story.get_description()
        return  super().is_phrase_in(description)

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self, triggertime):
        super().__init__()
        self.triggertime = datetime.strptime(triggertime, "%d %b %Y %H:%M:%S").replace(tzinfo=pytz.timezone('EST'))     # string to datetime and add timezone info

# Problem 6
# TODO: read https://docs.python.org/3.5/library/datetime.html# and correct problem 6
class BeforeTrigger(TimeTrigger):
    def __init__(self, triggertime):        # TimeTrigger's constructor
        super().__init__(triggertime)

    def evaluate(self, story):
        pubdate = story.get_pubdate()       # get pubdate from NewsStory instance
        if pubdate.tzinfo == None:      # if pubdate doesn't have timezone attribute
            pubdate = pubdate.replace(tzinfo=pytz.timezone('EST'))      # set it to EST
        return pubdate < self.triggertime       # if pubdate is befoer self.triggertime, triggers

class AfterTrigger(TimeTrigger):
    def __init__(self, triggertime):        # TimeTrigger's constructor
        super().__init__(triggertime)

    def evaluate(self, story):      # similar to BeforeTrigger's evaluate fucntion
        pubdate = story.get_pubdate()
        if pubdate.tzinfo == None:
            pubdate = pubdate.replace(tzinfo=pytz.timezone('EST'))
        return pubdate > self.triggertime

# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, trigger):        # NotTrigger takes a trigger as an input
        super().__init__()
        self.trigger = trigger

    def evaluate(self, story):      # and reverse its evaluate function's result
        return not self.trigger.evaluate(story)

# Problem 8
class AndTrigger(Trigger):
    def __init__(self, trigger_1, trigger_2):       # AndTrigger takes two triggers as inputs
        super().__init__()
        self.trigger_1 = trigger_1
        self.trigger_2 = trigger_2
    
    def evaluate(self, story):      # and fires when two input triggers fire
        return self.trigger_1.evaluate(story) and self.trigger_2.evaluate(story)

# Problem 9
class OrTrigger(Trigger):       # OrTrigger takes two triggers as inputs
    def __init__(self, trigger_1, trigger_2):
        super().__init__()
        self.trigger_1 = trigger_1
        self.trigger_2 = trigger_2

    def evaluate(self, story):      # and fires when either or both of the trigger fire
        return self.trigger_1.evaluate(story) or self.trigger_2.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filtered_stories = []       # create empty list of stories after filter
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):     # if any of the trigger in triggerlist triggers, add it to filtered_stories and end the iteration over triggerlist
                filtered_stories.append(story)
                break
            else:
                continue
    return filtered_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

