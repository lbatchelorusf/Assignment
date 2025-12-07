# return a greeting to the user
def get_greeting(name):
    return f"Hello, {name}!"

# generate the first 12 Fibonacci numbers
def generate_fibonacci(n=12):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]
