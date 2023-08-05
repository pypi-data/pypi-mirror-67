.. _status page:

Status Page
===========

This page indicates the development status of `sbpy`. The development
is expected to conclude in 2021.

The current development version is **v0.2dev**; its status is as follows:

.. image:: https://api.travis-ci.org/NASA-Planetary-Science/sbpy.svg?branch=master
    :target: https://travis-ci.org/NASA-Planetary-Science/sbpy
    :alt: Travis-CI status

.. image:: https://codecov.io/gh/NASA-Planetary-Science/sbpy/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/NASA-Planetary-Science/sbpy
    :alt: codecov status

.. image:: https://readthedocs.org/projects/sbpy/badge/?version=latest
    :target: https://sbpy.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


Current development status
~~~~~~~~~~~~~~~~~~~~~~~~~~

The current development status of `sbpy` sub-modules is indicated in
the following tables.  The column `Dev` indicates the lead developer
(MM: Michael Mommert, MSK: Michael S. Kelley, MdVB: Miguel de
Val-Borro, JYL: Jian-Yang Li) for the respective sub-packages and
classes.

.. raw:: html

    <style>
         .planned:before {
              color: #cbcbcb;
              content: "⬤";
         }
         .dev:before {
              color: #ffad00;
              content: "⬤";
         }
         .stable:before {
              color: #4e72c3;
              content: "⬤";
         }
         .mature:before {
              color: #03a913;
              content: "⬤";
         }
         .pendingdep:before {
              color: #a84b03;
              content: "⬤";
         }
         .deprecated:before {
              color: #ff0000;
              content: "⬤";
         }
    </style>

    <table align='center'>
      <tr>
        <td align='center'><span class="planned"></span></td>
        <td>Planned</td>
      </tr>
      <tr>
        <td align='center'><span class="dev"></span></td>
        <td>Actively developed, be prepared for possible significant changes.</td>
      </tr>
      <tr>
        <td align='center'><span class="stable"></span></td>
        <td>Reasonably stable, but potentially incomplete; any significant changes/additions will generally include backwards-compatiblity.</td>
      </tr>
      <tr>
        <td align='center'><span class="mature"></span></td>
        <td>Mature.  Additions/improvements possible, but no major changes planned. </td>
      </tr>
      <tr>
        <td align='center'><span class="pendingdep"></span></td>
        <td>Pending deprecation.  Might be deprecated in a future version.</td>
      </tr>
      <tr>
        <td align='center'><span class="deprecated"></span></td>
        <td>Deprecated.  Might be removed in a future version.</td>
      </tr>
    </table>






`sbpy.data`
-----------

.. raw:: html

    <table border="1" class="docutils stability" align='center'>
        <tr>
            <th class="head">
                Sub-Packages and Classes
            </th>
            <th class="head">
                &nbsp;
            </th>
            <th class="head">
                Dev
            </th>
            <th class="head">
                Comments
            </th>
        </tr>
        <tr>
            <td>
                <em>sbpy.data.DataClass</em>
            </td>
            <td align='center'>
                <span class="mature"></span>
            </td>
            <td align='center'>
                MM
            </td>
            <td>
                fully implemented
            </td>
        </tr>
        <tr>
            <td>
                <em>sbpy.data.Names</em>
            </td>
            <td align='center'>
                <span class="stable"></span>
            </td>
            <td align='center'>
                MM
            </td>
             <td>
                waiting for Lowell ASTORB functionality for alternative name queries 
             </td>
        </tr>
        <tr>
            <td>
                <em>sbpy.data.Ephem</em>
            </td>
            <td align='center'>
                <span class="mature"></span>
            </td>
            <td align='center'>
                MM
            </td>
            <td>
	       fully implemented
            </td>
        </tr>
        <tr>
            <td>
                <em>sbpy.data.Obs</em>
            </td>
            <td align='center'>
                <span class="mature"></span>
            </td>
            <td align='center'>
                MM
            </td>
            <td>
                fully implemented
            </td>
        </tr>
        <tr>
            <td>
                <em>sbpy.data.Orbit</em>
            </td>
            <td align='center'>
                <span class="stable"></span>
            </td>
            <td align='center'>
                MM
            </td>
            <td>
	        OpenOrb ranging to be implemented
            </td>
        </tr>
        <tr>
            <td>
                <em>sbpy.data.Phys</em>
            </td>
            <td align='center'>
                <span class="stable"></span>
            </td>
            <td align='center'>
                MM
            </td>
            <td>
                waiting for Lowell ASTORB functionality for physical properties queries
            </td>
        </tr>
    </table>


`sbpy.activity`
---------------

.. raw:: html

    <table border="1" class="docutils stability" align='center'>
        <tr>
            <th class="head">
                Sub-Packages and Classes
            </th>
            <th class="head">
                &nbsp;
            </th>
            <th class="head">
                Dev
            </th>
            <th class="head">
                Comments
            </th>
        </tr>
        <tr>
            <td>
                <em>sbpy.activity.dust</em>
            </td>
            <td align='center'>
                <span class="dev"></span>
            </td>
            <td align='center'>
                MSK
            </td>
            <td>
                Halley-Marcus phase function implemented; *Afρ* and *εfρ* classes fully implemented; Syndynes and synchrones tbd.
            </td>
        </tr>
        <tr>
            <td>
                <em>sbpy.activity.gas</em>
            </td>
            <td align='center'>
                <span class="dev"></span>
            </td>
            <td align='center'>
                MSK / MdVB
            </td>
             <td>
                Haser model implemented; Vectorial model TBD;
            </td>
        </tr>
        <tr>
            <td>
                <em>sbpy.activity.sublimation</em>
            </td>
            <td align='center'>
                <span class="planned"></span>
            </td>
            <td align='center'>
                MSK
            </td>
             <td>
                tbd.
            </td>
        </tr>
    </table>


`sbpy.calib`
--------------

.. raw:: html

    <table border="1" class="docutils stability" align='center'>
        <tr>
            <th class="head">
                Sub-Packages and Classes
            </th>
            <th class="head">
                &nbsp;
            </th>
            <th class="head">
                Dev
            </th>
            <th class="head">
                Comments
            </th>
        </tr>
        <tr>
            <td>
                <em>sbpy.calib</em>
            </td>
            <td align='center'>
                <span class="stable"></span>
            </td>
            <td align='center'>
                MSK
            </td>
            <td>
                Sun and Vega spectra built in; Calibration system (photometric and spectrosopic) fully implemented.
            </td>
        </tr>
   </table>


`sbpy.photometry`
-----------------

.. raw:: html

    <table border="1" class="docutils stability" align='center'>
        <tr>
            <th class="head">
                Sub-Packages and Classes
            </th>
            <th class="head">
                &nbsp;
            </th>
            <th class="head">
                Dev
            </th>
            <th class="head">
                Comments
            </th>
        </tr>
        <tr>
            <td>
                <em>sbpy.photometry</em>
            </td>
            <td align='center'>
                <span class="dev"></span>
            </td>
            <td align='center'>
                JYL
            </td>
            <td>
                Disk integrated phase functions implemented: HG, HG1G2, HG12,
                HG12_Pen16, linear phasecurve; disk-resolved phase functions
                tbd.
            </td>
        </tr>
        <tr>
            <td>
                <em>sbpy.photometry.hapke</em>
            </td>
            <td align='center'>
                <span class="planned"></span>
            </td>
            <td align='center'>
                JYL
            </td>
            <td>
                Hapke photometric model TBD.
            </td>
        </tr>
        <tr>
            <td>
                <em>sbpy.photometry.dust</em>
            </td>
            <td align='center'>
                <span class="planned"></span>
            </td>
            <td align='center'>
                JYL
            </td>
            <td>
                Phase function of dust grains in cometary comae TBD.
            </td>
        </tr>
    </table>


`sbpy.shape`
------------

.. raw:: html

    <table border="1" class="docutils stability" align='center'>
        <tr>
            <th class="head">
                Sub-Packages and Classes
            </th>
            <th class="head">
                &nbsp;
            </th>
            <th class="head">
                Dev
            </th>
            <th class="head">
                Comments
            </th>
        </tr>
        <tr>
            <td>
                <em>sbpy.shape.lightcurve</em>
            </td>
            <td align='center'>
                <span class="planned"></span>
            </td>
            <td align='center'>
                MM
            </td>
            <td>
                lightcurve periodicity modeling tools and wrappers (periodograms, Fourier analysis) tbd.
            </td>
        </tr>
        <tr>
            <td>
                <em>sbpy.shape.inversion</em>
            </td>
            <td align='center'>
                <span class="planned"></span>
            </td>
            <td align='center'>
                MM
            </td>
             <td>
                Kaasalainen lightcurve inversion tool interface tbd.
            </td>
        </tr>
    </table>


`sbpy.spectroscopy`
-------------------

.. raw:: html

    <table border="1" class="docutils stability" align='center'>
        <tr>
            <th class="head">
                Sub-Packages and Classes
            </th>
            <th class="head">
                &nbsp;
            </th>
            <th class="head">
                Dev
            </th>
            <th class="head">
                Comments
            </th>
        </tr>
        <tr>
            <td>
                <em>sbpy.spectroscopy</em>
            </td>
            <td align='center'>
                <span class="dev"></span>
            </td>
            <td align='center'>
                MdVB
            </td>
            <td>
                some preliminary methods for absorption and emission spectroscopy implemented
            </td>
        </tr>
        <tr>
            <td>
                <em>sbpy.spectroscopy.reflectance</em>
            </td>
            <td align='center'>
                <span class="planned"></span>
            </td>
            <td align='center'>
                MM
            </td>
            <td>
                tools for identification of asteroid reflectance spectra tbd.
            </td>
        </tr>
        <tr>
            <td>
                <em>sbpy.spectroscopy.spectrophotometry</em>
            </td>
            <td align='center'>
                <span class="planned"></span>
            </td>
            <td align='center'>
                MM
            </td>
             <td>
                spectrophotometry tools tbd.
            </td>
        </tr>
        <tr>
            <td>
                <em>sbpy.spectroscopy.sources</em>
            </td>
            <td align='center'>
                <span class="planned"></span>
            </td>
            <td align='center'>
                MM
            </td>
            <td>
                `synphot` integration complete, basic quantities (bandpass filtering, color index) complete.
            </td>
        </tr>
        <tr>
            <td>
                <em>sbpy.spectroscopy.hapke</em>
            </td>
            <td align='center'>
                <span class="planned"></span>
            </td>
            <td align='center'>
                JYL
            </td>
             <td>
                Hapke spectral mixing model, TBD.
            </td>
        </tr>
    </table>

`sbpy.thermal`
--------------

.. raw:: html

    <table border="1" class="docutils stability" align='center'>
        <tr>
            <th class="head">
                Sub-Packages and Classes
            </th>
            <th class="head">
                &nbsp;
            </th>
            <th class="head">
                Dev
            </th>
            <th class="head">
                Comments
            </th>
        </tr>
        <tr>
            <td>
                <em>sbpy.thermal</em>
            </td>
            <td align='center'>
                <span class="dev"></span>
            </td>
            <td align='center'>
                MM
            </td>
            <td>
                currently under development
            </td>
        </tr>
   </table>


`sbpy.imageanalysis`
--------------------

.. raw:: html

    <table border="1" class="docutils stability" align='center'>
        <tr>
            <th class="head">
                Sub-Packages and Classes
            </th>
            <th class="head">
                &nbsp;
            </th>
            <th class="head">
                Dev
            </th>
            <th class="head">
                Comments
            </th>
        </tr>
        <tr>
            <td>
                <em>sbpy.imageanalysis.comettools</em>
            </td>
            <td align='center'>
                <span class="planned"></span>
            </td>
            <td align='center'>
                MSK
            </td>
            <td>
                comet coma image enhancement tools and image handling tbd.
            </td>
        </tr>
        <tr>
            <td>
                <em>sbpy.imageanalysis.psfsubtraction</em>
            </td>
            <td align='center'>
                <span class="planned"></span>
            </td>
            <td align='center'>
                MM
            </td>
            <td>
                 PSF subtraction techniques and wrappers tbd.
            </td>
        </tr>
    </table>


`sbpy.obsutil`
--------------

.. raw:: html

    <table border="1" class="docutils stability" align='center'>
        <tr>
            <th class="head">
                Sub-Packages and Classes
            </th>
            <th class="head">
                &nbsp;
            </th>
            <th class="head">
                Dev
            </th>
            <th class="head">
                Comments
            </th>
        </tr>
        <tr>
            <td>
                <em>sbpy.obsutil</em>
            </td>
            <td align='center'>
                <span class="planned"></span>
            </td>
            <td align='center'>
                MSK/MM
            </td>
            <td>
                finder charts, general observability and peak observability, planning tools, etc. tbd.
            </td>
        </tr>
    </table>


`sbpy.bib`
----------

.. raw:: html

    <table border="1" class="docutils stability" align='center'>
        <tr>
            <th class="head">
                Sub-Packages and Classes
            </th>
            <th class="head">
                &nbsp;
            </th>
            <th class="head">
                Dev
            </th>
            <th class="head">
                Comments
            </th>
        </tr>
        <tr>
            <td>
                <em>sbpy.bib</em>
            </td>
            <td align='center'>
                <span class="mature"></span>
            </td>
            <td align='center'>
                MSK/MdVB/MM
            </td>
            <td>
                fully implemented
            </td>
        </tr>
    </table>

`sbpy.calib`
------------

.. raw:: html

    <table border="1" class="docutils stability" align='center'>
        <tr>
            <th class="head">
                Sub-Packages and Classes
            </th>
            <th class="head">
                &nbsp;
            </th>
            <th class="head">
                Dev
            </th>
            <th class="head">
                Comments
            </th>
        </tr>
        <tr>
            <td>
                <em>sbpy.calib.sun</em>
            </td>
            <td align='center'>
                <span class="stable"></span>
            </td>
            <td align='center'>
                MSK
            </td>
            <td>
                <em>sbpy.calib.sun</em> implemented and fully tested.
            </td>
        </tr>
        <tr>
            <td>
                <em>sbpy.calib.vega</em>
            </td>
            <td align='center'>
                <span class="stable"></span>
            </td>
            <td align='center'>
                MSK
            </td>
            <td>
                <em>sbpy.calib.vega</em> implemented and fully tested.
            </td>
        </tr>
    </table>

