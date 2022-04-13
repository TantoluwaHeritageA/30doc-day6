def climb_days(depth):
    height = 0
    days = 0
    while height < depth:
        days += 1
        height = 8 + height
        if height >= depth:
            return days
        else:
            height = height - 3


output = climb_days(int(input("Enter a depth: ")))
print(f"It took {output} days to climb up the well.")
