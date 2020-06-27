class PokerHand(object):
    """
    Program that compares your poker hand with other hand and returns the better
    hand as per standard Texas Hold'em rules.
    See also: https://www.codewars.com/kata/5739174624fc28e188000465/train/python
    Returns Loss, Tie or Win.
    """

    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
        pass

    def convert_hand(self, hand):
        """
        Converts a hand to a sequence of cards and suits, returns if it is the
        same suit.
        """
        pass

    def get_highest(self, hand1, hand2):
        """
        Returns the hand whose highest card is higher.
        """
        pass

    def compare_with(self, other):
        pass
