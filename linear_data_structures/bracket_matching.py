from stack_class import Stack


def is_matching(brackets):
    bracket_mapping = {'(': ')', '[': ']'}
    stack = Stack()
    for bracket in brackets:
        # ukladanie otvarajucej zatvorky do stacku
        if bracket in bracket_mapping.keys():
            stack.push(bracket)

        # pokusame sa uzatvorit neexistujucu zatvorku
        elif stack.is_empty():
            return False

        # zatvarajuca zatvorka sa nezhoduje s otvarajucou
        elif bracket_mapping[stack.pop()] != bracket:
            return False

    # Ak stack na konci nie je prazdny, niektore zatvorky neboli uzavrete
    return stack.is_empty()


if __name__ == '__main__':
    print(is_matching('()[]'))  # True
    print(is_matching(''))  # True
    print(is_matching('()'))  # True
    print(is_matching('('))  # False
    print(is_matching('[)'))  # False
    print(is_matching('([])'))  # True
    print(is_matching('([])[]'))  # True
    print(is_matching('([)]'))  # False
    print(is_matching(']'))  # False
