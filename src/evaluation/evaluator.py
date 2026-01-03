from ragas import evaluate

def run_evaluation(dataset, metrics):
    return evaluate(dataset, metrics)