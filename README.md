# BlockV1

## Code for programming education with Python

This is a project to make framework for children who are not familiar with programming language. And the goal of this framework is to get familiar with programming(language) and computational thinking. So this framework should make children to write their own code of their algorithm in abstract manner. As the final goal is getting familiar with programming, it is ***not*** recommended to use 'block-style' coding like 'Skretch'.

## Requirements
You need to install module `pygame` to run this code.

Open terminal and run this command below.
> `pip install pygame`

or

> `pip3 install pygame`


## Versions

### V1-0.01

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
    class change_color:
```
You can change a color of your `Box` with `change_color`. For example, the code
> ```python
>  actions.append(action.change_color((0, 0, 0)))


would change the color of your `Box` to black.

```python

    class Sequential:
```
For example if you want to move your box **left -> right -> down -> up** then
```python
action.Sequential(action.left, action.right, action.down, action.up)
```
would work.

## Run

*   V1-0.01

    Clone this repository and run
    ```
    python3 main.py
    ```
    Modify `move.py` to move red box.


## New features in consideration

> * Level selection system
> * New loading module system (with click)
> * Auto simulation system
> * Assignment system
> * Voice control system  
> and so on...