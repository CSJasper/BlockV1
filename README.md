# Code for education with Python Programming (On progress)


## Requirements
You need to install module `pygame` to run this code.

Open terminal and run this command below.
> `pip install pygame`

or

> `pip3 install pygame`


## Versions

### Ver-0.01

Complete code in `move.py` to move your blocks on screen.

#### Supported class and method

In class **action** 

```python
    @staticmethod
    def move_left(obj: Box):
```
is a function to move your object `Box` left from its current position. If you write your code to move your `Box` to invalid position such as outside of the screen just do nothing. Other methods(functions) below work similarly.

```python
    @staticmethod
    def move_right(obj: Box):

    @staticmethod
    def move_down(obj: Box):

    @staticmethod
    def move_up(obj: Box):
```
`move_random()` will moves your box to random valid positions.
```python
    @staticmethod
    def move_random(obj: Box):
```

The class `Sequential` inside the class `action` is a callable class which enable us to move object `Box` with series of ordered actions
```python
    @staticmethod
    def change_color(obj: Box, color: tuple):

    class Sequential:
```
For example if you want to move your box **left -> right -> down -> up** then
```python
action.Sequential(action.left, action.right, action.down, action.up)
```
would work.