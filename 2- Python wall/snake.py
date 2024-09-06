import random
import time

def python_snake_paints():
    print("The Python snake is feeling artistic today...")
    time.sleep(2)
    
    canvas = [" " * 20 for _ in range(10)]
    snake = "🐍"
    
    print("\nPython snake is now painting...")
    for i in range(100):
        x = random.randint(0, 19)
        y = random.randint(0, 9)
        if random.random() < 0.5:
            canvas[y] = canvas[y][:x] + snake + canvas[y][x+1:]
        print("\n".join(canvas))
        time.sleep(0.1)
        print("\r" + " " * 80, end="\r")  # Clear the line
    
    print("\nPython snake has finished its masterpiece!")
    return "\n".join(canvas)

# Let's see the Python snake's artistic creation
masterpiece = python_snake_paints()
print("\nHere's the final image:\n")
print(masterpiece)