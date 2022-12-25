from math import lcm
from operator import attrgetter
from typing import Callable


class Monkey:
    @staticmethod
    def _description_to_args(description: str) -> list[str]:
        lines: list[str] = description.split('\n')
        args: list[str] = []
        for i in range(1, len(lines)):
            arg: str = lines[i].strip() \
                .replace('Starting items: ', '') \
                .replace('Operation: new = ', '') \
                .replace('Test: divisible by ', '') \
                .replace('If true: throw to monkey ', '') \
                .replace('If false: throw to monkey ', '')
            args.append(arg)
        return args

    @staticmethod
    def _parse_inspection_function(operation_description: str):
        return lambda old: eval(operation_description)

    def perform_inspection(self, item: int) -> int:
        self.performed_inspections += 1
        result = self._inspection_function(item)
        if self.part1:
            result = result // 3
        return result

    def perform_test(self, item: int) -> int:
        return self._success_monkey if self._test_function(item) else self._fail_monkey

    def __init__(self, description: str, part1: bool):
        args: list[str] = Monkey._description_to_args(description)
        self.part1: bool = part1
        self.performed_inspections: int = 0
        self.items: list[int] = [int(item) for item in args[0].split(', ')]
        self._inspection_function: Callable[[int], int] = Monkey._parse_inspection_function(args[1])
        self.divisor = int(args[2])
        self._test_function: Callable[[int], bool] = lambda x: (x % self.divisor == 0)
        self._success_monkey: int = int(args[3])
        self._fail_monkey: int = int(args[4])

    def __repr__(self):
        return f"Monkey with items: {', '.join(str(i) for i in self.items)}"


class MonkeyGroup:
    def __init__(self, input_str, part1: bool):
        self.monkeys: dict[int, Monkey] = \
            {i: Monkey(description, part1) for i, description in enumerate(input_str.split('\n\n'))}
        self.modulus = lcm(*map(attrgetter('divisor'), self.monkeys.values()))

    def __repr__(self):
        return '\n'.join([f'{i} -> {m}' for i, m in self.monkeys.items()])

    @staticmethod
    def logger(verbose: bool):
        return lambda message: print(message) if verbose else print(end='')

    def simulate(self, rounds, verbose: bool = False) -> int:
        for _ in range(rounds):
            self._round(verbose)
        first, second = sorted([m.performed_inspections for m in self.monkeys.values()], reverse=True)[:2]
        return first * second

    def _round(self, verbose: bool):
        log = self.logger(verbose)
        log('==== PROCESS ROUND ====')
        for i, monkey in self.monkeys.items():
            log(f'Monkey {i}')
            while len(monkey.items) > 0:
                item: int = monkey.items[0]
                del monkey.items[0]
                log(f'Item {item}')
                new_worry_level: int = monkey.perform_inspection(item) % self.modulus
                log(f'New worry level {new_worry_level}')
                to_monkey: int = monkey.perform_test(new_worry_level)
                log(f'To monkey {to_monkey}')
                self.monkeys[to_monkey].items.append(new_worry_level)
                log('')
                log(self)
                log('\n')


input_str = open('input.txt', 'r').read()

print(f"Task 1: {MonkeyGroup(input_str, True).simulate(20)}")
print(f"Task 2: {MonkeyGroup(input_str, False).simulate(10000)}")
