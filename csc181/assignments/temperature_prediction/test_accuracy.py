def test_accuracy(n, prediction_temperature, test_temperature):
    if len(prediction_temperature) != n * 24:
        print("The shape of your array is incorrect. It must be size: {}".format(n * 24))
    else:
        accuracy_score = 0
        for p, t in zip(prediction_temperature, test_temperature):
            accuracy_score += int(abs(t - p) <= 5)
        return "Your accuracy score was: {}".format(accuracy_score)