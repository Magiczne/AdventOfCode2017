def main():
    with open('input.txt') as f:
        data = list(f.read())

    calc(data, 1)
    calc(data, int(len(data) / 2))


def calc(data, distance):
    data_sum = 0

    for i in range(len(data)):
        if data[i] == data[(i + distance) % len(data)]:
            data_sum += int(data[i])

    print(data_sum)


if __name__ == '__main__':
    main()
