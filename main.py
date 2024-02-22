class Queue:
    def __init__(self):
        self.cards = []

    def push(self, card):
        # The push method adds a card to the back of the queue
        self.cards.append(card)

    def pop(self):
        # The pop method removes and returns the card from the front of the queue
        if self.is_empty():
            raise IndexError("Queue is empty, cannot pop.")
        return self.cards.pop(0)

#comment

    def is_empty(self):
        # Check if the queue is empty
        return len(self.cards) == 0

# Example usage:
# Create a queue
deck_queue = Queue()

# Add cards to the queue
deck_queue.push("Card1")
deck_queue.push("Card2")
deck_queue.push("Card3")

# Pop cards from the queue (FIFO behavior)
first_card = deck_queue.pop()
second_card = deck_queue.pop()

print("First card served:", first_card)
print("Second card served:", second_card)
