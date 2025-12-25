def build_pipeline(operation_names):
    operations = {
        "square": lambda x: x * x,
        "double": lambda x: x * 2,
        "half": lambda x: x / 2,
        "negate": lambda x: -x,
        "increment": lambda x: x + 1,
        "decrement": lambda x: x - 1
    }

    for name in operation_names:
        if name not in operations:
            raise ValueError(f"Unknown operation: {name}")

    def pipeline(value):
        result = value
        for name in operation_names:
            result = operations[name](result)
        return result

    return pipeline
