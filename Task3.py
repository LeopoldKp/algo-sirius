"""
Теоретическая оценка сложности алгоритма и затрат по памяти:

    Временная сложность:
        Инвертирование бинарного дерева поиска (BST) требует обхода всех узлов дерева.
        В лучшем и худшем случае, временная сложность составляет O(n), где n — количество узлов в дереве.

    Затраты по памяти:
        Если использовать рекурсивный подход, то стек вызовов может занять O(h) памяти, где h — высота дерева.
        В худшем случае (для несбалансированного дерева) высота может быть равна n, что дает O(n) памяти.
        В сбалансированном дереве высота будет O(log n), что дает O(log n) памяти.

"""

class TreeNode:
    def __init__(self, value):
        """Инициализация узла дерева."""
        self.value = value  # Значение узла
        self.left = None    # Левый дочерний узел
        self.right = None   # Правый дочерний узел

def invert_tree(node):
    """Инвертирует бинарное дерево."""
    if node is None:
        return None  # Если узел пустой, ничего не делаем

    # Рекурсивно инвертируем левое и правое поддеревья
    left = invert_tree(node.left)
    right = invert_tree(node.right)

    # Меняем местами левое и правое поддеревья
    node.left = right
    node.right = left

    return node  # Возвращаем инвертированный узел

def print_tree(node, level=0):
    """Выводит дерево в удобочитаемом формате."""
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.value)
        print_tree(node.left, level + 1)

# Пример использования
if __name__ == "__main__":
    # Создаем бинарное дерево
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print("Исходное дерево:")
    print_tree(root)

    # Инвертируем дерево
    invert_tree(root)

    print("\nИнвертированное дерево:")
    print_tree(root)
