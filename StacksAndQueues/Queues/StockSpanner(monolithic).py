# Design an algorithm that collects daily price quotes for some stock and returns the span
# of that stock's price for the current day.
# The span of the stock's price in one day is the maximum number of consecutive days
# (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

# For example, if the prices of the stock in the last four days is [7,2,1,2]
# and the price of the stock today is 2, then the span of today is 4 because starting from today,
# the price of the stock was less than or equal 2 for 4 consecutive days.

# Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8,
# then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.


class StockSpanner:
    def __init__(self):
        self.stack = []
        self.index = 0

    def next(self, price: int) -> int:
        tuple = (price, self.index)
        # maintain monotonically decreasing stack
        while self.stack and price >= self.stack[-1][0]:  # price >= than price from tuple at top of stack
            self.stack.pop()
        self.stack.append(tuple)
        self.index += 1  # the count of each item pushed onto stack starting at 0
        if len(self.stack) == 1:
            return self.stack[0][1] + 1  # return index value of only tuple on stack
        return self.stack[-1][1] - self.stack[-2][1]  # return top of stack index value minus next-to-top index value


obj = StockSpanner()
prices = [100, 80, 60, 70, 60, 75, 85]  # output = [1,1,1,2,1,4,6]
# prices = [31, 41, 48, 59, 79]  # output = [1,2,3,4,5]
# prices = [28, 14, 28, 35, 46, 53, 66, 80, 87, 88]  # output = [1,1,3,4,5,6,7,8,9,10]
for price in prices:
    print(obj.next(price), end=" ")
print("")
