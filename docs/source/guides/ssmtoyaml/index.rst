SSMtoYAML
=========

SSMtoYAML is a tool written in golang. It aims to be able to interact with AWS Parameter Store entries via CLI using yaml format. 

Documentation can be found `here <https://pkg.go.dev/gitlab.com/dkub/ssmtoyaml#section-readme>`_

Installation
------------


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
                    --ignore-tags       Do not write _tags keys to the output file.
-o                  --out-file string   The file to write YAML commands out to. (default "./ssmtoyaml_out.yaml")
-r                  --ssm-root string   A path root to retrieve from. (default "/")
                    --region string     AWS Region to run against. (default "us-east-1")
============        =================   ========================================================================
