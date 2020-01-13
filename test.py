import string
a = 'purple co?@!#w'
b = 'this is a purple%#$%@%%cow'
for i in string.punctuation:
    (a, b) = (a.replace(i, ''), b.replace(i, ' '))
print(string.punctuation)

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
        self.phrase = phrase.lower().strip(string.punctuation)

    def evaluate(self, story):
        story = story.lower()

        for i in string.punctuation:
            story = story.replace(i, ' ')
        
        story = story.split()
        words_valid_check = True

        for i in self.phrase.split():
            if i in story:
                continue
            else:
                words_valid_check = False
                break
        
        story = ' '.join(story)

        if self.phrase in story and words_valid_check:
            return True
        else:
            return False

a = PharseTrigger('purple cow')
print(a.evaluate('purple@#$%cows'))
