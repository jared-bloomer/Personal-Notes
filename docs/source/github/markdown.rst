Github Markdown Cheatsheet
==========================

Text Formatting
---------------

Official Documentation can be found in the `Github Docs <https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax>`_

=============   ======================      =========================================   ==================================================
Formatting      Markdown                    Example                                     Output
=============   ======================      =========================================   ==================================================
Bold            ``** **`` or ``__ __``      ``**This is bold text**``                   **This is bold text**
Italics         ``* *`` or ``_ _``          ``_This text is italicized_``               *This text is italicized*
Strikethrough   ``~~ ~~``                   ``~~This was mistaken text~~``              T̶h̶i̶s̶ ̶w̶a̶s̶ ̶m̶i̶s̶t̶a̶k̶e̶n̶ ̶t̶e̶x̶t̶
Subscript       ``<sub> </sub>``            ``This is a <sub>subscript</sub> text``     This is a :sub:`subscript` text
Superscript     ``<sup> </sup>``            ``This is a <sup>superscript</sup> text``   This is a :sup:`superscript` text
=============   ======================      =========================================   ==================================================


Callouts
--------

Documentation on this feature can be found in the `Github Discussions <https://github.com/orgs/community/discussions/16925>`_

.. image:: _static/callouts.png

.. code::

    [!NOTE]  
    Highlights information that users should take into account, even when skimming.

    [!TIP]
    Optional information to help a user be more successful.

    [!IMPORTANT]  
    Crucial information necessary for users to succeed.

    [!WARNING]  
    Critical content demanding immediate user attention due to potential risks.

    [!CAUTION]
    Negative potential consequences of an action.

Badges
------

More Advanced Documentation can be found `here <https://daily.dev/blog/readme-badges-github-workflow-status-indicators>`_

For Licensing Badges, go view them on this `Github gist <https://gist.github.com/lukas-h/2a5d00690736b4c3a7ba>`_

===============         =======================================================================================================================   =======================================================================================================
Badges                  Markdown                                                                                                                  Output
===============         =======================================================================================================================   =======================================================================================================
Workflow Status         ``![Github Pages](https://github.com/jared-bloomer/Personal-Notes/actions/workflows/github-pages.yml/badge.svg)``         .. image:: https://github.com/jared-bloomer/Personal-Notes/actions/workflows/github-pages.yml/badge.svg
Code Coverage           ``[![Coverage](https://img.shields.io/badge/Coverage-83%25-brightgreen.svg)](https://my-app.com/coverage/report.html)``   .. image:: https://img.shields.io/badge/Coverage-83%25-brightgreen.svg
License                 ``[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)``    .. image:: https://img.shields.io/badge/License-Apache_2.0-blue.svg
Contributors            ``![Contributors](https://img.shields.io/github/contributors/jared-bloomer/Personal-Notes)``                              .. image:: https://img.shields.io/github/contributors/jared-bloomer/Personal-Notes
Issues                  ``![Issues](https://img.shields.io/github/issues/jared-bloomer/Personal-Notes?color=0088ff)``                             .. image:: https://img.shields.io/github/issues/jared-bloomer/Personal-Notes?color=0088ff
Pull Request            ``![Pull Request](https://img.shields.io/github/issues-pr/jared-bloomer/Personal-Notes?color=0088ff)``                    .. image:: https://img.shields.io/github/issues-pr/jared-bloomer/Personal-Notes?color=0088ff
===============         =======================================================================================================================   =======================================================================================================