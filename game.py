"""
This is the "game" module.

The game module supplies the store data for each word user played with.
"""
class game:
    """
    dictionary for storing data of each letter value.
    """
    points = {
        "a": 8.17,
        "b": 1.49,
        "c": 2.78,
        "d": 4.25,
        "e": 12.70,
        "f": 2.23,
        "g": 2.02,
        "h": 6.09,
        "i": 6.97,
        "j": 0.15,
        "k": 0.77,
        "l": 4.03,
        "m": 2.41,
        "n": 6.75,
        "o": 7.51,
        "p": 1.93,
        "q": 0.10,
        "r": 5.99,
        "s": 6.33,
        "t": 9.06,
        "u": 2.76,
        "w": 0.98,
        "v": 2.36,
        "x": 0.15,
        "y": 1.97,
        "z": 0.07
    }

    ud_score = 0
    def __init__(self,number,word):
        """
        This is initial  values in constructor
        """
        self.number = number
        self.word = word
        self.status = "PROCESSING"
        self.bad_guess = 0
        self.missed_letters = 0
        self.score = 0
        self.ud_letters = word
        for letter in word:
            self.score = self.score + self.points.get(letter)

    def getWord(self):
        """
        get word value
        """
        return self.word

    def getStatus(self):
        """
        get status value
        """
        return self.status

    def getBad_guess(self):
        """
        get bad guess value
        """
        return self.bad_guess
    def getUd_score(self):
        """
        get score for undiscover letters
        """
        for letter in self.ud_letters:
            self.ud_score = self.ud_score + self.points.get(letter)

    def getMissed_letters(self):
        """
        get missed_letters
        """
        return self.missed_letters

    def getScore(self):
        """
        get  current score
        """
        return self.score

    def setScore(self, vlaue):
        """
        set  current score
        """
        self.score = self.score - value

    def setStatus(self, status):
        """
        set  current status
        """
        self.status = status

    def setBad_guess(self):
        """
        set  bad guess count
        """
        self.bad_guess = self.bad_guess + 1

    def setMissed_letters(self):
        """
        set wrong letter count
        """
        self.missed_letters = self.missed_letters + 1

    def setTried_letters(self, vlaue):
        self.score = value
