from typing import List


def main() -> None:
    """Main function"""
    pass


def syracuse_sequence(n: int) -> List[int]:
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        sequence.append(n)
    return sequence


if __name__ == '__main__':
    main()