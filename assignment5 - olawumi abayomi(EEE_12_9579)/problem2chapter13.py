# Write a program that reads a file and prints only those lines that contain the substring snake.
# Content of the file
"""
    A snake can be very dangerous in the night
    Kunle objected with acerbically
    However, we have some indians who tame snake and live with them
    Kunle, insisted that there is nothing alluring about snake
    The end of the hot argument.
    A story that was told on a snakeisland

"""
file = open('snake_file.txt', 'r')
content = file.readlines()
file.close()
for each_line in content:
    if 'snake' in each_line.lower():
        print(each_line)