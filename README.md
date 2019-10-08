# STREAM.SeedEPGStructure

Seeding the initial elastic principal graph

* init_nodes_pos: `array`, shape = [n_nodes,n_dimension], optional (default: `None`)
    initial node positions
* init_edges: `array`, shape = [n_edges,2], optional (default: `None`)
    initial edges, all the initial nodes should be included in the tree structure
* clustering: `str`, optional (default: 'kmeans')
    Choose from {{'ap','kmeans','sc'}}
    clustering method used to infer the initial nodes.
    'ap' affinity propagation
    'kmeans' K-Means clustering
    'sc' spectral clustering
* damping: `float`, optional (default: 0.75)
    Damping factor (between 0.5 and 1) for affinity propagation.
* pref_perc: `int`, optional (default: 50)
    Preference percentile (between 0 and 100). The percentile of the input similarities for affinity propagation.
* n_clusters: `int`, optional (default: 10)
    Number of clusters (only valid once 'clustering' is specificed as 'sc' or 'kmeans').
* max_n_clusters: `int`, optional (default: 200)
    The allowed maximum number of clusters for 'ap'.
* nb_pct: `float`, optional (default: 0.1)
    Neighbor percentage. The percentage of points used as neighbors for spectral clustering.
