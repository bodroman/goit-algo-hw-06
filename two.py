import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин з іменами людей
people = ['Саша', 'Маша', 'Паша', 'Міша', 'Тіша', 'Гріша']
G.add_nodes_from(people)

# Додавання ребер(дружні зв'язки)
friendships = [
    ('Саша', 'Маша'),
    ('Саша', 'Паша'),
    ('Маша', 'Паша'),
    ('Маша', 'Міша'),
    ('Паша', 'Тіша'),
    ('Міша', 'Тіша'),
    ('Тіша', 'Гріша'),
    ('Гріша', 'Саша')
]
G.add_edges_from(friendships)

# Візуалізація графа
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G)  # Розташування вершин
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=16, font_weight='bold', edge_color='gray')
plt.title('Social Network Graph')
plt.show()

# Функція для виконання DFS
def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# Функція для виконання BFS
def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Виконання DFS та BFS
start_node = 'Саша'
goal_node = 'Тіша'

dfs_paths = list(dfs_path(G, start_node, goal_node))
bfs_paths = list(bfs_path(G, start_node, goal_node))

print("DFS шляхи від 'Саша' до 'Тіша':")
for path in dfs_paths:
    print(path)

print("\nBFS шляхи від 'Саша' до 'Тіша':")
for path in bfs_paths:
    print(path)

#Аналізуємо результати
#DFS (Пошук в глибину)
#DFS шукає шлях від стартової вершини до цільової, глибоко заходячи по кожному можливому шляху до кінця перед переходом до наступного. Це може призвести до знаходження більш довгих або нестандартних шляхів.

#BFS (Пошук в ширину)
#BFS шукає шлях, розширюючи всі можливі шляхи на кожному рівні від стартової вершини до цільової. Це гарантує, що знайдений шлях буде найкоротшим у сенсі кількості ребер.

#Порівняння результатів
#DFS шляхи можуть бути довшими або містити більше вершин, оскільки цей алгоритм йде вглиб.
#BFS шляхи будуть коротшими або містити менше вершин, оскільки цей алгоритм йде вшир, гарантуючи найкоротший шлях.
#Шляхи можуть відрізнятися в залежності від структури графа та від того, як саме алгоритми обходять вершини.
