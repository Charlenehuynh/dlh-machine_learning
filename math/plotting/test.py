try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("caught:", e)
finally:
    print("done")