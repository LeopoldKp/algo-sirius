"""
Теоретическая оценка сложности алгоритма и затраты по памяти:

    Временная сложность:
        Вставка (insert): O(log n) в среднем и в худшем случае, так как красно-черное дерево является сбалансированным.
        Поиск (search): O(log n) в среднем и в худшем случае, по той же причине.

    Затраты по памяти:
        Каждый узел занимает постоянное количество памяти для хранения данных, цвета,
        указателей на левых и правых потомков, а также указателя на родителя.
        Общие затраты по памяти для хранения n узлов составляют O(n), где n - количество узлов в дереве.
"""
from Task4 import Node, RedBlackTree


class KeyValueRedBlackTree(RedBlackTree):
    def insert(self, key, value):
        """Вставляет новый узел с парой (ключ, значение) в дерево."""
        new_node = Node(key)  # Создаем новый узел с ключом
        new_node.left = self.NIL_LEAF  # Левый потомок у нового узла - черный лист
        new_node.right = self.NIL_LEAF  # Правый потомок у нового узла - черный лист
        new_node.value = value  # Сохраняем значение в узле

        parent = None  # Родитель нового узла
        current = self.root  # Начинаем с корня

        # Поиск места для вставки нового узла
        while current != self.NIL_LEAF:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent  # Устанавливаем родителя для нового узла
        if parent is None:
            self.root = new_node  # Если дерево пустое, новый узел становится корнем
        elif new_node.data < parent.data:
            parent.left = new_node  # Новый узел становится левым потомком
        else:
            parent.right = new_node  # Новый узел становится правым потомком

        new_node.color = 'red'  # Новый узел всегда красный
        self.fix_insert(new_node)  # Исправляем нарушения свойств дерева

    def search(self, key):
        """Ищет значение по ключу в дереве."""
        current = self.root
        while current != self.NIL_LEAF:
            if key == current.data:
                return current.value  # Возвращаем значение, если ключ найден
            elif key < current.data:
                current = current.left
            else:
                current = current.right
        return None  # Если ключ не найден, возвращаем None

    def print_tree(self, node=None, level=0, prefix="Root:"):
        """Рекурсивно выводит дерево в консоль с ключами и значениями."""
        if node is None:
            node = self.root
        if node != self.NIL_LEAF:
            print(" " * (level * 4) + prefix + f" {node.data}: {node.value} ({node.color})")
            self.print_tree(node.left, level + 1, "L---")
            self.print_tree(node.right, level + 1, "R---")


# Пример использования
if __name__ == "__main__":
    kv_rbt = KeyValueRedBlackTree()  # Создаем экземпляр красно-черного дерева для пар ключ-значение
    pairs = [(20, "Value 20"), (15, "Value 15"), (25, "Value 25"),
             (10, "Value 10"), (5, "Value 5"), (1, "Value 1"),
             (30, "Value 30"), (35, "Value 35")]  # Пары (ключ, значение)

    for key, value in pairs:
        kv_rbt.insert(key, value)  # Вставляем пары в дерево

    kv_rbt.print_tree()  # Выводим дерево в консоль
    print("Поиск значения по ключу 15:", kv_rbt.search(15))  # Пример поиска
    print("Поиск значения по ключу 100:", kv_rbt.search(100))  # Пример поиска несуществующего ключа
