.. _examples_link:

Examples
========

.. contents::
   :depth: 2
   :local:

Phonopy supports various external force calculators (mainly for
abinitio codes). The examples below are given for the default system
that is equivalent to VASP style. Most of usage is universal among the
force calculators. So it is also useful for non-VASP users to see the
examples below. The list of the force calculators and the links to
their specific usages are shown at :ref:`calculator_interfaces`.

Example files are found at
https://github.com/phonopy/phonopy/tree/master/example. The same are
found in the example directory of the phonopy package downloaded at
https://github.com/phonopy/phonopy/archive/master.zip. The followings
show how some of those examples work. Note that sometimes the
followings are outdated than the examples in the phonopy package. So
the results or displace outputs can be different.


Si
---

``FORCE_SETS`` file creation for VASP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   % phonopy -f vasprun.xml
           _
     _ __ | |__   ___  _ __   ___   _ __  _   _
    | '_ \| '_ \ / _ \| '_ \ / _ \ | '_ \| | | |
    | |_) | | | | (_) | | | | (_) || |_) | |_| |
    | .__/|_| |_|\___/|_| |_|\___(_) .__/ \__, |
    |_|                            |_|    |___/

                                        0.9.4
   counter (file index): 1 (1)

   FORCE_SETS has been created.
                    _
      ___ _ __   __| |
     / _ \ '_ \ / _` |
    |  __/ | | | (_| |
     \___|_| |_|\__,_|


where ``vasprun.xml`` is the VASP output.

DOS
~~~~

::

   % phonopy -p mesh.conf
           _
     _ __ | |__   ___  _ __   ___   _ __  _   _
    | '_ \| '_ \ / _ \| '_ \ / _ \ | '_ \| | | |
    | |_) | | | | (_) | | | | (_) || |_) | |_| |
    | .__/|_| |_|\___/|_| |_|\___(_) .__/ \__, |
    |_|                            |_|    |___/

                                        0.9.4
   Mesh sampling mode
   Settings:
     Sampling mesh:  [31 31 31]
     Supercell:  [2 2 2]
   Spacegroup:  Fd -3 m (227)
   Number of irreducible q-points:  816
   ...

.. |Si-DOS| image:: Si-DOS.png
            :width: 50%

|Si-DOS|


Thermal properties
~~~~~~~~~~~~~~~~~~

::

   % phonopy -t -p mesh.conf

           _
     _ __ | |__   ___  _ __   ___   _ __  _   _
    | '_ \| '_ \ / _ \| '_ \ / _ \ | '_ \| | | |
    | |_) | | | | (_) | | | | (_) || |_) | |_| |
    | .__/|_| |_|\___/|_| |_|\___(_) .__/ \__, |
    |_|                            |_|    |___/

                                        0.9.4
   Mesh sampling mode
   Settings:
     Sampling mesh:  [31 31 31]
     Supercell:  [2 2 2]
   Spacegroup:  Fd -3 m (227)
   Number of irreducible q-points:  816
   #      T [K]      F [kJ/mol]    S [J/K/mol]  C_v [J/K/mol]
          0.000      11.7110491      0.0000000      0.0000000
         10.000      11.7110005      0.0207133      0.0652014
         20.000      11.7101707      0.1826665      0.5801980
         30.000      11.7063149      0.6494417      1.9566658
         40.000      11.6959681      1.4755146      3.9391312
         50.000      11.6758627      2.5838025      6.0729958
         60.000      11.6436850      3.8753235      8.1398560
         70.000      11.5979859      5.2789839     10.1081936
         80.000      11.5378707      6.7536680     12.0151390
         90.000      11.4627491      8.2777066     13.8988294
        100.000      11.3721917      9.8393077     15.7763729
   ...


.. |Si-props| image:: Si-props.png
              :width: 50%

|Si-props|

NaCl
----

Band structure
~~~~~~~~~~~~~~

::

   % phonopy -p band.conf
           _
     _ __ | |__   ___  _ __   ___   _ __  _   _
    | '_ \| '_ \ / _ \| '_ \ / _ \ | '_ \| | | |
    | |_) | | | | (_) | | | | (_) || |_) | |_| |
    | .__/|_| |_|\___/|_| |_|\___(_) .__/ \__, |
    |_|                            |_|    |___/

                                        0.9.1.4
   Band structure mode
   Settings:
     Supercell:  [2 2 2]
     Primitive axis:
        [ 0.   0.5  0.5]
        [ 0.5  0.   0.5]
        [ 0.5  0.5  0. ]
   Spacegroup:  Fm -3 m (225)
   Paths in reciprocal reduced coordinates:
   [ 0.00  0.00  0.00] --> [ 0.50  0.00  0.00]
   [ 0.50  0.00  0.00] --> [ 0.50  0.50  0.00]
   [ 0.50  0.50  0.00] --> [-0.00 -0.00  0.00]
   [ 0.00  0.00  0.00] --> [ 0.50  0.50  0.50]
   ...

.. |NaCl-band| image:: NaCl-band.png
               :width: 50%

|NaCl-band|

Band structure with non-analytical term correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This requires to prepare BORN file.

::

   % phonopy -p --nac band.conf
           _
     _ __ | |__   ___  _ __   ___   _ __  _   _
    | '_ \| '_ \ / _ \| '_ \ / _ \ | '_ \| | | |
    | |_) | | | | (_) | | | | (_) || |_) | |_| |
    | .__/|_| |_|\___/|_| |_|\___(_) .__/ \__, |
    |_|                            |_|    |___/
                                         1.13.0

   Python version 2.7.14
   Spglib version 1.10.3
   Band structure mode
   Settings:
     Non-analytical term correction (NAC): on
     Supercell: [2 2 2]
     Primitive axis:
       [ 0.   0.5  0.5]
       [ 0.5  0.   0.5]
       [ 0.5  0.5  0. ]
   Spacegroup: Fm-3m (225)
   Computing force constants...
   max drift of force constants: 0.040159 (zz) 0.000009 (zz)
   Reciprocal space paths in reduced coordinates:
   [ 0.00  0.00  0.00] --> [ 0.50  0.00  0.00]
   [ 0.50  0.00  0.00] --> [ 0.50  0.50  0.00]
   [ 0.50  0.50  0.00] --> [-0.00 -0.00  0.00]
   [ 0.00  0.00  0.00] --> [ 0.50  0.50  0.50]
   NAC by Gonze et al., PRB 50, 13035(R) (1994), PRB 55, 10355 (1997):
     G-cutoff distance:  1.16
     Number of G-points: 307
     Lambda:   0.19
   ...

.. |NaCl-band-NAC| image:: NaCl-band-NAC.png
                   :width: 50%

|NaCl-band-NAC|


.. _example_pdos:

PDOS
~~~~~~~

::

   % phonopy -p pdos.conf
           _
     _ __ | |__   ___  _ __   ___   _ __  _   _
    | '_ \| '_ \ / _ \| '_ \ / _ \ | '_ \| | | |
    | |_) | | | | (_) | | | | (_) || |_) | |_| |
    | .__/|_| |_|\___/|_| |_|\___(_) .__/ \__, |
    |_|                            |_|    |___/
                                         1.13.0

   Python version 2.7.14
   Spglib version 1.10.3
   Mesh sampling mode
   Settings:
     Sampling mesh: [41 41 41]
     Supercell: [2 2 2]
     Primitive axis:
       [ 0.   0.5  0.5]
       [ 0.5  0.   0.5]
       [ 0.5  0.5  0. ]
   Spacegroup: Fm-3m (225)
   Computing force constants...
   max drift of force constants: 0.040159 (zz) 0.000009 (zz)
   Number of q-points on sampling mesh: 68921
   Calculating phonons on sampling mesh...
   ...

.. |NaCl-PDOS| image:: NaCl-PDOS.png
               :width: 50%

|NaCl-PDOS|

With non-analytical term correction, the PDOS may not change very much
because it mainly affects phonon modes in the reciprocal
region close to :math:`\Gamma` point.

::

   % phonopy --nac -p pdos.conf
           _
     _ __ | |__   ___  _ __   ___   _ __  _   _
    | '_ \| '_ \ / _ \| '_ \ / _ \ | '_ \| | | |
    | |_) | | | | (_) | | | | (_) || |_) | |_| |
    | .__/|_| |_|\___/|_| |_|\___(_) .__/ \__, |
    |_|                            |_|    |___/
                                         1.13.0

   Python version 2.7.14
   Spglib version 1.10.3
   Mesh sampling mode
   Settings:
     Non-analytical term correction (NAC): on
     Sampling mesh: [41 41 41]
     Supercell: [2 2 2]
     Primitive axis:
       [ 0.   0.5  0.5]
       [ 0.5  0.   0.5]
       [ 0.5  0.5  0. ]
   Spacegroup: Fm-3m (225)
   Computing force constants...
   max drift of force constants: 0.040159 (zz) 0.000009 (zz)
   Number of q-points on sampling mesh: 68921
   Calculating phonons on sampling mesh...
   NAC by Gonze et al., PRB 50, 13035(R) (1994), PRB 55, 10355 (1997):
     G-cutoff distance:  1.16
     Number of G-points: 307
     Lambda:   0.19
   ...

.. |NaCl-PDOS-nac| image:: NaCl-PDOS-nac.png
                   :width: 50%

|NaCl-PDOS-nac|

The above examples use a smearing method to calculate DOS. A linear
tetrahedron method can be also chosen. The obtained DOS shows sharper
profile than that given by the smearing method.

::

   % phonopy pdos.conf --nac --thm -p
           _
     _ __ | |__   ___  _ __   ___   _ __  _   _
    | '_ \| '_ \ / _ \| '_ \ / _ \ | '_ \| | | |
    | |_) | | | | (_) | | | | (_) || |_) | |_| |
    | .__/|_| |_|\___/|_| |_|\___(_) .__/ \__, |
    |_|                            |_|    |___/
                                         1.13.0

   Python version 2.7.14
   Spglib version 1.10.3
   Mesh sampling mode
   Settings:
     Non-analytical term correction (NAC): on
     Sampling mesh: [41 41 41]
     Supercell: [2 2 2]
     Primitive axis:
       [ 0.   0.5  0.5]
       [ 0.5  0.   0.5]
       [ 0.5  0.5  0. ]
   Spacegroup: Fm-3m (225)
   Computing force constants...
   max drift of force constants: 0.040159 (zz) 0.000009 (zz)
   Number of q-points on sampling mesh: 68921
   Calculating phonons on sampling mesh...
   NAC by Gonze et al., PRB 50, 13035(R) (1994), PRB 55, 10355 (1997):
     G-cutoff distance:  1.16
     Number of G-points: 307
     Lambda:   0.19
   ...

.. |NaCl-PDOS-thm-nac| image:: NaCl-PDOS-thm-nac.png
                       :width: 50%

|NaCl-PDOS-thm-nac|


Plot band structure and DOS at once
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Band structure and DOS or PDOS can be plotted on one figure together by

::

   % phonopy band-pdos.conf --nac  --thm -p
           _
     _ __ | |__   ___  _ __   ___   _ __  _   _
    | '_ \| '_ \ / _ \| '_ \ / _ \ | '_ \| | | |
    | |_) | | | | (_) | | | | (_) || |_) | |_| |
    | .__/|_| |_|\___/|_| |_|\___(_) .__/ \__, |
    |_|                            |_|    |___/
                                         1.13.0

   Python version 2.7.14
   Spglib version 1.10.3
   Band structure and mesh sampling mode
   Settings:
     Non-analytical term correction (NAC): on
     Sampling mesh: [41 41 41]
     Supercell: [2 2 2]
     Primitive axis:
       [ 0.   0.5  0.5]
       [ 0.5  0.   0.5]
       [ 0.5  0.5  0. ]
   Spacegroup: Fm-3m (225)
   Computing force constants...
   max drift of force constants: 0.040159 (zz) 0.000009 (zz)
   Reciprocal space paths in reduced coordinates:
   [ 0.00  0.00  0.00] --> [ 0.50  0.00  0.00]
   [ 0.50  0.00  0.00] --> [ 0.50  0.50  0.00]
   [ 0.50  0.50  0.00] --> [-0.00 -0.00  0.00]
   [ 0.00  0.00  0.00] --> [ 0.50  0.50  0.50]
   NAC by Gonze et al., PRB 50, 13035(R) (1994), PRB 55, 10355 (1997):
     G-cutoff distance:  1.16
     Number of G-points: 307
     Lambda:   0.19
   Number of q-points on sampling mesh: 68921
   Calculating phonons on sampling mesh...
   ...

.. |NaCl-band-PDOS-NAC| image:: NaCl-band-PDOS-NAC.png
                        :width: 50%

|NaCl-band-PDOS-NAC|

MgB2 characters of ireducible representations
----------------------------------------------

::

   % phonopy -f vasprun.xml-{001,002}
   % phonopy --dim="3 3 2" --irreps="0 0 0"
           _
     _ __ | |__   ___  _ __   ___   _ __  _   _
    | '_ \| '_ \ / _ \| '_ \ / _ \ | '_ \| | | |
    | |_) | | | | (_) | | | | (_) || |_) | |_| |
    | .__/|_| |_|\___/|_| |_|\___(_) .__/ \__, |
    |_|                            |_|    |___/
                                        1.11.10

   Python version 3.6.0
   Spglib version 1.9.9
   Ir-representation mode
   Settings:
     Supercell: [3 3 2]
   Spacegroup: P6/mmm (191)
   Computing force constants...

   -------------------------------
     Irreducible representations
   -------------------------------
   q-point: [ 0.  0.  0.]
   Point group: 6/mmm

   Original rotation matrices:

        1         2         3         4         5         6
    --------  --------  --------  --------  --------  --------
     1  0  0  -1  0  0   1 -1  0  -1  1  0   0 -1  0   0  1  0
     0  1  0   0 -1  0   1  0  0  -1  0  0   1 -1  0  -1  1  0
     0  0  1   0  0 -1   0  0  1   0  0 -1   0  0  1   0  0 -1

        7         8         9        10        11        12
    --------  --------  --------  --------  --------  --------
    -1  0  0   1  0  0  -1  1  0   1 -1  0   0  1  0   0 -1  0
     0 -1  0   0  1  0  -1  0  0   1  0  0  -1  1  0   1 -1  0
     0  0  1   0  0 -1   0  0  1   0  0 -1   0  0  1   0  0 -1

       13        14        15        16        17        18
    --------  --------  --------  --------  --------  --------
     0 -1  0   0  1  0  -1  0  0   1  0  0  -1  1  0   1 -1  0
    -1  0  0   1  0  0  -1  1  0   1 -1  0   0  1  0   0 -1  0
     0  0 -1   0  0  1   0  0 -1   0  0  1   0  0 -1   0  0  1

       19        20        21        22        23        24
    --------  --------  --------  --------  --------  --------
     0  1  0   0 -1  0   1  0  0  -1  0  0   1 -1  0  -1  1  0
     1  0  0  -1  0  0   1 -1  0  -1  1  0   0 -1  0   0  1  0
     0  0 -1   0  0  1   0  0 -1   0  0  1   0  0 -1   0  0  1

   Transformation matrix:

    1.000  0.000  0.000
    0.000  1.000  0.000
    0.000  0.000  1.000

   Rotation matrices by transformation matrix:

        E         i        C6        S3        C3        S6
    --------  --------  --------  --------  --------  --------
     1  0  0  -1  0  0   1 -1  0  -1  1  0   0 -1  0   0  1  0
     0  1  0   0 -1  0   1  0  0  -1  0  0   1 -1  0  -1  1  0
     0  0  1   0  0 -1   0  0  1   0  0 -1   0  0  1   0  0 -1

       C2        sgh       C3        S6        C6        S3
    --------  --------  --------  --------  --------  --------
    -1  0  0   1  0  0  -1  1  0   1 -1  0   0  1  0   0 -1  0
     0 -1  0   0  1  0  -1  0  0   1  0  0  -1  1  0   1 -1  0
     0  0  1   0  0 -1   0  0  1   0  0 -1   0  0  1   0  0 -1

       C2'       sgd      C2''       sgv       C2'       sgd
    --------  --------  --------  --------  --------  --------
     0 -1  0   0  1  0  -1  0  0   1  0  0  -1  1  0   1 -1  0
    -1  0  0   1  0  0  -1  1  0   1 -1  0   0  1  0   0 -1  0
     0  0 -1   0  0  1   0  0 -1   0  0  1   0  0 -1   0  0  1

      C2''       sgv       C2'       sgd      C2''       sgv
    --------  --------  --------  --------  --------  --------
     0  1  0   0 -1  0   1  0  0  -1  0  0   1 -1  0  -1  1  0
     1  0  0  -1  0  0   1 -1  0  -1  1  0   0 -1  0   0  1  0
     0  0 -1   0  0  1   0  0 -1   0  0  1   0  0 -1   0  0  1

   Character table:

     1 (  -0.019): A2u
       ( 1,   0.0) ( 1, 180.0) ( 1,   0.0) ( 1, 180.0) ( 1,   0.0) ( 1, 180.0)
       ( 1,   0.0) ( 1, 180.0) ( 1,   0.0) ( 1, 180.0) ( 1,   0.0) ( 1, 180.0)
       ( 1, 180.0) ( 1,   0.0) ( 1, 180.0) ( 1,   0.0) ( 1, 180.0) ( 1,   0.0)
       ( 1, 180.0) ( 1,   0.0) ( 1, 180.0) ( 1,   0.0) ( 1, 180.0) ( 1,   0.0)

     2 (   0.004): E1u
       ( 2,   0.0) ( 2, 180.0) ( 1,   0.0) ( 1, 180.0) ( 1, 180.0) ( 1,   0.0)
       ( 2, 180.0) ( 2,   0.0) ( 1, 180.0) ( 1,   0.0) ( 1,   0.0) ( 1, 180.0)
       ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0)
       ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0)

     4 (   9.953): E1u
       ( 2,   0.0) ( 2, 180.0) ( 1,   0.0) ( 1, 180.0) ( 1, 180.0) ( 1,   0.0)
       ( 2, 180.0) ( 2,   0.0) ( 1, 180.0) ( 1,   0.0) ( 1,   0.0) ( 1, 180.0)
       ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0)
       ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0)

     6 (  11.982): A2u
       ( 1,   0.0) ( 1, 180.0) ( 1,   0.0) ( 1, 180.0) ( 1,   0.0) ( 1, 180.0)
       ( 1,   0.0) ( 1, 180.0) ( 1,   0.0) ( 1, 180.0) ( 1,   0.0) ( 1, 180.0)
       ( 1, 180.0) ( 1,   0.0) ( 1, 180.0) ( 1,   0.0) ( 1, 180.0) ( 1,   0.0)
       ( 1, 180.0) ( 1,   0.0) ( 1, 180.0) ( 1,   0.0) ( 1, 180.0) ( 1,   0.0)

     7 (  17.269): E2g
       ( 2,   0.0) ( 2,   0.0) ( 1, 180.0) ( 1, 180.0) ( 1, 180.0) ( 1, 180.0)
       ( 2,   0.0) ( 2,   0.0) ( 1, 180.0) ( 1, 180.0) ( 1, 180.0) ( 1, 180.0)
       ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0)
       ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0) ( 0,   0.0)

     9 (  20.565): B2g
       ( 1,   0.0) ( 1,   0.0) ( 1, 180.0) ( 1, 180.0) ( 1,   0.0) ( 1,   0.0)
       ( 1, 180.0) ( 1, 180.0) ( 1,   0.0) ( 1,   0.0) ( 1, 180.0) ( 1, 180.0)
       ( 1, 180.0) ( 1, 180.0) ( 1,   0.0) ( 1,   0.0) ( 1, 180.0) ( 1, 180.0)
       ( 1,   0.0) ( 1,   0.0) ( 1, 180.0) ( 1, 180.0) ( 1,   0.0) ( 1,   0.0)

                    _
      ___ _ __   __| |
     / _ \ '_ \ / _` |
    |  __/ | | | (_| |
     \___|_| |_|\__,_|


Al-QHA
-------

::

   % phonopy-qha e-v.dat thermal_properties.yaml-{-{5..1},{0..5}} --sparse=50
   # Vinet EOS
   #          T           E_0           B_0          B'_0           V_0
         0.000000    -14.796263     75.231724      4.758283     66.697923
         2.000000    -14.796263     75.231723      4.758283     66.697923
         4.000000    -14.796263     75.231718      4.758284     66.697923
         6.000000    -14.796263     75.231695      4.758286     66.697924
         8.000000    -14.796263     75.231634      4.758294     66.697928
        10.000000    -14.796264     75.231510      4.758308     66.697934
   ...

.. |Al-QHA| image:: Al-QHA.png
            :width: 50%

|Al-QHA|


Si-gruneisen
-----------------------------

See :ref:`phonopy_gruneisen`.
