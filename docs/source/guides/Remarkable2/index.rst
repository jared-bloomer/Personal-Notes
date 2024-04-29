Remarkable2
===========

Remarkable does not officially support custom templates. When you sync documents to your remarkable app you will NOT see your custom templates. If you email the document from your remarkable2 to yourself, it will contain the template. Also after your Remarkable2 installs any updates, your custom templates may disappear and need to be reinstalled. 

Managing Custom Templates
-------------------------

The easiest way to manage custom templates is to use the `templatectl <https://github.com/PeterGrace/templatectl>`_. 

To Install ``templatectl``
__________________________

1. Go to the `release page <https://github.com/PeterGrace/templatectl/releases>`_ of the repo, and download the ``templatectl`` file to your machine. 
2. You then want to upload this file to your remarkable2 tablet. You can use scp to do this 
``scp templatectl root@<IP Address of your Remarkable2>:/home/root/.``

Adding New Templates
____________________

