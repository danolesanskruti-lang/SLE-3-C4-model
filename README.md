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


## 2.1 PlantUML Web Editor Rendering

The C4 diagram source is written in PlantUML and can be opened in the PlantUML Web Editor for live rendering and SVG export. PlantUML supports SVG output from its web service.

- [Level 1 – Context: Open in PlantUML](https://plantuml.joor.net/editor/svg/TP31JiCm38RlUGfhzsf2uiG1JQmC8N6hk76nMfD6f4vaksDxUvAkG-F0APBz_zzdPQU6OlCKdGMB1FjxUACZHRY31lQ9ZKu6RK0lE9N9qw7RjeSENWJp21sXzEKvgz7az2jmnfhhqvGJ4rjdvy8KwWtPHxg9w8X3-WxiuHEZaiFUai2xahZVE6oA3hRmZt03g5VtJUUIVEKyM-ckZHODb_ppoKWOewigQ9h7bG0Fe1GBHG6ZJn9id3uOUO0iwHW6Kl0LxAw0lzrb1qEnk7LMrukZWfSRCjfuGGhf7CtjY8Voypy0)
- [Level 2 – Container: Open in PlantUML](https://plantuml.joor.net/editor/svg/TLF1Qjmm4BthAuQz9akWvEH32Sas9T3GacrxsiiWJMmHUUHgHjikfVzUIVQcpg4dmynxJ--zmJUYc3IFmQZNG71t3P_eI07UmHRk8YjwfWGxZtt2iSnkx_TNk_izV4mu3R0dJBPyJg8q6ddnF675sJXEaObrhwUYciWgSXze1P41NVpfkOTd3486hSO4tuIIUON3fZm7L_2V1pVmUurzu2ahF4QN0ntuYIpv8mdqbNW9BUWbz173WP4TOEXZyZeKjqFqbZQ00arZBRey-87xKaHHpIor0oXUYwl6cI5hqdSlNiaLvuyqndHwDVKreNqHe5zJYAa0E3gI9Z83ro9VK0SeAIABfcpLHow2JoGvw85limzEuDap1fWgj6PARTi4AtqjzpdhkfwTbodWIVvnPKxgKB49p0JpnzIRm7RxVYu7khbHk81sI59AOkPL1Is5TMUzH3yoYPfbNY5BAHqSbvvQ3MOPln4v8yhrDCjQfDNJWVDYuv5gcIr9jM_QheAMqDtIqroFMQOLqB9rC_NYlByXTkMN-0i0)
- [Level 3 – Component: Open in PlantUML](https://plantuml.joor.net/editor/svg/LP8_JmCn3CNtV0ghUyK0KmTKqJyiL0AkOnUJStDHhyufSGe8yTrnWdgwRedzUo_FLfP9C4e-zqQyz0Ih1tYX2_Lm3tDOXVCGc5XWxT55F6kj8OosWmqxpsJIoVE0fMElR2FVwXF92hBhfqZgi0sVdXqSiKzaHWPcDwup-9dsjZ6mU8gmGqP7yS1lcJB1CKHusZPm1usWFTNxUjlC01DSDLEVpTVGXqYjZY07taVL9BZuv4Lh75fALNh5fjBdW3tiAQbkrL7HsHnZMKpH0Jhqd0ISOjMZy5FzAqe7xsI3KZ5R2Jh4JZLIT83SwhuaHpqFIbQBIfjVCqu_dp-EsM01jkJGsVFGej0jLkCkRZAQMYlDQgpT4bQVHJLgpMXSYD5h0Pd71P5ttKV8CPb_Xyb39JJeHz8SI-9MVzCV)
- [Level 4 – Code: Open in PlantUML](https://plantuml.joor.net/editor/svg/TL5BRy8m3BxdL_Z8f1Okd3XC353POT8G_G78Izms8uykIOkgQVzzQTUAFTZDzlVmPtdj0xhGQCM238fWkuGdQad14bBOMa5Z-zoIQoLTudIJvOjTbZD_bgP6XngurRKrP48UkkZXY0SqfQ9l55-Xi1TfIYXGUM9SeVUmTrXNEmm8xsn_V3WyCXIloCdmBbNI1n2I1saDkevzZ9gSqF4gQyo0-AXyAVoix9qI6Av9eBIexfZuPpuvRUAUIgCxznvJFVE3_waO5oHWKDDLTEX2PSsnCK5gYa9kbQAlA7D1Rmsn7fZNv8eJjv56BcglXwRf_PyJLk2RkbQIF0nvsMz2BxgcZVG1XodZJVxFe2k8qHg21SGsle6joOZuzay0)

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
