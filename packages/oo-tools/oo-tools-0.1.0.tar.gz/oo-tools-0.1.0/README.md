# oo-tools

Some basic object oriented tools for Python3.6+

## Development

Development occurs inside a Docker container.

Use the commands inside the ./bin directory to perform basic functions

`build.sh` will build the docker container

`enter.sh` will mount the current working directory of this repo into the docker container

`test.sh` will run the unit tests inside the docker container

## Examples

### Create an object that can save and load itself

```python
from oo_tools.save import Saver

class MyObj(Saver):
    name = 'foo'

filepath = '/tmp/myobj.obj'

myobj = MyObj
myobj.name = 'bar'

myobj.filepath = filepath
myobj.save()

del myobj # delete it from memory

myobj2 = MyObj()
myobj2.filepath = filepath

myobj2.name # equals 'foo'

myobj2.load()

myobj2.name # now equals 'bar' from save file
```

## Add a chain of responsibility pattern

Say you have some complex logic that you want to implement with the potential for nested ifs, fors, whatever. You can help flatten out this structure by breaking each control block into a separate class and then linking them together.

```python

from oo_tools.chain import Link

class StartChain(Link):

    # every link object must implement a process() method
    def process(self, *args, **kwargs):
        print('starting chain...')

        # calling do_next() will start the next chain
        self.do_next(1)

class CheckDatabase(Link):
    def process(self):
        # TODO ping the database

        database_is_up = True

        if database_is_up:
            self.next = InsertRecord()
            self.do_next('INSERT INTO test (test_value1) VALUES 1')
        else:
            print('Database is not available')
            exit

class InsertRecord(Link):
    def process(self, *args, **kwargs):
        # TODO connect to the database, insert record
        print('all done!')

if __name__ == '__main__':
    start = StartChain()
    start.next = CheckDatabase() # next defines the next portion of the chain

    start.process() # this will call the links in the order defined
```
