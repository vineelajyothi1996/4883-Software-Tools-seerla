import csv
from graphviz import Digraph

# CSV file reader
def read_csv_file(filename):
    with open(filename, 'r') as file:
        data = csv.DictReader(file)
        rows = [row for row in data]
    return rows, set(row['clan'] for row in rows)

# creating family tree
def create_family_tree(rows, clans):
    g = Digraph('G', filename='family_tree.dot')
    
    # colors for clans
    colors = ['red', 'green', 'blue', 'purple', 'orange', 'pink', 'brown', 'gray']
    
    # sorting unique clan names
    sorted_clans = sorted(list(clans))
    
    # mapping clan names to colors
    clan_colors = {clan: colors[i % len(colors)] for i, clan in enumerate(sorted_clans)}
    
    # dictonary to hold names by generations
    generations = {}

    # creating nodes
    for row in rows:
        # get colors based on clan
        clan_color = clan_colors.get(row['clan'], 'yellow') 
        node_shape = 'rectangle' if row['gender'] == 'M' else 'oval'
        g.node(row['pid'], f"{row['name']}\nBorn: {row['byear']}\nDied: {row['dyear']}\nGender: {row['gender']}\nClan: {row['clan']}", color=clan_color, fillcolor=clan_color, style='filled', shape=node_shape)

        # adding node to according to generations
        if row['generation'] not in generations:
            generations[row['generation']] = []
        generations[row['generation']].append(row['pid'])
        
    # grouping nodes to equal generations
    for generation, nodes in generations.items():
        with g.subgraph() as s:
            s.attr(rank='same')
            for node in nodes:
                s.node(node)

    # Create the edges
    for row in rows:
        # edging from each parent 
        if row['parentId1']:
            g.edge(row['parentId1'], row['pid'])
        if row['parentId2']:
            g.edge(row['parentId2'], row['pid'])

        # linking as married to their spouse
        if row['spouseId'] and row['gender'] == 'M':
            g.edge(row['pid'], row['spouseId'], label='married', color='red')
    
    # Saving dot output file
    g.save()

# calling the functions
rows, clans = read_csv_file('family_tree_data.csv')
create_family_tree(rows, clans)
