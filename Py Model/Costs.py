# Calculating costs
class Costs:
    def __init__(self, ppl_sample_size, number_of_points):
        self.ppl_sample_size = ppl_sample_size
        self.number_of_points = number_of_points

    # Calculating costs for spam campaign
    def spam_costs(self, spam_price):
        return self.ppl_sample_size * spam_price

    # Calculating costs for time passed
    def time_costs(self, price_function):
        price = price_function(self.number_of_points)
        return price
