import heapq

# Створення графа у вигляді словника
graph = {
    'Саша': {'Паша': 1, 'Маша': 4},
    'Паша': {'Саша': 1, 'Маша': 2, 'Тіша': 5},
    'Маша': {'Саша': 4, 'Паша': 2, 'Міша': 3},
    'Тіша': {'Паша': 5, 'Міша': 1},
    'Міша': {'Маша': 3, 'Тіша': 1, 'Гріша': 2},
    'Гріша': {'Міша': 2, 'Саша': 7}
}

def dijkstra(graph, start):
    # Ініціалізація
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    shortest_paths = {node: [] for node in graph}
    shortest_paths[start] = [start]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Якщо відстань у черзі більша, ніж відстань в масиві distances, продовжити
        if current_distance > distances[current_node]:
            continue

        # Перегляд сусідів поточної вершини
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Якщо знайдена коротша відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_paths[neighbor] = shortest_paths[current_node] + [neighbor]

    return distances, shortest_paths

# Виконання алгоритму Дейкстри для всіх вершин
all_shortest_paths = {}
for node in graph:
    _, paths = dijkstra(graph, node)
    all_shortest_paths[node] = paths

print("Найкоротші шляхи між всіма вершинами (Алгоритм Дейкстри):")
for start in all_shortest_paths:
    for end in all_shortest_paths[start]:
        print(f"Шлях від {start} до {end}: {all_shortest_paths[start][end]}")

# Для прикладу виведемо відстані
print("\nНайкоротші відстані від кожної вершини:")
for node in graph:
    distances, _ = dijkstra(graph, node)
    print(f"Відстані від {node}: {distances}")

