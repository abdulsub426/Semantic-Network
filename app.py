# app.py
# Semantic Network Simulation using Streamlit
# Includes text display + graph visualization

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# -------------------------------
# Sample Semantic Network Data
# -------------------------------
semantic_network = {
    "Dog": {"is-a": ["Animal"], "has-a": ["Tail", "Legs"]},
    "Cat": {"is-a": ["Animal"], "has-a": ["Whiskers", "Tail"]},
    "Bird": {"is-a": ["Animal"], "can": ["Fly"], "has-a": ["Wings", "Beak"]},
    "Animal": {"is-a": ["Living Being"]},
}

# -------------------------------
# Streamlit App Layout
# -------------------------------
st.title("Semantic Network Simulation")
st.write("Enter an entity to see its relationships:")

# User input for entity
entity_input = st.text_input("Entity name:")

if entity_input:
    entity_input = entity_input.strip()  # Clean input
    
    if entity_input in semantic_network:
        st.subheader(f"Relationships for '{entity_input}':")
        relationships = semantic_network[entity_input]
        
        # Display each relationship
        for rel_type, rel_values in relationships.items():
            st.write(f"**{rel_type}:** {', '.join(rel_values)}")
        
        # -------------------------------
        # Graph Visualization
        # -------------------------------
        st.subheader("Graph Visualization:")
        G = nx.DiGraph()  # Directed graph
        
        # Add edges based on relationships
        for rel_type, rel_values in relationships.items():
            for val in rel_values:
                G.add_edge(entity_input, val, label=rel_type)
        
        pos = nx.spring_layout(G)
        edge_labels = nx.get_edge_attributes(G, 'label')
        
        plt.figure(figsize=(6,4))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12, arrows=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
        st.pyplot(plt)
    
    else:
        st.warning(f"Entity '{entity_input}' not found in the network.")
