import itertools


def main():
    with open('input.txt') as f:
        data = []

        for line in f.readlines():
            data.append([int(item) for item in line.strip('\n').split('\t')])

    part1(data)
    part2(data)


def part1(data):
    checksum = 0
    for line in data:
        diff = max(line) - min(line)
        checksum += diff

    print(checksum)


def part2(data):
    s = 0

    for line in data:
        for comb in itertools.combinations(line, 2):
            tmp = sorted(comb)

            if tmp[1] % tmp[0] == 0:
                s += tmp[1] / tmp[0]
                continue

    print(s)


if __name__ == '__main__':
    main()
