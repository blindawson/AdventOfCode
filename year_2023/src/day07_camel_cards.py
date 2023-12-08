from AdventOfCode.support import support


class ClassName:
    def __init__(self, filename, jokers_wild: bool = False):
        self.file_input = support.read_input(filename, flavor="split", split_char=" ")
        self.jokers_wild = jokers_wild
        if self.jokers_wild:
            self.card_dict = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
        else:
            self.card_dict = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        self.sum = 0
        for index, item in enumerate(self.file_input):
            hand, _ = item
            hand_score = self.hand_rank(hand) + self.card_rank(hand)
            self.file_input[index].append(hand_score)
        self.sorted_hands = sorted(self.file_input, key=lambda x: x[-1])
        for index, item in enumerate(self.sorted_hands):
            bid = int(item[1])
            print(f"{bid} * {index + 1}")
            self.sum += bid * (index + 1)

    def card_rank(self, hand: str):
        power = 1
        rank = 0
        for card in hand:
            if card.isnumeric():
                rank += float(card) * power
            else:
                rank += self.card_dict[card] * power
            power /= 100
        return rank

    def hand_rank(self, hand: str):
        joker_count = hand.count("J")
        # five of a kind
        if hand.count(hand[0]) == 5:
            rank = 700
        # four of a kind
        elif (hand.count(hand[0]) == 4) or (hand.count(hand[1]) == 4):
            if self.jokers_wild and ((joker_count == 1) or (joker_count == 4)):
                rank = 700
            else:
                rank = 600
        # three of a kind
        elif (
            (hand.count(hand[0]) == 3)
            or (hand.count(hand[1]) == 3)
            or (hand.count(hand[2]) == 3)
        ):
            rank = 400

            if self.jokers_wild:
                if joker_count == 3:
                    if len(set(hand)) == 2:
                        rank = 700
                    else:
                        rank = 600
                elif joker_count == 2:
                    rank = 700
                elif joker_count == 1:
                    rank = 600
                else:
                    rank = 400
            # full house
            for i in range(4):
                if hand.count(hand[i]) == 2:
                    rank = max(rank, 500)
                    break
        # two pair
        elif len(set(hand)) == 3:
            if self.jokers_wild:
                if joker_count == 2:
                    rank = 600
                elif joker_count == 1:
                    rank = 500
                else:
                    rank = 300
            else:
                rank = 300
        # one pair
        elif len(set(hand)) == 4:
            if self.jokers_wild:
                if joker_count == 2:
                    rank = 400
                elif joker_count == 1:
                    rank = 400
                else:
                    rank = 200
            else:
                rank = 200
        # high card
        else:
            if self.jokers_wild and (joker_count == 1):
                rank = 200
            else:
                rank = 100
        return rank
