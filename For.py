import time
def for_loop():
    for i in range(1, 11):
        print(i)
    print("trying another way...")
    for j in range(10):
        print(j + 1)

    for n in range(100):
        print("hello!!!")
    print("let's count for a minute")
    for s in range(60):
        print(s)
        time.sleep(1)

for_loop()
