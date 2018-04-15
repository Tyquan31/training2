# Data Structures amd Algorithms

## Building Stacks for Application State Management

> Stacks are a last in first out data structure, that provides operations like push, pop, peek,clear and size

> In most object-oriented programming (OOP) languages, you would find the stack data structure built-in, Not Javascript. Creating a stack using
JS is fairly easy though.

### Terminology

#### Top

> Indicates the top of the stack

#### Bottom

> Indicates the bottom of the stack

### API

> It is very hard to predict ahead of time what kinds of method your application will require. Therefore, it's usually a good idea to start off with whatever is the norm and then make changes as your applications demand.

#### Push

> Adds an item to the top of the stack

#### Pop

> Adds an item to the bottom of the stack

#### Peek

> Shows the last item pushed into the stack

#### Clear

> Empties the stack

#### Size

> Gets the current size of the stack

### Creating a stack

> "We will use a WeakMap() for our implementation. You can use any native data type for your implementation, but there are certain reasons why WeakMap() would be a strong contender. WeakMap() retains a weak reference to the keys that it holds. This means that once you are no longer referring to that particular key, it gets garbage-collected along with the value. However, WeakMap() come with its own downsides: keys can only be nonprimitives and are not enumerable, that is, you cannot get a list of all the keys, as they are dependent on the garbage collector.
However, in our case, we are more concerned with the values that our WeakMap() holds rather than keys and their internal memory management."

> ./stack1/1stack.js