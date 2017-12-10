def main():
    lengths = [int(i) for i in open('input.txt').read().strip().split(',')]
    sequence = [i for i in range(0, 256)]

    print(part1(sequence, lengths))


def part1(sequence, lengths):
    current_pos = 0
    skip_size = 0

    for i in range(len(lengths)):
        reverse_fragment(sequence, current_pos, lengths[i])

        current_pos = (current_pos + lengths[i] + skip_size) % len(sequence)
        skip_size += 1

    return sequence[0] * sequence[1]


def reverse_fragment(arr, start, length):
    tmp = arr * 2
    tmp[start:start+length] = tmp[start:start+length][::-1]

    tmp[0:start] = tmp[len(arr):start+len(arr)]
    arr[:] = tmp[0:len(arr)]


if __name__ == '__main__':
    main()
