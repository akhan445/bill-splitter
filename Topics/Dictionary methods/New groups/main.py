# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
n = int(input())

classes = dict.fromkeys(groups)  # defaults to None
classes.update({groups[i]: int(input()) for i in range(0, n)})

# n = int(input())

# for i in range(0, n):
#     group = groups[i]
#     classes[group] = int(input())

print(classes)
