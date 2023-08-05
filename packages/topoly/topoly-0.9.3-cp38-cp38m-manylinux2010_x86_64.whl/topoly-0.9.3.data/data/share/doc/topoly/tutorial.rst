.. _tutorial:

***************
Tutorial
***************
Here is how to use our package:

* For detailed reference of each function please have a look into our :ref:`Documentation`.
* For examples check our `topoly_tutorial project on GitHub 
  <https://github.com/ilbsm/topoly_tutorial/>`_.

Whatever you want to do, start by importing topoly functions::

    >>from topoly import *

Accepted structures
====================
Examples: `topoly_tutorial/import_and_find.py 
<https://github.com/ilbsm/topoly_tutorial/blob/master/import_and_find.py/>`_.

The first step is to provide the structure you want to analyze.
Topoly is flexible in this case and supports 2 ways of input (file and variable) and multiple formats:

From file:

* .xyz  -- three columns with coordinates, or four columns, first with index and others with coordinates,
* .pdb  -- standard format for protein structure data,
* .cif  -- standard format for crystallographic structure data,
* .math -- mathematica array format (nested curly-braced lists)

From variable:

* python nested lists,
* PD code,
* EM code.

Importing a structure works the same way in each of topoly functions.


What is PD code and EM code?
-----------------------------

EM code (Ewing-Millett code) and PD code (planat diagram code) are methods of 
descirbing knots in detail. To find EM code of your knot diagram:
    
* Give each crossing a number 
* Give each crossing a sign according to,
* For each crossing:

  * Name "a" direction of outgoing overpassing arc. 
  * Name every other direction in clockwise order ”b", "c" and „d".
  * In this way, every arc is consists of two directions, each described
    by a number and a letter.

* A code for a crossing consists of its number, its sign, and a list of 
  directions coming from other crossings.
* A code for a structure consists of a list of codes for crossings.

.. figure:: _static/emcode.png
    :scale: 25%
    :alt: EM code

Finding PD code is easier:

* Go along the structure according to its orientation and after each 
  crossing asign next number to it (starting from 1).
* Each crossing is described by "X" symbol with numbers of its neighbouring
  arcs: counter-clockwise starting from ingoing underpassing.
* Structure code is described by a list of its crossings.

In case of spatial graphs (theta-curves, handcuffs) PD code can be extened. 
In such a case every vertex connected to three arcs is described by "V" 
symbol with numbers of its neighbouring arcs in any order.

.. figure:: _static/pdcode.png
    :scale: 25%
    :alt: PD code

You can calculate PD code of a given topology using **import_structure** 
function and translate your PD code into EM code (or vice-versa) using 
**translate_code**.


Knot, link, theta-curve and handcuff type identification (invariants calculation)      
==================================================================================
Examples: `topoly_tutorial/knots_links.py 
<https://github.com/ilbsm/topoly_tutorial/blob/master/knots_links.py/>`_.

Documentation section: :ref:`doc_invariants`. 

In Topoly there is a number of knot invariant calculating functions, with only
one obligatory parameter, the structure itself::

    >>alexander(structure)
    >>jones(structure)   
    >>conway(structure) 
    >>homfly(structure)
    >>kauffman_bracket(structure)
    >>kauffman_polynomial(structure)
    >>blmho(structure)  
    >>yamada(structure)
    >>aps(structure)
    >>writhe(structure)

Links to documentation: 
`Alexander <https://topoly.cent.uw.edu.pl/documentation.html#topoly.alexander>`_, 
`Jones <https://topoly.cent.uw.edu.pl/documentation.html#topoly.jones>`_, 
`Conway <https://topoly.cent.uw.edu.pl/documentation.html#topoly.conway>`_, 
`HOMFLY <https://topoly.cent.uw.edu.pl/documentation.html#topoly.homfly>`_, 
`Kauffman bracket <https://topoly.cent.uw.edu.pl/documentation.html#topoly.kauffman_bracket>`_, 
`Kauffman polynomial <https://topoly.cent.uw.edu.pl/documentation.html#topoly.kauffman_polynomial>`_, 
`BLM/Ho <https://topoly.cent.uw.edu.pl/documentation.html#topoly.blmho>`_, 
`Yamada <https://topoly.cent.uw.edu.pl/documentation.html#topoly.yamada>`_, 
`APS bracket <https://topoly.cent.uw.edu.pl/documentation.html#topoly.aps>`_, 
`writhe <https://topoly.cent.uw.edu.pl/documentation.html#topoly.writhe>`_, 
All of them have optional input paramters. Understanding their usage may be
crucial for using them. They can be divided into three categories, defining:

* how input chain should be closed (closure, tries),
* how structure should be simplified (reduce_method, max_cross),
* if and which subchains should be analysed (boundaries, matrix, level, matrix_plot).


Which invariant should I choose?
----------------------------------
Here is a table presenting short characteristics of available invariants.

.. list-table:: Comparison of available invariant calculating algorithms.
   :widths: 25 25 25 25 25
   :header-rows: 1

   * - Invariant
     - Relative speed
     - Check chirality
     - Identify links
     - Identify theta-curves and handcuffs
   * - Alexander
     - 1st (fastest)
     - no
     - no
     - no
   * - Conway
     - 2nd (faster)
     - no
     - no
     - no
   * - Jones
     - 2nd (faster)
     - yes
     - yes
     - no
   * - HOMFLY
     - 2nd (faster)
     - yes
     - yes
     - no
   * - Kauffman polynomial
     - 3rd (average)
     - yes
     - yes
     - no
   * - BLM/Ho
     - 3rd (average)
     - no
     - yes
     - no
   * - Yamada
     - 4th (slower)
     - yes
     - yes
     - yes
   * - Kauffman bracket
     - 5th (slowest)
     - yes
     - yes
     - no


.. _tutorial_closure:

Structure closing -- closure, tries 
-------------------------------------
If your input structure is a **closed chain** (or you want to connect directly
two endpoints of your structure), you need to pass closure=Closure.CLOSED 
(or closure=0) argument. 

If your structure is an **open chain**, then two endpoints of a structure `have to
be connected somehow 
<https://portlandpress.com/biochemsoctrans/article-abstract/41/2/533/66520>`_. 
In that case Topoly creates a big sphere around the structure,
with the center at the geometric center of the structure. Then each of the 
structure's endpoints are connected with a chosen point on the big sphere. 
Finally these big sphere points are connected with a sphere arc. Thanks to this
operation an open chain can be closed. In short the algorithm performs the
following steps:
whole structure -> structures last point -> first point on the big
sphere -> second point on the big sphere -> structures first point -> whole
structure.

.. figure:: _static/domykanie.png
    :scale: 70%
    :alt: Closure using a sphere
    
    Closure using a sphere (left) and direct closure (right).

In Topoly there are five slightly different methods of creating these two
points on the big sphere: two deterministic and three random.

Deterministic closure:

* closure = Closure.MASS_CENTER (closure = 1) segments are added to two 
  endpoints in the direction "going out of the center of mass";
* closure = Closure.DIRECTION (closure = 5) segments connecting each endpoint 
  with a sphere, are parallel and their direction is user defined.

Random closure:

* closure = Closure.TWO_POINTS (closure = 2): each endpoint is connected with 
  a different random point on the big sphere, **this is the default option**;
* closure = Closure.ONE_POINT (closure = 3): both endpoints are connected with
  the same random point on the big sphere;
* closure = Closure.RAYS (closure = 4) like DIRECTION but direction is randomly
  chosen.

For random closure there is another parameter available: **tries** (default 
200). It specifies how many times the operation of closing and checking the
topology must be repeated. Naturally it requires longer computations, but also
gives more accurate information about the structure.

.. _tutorial_reduction:

Structure reduction -- reduce_method, max_cross 
-------------------------------------------------
After closing the structure, the second step of the algorithm is the creation
of a 2D projection of the 3D structure. The subsequent analysis is performed 
based on the crossings found on this 2D projection. Many of such crossings can
be reduced, because they do not change the topology of the structure. This is
important, because the invariant's calculation time strongly depends on the
number of crossings.

In knot theory such reductions are made using the Reidemeister moves.

.. figure:: _static/ReidemeisterMoves.gif
    :scale: 80%
    :alt: Reidemeister moves
    
    Three types of Reidemeister moves

There is another method: `KMT algorithm <https://doi.org/10.1063/1.460889>`_. 
This algorithm analyzes all triangles in a chain made by three consecutive 
points, and removes the middle point in case a given triangle is not 
intersected by any other segment of the chain. In effect, after a number of 
iterations, the initial chain is replaced by a shorter chain of the same
topological type.

.. figure:: _static/kmt.png
    :scale: 40%
    :alt: KMT algorithm
    
    Representation of KMT algorithm

In Topoly there are three available reduction methods:

* reduce_method = ReduceMethod.KMT (reduce_method = 1)
* reduce_method = ReduceMethod.REIDEMEISTER (reduce_method = 2)
* reduce_method = ReduceMethod.EASY (reduce_method = 3)

Some complicated chains can still have many crossings after reduction. 
The calculation of their polynomial can last very long. For such situations there
is the **max_cross** parameter (default 15). If the number of crossings after the
reduction is larger than the max_cross parameter, then the calculation is stopped.

.. _tutorial_subchain:

Subchain topology -- boundaries, matrix, density, level, matrix_plot
----------------------------------------------------------------------
If you are interested in the topology of certain parts of a chain, you can use the
**boundaries** parameter. It accepts the indices of the first and the last desired
aminoacids in the subchain. If you are interested in multiple such subchains,
you can pass a list of such lists i.e.::

    boundaries=[[10,30],[31,50],[10,50]]

will find the topology of three subchains: indices 10-30, indices 31-50 and indices
10-50.

If you are interested in the topology of a whole spectrum of possible subchains
it is even easier: just use the **matrix** parameter (default False). This will
make the algorithm run the invariant for all possible combinations of subchains of
the original chain. Consequently, this can take very long to compute, therefore,
Topoly also contains the  **density** (default 1) parameter which controls how
precisely the space of all possible subchains will be explored. For density=1
all possible subchains are checked. For higher values passed to the density
parameter, the number of atoms will be cut and analysed subsequently. After
finding a knot with a probability higher than the **level** parameter
(default 0), additional subchains with a similar length will be checked.

I.e. lets say you pass a structure with 30 atoms, density=10 and level=30
parameter. Then subchains 1-30, 1-20, 1-10, 10-30, 10-20 and 20-30 are checked.
Imagine in 10-20 chain $3_1$ knot has been found with a probability of 50%.
Then 9-20, 11-20, 10-19, 10-21 subchains are also checked. Operations are
repeated until no more knots with probability higher than 30% are found.

You can plot your matrix using the **matrix_plot** (default False).

.. figure:: _static/map_4m8j_A.png
    :scale: 100%
    :alt: knot matrix
    
    Knot matrix of `exemplary structure <https://knotprot.cent.uw.edu.pl/view/4m8j/A/>`_.
    Horizontal and vertical axes represent first and last aminoacid subchain 
    respectively.
    

Calculating invariants of conjoined structures                                  
===============================================
Documentation section: :ref:`doc_joined`. 

In our dictionary of topologies are mainly prime structures. You may want to
find polynomials of more complex structures: unjoined unions (U) and conjoined
unions (#) of prime structures. 

You need to create objects of your basic structures. Lets start with the 3_1
knot::

    >>knot_31 = getpoly('HOMFLYPT', '3_1')
    >>print(knot_31)
    [+3_1: [-1 0 -2 0 [0]]|[0]|1 0 [0], -3_1: [[0] 0 -2 0 -1]|[0]|[0] 0 1]

The output finds all subtypes of the 3_1 knot and gives a list of corresponding
structures. Each topology is represented by two values: 

* name (here +3_1, -3_1),
* code corresponding to coefficients of its polynomial. 

If you want to check what are the polynomial coefficients of +3_1 U -3_1
(unjoined union of knots) and +3_1 # -3_1 (conjoined knots) write::

    >>plus_31, minus_31 = knot_31
    >>plus_31 + minus_31
    +3_1 U -3_1: [[0]]|-2 0 -3 [0] 3 0 2|[0]|1 0 3 [0] -3 0 -1|[0]|-1 [0] 1
    >>plus_31 * minus_31
    +3_1 # -3_1: [2 0 [5] 0 2]|[0]|-1 0 [-4] 0 -1|[0]|[1]

Which are the coefficients of HOMFLYPT polynomial of the knot compositions. List of
such objects can be exported to a new dictionary file::

    >>exportpoly(polynomials, exportfile='new_polvalues.py')

Documentation section: :ref:`doc_joined`.

Gaussian Linking Number calculation (GLN)
=========================================
Examples: `topoly_tutorial/GLN.py
<https://github.com/ilbsm/topoly_tutorial/blob/master/GLN.py/>`_.

Documentation section: `GLN
<https://topoly.cent.uw.edu.pl/documentation.html#topoly.gln>`_.
 
Gaussian linking number is a measure of how two chains are linked. If there are
two closed curves, then this number is always an integer::

    >>gln(structure1, structure2)
    -0.011

You can also calculate the GLN of subchains::

    >>gln(structure1, structure2, chain1_boundary=[3,8], chain2_boundary=[5,16])
    0.372

Find maximal absolute value between all possible subchains of two subchains::

    >>gln(structure1, structure2, mode=GlnMode.MAX, max_density=1) 
    {'whole chains': [-0.011], 'subchain of chain 2': [-0.967, '13-24'], 
     'subchain of chain 1': [-0.249, '2-6'], 'local maximum': [-0.967, '1-12', '13-24']}

You can even create a matrix of GLN values between one chain and all possible
subchains of another chain::

    >>gln(structure1, structure2, mode=GlnMode.MATRIX)

.. figure:: _static/GLN_map.png
    :scale: 100%
    :alt: GLN map

    Exemplary GLN map.


Lasso type identification (minimal surface calculation)
==========================================================
Examples: `topoly_tutorial/lasso_minimal_surface.py 
<https://github.com/ilbsm/topoly_tutorial/blob/master/lasso_minimal_surface.py/>`_.

Documentation section: :ref:`doc_lasso`.

For checking the type of a lasso topology Topoly checks how many times a lasso loop is
pinned by a lasso tail. For checking if the pinning happened, Topoly calculates the
`minimal surface spanned on a lasso loop <https://www.nature.com/articles/srep36895>`_
and checks if it is crossed. For more information look at
`this subpage of LassoProt database. <https://lassoprot.cent.uw.edu.pl/lasso_detection>`_.

.. figure:: _static/min_surf.png
    :scale: 20%
    :alt: minimal surface

    Minimal surface on an exemplary frame. Similar structures are created by
    soap bubbles.

For checking a lasso topology, input your structure and indices of the first and the last
point of a loop.::

    >>lasso_type(structure, [1,30])
    {(1, 30): 'L+1N'}

Which means that through a lasso loop with indices 1-30 the tail crosses once.
Symbols '+' and 'N' are connected with orientation of the lasso. For further
explanation look at this `subpage of LassoProt database. 
<https://lassoprot.cent.uw.edu.pl/lasso_classification#lasso_type> _`

You can also get more precise output using the parameter more_info::

    >>lasso_type(structure, [1,30], more_info=True)
    {(1, 12): {'class': 'L+2C', 'beforeN': [], 'beforeC': ['+25', '-27'], 'crossingsN': [], 'crossingsC': ['+25', '-27'], 
    'Area': 100.766, 'loop_length': 36.0001, 'Rg': 8.12732, 'smoothing_iterations': 0}}

If you are only interested in a shape of minimal surface, type::

    >>make_surface(structure, [1,30])
    [{'A': {'x': -5.796, 'y': -0.0, 'z': 0.0}, 'B': {'x': 0.0, 'y': 0.0, 'z': 0.0}, 'C': {'x': -5.019, 'y': 2.898, 'z': 0.0}}, 
    {'A': {'x': -5.019, 'y': 2.898, 'z': 0.0}, 'B': {'x': 0.0, 'y': 0.0, 'z': 0.0}, 'C': {'x': -2.898, 'y': 5.019, 'z': 0.0}}, 
    {'A': {'x': -2.898, 'y': 5.019, 'z': 0.0}, 'B': {'x': 0.0, 'y': 0.0, 'z': 0.0}, 'C': {'x': -0.0, 'y': 5.796, 'z': 0.0}},
    {'A':....

to get a complete information about a mesh creating a minimal surface.


Random polygons generation
=============================
Documentation section: :ref:`doc_generate`.

You can generate equilateral random walks, random loops and structures composed
of them: lassos and handcuffs. Loop generation in these functions is based on 
`Jason Cantarellas work 
<https://iopscience.iop.org/article/10.1088/1751-8113/49/27/275202/meta>`_. 
To generate such structures type::

    >>generate_walk(30, 100)           # 100 walks of length 30
    >>generate_loop(27, 100)           # 100 loops of length 27
    >>generate_lasso(12, 8, 100)       # 100 lassos with loop length of 12 and tail length of 8
    >>generate_handcuff([4,7], 5, 100) # 100 handcuffs with loops of length 4 and 7 and tail length of 5
    >>generate_link([4,7], 2, 100)     # 100 loop pairs of length 4 and 7 and distance between their geometric centers of 2


Visualization
=================
Documentation section: :ref:`doc_vis`.

You can see your structure using VMD or Python's matplotlib.

If you want to view a .xyz structure in VMD, use the function::

    >>xyz2vmd('file.xyz')

it converts a .xyz file into a .pdb structure file and a .psf topology file.
To open your structure in vmd, type in terminal::
    
    >>vmd file.pdb -psf file.psf                                              

If you want to view a structure (using matplotlib) in any of the supported formats,
type::

   >>plot_graph(structure)


Finding loops, theta-curves and handcuffs in structure
======================================================
Examples: `topoly_tutorial/import_and_find.py 
<https://github.com/ilbsm/topoly_tutorial/blob/master/import_and_find.py/>`_.

Documentation section :ref:`doc_find`.

If you want to find loops, theta-curves or handcuffs in your structure, type 
one of these functions::

    >>find_loops(structure)
    >>find_thetas(structure)
    >>find_handcuffs(structure)

To find the corresponding topology please set the **output_type** parameter
that selects the output type: python list, .xyz file or generator.

Matrix functions
================
Examples: `topoly_tutorial/matrices.py 
<https://github.com/ilbsm/topoly_tutorial/blob/master/matrices.py/>`_.

Documentation section :ref:`doc_matrix`.

Matrix functions gives you more control over matrices created by gln or
invariant methods.

plot_matrix prints a map after passing a matrix created by gln or one of the invariant
functions (conway, homfly, etc.). It has more plotting parameters than the invariant functions
giving you more control over the generated output.

* find_spots(matrix) -- finds geometrical centers of each identified topology
  field.
* plot_matrix(matrix) -- plots map basing on given matrix. It has more plotting 
  parameters than invariant calculating functions, giving you more control over the generated output.
* translate_matrix(matrix) -- changes format of a given matrix (to dictionary or
  list of lists)

Data manipulation
==================
Documentation section: :ref:`doc_manipulation`.

There are three more functions:

* **find_matching** translating polynomial coefficient data into topology type,
* **reduce_structure** reducing a structure using Reidemeister moves/KMT 
  algorithm (check :ref:`tutorial_reduction`),
* **close_curve** for closing an open curve (check :ref:`tutorial_closure`), 

Examples of find_matching usage
-------------------------------
If you have invariant a (i.e. Yamada) polynomial coefficients string use
find_matching to identify the topology type::

    >>find_matching('1 1 1 1 1 1 1 1 1', 'Yamada')
    '2^2_1'

You can also check more complicated inputs which can be outputs of some Topoly 
functions -- i.e. dictionary of polynomial probabilities::

    >>find_matching({'1 -1 1': 0.8, '1 -3 1': 0.2}, 'Alexander')
    {'3_1': 0.8, '4_1': 0.2}


or dictionary of polynomial probabilities for each subchain::

    >>find_matching({(0, 100): {'1 -1 1': 0.8, '1 -3 1': 0.2}, (50, 100): {'1 -1 1': 0.3, '1': 0.7}}, 'Alexander')
    {(0, 100): {'3_1': 0.8, '4_1': 0.2}, (50, 100): {'3_1': 0.3, '0_1': 0.7}}
