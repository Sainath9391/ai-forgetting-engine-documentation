import math
def decay(memory, current_time, decay_rate=0.01):
    age = current_time - memory.timestamp
    return memory.salience * math.exp(-decay_rate * age)
