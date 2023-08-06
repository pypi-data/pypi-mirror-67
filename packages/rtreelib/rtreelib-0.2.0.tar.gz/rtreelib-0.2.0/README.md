# rtreelib

Pluggable R-tree implementation in pure Python.

## Overview

Since the original R-tree data structure has been initially proposed in 1984, there have been
many variations introduced over the years optimized for various use cases [1]. However, when
working in Python (one of the most popular languages for spatial data processing), there is
no easy way to quickly compare how these various implementations behave on real data.

The aim of this library is to provide a "pluggable" R-tree implementation that allows swapping
out the various strategies for insertion, node deletion, and other behaviors so that their
impact can be easily compared (without having to install separate libraries and having to
make code changes to accommodate for API differences). Several of the more common R-tree
variations will soon be provided as ready-built implementations (see the **Status** section
below).

In addition, this library also provides utilities for inspecting the R-tree structure. It
allows creating diagrams (using matplotlib and graphviz) that show the R-tree nodes and
entries (including all the intermediate, non-leaf nodes), along with plots of their
corresponding bounding boxes. It also allows exporting the R-tree to PostGIS so it could
be examined using a GIS viewer like QGIS.

## Status

This library is currently in early development. The table below shows which R-tree variants
have been implemented, along with which operations they currently support:

| R-Tree Variant        | Insert                | Update                | Delete                |
|-----------------------|-----------------------|-----------------------|-----------------------|
| **Guttman** [2]       | :heavy_check_mark:    | :black_square_button: | :black_square_button: |
| **R\*-Tree** [3]      | :heavy_check_mark:    | :black_square_button: | :black_square_button: |

The library has a framework in place for swapping out the various strategies, making it
possible to add a new R-tree variant. However, given that this library is still early in
development, it is anticipated that this framework may need to be extended, resulting in
breaking changes.

Contributions for implementing additional strategies and operations are welcome. See
the section on **Extending** below.

## Setup

This package is available on PyPI and can be installed using pip:

```
pip install rtreelib
```

This package requires Python 3.6+.

There are additional optional dependencies you can install if you want to be able to
create diagrams or export the R-tree data to PostGIS. See the corresponding sections
below for additional setup information.

## Usage

To instantiate the default implementation and insert some entries:

```python
from rtreelib import RTree, Rect

t = RTree()
t.insert('a', Rect(0, 0, 3, 3))
t.insert('b', Rect(2, 2, 4, 4))
t.insert('c', Rect(1, 1, 2, 4))
t.insert('d', Rect(8, 8, 10, 10))
t.insert('e', Rect(7, 7, 9, 9))
```

The first parameter to the `insert` method represents the data, and can be of any data type
(though you will want to stick to strings, numbers, and other basic data types that can be
easily and succintly represented as a string if you want to create diagrams). The second
parameter represents the minimum bounding rectangle (MBR) of the associated data element.

The default implementation uses Guttman's original strategies for insertion, node splitting,
and deletion, as outlined in his paper from 1984 [2].

To use the R* implementation instead:

```python
from rtreelib import RStarTree, Rect

t = RStarTree()
t.insert('a', Rect(0, 0, 3, 3))
t.insert('b', Rect(2, 2, 4, 4))
t.insert('c', Rect(1, 1, 2, 4))
t.insert('d', Rect(8, 8, 10, 10))
t.insert('e', Rect(7, 7, 9, 9))
```

You can also create a custom implementation by inheriting from `RTreeBase` and providing
your own implementations for the various behaviors (insert, overflow, etc.). See the
following section for more information.

## Querying

Use the `query` method to find entries at a given location. The library supports querying
by either a point or a rectangle, and returns an iterable of matching entries that
intersect the given location.

To query using `Point`:

```python
entries = t.query(Point(2, 4))
```

Alternatively, you can also pass a tuple or list of 2 coordinates (`x` and `y`):

```python
entries = t.query((2, 4))
```

When querying by point, note that points that lie on the border (rather than the
interior) of a bounding rectangle are considered to intersect the rectangle.

To query using `Rect`:

```python
entries = t.query(Rect(2, 1, 4, 5))
```

Alternatively, you can also pass a tuple or list of 4 coordinates (the order is the
same as when using `Rect`, namely `min_x`, `min_y`, `max_x`, and `max_y`):

```python
entries = t.query((2, 1, 4, 5))
```

When querying by rectangle, note that the rectangles must have a non-zero intersection
area. Rectangles that intersect at the border but whose interiors do not overlap will
*not* match the query.

Note the above methods return entries rather than nodes. To get an iterable of leaf
nodes instead, use `query_nodes`:

```python
nodes = t.query_nodes(Rect(2, 1, 4, 5))
```

By default, this method will only return leaf-level nodes. To include all
intermediate-level nodes (including the root), set the optional `leaves` parameter
to `False` (it defaults to `True` if not passed in):

```python
all_nodes = t.query_nodes(Rect(2, 1, 4, 5), leaves=False)
```

## Extending

As noted above, the purpose of this library is to provide a pluggable R-tree implementation
where the various behaviors can be swapped out and customized to allow comparison. To that
end, this library provides a framework for achieving this.

As an example, the [`RTreeGuttman`](https://github.com/sergkr/rtreelib/blob/master/rtreelib/strategies/guttman.py)
class (aliased as `RTree`) simply inherits from `RTreeBase`, providing an implementation
for the `insert`, `choose_leaf`, `adjust_tree`, and `overflow_strategy` behaviors as follows:

```python
class RTreeGuttman(RTreeBase[T]):
    """R-Tree implementation that uses Guttman's strategies for insertion, splitting, and deletion."""

    def __init__(self, max_entries: int = DEFAULT_MAX_ENTRIES, min_entries: int = None):
        """
        Initializes the R-Tree using Guttman's strategies for insertion, splitting, and deletion.
        :param max_entries: Maximum number of entries per node.
        :param min_entries: Minimum number of entries per node. Defaults to ceil(max_entries/2).
        """
        super().__init__(
            max_entries=max_entries,
            min_entries=min_entries,
            insert=insert,
            choose_leaf=guttman_choose_leaf,
            adjust_tree=adjust_tree_strategy,
            overflow_strategy=quadratic_split
        )
```

Each behavior should be a function that implements a specific signature and performs a given
task. Here are the behaviors that are currently required to be specified:

* **`insert`**: Strategy used for inserting a single new entry into the tree.
  * Signature: `(tree: RTreeBase[T], data: T, rect: Rect) → RTreeEntry[T]`
  * Arguments:
    * `tree: RTreeBase[T]`: R-tree instance.
    * `data: T`: Data stored in this entry.
    * `rect: Rect`: Bounding rectangle.
  * Returns: `RTreeEntry[T]`
    * This function should return the newly inserted entry.
* **`choose_leaf`**: Strategy used for choosing a leaf node when inserting a new entry.
  * Signature: `(tree: RTreeBase[T], entry: RTreeEntry[T]) → RTreeNode[T]`
  * Arguments:
    * `tree: RTreeBase[T]`: R-tree instance.
    * `entry: RTreeEntry[T]`: Entry being inserted.
  * Returns: `RTreeNode[T]`
    * This function should return the leaf node where the new entry should be inserted. This
    node may or may not have the capacity for the new entry. If the insertion of the new node
    results in the node overflowing, then `overflow_strategy` will be invoked on the node.
* **`adjust_tree`**: Strategy used for balancing the tree, including propagating node splits,
updating bounding boxes on all nodes and entries as necessary, and growing the tree by
creating a new root if necessary. This strategy is executed after inserting or deleting an
entry.
  * Signature: `(tree: RTreeBase[T], node: RTreeNode[T], split_node: RTreeNode[T]) → None`
  * Arguments:
    * `tree: RTreeBase[T]`: R-tree instance.
    * `node: RTreeNode[T]`: Node where a newly-inserted entry has just been added.
    * `split_node: RTreeNode[T]`: If the insertion of a new entry has caused the node to
    split, this is the newly-created split node. Otherwise, this will be `None`.
  * Returns: `None`
* **`overflow_strategy`**: Strategy used for handling an overflowing node (a node that
contains more than `max_entries`). Depending on the implementation, this may involve
splitting the node and potentially growing the tree (Guttman), performing a forced
reinsert of entries (R*), or some other strategy.
  * Signature: `(tree: RTreeBase[T], node: RTreeNode[T]) → RTreeNode[T]`
  * Arguments:
    * `tree: RTreeBase[T]`: R-tree instance.
    * `node: RTreeNode[T]`: Overflowing node.
  * Returns: `RTreeNode[T]`
    * Depending on the implementation, this function may return a newly-created split
    node whose entries are a subset of the original node's entries (Guttman), or simply
    return `None`.

## Creating R-tree Diagrams

This library provides a set of utility functions that can be used to create diagrams of the
entire R-tree structure, including the root and all intermediate and leaf level nodes and
entries.

These features are optional, and the required dependencies are *not* automatically installed
when installing this library. Therefore, you must install them manually. This includes the
following Python dependencies which can be installed using pip:

```
pip install matplotlib pydot tqdm
```

This also includes the following system-level dependencies:

* TkInter
* Graphviz

On Ubuntu, these can be installed using:

```
sudo apt install python3-tk graphviz
```

Once the above dependencies are installed, you can create an R-tree diagram as follows:

```python
from rtreelib import RTree, Rect
from rtreelib.diagram import create_rtree_diagram


# Create an RTree instance with some sample data
t = RTree(max_entries=4)
t.insert('a', Rect(0, 0, 3, 3))
t.insert('b', Rect(2, 2, 4, 4))
t.insert('c', Rect(1, 1, 2, 4))
t.insert('d', Rect(8, 8, 10, 10))
t.insert('e', Rect(7, 7, 9, 9))

# Create a diagram of the R-tree structure
create_rtree_diagram(t)
```

This creates a diagram like the following:

![R-tree Diagram](https://github.com/sergkr/rtreelib/blob/master/doc/rtree_diagram.png "R-tree Diagram")

The diagram is created in a temp directory as a PNG file, and the default viewer
is automatically launched for convenience. Each box in the main diagram represents a node
(except at the leaf level, where it represents the leaf entry), and contains a plot that
depicts all of the data spatially. The bounding boxes of each node are represented using
tan rectangles with a dashed outline. The bounding box corresponding to the current node
is highlighted in pink.

The bounding boxes for the original data entries themselves are depicted in blue, and are
labeled using the value that was passed in to `insert`. At the leaf level, the corresponding
data element is highlighted in pink.

The entries contained in each node are depicted along the bottom of the node's box, and
point to either a child node (for non-leaf nodes), or to the data entries (for leaf nodes).

As can be seen in the above screenshot, the diagram depicts the entire tree structure, which
can be quite large depending on the number of nodes and entries. It may also take a while to
generate, since it launches matplotlib to plot the data spatially for each node and entry, and
then graphviz to generate the overall diagram. Given the size and execution time required to
generate these diagrams, it's only practical for R-trees containing a relatively small
amount of data (e.g., no more than about a dozen total entries). To analyze the resulting
R-tree structure when working with a large amount of data, it is recommended to export the
data to PostGIS and use a viewer like QGIS (as explained in the following section).

## Exporting to PostGIS

In addition to creating diagrams, this library also allows exporting R-trees to a
PostGIS database.

To do so, you will first need to install the [psycopg2](http://initd.org/psycopg/) driver.
This is an optional dependency, so it is not automatically installed when you install
this package. Refer to the
[installation instructions for psycopg2](http://initd.org/psycopg/docs/install.html) to
ensure that you have all the necessary system-wide prerequisites installed (C compiler,
Python header files, etc.). Then, install `psycopg2` using the following command (passing
the `--no-binary` flag to ensure that it is built from source, and also to avoid a console
warning when using `psycopg2`):

```
pip install psycopg2 --no-binary psycopg2
```

Once `psycopg2` is installed, you should be able to import the functions you need from the
`rtreelib.pg` module:

```python
from rtreelib.pg import init_db_pool, create_rtree_tables, export_to_postgis
```

The subsections below guide you throw how to use this library to export R-trees to the
database. You will first need to decide on your preferred method for connecting to the
database, as well as create the necessary tables to store the R-tree data. Once these
prerequisites are met, exporting the R-tree can be done using a simple function call.
Finally, this guide shows how you can visualize the exported data using QGIS, a popular
and freely-available GIS viewer.

### Initializing a Connection Pool

When working with the `rtreelib.pg` module, there are three ways of passing database
connection information:

1. Initialize a connection pool by calling `init_db_pool`. This allows using the other
functions in this module without having to pass around connection info.
2. Manually open the connection yourself, and pass in the connection object to the
function.
3. Pass in keyword arguments that can be used to establish the database connection.

The first method is generally the easiest - you just have to call it once, and not
have to worry about passing in connection information to the other functions. This
section explains this method, and the following sections assume that you are using
it. However, the other methods are also explained later on in this guide.

`init_db_pool` accepts the same parameters as the
[psycopg2.connect](http://initd.org/psycopg/docs/module.html#psycopg2.connect) function.
For example, you can pass in a connection string:

```python
init_db_pool("dbname=mydb user=postgres password=temp123!")
```

Alternatively, using the URL syntax:

```python
init_db_pool("postgresql://localhost/mydb?user=postgres&password=temp123!")
```

Or keyword arguments:

```python
init_db_pool(user="postgres", password="temp123!", host="localhost", database="mydb")
```

Next, before you can export an R-tree, you first need to create a few database
tables to store the data. The following section explains how to achieve this.

### Creating Tables to Store R-tree Data

When exporting an R-tree using this library, the data is populated inside three
tables:

* `rtree`: This tables simply contains the ID of each R-tree that was exported.
This library allows you to export multiple R-trees at once, and they are
differentiated by ID (you can also clear the contents of all tables using
`clear_rtree_tables`).
* `rtree_node`: Contains information about each node in the R-tree, including
its bounding box (as a PostGIS geometry column), a pointer to the parent entry
containing this node, and the level of this node (starting at 0 for the root).
The node also contains a reference to the `rtree` that it is a part of.
* `rtree_entry`: Contains information about each entry in the R-tree, including
its bounding box (as a PostGIS geometry column) and a pointer to the node
containing this entry. For leaf entries, this also contains the value of the
data element.

These tables can be created using the `create_rtree_tables` function. This is
something you only need to do once.

This function can be called without any arguments if you have established the
connection pool, and your data does not use a spatial reference system (`srid`).
However, generally when working with spatial data, you will have a particular
SRID that your data is in, in which case you should pass it in to ensure that
all geometry columns use the correct SRID:

```python
create_rtree_tables(srid=4326)
```

You can also choose to create the tables in a different schema (other than `public`):

```python
create_rtree_tables(srid=4326, schema="temp")
```

However, in this case, be sure to pass in the same schema to the other functions in
this module.

You can also pass in a `datatype`, which indicates the type of data stored in the leaf
entries (i.e., the type of the data you pass in to the `insert` method of `RTree`).
This can either be a string containing a PostgreSQL column type:

```python
create_rtree_tables(srid=4326, datatype='VARCHAR(255)')
```

Or a Python type, in which case an appropriate PostgreSQL data type will be inferred:

```python
create_rtree_tables(srid=4326, datatype=int)
```

If you don't pass anything in, or an appropriate PostgreSQL data type cannot be
determined from the Python type, the column type will default to `TEXT`, which allows
storing arbitrary-length strings.

When passing a string containing a PostgreSQL column type, you also have the option
of adding a modifier such as `NOT NULL`, or even a foreign key constraint:

```python
create_rtree_tables(srid=4326, datatype='INT REFERENCES my_other_table (my_id_column)')
```

### Exporting the R-tree

To export the R-tree once the tables have been created, simply call the
`export_to_postgis` function, passing in the R-tree instance (and optionally an SRID):

```python
rtree_id = export_to_postgis(tree, srid=4326)
```

This function populates the `rtree`, `rtree_node`, and `rtree_entry` tables with
the data from the R-tree, and returns the ID of the newly-inserted R-tree in the
`rtree` table.

Note that if you used a schema other than `public` when calling
`create_rtree_tables`, you will need to pass in the same schema when calling
`export_to_postgis`:

```python
rtree_id = export_to_postgis(tree, srid=4326, schema='temp')
```

### Viewing the Data Using QGIS

[QGIS](https://qgis.org/en/site/) is a popular and freely-available GIS viewer which
can be used to visualize the exported R-tree data. To do so, launch QGIS and create
a new project. Then, follow these steps to add the exported R-tree data as a layer:

* Go to Layer → Add Layer → Add PostGIS Layers
* Connect to the database where you exported the data
* Select either the `rtree_node` or `rtree_entry` table, depending on which part of
the structure you wish to visualize. For this example, we will be looking at the
nodes, so select `rtree_node`.
* Optionally, you can set a layer filter to only include the nodes belonging to a
particular tree (if you exported multiple R-trees). To do so, click the
**Set Filter** button, and enter a filter expression (such as `rtree_id=1`).
* Click **Add**

At this point, the layer will be displaying all nodes at every level of the tree,
which may be a bit hard to decipher if you have a lot of data. After adjusting the
layer style to make it partially transparent, here is an example of what an R-tree
with a couple hundred leaf entries might look like (41 nodes across 3 levels):

![QGIS - All Nodes](https://github.com/sergkr/rtreelib/blob/master/doc/qgis_all_nodes.png)

To make it easier to understand the structure, it might help to be able to view each
level of the tree independently. To do this, double click the layer in the Layers
panel, switch to the Style tab, and change the style type at the top from
"Single symbol" (the default) to "Categorized". Then in the Column dropdown, select
the "level" column. You can optionally assign a color ramp or use random colors so
that each level gets a different color. Then click **Classify** to automatically
create a separate style for each layer:

![QGIS - Layer Style](https://github.com/sergkr/rtreelib/blob/master/doc/qgis_layer_style.png)

Now in the layers panel, each level will be shown as a separate entry and can be
toggled on and off, making it possible to explore the R-tree structure one level
at a time:

![QGIS - Layers Panel](https://github.com/sergkr/rtreelib/blob/master/doc/qgis_layers_panel.png)

The advantage with exporting the data to QGIS is you can also bring in your
original dataset as a layer to see how it was partitioned spatially. Further,
you can import multiple R-trees as separate layers and be able to compare them
side by side.

Below, I am using a subset of the FAA airspace data for a portion of the
Northeastern US, and then toggling each level of the `rtree_node` layer individually
so we can examine the resulting R-tree structure one level at a time. After
compositing these together, you can see how the Guttman R-Tree performs against
R*.

**Guttman**:

![Guttman R-Tree](https://github.com/sergkr/rtreelib/blob/master/doc/qgis_guttman.gif)

**R\*-Tree**:

![R*-Tree](https://github.com/sergkr/rtreelib/blob/master/doc/qgis_rstar.gif)

It is evident that R* has resulted in more square-like bounding rectangles with
less overlap at the intermediate levels, compared to Guttman. The areas of overlap
are made especially evident when using a partially transparent fill. Ideally, the
spatial partitioning scheme should aim to minimize this overlap, since a query to
find the leaf entry for a given point would require visiting multiple subtrees if
that point happens to land in one of these darker shaded areas of overlap.

You can also write a query to analyze the amount of overlap that resulted in each
level of the tree. For example, the query below returns the total amount of overlap
area of all nodes at level 2 of an exported R-tree having ID 1:

```postgresql
SELECT ST_Area(ST_Union(ST_Intersection(n1.bbox, n2.bbox))) AS OverlapArea
FROM temp.rtree t
  INNER JOIN temp.rtree_node n1 ON n1.rtree_id = t.id
  INNER JOIN temp.rtree_node n2 ON n2.rtree_id = t.id AND n1.level = n2.level
WHERE
  t.id = 1
  AND n1.level = 2
  AND ST_Overlaps(n1.bbox, n2.bbox)
  AND n1.id <> n2.id;
```

Extending this even further, you can compare the total overlap area of multiple exported
R-trees by level:

```postgresql
SELECT
  CASE t.id
    WHEN 1 THEN 'Guttman'
    WHEN 2 THEN 'R*'
  END AS tree,
  n.level,
  ST_Area(ST_Union(ST_Intersection(n.bbox, n2.bbox))) AS OverlapArea
FROM temp.rtree t
  INNER JOIN temp.rtree_node n ON n.rtree_id = t.id
  INNER JOIN temp.rtree_node n2 ON n2.rtree_id = t.id AND n.level = n2.level
WHERE
  ST_Overlaps(n.bbox, n2.bbox)
  AND n.id <> n2.id
GROUP BY
  t.id,
  n.level
ORDER BY
  t.id,
  n.level;
```

The above query may return a result like the following:

tree    | level | OverlapArea |
--------|-------|-------------|
Guttman | 1     | 7.89e+11    |
Guttman | 2     | 9.12e+11    |
Guttman | 3     | 4.75e+11    |
R*      | 1     | 3.97e+11    |
R*      | 2     | 4.35e+11    |
R*      | 3     | 1.80e+11    |

In the above example, the R*-Tree (`id`=2) achieved a smaller overlap area at
every level of the tree compared to Guttman (`id`=1).

### Cleaning Up

As mentioned above, when you call `export_to_postgis`, the existing data in the
tables is *not* cleared. This allows you to export multiple R-trees at once and
compare them side-by-side.

However, for simplicity, you may wish to clear out the existing data prior to
exporting new data. To do so, call `clear_rtree_tables`:

```python
clear_rtree_tables()
```

This will perform a SQL `TRUNCATE` on all R-tree tables.

Note that if you created the tables in a different schema (other than `public`),
you will need to pass in that same schema to this function:

```python
clear_rtree_tables(schema='temp')
```

You may also wish to completely drop all the tables that were created by
`create_rtree_tables`. To do so, call `drop_rtree_tables`:

```python
drop_rtree_tables()
```

Again, you may need to pass in a schema if it is something other than `public`:

```python
drop_rtree_tables(schema='temp')
```

### Alternate Database Connection Handling Methods

As mentioned earlier in this guide, instead of initializing a connection pool,
you have other options for how to handle establishing database connections when
using this library. You can choose to handle opening and closing the connection
yourself and pass in the connection object; alternatively, you can pass in the
connection information as keyword arguments.

To establish the database connection yourself, the typical usage scenario might
look like this:

```python
import psycopg2
from rtreelib import RTree, Rect
from rtreelib.pg import init_db_pool, create_rtree_tables, clear_rtree_tables, export_to_postgis, drop_rtree_tables


# Create an RTree instance with some sample data
t = RTree(max_entries=4)
t.insert('a', Rect(0, 0, 3, 3))
t.insert('b', Rect(2, 2, 4, 4))
t.insert('c', Rect(1, 1, 2, 4))
t.insert('d', Rect(8, 8, 10, 10))
t.insert('e', Rect(7, 7, 9, 9))

# Export R-tree to PostGIS (using explicit connection)
conn = None
try:
    conn = psycopg2.connect(user="postgres", password="temp123!", host="localhost", database="mydb")
    create_rtree_tables(conn, schema='temp')
    rtree_id = export_to_postgis(t, conn=conn, schema='temp')
    print(rtree_id)
finally:
    if conn:
        conn.close()
```

You can also pass in the database connection information separately to each method as
keyword arguments. These keyword arguments should be the same ones as required by the
[psycopg2.connect](http://initd.org/psycopg/docs/module.html#psycopg2.connect) function:

```python
rtree_id = export_to_postgis(tree, schema='temp', user="postgres", password="temp123!", host="localhost", database="mydb")
```

## References

[1]: Nanopoulos, Alexandros & Papadopoulos, Apostolos (2003):
["R-Trees Have Grown Everywhere"](https://pdfs.semanticscholar.org/4e07/e800fe71505fbad686b08334abb49d41fcda.pdf)

[2]:  Guttman, A. (1984):
["R-trees: a Dynamic Index Structure for Spatial Searching"](http://www-db.deis.unibo.it/courses/SI-LS/papers/Gut84.pdf)
(PDF), *Proceedings of the 1984 ACM SIGMOD international conference on Management of data – SIGMOD
'84.* p. 47.

[3]: Beckmann, Norbert, et al.
["The R*-tree: an efficient and robust access method for points and rectangles."](https://infolab.usc.edu/csci599/Fall2001/paper/rstar-tree.pdf)
*Proceedings of the 1990 ACM SIGMOD international conference on Management of data.* 1990.
