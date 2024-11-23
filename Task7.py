"""
Теоретическая оценка сложности алгоритма и затрат по памяти:

    Временная сложность:
        Алгоритм Беллмана-Форда требует O(V * E) времени, где V — количество вершин, а E — количество рёбер в графе.

    Затраты по памяти:
        Алгоритм использует O(V) памяти для хранения расстояний до вершин и O(V) для хранения предшественников (если требуется).
        Таким образом, общие затраты по памяти составляют O(V).
"""

class Edge:
    def __init__(self, u, v, weight):
        """Инициализация рёбер графа."""
        self.u = u  # Начальная вершина
        self.v = v  # Конечная вершина
        self.weight = weight  # Вес ребра

def bellman_ford(edges, V, start):
    """Алгоритм Беллмана-Форда для нахождения кратчайших путей."""
    # Шаг 1: Инициализация расстояний
    distances = [float('inf')] * V  # Инициализируем все расстояния как бесконечность
    distances[start] = 0  # Расстояние до стартовой вершины равно 0

    # Шаг 2: Основной цикл алгоритма
    for _ in range(V - 1):
        for edge in edges:
            # Если расстояние до начальной вершины + вес ребра < расстояние до конечной вершины
            if distances[edge.u] != float('inf') and distances[edge.u] + edge.weight < distances[edge.v]:
                distances[edge.v] = distances[edge.u] + edge.weight

    # Шаг 3: Проверка на наличие отрицательных циклов
    for edge in edges:
        if distances[edge.u] != float('inf') and distances[edge.u] + edge.weight < distances[edge.v]:
            print("Граф содержит отрицательный цикл.")
            return None

    return distances  # Возвращаем список кратчайших расстояний до всех вершин

# Пример использования
if __name__ == "__main__":
    # Создаем граф
    edges = [
        Edge(0, 1, -1),
        Edge(0, 2, 4),
        Edge(1, 2, 3),
        Edge(1, 3, 2),
        Edge(1, 4, 2),
        Edge(3, 2, 5),
        Edge(3, 1, 1),
        Edge(4, 3, -3)
    ]
    V = 5  # Количество вершин
    start_vertex = 0  # Стартовая вершина

    distances = bellman_ford(edges, V, start_vertex)

    if distances is not None:
        print("Кратчайшие расстояния от стартовой вершины:")
        for i in range(V):
            print(f"До вершины {i}: {distances[i]}")
