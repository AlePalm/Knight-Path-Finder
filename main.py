from collections import deque
import sys
from graphviz import Graph

def is_valid_move(x, y):
    """Check if the position (x, y) is within the chessboard."""
    return 1 <= x <= 8 and 1 <= y <= 8

def knight_moves():
    """Return all possible moves for a knight."""
    return [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

def algebraic_notation(x, y):
    """Convert chessboard coordinates (x, y) to algebraic notation."""
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  
    return f"{columns[x - 1]}{8 - y + 1}"

def bfs_knight_paths(start, end):
    """Find all shortest paths for a knight from start to end."""

    string = deque([(start, [start])])  # (current_position, path)
    old = set()  # To avoid revisiting positions
    shortest_paths = []  # Store all shortest paths
    found = False  # Flag to stop searching once the shortest paths are found

    while string:
        current, path = string.popleft()

        # If we reach the target, add the path to the results
        if current == end:
            shortest_paths.append(path)
            found = True
            continue  # Keep exploring the same level

        # If we've already found a shortest path, skip further exploration
        if found:
            continue

        # Mark the current position as visited
        old.add(current)

        # Explore all valid knight moves
        for dx, dy in knight_moves():
            next_pos = (current[0] + dx, current[1] + dy)

            if is_valid_move(*next_pos) and next_pos not in old:
                string.append((next_pos, path + [next_pos]))

    # Convert all paths to algebraic notation
    return [[algebraic_notation(x, y) for x, y in path] for path in shortest_paths]

def generate_dot_graph(paths, start, end, output_file="chess_paths"):
    """Generate a graph image from the given paths."""
    # Create a Graph object
    dot = Graph("Knight Paths", format="png")

    # Add the start node with a green color
    dot.node(algebraic_notation(*start), style="filled", fillcolor="green", color="black", shape="circle")
    # Add the end node with an orange color
    dot.node(algebraic_notation(*end), style="filled", fillcolor="orange", color="black", shape="circle")

    edges_added = set()

    for path in paths:
        for i in range(len(path) - 1):
            # Create an edge as a tuple (from_node, to_node) and sort to ensure consistency
            edge = tuple(sorted([path[i], path[i+1]]))

            # Add the edge only if it has not been added before
            if edge not in edges_added:
                dot.edge(path[i], path[i+1])  # Add an edge between two positions
                edges_added.add(edge)

    # Render the graph to a file
    output_path = dot.render(filename=output_file, cleanup=True)
    print(f"Graph image generated successfully: {output_path}")

def parse_input(input_str):
    """Converts an algebraic notation input (e.g. 'd4') to numerical coordinates."""
    column_mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    col, row = input_str[0], input_str[1]
    return (column_mapping[col], 9 - int(row))  

def get_coordinates():
    """Prompt the user to input starting and ending coordinates."""
    while True:
        start_input = input("Enter the starting position (e.g., d4): ").strip().lower()
        end_input = input("Enter the ending position (e.g., f5): ").strip().lower()

        # Check if input is valid
        if len(start_input) == 2 and len(end_input) == 2:
            try:
                start = parse_input(start_input)
                end = parse_input(end_input)
                if is_valid_move(*start) and is_valid_move(*end):
                    return start, end
                else:
                    print("Error: Coordinates out of bounds. Please enter valid positions (e.g., a1, h8).")
                    sys.exit()
            except KeyError:
                print("Error: Invalid coordinates entered. Use the format 'a1', 'h8', etc.")
                sys.exit()
        else:
            print("Error: Invalid format. Please enter coordinates in the format (e.g., d4).")
            sys.exit()


def main():
    print("Welcome to the Knight Path Finder!")
    print("You will be asked to enter a starting and an ending position for the knight.")
    
    start, end = get_coordinates()  # Get coordinates from user
    
    paths = bfs_knight_paths(start, end)
    if paths:
        print(f"\nNumber of shortest paths: {len(paths)}")
        for path in paths:
            print(path)

        generate_dot_graph(paths, start, end, output_file="chess_paths")
    else:
        print("No paths found!")

if __name__ == "__main__":
    main()

