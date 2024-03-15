SSMtoYAML
=========

SSMtoYAML is a tool written in golang. It aims to be able to interact with AWS Parameter Store entries via CLI using yaml format. 

Documentation can be found `here <https://pkg.go.dev/gitlab.com/dkub/ssmtoyaml#section-readme>`_

Installation
------------

1. Ensure go is installed on your system. 
2. Clone the repository down to your machine (location does not matter)
   ``git clone https://gitlab.com/dkub/ssmtoyaml.git``
3. cd into the cloned directory
4. run the command ``go build``
5. Move the file ``ssmtoyaml`` to wherever you wish to store the executable


Usage
-----

Syntax of usage is ``ssmtoyaml [get|put] [options]``

Available inline options to use

============        =================   ========================================================================
Short Option        Long Option         Description
============        =================   ========================================================================
-d                  --decrypt           Set to decrypt SecureString values.
-f                  --force-overwrite   Overwrite the --out-file if it exists.
-h                  --help              help for get
-                   --ignore-tags       Do not write _tags keys to the output file.
-o                  --out-file string   The file to write YAML commands out to. (default "./ssmtoyaml_out.yaml")
-r                  --ssm-root string   A path root to retrieve from. (default "/")
-                   --region string     AWS Region to run against. (default "us-east-1")
============        =================   ========================================================================
