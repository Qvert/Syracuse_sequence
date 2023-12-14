"""glebas vvpd 4"""

from typing import List


def syracuse_sequence(n: int) -> List[int]:
    """
    Generation syracuse sequence
    :param n: Number
    :return: List numbers
    """
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        sequence.append(n)
    return sequence


def syracuse_max(n: int) -> int:
    """
    Finding the maximum number in the syracuse sequence
    :param n: The number from which the sequence is built
    :return: Number
    """
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
