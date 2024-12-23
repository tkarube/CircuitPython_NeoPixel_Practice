def color_cycle():
    colors = ['red', 'green', 'blue']
    while True:
        for color in colors:
            yield color  # 色を1つずつ返す

# 使用例
color_iter = color_cycle()

print(next(color_iter))  # red
print(next(color_iter))  # green
print(next(color_iter))  # blue
print(next(color_iter))  # red (再び始まる)
