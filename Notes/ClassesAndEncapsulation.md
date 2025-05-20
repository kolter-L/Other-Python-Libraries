## BEST PRACTICE FOR PRIAVATE VARS

python does not actually have private vars, but we can use single or double underscores to show that something is private.

Single, like this does not actually change anything:

`my_class._my_var`

Double, like this creates name mangling where the var name is mangled with class name:

`my_class.__my_var`

To access either with a read only method, we use the @propery annotation:

```
    @property
    def my_var(self):
        return self.__my_var
```