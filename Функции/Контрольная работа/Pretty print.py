def pretty_print(data, side='-', delimiter='|'):
    data_str = f" {delimiter} ".join(map(str, data))
    content_line = f"{delimiter} {data_str} {delimiter}"
    frame_line = f" {side * (len(content_line) - 2)} "  # -2 потому что пробелы по краям

    # Выводим три строки: верхняя рамка, содержимое, нижняя рамка
    print(frame_line)
    print(content_line)
    print(frame_line)

pretty_print([1, 2, 10, 23, 123, 3000])