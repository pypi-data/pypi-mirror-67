.. _install:

Installation
=============

.. contents::
   :depth: 3
   :local:

.. _install_conda:

Using conda
-----------

Conda is an open source package management system. Once the conda
system is set-up (see `details about conda setting up
<https://conda.io/docs/user-guide/install/index.html>`_), the installation
of phonopy is super easy for any of Linux, MacOSX, and Windows.
To install::

   % conda install -c conda-forge phonopy h5py

This phonopy's conda package is prepared and maintained by
Paweł T. Jochym at conda-forge channel (please be aware that this is
not a trivial job). Installation of h5py is optional. When using hdf5
files from NFS mouted location, the latest h5py may not work. In this
case, installation of an older version is recommended::

   % conda install hdf5=1.8.18

Minimum steps to install and use phonopy via conda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the following procedure, conda's environment (see `details at conda
web site
<https://conda.io/docs/user-guide/tasks/manage-environments.html>`_)
is used not to interfere existing environment (mainly python
environment).

::

   % conda create -n phonopy -c conda-forge python=3
   % conda activate phonopy
   % conda install -c conda-forge phonopy h5py

To exit from this conda's environment::

   % conda deactivate

To use this phonopy, entering this environment is necessary like below.

::

   % conda activate phonopy
   (phonopy) % phonopy
           _
     _ __ | |__   ___  _ __   ___   _ __  _   _
    | '_ \| '_ \ / _ \| '_ \ / _ \ | '_ \| | | |
    | |_) | | | | (_) | | | | (_) || |_) | |_| |
    | .__/|_| |_|\___/|_| |_|\___(_) .__/ \__, |
    |_|                            |_|    |___/
                                    1.13.2-r107


   Crystal structure file of POSCAR (default file name) could not be found.
     ___ _ __ _ __ ___  _ __
    / _ \ '__| '__/ _ \| '__|
   |  __/ |  | | | (_) | |
    \___|_|  |_|  \___/|_|


Using pip
---------

Installation of phonopy via pip is not very recommended. :ref:`install_conda`
as rewritten above is recommended.

Phonopy pip wheel is not prepared. So before installing phonopy using
pip, Python C-API compilation environment has to be prepared. Then
phonopy is installed using pip by::

   % pip install phonopy

If you see the error message like below in the installation process::

   _phonopy.c:35:20: fatal error: Python.h: No such file or directory

development tools for building python module are additionally
necessary and are installed using OS's package management system,
e.g.,::

   sudo apt-get install python-dev

.. _install_from_source:

From source code
-----------------

System requirement
~~~~~~~~~~~~~~~~~~

The procedure to setup phonopy is explained in this section. It is
supposed that phonopy is installed on the recent linux distribution
like Ubuntu or Fedora with Python version 2.6 or later. Python version
3.4 or later is expected to work. Mac OS X users may use conda packages
and also find some more information at :ref:`install_MacOSX`.
Windows users should use conda packages as well.

Prepare the following Python libraries:

* Python and its header files
* numpy
* matplotlib
* python-yaml (pyyaml)
* python-h5py (h5py)

And optionally the following:

* cp2k-input-tools, for the CP2K force calculator backend


By Ubuntu package manager
^^^^^^^^^^^^^^^^^^^^^^^^^^

The most recommended system is Ubuntu linux version 14.04 (64-bit) or
later. If you have any installation problem that you may feel
difficult to solve, please use a virtual machine environment such as
VirtualBox and install Ubuntu linux on it.

The python libraries are installed by::

   % sudo apt-get install python-dev python-numpy  python-matplotlib python-yaml python-h5py

``python-scipy`` is also required to use ``phonopy-qha`` or
``DEBYE_MODEL`` tag.

By conda
^^^^^^^^^

The python libraries may be also installed using pip or
conda. Conda packages are distributed in binary and recommended often
more than pip. The installation of necessary libraries is done as
follows::

   % conda install numpy scipy h5py pyyaml matplotlib

.. _install_setup_py:

Building using setup.py
~~~~~~~~~~~~~~~~~~~~~~~~

If package installation is not possible or you want to compile with
special compiler or special options, phonopy is built using
setup.py. In this case, manual modification of ``setup.py`` may be
needed.

1. Download the source code at

   https://pypi.python.org/pypi/phonopy

   and extract it::

      % tar xvfz phonopy-1.11.12.31.tar.gz
      % cd phonopy-1.11.12.31

   The other option is using git to clone the phonopy repository from github::

     % git clone https://github.com/phonopy/phonopy.git
     % cd phonopy

2. Set up C-libraries for python C-API and python codes. This can be
   done as follows:

   Run ``setup.py`` script::

      % python setup.py install --user

   Watching carefully where the phonopy commands and library are
   installed. Those locations can be ``~/.local/bin`` and
   ``~/.local/lib`` directories, respectively.

3. Assuming the installation location is those shown in the step 2,
   set ``$PATH`` and ``$PYTHONPATH``::

      export PYTHONPATH=~/.local/lib:$PYTHONPATH
      export PATH=~/.local/bin:$PATH

   or if ``PYTHONPATH`` is not yet set in your system::

      export PYTHONPATH=~/.local/lib
      export PATH=~/.local/bin:$PATH

   in your ``.bashrc`` (or maybe ``.bash_profile``), ``.zshenv``, or
   other script for the other shells.



.. _install_trouble_shooting:


Multithreading support
-----------------------

Two kinds of multithreadings can be used in phonopy.

1. Multithreaded BLAS linked numpy

   Phonopy uses numpy to run singular value decomposition in the
   calculation of force constants and diagonalizaion of dynamical
   matrices. For these, numpy internally calls the LAPACK
   routines. Therefore if a user installs a numpy that is linked with
   multithreaded BLAS, these parts are multithreaded. For example, MKL
   linked numpy is easily installed using conda.

2. OpenMP support in phonopy and spglib

   OpenMP are applied in the symmetry finding of spglib and the
   distribution of symmetry reduced force constants elements to full
   force constants elements in phonopy. When a chosen supercell is
   very large and there are many cores on a computer, these parts may
   work well to reduce the computational time. In the default phonopy
   setting, this is not activated. To enable this, it is necessary to
   build phonopy using modified ``setup.py`` in which ``with_openmp =
   False`` must be changed to ``with_openmp = True``. For this,
   currently only gcc is supported.

.. include:: MacOSX.inc


Trouble shooting
-----------------

Remove previous phonopy installations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes previous installations of phonopy prevent from loading newly
installed phonopy. In this case, it is recommended to uninstall all
the older phonopy packages by

1. Running ``pip uninstall phonopy`` as many times as no phonopy
   packages will be found. Error message may be shown, but don't mind
   it. Similarly do ``conda uninstall phonopy``.

2. There may still exist litter of phonopy packages. So it is also
   recommend to remove them if it is found, e.g.::

     % rm -fr ~/.local/lib/python*/site-packages/phonopy*

Set correct environment variables ``PATH`` and ``PYTHONPATH``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In phonopy, ``PATH`` and ``PYTHONPATH`` play important roles. Of
course the information about them can be easily found in internet
(e.g. https://en.wikipedia.org/wiki/PATH_(variable)), so you really
have to find information by yourself and read them. Even if you can't
understand them, first you must ask to your colleagues or people
before sending this unnecessary question (as a researcher using
computer simulation) to the mailing list.

The problem appears when phonopy execution and library paths are set
multiple times in those environment variable. It is easy to check
current environment variables by::

   % echo $PATH

::

   % echo $PYTHONPATH

When multiple different phonopy paths are found, remove all except for
what you really need. Then logout from the current shell (terminal)
and open new shell (terminal) to confirm that the modification is activated.

Error in plotting on display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``texlive-fonts-recommended`` and ``dviping`` packages may be required
to install on your system, if you see something like the following
messages when ploting::

   ! I can't find file `pncr7t'.

or::

   ! LaTeX Error: File `type1cm.sty' not found.
