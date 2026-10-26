# 1. Друк рядка у зворотному порядку
def print_reverse(text):
    def print_from(index):
        if index == len(text):
            return

        print_from(index + 1)
        print(text[index], end="")

    print_from(0)


# 2. Попарна перестановка вузлів однозв'язного списку
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head):
    if head is None or head.next is None:
        return head

    second = head.next
    head.next = swap_pairs(second.next)
    second.next = head
    return second


def build_list(values, index=0):
    if index == len(values):
        return None

    return ListNode(values[index], build_list(values, index + 1))


def to_list(head):
    result = []

    def collect(node):
        if node is None:
            return

        result.append(node.val)
        collect(node.next)

    collect(head)
    return result


# 3. Число Фібоначчі
def fibonacci(n):
    if n < 0:
        raise ValueError("n має бути невід'ємним")

    def calculate(remaining, current, following):
        if remaining == 0:
            return current

        return calculate(remaining - 1, following, current + following)

    return calculate(n, 0, 1)


# 4. Кількість способів піднятися сходами
def climb_stairs(n):
    if n < 0:
        raise ValueError("Кількість сходинок має бути невід'ємною")

    def count(remaining, current, following):
        if remaining == 0:
            return current

        return count(remaining - 1, following, current + following)

    return count(n, 1, 1)


# 5. Піднесення до цілого степеня
def power(x, n):
    def positive_power(base, exponent):
        if exponent == 0:
            return 1.0

        half = positive_power(base, exponent // 2)
        result = half * half

        if exponent % 2 == 0:
            return result

        return result * base

    if n < 0:
        return positive_power(1.0 / x, -n)

    return positive_power(x, n)


if __name__ == "__main__":
    print("1. Рядок у зворотному порядку:")
    print_reverse("tiger")
    print()

    print("\n2. Попарна перестановка вузлів:")
    print(to_list(swap_pairs(build_list([1, 2, 3, 4]))))
    print(to_list(swap_pairs(build_list([]))))
    print(to_list(swap_pairs(build_list([1]))))

    print("\n3. Числа Фібоначчі:")
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(4))

    print("\n4. Способи піднятися сходами:")
    print(climb_stairs(2))
    print(climb_stairs(3))

    print("\n5. Піднесення до степеня:")
    print(f"{power(2.0, 10):.5f}")
    print(f"{power(2.1, 3):.5f}")
    print(f"{power(2.0, -2):.5f}")
