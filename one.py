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

# Аналіз основних характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступені вершин:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")
