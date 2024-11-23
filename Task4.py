"""
Красно-черное дерево - это самобалансирующееся бинарное дерево поиска, которое обеспечивает 
логарифмическое время выполнения операций поиска, вставки и удаления. 

    Теоретическая оценка сложности:
        Поиск: O(log n)
        Вставка: O(log n)
        Удаление: O(log n)

    Затраты по памяти:
        Каждый узел занимает фиксированное количество памяти для хранения данных,
        указателей на потомков и родителя, а также цвета (красный или черный).
        Общее количество памяти, используемой деревом, пропорционально количеству узлов, то есть O(n).

"""


class Node:
    def __init__(self, data, color='red'):
        self.data = data  # Данные узла
        self.color = color  # Цвет узла ('red' или 'black')
        self.left = None  # Левый потомок
        self.right = None  # Правый потомок
        self.parent = None  # Родительский узел


class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(None, 'black')  # Сентинельный узел (черный)
        self.root = self.NIL_LEAF  # Корень дерева

    def rotate_left(self, x):
        """Выполняет левый поворот вокруг узла x."""
        y = x.right  # Указатель на правого потомка
        x.right = y.left  # Перемещение левого поддерева y к x

        if y.left != self.NIL_LEAF:
            y.left.parent = x  # Установка родителя для левого поддерева y

        y.parent = x.parent  # Установка родителя для y
        if x.parent is None:
            self.root = y  # Если x был корнем, то y становится новым корнем
        elif x == x.parent.left:
            x.parent.left = y  # y становится левым потомком
        else:
            x.parent.right = y  # y становится правым потомком

        y.left = x  # Устанавливаем x как левого потомка y
        x.parent = y  # Устанавливаем y как родителя x

    def rotate_right(self, y):
        """Выполняет правый поворот вокруг узла y."""
        x = y.left  # Указатель на левого потомка
        y.left = x.right  # Перемещение правого поддерева x к y

        if x.right != self.NIL_LEAF:
            x.right.parent = y  # Установка родителя для правого поддерева x

        x.parent = y.parent  # Установка родителя для x
        if y.parent is None:
            self.root = x  # Если y был корнем, то x становится новым корнем
        elif y == y.parent.right:
            y.parent.right = x  # x становится правым потомком
        else:
            y.parent.left = x  # x становится левым потомком

        x.right = y  # Устанавливаем y как правого потомка x
        y.parent = x  # Устанавливаем x как родителя y

    def insert(self, data):
        """Вставляет новый узел с данными data в дерево."""
        new_node = Node(data)  # Создаем новый узел
        new_node.left = self.NIL_LEAF  # Левый потомок у нового узла - черный лист
        new_node.right = self.NIL_LEAF  # Правый потомок у нового узла - черный лист

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

    def fix_insert(self, z):
        """Исправляет дерево после вставки нового узла z."""
        while z.parent and z.parent.color == 'red':
            if z.parent == z.parent.parent.left:  # Если родитель z - левый потомок
                y = z.parent.parent.right  # Дядя z
                if y.color == 'red':  # Случай 1: дядя z красный
                    z.parent.color = 'black'  # Перекрашиваем родителя в черный
                    y.color = 'black'  # Перекрашиваем дядю в черный
                    z.parent.parent.color = 'red'  # Перекрашиваем дедушку в красный
                    z = z.parent.parent  # Поднимаемся к дедушке
                else:
                    if z == z.parent.right:  # Случай 2: z - правый потомок
                        z = z.parent  # Поворачиваем к родителю
                        self.rotate_left(z)  # Левый поворот
                    z.parent.color = 'black'  # Случай 3: z - левый потомок
                    z.parent.parent.color = 'red'  # Перекрашиваем дедушку в красный
                    self.rotate_right(z.parent.parent)  # Правый поворот
            else:  # Если родитель z - правый потомок
                y = z.parent.parent.left  # Дядя z
                if y.color == 'red':  # Случай 1: дядя z красный
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:  # Случай 2: z - левый потомок
                        z = z.parent  # Поворачиваем к родителю
                        self.rotate_right(z)  # Правый поворот
                    z.parent.color = 'black'  # Случай 3: z - правый потомок
                    z.parent.parent.color = 'red'
                    self.rotate_left(z.parent.parent)  # Левый поворот
        self.root.color = 'black'  # Корень всегда черный

    def print_tree(self, node=None, level=0, prefix="Root:"):
        """Рекурсивно выводит дерево в консоль."""
        if node is None:
            node = self.root
        if node != self.NIL_LEAF:
            print(" " * (level * 4) + prefix + f" {node.data} ({node.color})")
            self.print_tree(node.left, level + 1, "L---")
            self.print_tree(node.right, level + 1, "R---")


# Пример использования
if __name__ == "__main__":
    rbt = RedBlackTree()  # Создаем экземпляр красно-черного дерева
    values = [20, 15, 25, 10, 5, 1, 30, 35]  # Значения для вставки

    for value in values:
        rbt.insert(value)  # Вставляем значения в дерево

    rbt.print_tree()
