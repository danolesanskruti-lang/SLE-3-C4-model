# SLE-3: Architectural Design using Full C4 Model

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Student:** Sanskruti Sandeep Danole  
**PRN:** 25UAM059  
**Division:** A  
**System:** BFS and DFS Graph Search System

## 1. System Description
This project presents the architecture of a graph search system using the complete C4 Model. The system accepts a graph, start node, and goal node from a user and searches for a path using Breadth-First Search (BFS) or Depth-First Search (DFS). It keeps track of visited nodes and returns the discovered path and search information.

## 2. C4 Model Diagrams
- Level 1 – Context: diagrams/01-context.svg
- Level 2 – Container: diagrams/02-container.svg
- Level 3 – Component: diagrams/03-component.svg
- Level 4 – Code: diagrams/04-code.svg

The PlantUML source files are stored in the plantuml folder.

## 3. Main Code
The reference implementation is in bfs_dfs.py and continues the BFS/DFS work from SLE-2.

Main functions:
- bfs(graph, start, goal): performs Breadth-First Search.
- dfs(graph, start, goal): performs Depth-First Search.
- benchmark(search_function, name): measures repeated execution.
- GRAPH: stores the graph as an adjacency-list dictionary.

## 4. Design Decisions
1. BFS and DFS are kept inside one Search Engine because both solve the same graph-search problem with different traversal strategies.
2. The visited set is represented separately at the architecture level to prevent repeated exploration and loops.
3. Only the Search Engine is expanded in the Component level.
4. The Code level contains names and responsibilities rather than large source-code blocks.

## 5. AI Contribution Note
**AI tools used:** ChatGPT for architecture planning, C4-level organization, explanation drafting, and diagram-source preparation.

**What AI helped with:** Converting the BFS/DFS system into a clear four-level C4 architecture and preparing concise documentation.

**What I did myself:** Selected the BFS/DFS system from the SLE-2 work, reviewed the architecture, verified the relationship between the code and diagrams, and prepared the repository.

## 6. Repository Structure
- README.md
- bfs_dfs.py
- diagrams/01-context.svg
- diagrams/02-container.svg
- diagrams/03-component.svg
- diagrams/04-code.svg
- plantuml/01-context.puml
- plantuml/02-container.puml
- plantuml/03-component.puml
- plantuml/04-code.puml

## 7. SLE-3 Checklist
- [x] SLE-2 BFS/DFS system continued
- [x] Context Diagram
- [x] Container Diagram with 4–7 main boxes
- [x] Component Diagram for one main container
- [x] Code Level Overview
- [x] Design Decisions
- [x] AI Contribution Note
- [x] SVG diagrams
- [x] PlantUML source files
- [x] English documentation

Architecture: Context → Container → Component → Code.
