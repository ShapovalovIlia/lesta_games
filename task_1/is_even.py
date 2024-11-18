def is_even_fast(value: int) -> bool:
    return (value & 1) == 0


def is_even_slow(value: int) -> bool:
    return value % 2 == 0
