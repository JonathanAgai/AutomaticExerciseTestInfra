

class Exercise:
    def __init__(self, features):
        self.features = features

    def calculate_scores(self):
        feature_scores = []
        for feature in self.features:
            feature_scores.append(feature.get_score())

        final_score = round(sum(feature_scores))

        return [final_score, [feature_scores]]


    def run(self):
        pass
        #TODO run all features

    def print(self):
        for feature in self.features:
            feature.print()