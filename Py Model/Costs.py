# Calculating costs
class Costs:
    def __init__(self, ppl_sample_size, number_of_points, spam_price):
        self.ppl_sample_size = ppl_sample_size
        self.number_of_points = number_of_points
        self.spam_price = spam_price

    # Calculating costs for spam campaign
    def survey_cost(self):
        return self.ppl_sample_size * self.spam_price

    def spam_cost(self):
        return self.survey_cost() * self.number_of_points

    def total(self):
        return self.spam_cost()
