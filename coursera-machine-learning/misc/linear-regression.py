def gradient_descent(learning_rate, training):
    terms = [0, 0]
    hypothesis = lambda x: terms[0] + terms[1]*x
    error = lambda : sum(map(lambda x_y: (hypothesis(x_y[0]) - x_y[1]) ** 2, training)) / (2*len(training))
    p = lambda : print(f'Equation is y = {terms[0]} + {terms[1]}x')

    iterations = 0
    while error() > 1:
        acc = [0, 0]
        for x, y in training:
            acc[0] += (hypothesis(x) - y)
            acc[1] += (hypothesis(x) - y) * x
        terms[0] -= learning_rate * acc[0] / float(len(training))
        terms[1] -= learning_rate * acc[1] / float(len(training))
        iterations += 1

    p()
    print(f'Finished after {iterations} iterations with error {error()}!')
    return terms

gradient_descent(0.00001, [ (x, x) for x in range(100)])
gradient_descent(0.0001, [ (x, 10) for x in range(100)])
gradient_descent(0.0001, [ (x, 100*x - 13337) for x in range(100)])
