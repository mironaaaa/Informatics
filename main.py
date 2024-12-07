from math import log2, ceil


def read(filename):
    with open(filename) as file:
        return file.read().strip()


def write(filename, sequence):
    with open(filename, "w") as file:
        file.write(sequence)


def parity_bits(sequence):
    bits = ""
    for i in range(ceil(log2(len(sequence)))):
        parity = 0
        for j in range(len(sequence)):
            if (j + 1) & (2**i) != 0:
                parity ^= int(sequence[j])
        bits += str(parity)

    return bits


def check_error(data):
    error = 0
    for i in range(ceil(log2(len(data)))):
        parity = 0
        for j in range(len(data)):
            if (j + 1) & (2**i) != 0:
                parity ^= int(data[j])
        if parity != 0:
            error += 2**i

    if error != 0:
        data = list(data)
        data[error - 1] = str(1 - int(data[error - 1]))
        data = "".join(data)

    return data, error


if __name__ == "__main__":
    data = read("input")
    output = data + parity_bits(data)
    print("Контрольные биты: ", output)
    write("output", output)

    received = read("received")
    correct, error_position = check_error(received)

    if error_position != 0:
        print(f"Ошибка в {error_position+1}")
        write("output", correct)
    else:
        print("Программа завершена.")
