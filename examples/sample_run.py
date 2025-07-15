from src.memory import Memory
from src.decay import decay
import time

# Create memory
m = Memory("Met a friend at cafe", salience=0.9, timestamp=time.time() - 3600)
# Apply decay
current_time = time.time()
new_score = decay(m, current_time)
print(f"Decayed score: {new_score}")
