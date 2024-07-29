import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин з іменами людей
people = ['Саша', 'Маша', 'Паша', 'Міша', 'Тіша', 'Гріша']
G.add_nodes_from(people)

# Додавання ребер(дружні зв'язки) з вагами
friendships = [
    ('Саша', 'Маша', 1),
    ('Саша', 'Паша', 4),
    ('Маша', 'Паша', 2),
    ('Маша', 'Міша', 5),
    ('Паша', 'Тіша', 3),
    ('Міша', 'Тіша', 1),
    ('Тіша', 'Гріша', 2),
    ('Гріша', 'Саша', 7)
]
G.add_weighted_edges_from(friendships)

# Візуалізація графа
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G)  # Розташування вершин
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=16, font_weight='bold', edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Social Network Graph with Weights')
plt.show()

# Алгоритм Дейкстри для знаходження найкоротших шляхів між усіма вершинами
shortest_paths = dict(nx.all_pairs_dijkstra_path(G))

print("Найкоротші шляхи між всіма вершинами:")
for start in shortest_paths:
    for end in shortest_paths[start]:
        print(f"Шлях від {start} до {end}: {shortest_paths[start][end]}")
