from typing import List


def syracuse_sequence(n: int) -> List[int]:
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        sequence.append(n)
    return sequence


def syracuse_max(n: int) -> int:
    sequence = syracuse_sequence(n)
    max_num = n
    for max_value in sequence:
        if max_value > max_num:
            max_num = max_value
    return max_num


def main() -> None:
    """Main function"""
    number = int(input('Введите число: '))
    sequence = syracuse_sequence(number)
    print(f'{sequence = }')
    print(f'{syracuse_max(number) = }')


if __name__ == '__main__':
    main()
