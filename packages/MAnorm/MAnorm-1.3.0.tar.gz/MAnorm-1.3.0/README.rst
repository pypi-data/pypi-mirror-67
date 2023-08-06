MAnorm
======

|github-actions| |Documentation Status| |pypi| |pyversion| |install with bioconda| |codecov| |license|

.. |github-actions| image:: https://github.com/shao-lab/MAnorm/workflows/Python%20package/badge.svg
   :target: https://github.com/shao-lab/MAnorm/actions
.. |Documentation Status| image:: https://readthedocs.org/projects/manorm/badge/?version=latest
   :target: http://manorm.readthedocs.io/en/latest/?badge=latest
.. |pypi| image:: https://img.shields.io/pypi/v/MAnorm.svg
   :target: https://pypi.org/project/MAnorm/
.. |pyversion| image:: https://img.shields.io/pypi/pyversions/MAnorm.svg
   :target: https://pypi.org/project/MAnorm/
.. |install with bioconda| image:: https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg
   :target: http://bioconda.github.io/recipes/manorm/README.html
.. |codecov| image:: https://codecov.io/gh/shao-lab/MAnorm/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/shao-lab/MAnorm
.. |license| image:: https://img.shields.io/pypi/l/MAnorm.svg
   :target: https://github.com/shao-lab/MAnorm/blob/master/LICENSE

Introduction
------------

ChIP-Seq is widely used to characterize genome-wide binding patterns of
transcription factors and other chromatin-associated proteins. Although
comparison of ChIP-Seq data sets is critical for understanding cell
type-dependent and cell state-specific binding, and thus the study of
cell-specific gene regulation, few quantitative approaches have been
developed.

Here, we present a simple and effective method, MAnorm, for quantitative
comparison of ChIP-Seq data sets describing transcription factor binding
sites and epigenetic modifications. The quantitative binding differences
inferred by MAnorm showed strong correlation with both the changes in
expression of target genes and the binding of cell type-specific
regulators.

Citation
--------

`Shao Z, Zhang Y, Yuan GC, Orkin SH, Waxman DJ. MAnorm: a robust model for quantitative comparison of
ChIP-Seq data sets. Genome biology. 2012 Mar 16;13(3):R16.
<https://genomebiology.biomedcentral.com/articles/10.1186/gb-2012-13-3-r16>`__

Documentation
-------------

To see the full documentation of MAnorm, please refer to: http://manorm.readthedocs.io

Installation
------------

The latest release of MAnorm is available at `PyPI <https://pypi.python.org/pypi/MAnorm>`__:

::

    $ pip install manorm

Or you can install MAnorm via conda:

::

    $ conda install -c bioconda manorm

Galaxy Installation
-------------------

MAnorm is also available on Galaxy_, you can incorporate MAnorm into your own Galaxy instance.

Please search and install MAnorm via the `Galaxy Tool Shed`_.

.. _Galaxy: https://galaxyproject.org
.. _`Galaxy Tool Shed`: https://toolshed.g2.bx.psu.edu/view/haydensun/manorm

Basic Usage
-----------

::

    $ manorm --p1 sample1_peaks.bed --p2 sample2_peaks.bed --r1 sample1_reads.bed --r2 sample2_reads.bed
    --n1 name1 --n2 name2 -o output_dir

**Note:** Using -h/--help for the details of all arguments.

License
-------

`BSD 3-Clause
License <https://github.com/shao-lab/MAnorm/blob/master/LICENSE>`__
