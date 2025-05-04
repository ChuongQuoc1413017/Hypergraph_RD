---
title: 'Gala: A Python package for galactic dynamics'
tags:
  - Python
  - hypergraph
  - dynamics
authors:
  - name: Quoc Chuong Nguyen
    orcid: 0000-0002-3260-9967
    equal-contrib: true
    affiliation: 1 # (Multiple affiliations must be quoted)
  - name: Trung Kien Le
    equal-contrib: true # (This is how you can denote equal contributions between multiple authors)
    affiliation: 2
affiliations:
 - name: Department of Mathematics, University at Buffalo, New York, NY 14260, United States
   index: 1
 - name: epartment of Applied Physics, Stanford University, Stanford, CA 94305, United States
   index: 2
date: 03 May 2025
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary

Hypergraphs, or generalization of graphs such that edges can contain more than two nodes, have become increasingly prominent in understanding complex network analysis. Unlike graphs, hypergraphs have relatively few supporting platforms, and such dearth presents a barrier to more widespread adaptation of hypergraph computational toolboxes that could enable further research in several areas. Here, we introduce \textbf{HyperRD}, a Python package for hypergraph computation, simulation, and interoperability with other powerful Python packages in graph and hypergraph research. Then, we will introduce two models on hypergraph, the general Schelling's model and the SIR model, and simulate them with HyperRD.

# Statement of need

Hypergraphs, a natural extension of traditional graphs, have emerged as a powerful mathematical tool for modeling complex relationships and structures across various domains [@federico2023; @bianconi2021; @battiston2021]. Unlike graphs, hypergraphs allow for edges to connect more than two vertices, providing a more expressive representation of intricate dependencies. Therefore, hypergraphs have a profound significance in diverse disciplines, including computer science [@santoro2023], biology [@klamt2009], and social networks [@federico2022]. The study of hypergraphs in computer science has far-reaching implications for algorithm design, especially in addressing optimization problems where traditional graph models may prove inadequate, as noted in \cite{dis_program}. Hypergraphs also capture complexity in complex interacting networks and provide a glimpse into qualitatively different emergent dynamics [@Zhang_2023]. Shifting the focus to the biological realm, hypergraphs find valuable applications in modeling molecular interactions and regulatory networks. Their unique capability to represent interactions among multiple biological entities, such as genes or proteins, contributes to a more nuanced understanding of the intricate relationships governing biological processes, as highlighted in [@genomic]. This dual application underscores the interdisciplinary significance of hypergraphs in both computational and biological domains.

For this reason, we introduce a novel Python-based platform designed to simulate and analyze hypergraphs, addressing a gap in current computational resources available to researchers and practitioners in mathematics and computer science. Our platform, distinguished by its near-comprehensive range of features, stands out in its ability to represent, manipulate, visualize, and analyze hypergraphs with a level of versatility and depth not commonly found in existing tools [@hat; @hypernetx; @halp; @hmetis; @phoenix; @hyperg; @xgi]. A significant feature of our platform is its interoperability, enabling integration with other established platforms and tools. This feature is instrumental in fostering a universal workspace, where users can leverage the strengths of various platforms to conduct more intricate and expansive research on hypergraphs. By bridging these tools, our platform facilitates a more efficient and cohesive workflow and propels the exploration of hypergraphs into new realms, allowing for more complex, interdisciplinary inquiries and applications.

# State of the field

The development of platforms for simulating normal graphs in applied mathematics and computer science has seen substantial progress over the past decades. One of the most significant contributions has been the NetworkX library in Python, which offers extensive tools for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks [@networkx]. NetworkX's ease of use and flexibility have made it a popular choice among researchers. Another notable platform is Gephi, an open-source network visualization software that allows for the exploration and understanding of graph structures through sophisticated graphical representations [@gephi]. These platforms have been instrumental in advancing the field of graph theory by facilitating complex analyses and visualizations.

The rationale for developing platforms specifically for simulating hypergraphs arises from the limitations of normal graph simulation tools in capturing multi-way relationships. While normal graphs represent binary relationships between entities, hypergraphs are capable of representing more complex, higher-order interactions among multiple entities simultaneously. This capability is crucial in fields such as computational biology, social network analysis, and complex system modeling, where interactions often occur among more than two entities. Therefore, the development of hypergraph-specific platforms is essential to address the nuanced requirements of these advanced applications, providing more accurate and comprehensive tools for researchers and practitioners. Notwithstanding the commendable attributes of some existing platforms such as HAT [@hat], HyperNetX [@hypernetx], halp [@halp], hMETIS [@hmetis], Phoenix [@phoenix], HyperG [@hyperg], and XGI [@xgi], each of them has their own limitations. These limitations, in turn, accentuate the compelling need for a Python-based simulation tool characterized by heightened comprehensiveness and versatility. The choice of Python as the language of the proposed simulation platform stems from its widespread adoption and versatility in scientific computing,  ensuring accessibility and adaptability for researchers and practitioners across various disciplines. Python's expressive syntax and rich ecosystem of libraries make it an ideal candidate for developing a tool that caters specifically to the nuanced requirements of hypergraph simulation.

# Acknowledgements

This work did not receive funding from any public, commercial, or non-profit organization. Q.C. and T.K. coordinated the project. Q.C. is the leading developer. All authors contributed to the library.

# References
