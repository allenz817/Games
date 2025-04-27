def generate_random_number(min_value, max_value):
    import random
    return random.randint(min_value, max_value)

def format_message(message):
    return f"[Game Message]: {message}"

def calculate_percentage(value, total):
    if total == 0:
        return 0
    return (value / total) * 100

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))