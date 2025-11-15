class RSI:
    def __init__(self, period=14):
        self.period = period
        self.gains = []
        self.losses = []

    def calculate(self, prices):
        if len(prices) < self.period:
            raise ValueError("Not enough data to calculate RSI")

        for i in range(1, len(prices)):
            change = prices[i] - prices[i - 1]
            if change > 0:
                self.gains.append(change)
                self.losses.append(0)
            else:
                self.gains.append(0)
                self.losses.append(-change)

        average_gain = sum(self.gains[-self.period:]) / self.period
        average_loss = sum(self.losses[-self.period:]) / self.period

        if average_loss == 0:
            return 100  # Avoid division by zero; RSI is 100 if no losses

        rs = average_gain / average_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi