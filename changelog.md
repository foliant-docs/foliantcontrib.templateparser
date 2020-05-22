# 1.0.4

-    All variables, supplied in context, are also available inside the `_foliant_context` variable
-    You can now supply a link to file on remote server in the `ext_context` parameter.
-    External context yaml-file now may be not a dictionary. In this case it will be available under the `context` template variable.

# 1.0.3

-    Now meta dictionary is available inside templates under `meta` variable.
-    Project's meta object is available inside templates under `meta_object` variable.

# 1.0.2

-    support PyYAML 5.1

# 1.0.1

-    add ext_context param for external file with context
-    allow separate templates to fail, the preprocessor would issue warning and skip them

# 1.0.0

-    Initial release