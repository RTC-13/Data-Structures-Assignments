def add_edge(mat, i, j):
    # Edge
    mat[i][j] = 1  # Graph is undirected
    mat[j][i] = 1  # Undirected

def display_matrix(mat):
    # Display the adjacency matrix
    for row in mat:
        print(" ".join(map(str, row)))

def del_vertex(mat, k):
    # Delete the specified vertex from the graph
    for i in range(len(mat)):
        mat[i][k] = 0  # Remove edges to the vertex
        mat[k][i] = 0  # Remove edges from the vertex

def input_graph(v):
    # Input graph from the keyboard
    mat = [[0] * v for _ in range(v)]
    edges = int(input("Enter the number of edges: "))
    for _ in range(edges):
        source, destination = map(int, input("Enter edge (origen → target): ").split())
        add_edge(mat, source, destination)
    return mat

# Driver code
if __name__ == "__main__":
    V = 5  # Number of vertices (0 to 4)
    mat = input_graph(V)  # Input the graph

    print("Initial adjacency matrix: ")
    display_matrix(mat)

    # Delete vertex 2 from the graph
    del_vertex(mat, 2)

    print("Adjacency matrix after deleting vertex 2: ")
    display_matrix(mat)
