from datetime import timedelta

def predict(last,cycle):
    return last+timedelta(days=cycle)