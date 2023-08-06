# Usage
|Usage|Params|Return Value|
|:----------|:----------|:----------|
|`ansiprint()`|`str: msg, str: color-name/ansi, str: end`|`str: msg`|
|`ansi()`|`str: color-name/ansi`|`str: ansi`|
|`clear()`|`None: None`|`None: None`|


# Examples
***
### `ansiprint()`
Code:
```python
ansiprint("This is red!","red")
ansiprint("This is blue!","blue")
ansiprint("This is white and ends with \"!\"",end="!")
```
Result:
![result](https://storage.googleapis.com/replit/images/1588596722137_d902a72107ec2e5dcd46ece46f8fa736.png)
***
### `ansi()`
Code:
```python
print(ansi("red") + "This is red!" + ansi("reset"))
print(ansi("blue") + "This is blue!" + ansi("reset"))
print(ansi(34) + "This is the ansi \"34\"!" + ansi("reset")) # ansi codes are in the ansi chart below
```
Result:
![result](https://storage.googleapis.com/replit/images/1588596889015_c9512973133f54b679fab0c2796e3dfc.png)
***
### `clear()`
Code:
```python
print("This message isn't seen because the console is cleared after!")
clear()
print("This message is seen because it is after the console is cleared!")
```
Result:
![result](https://storage.googleapis.com/replit/images/1588597110270_64b10e0243424eb8b2f7250b391e81fc.png)
***
## Ansi Chart
![ansi chart](https://storage.googleapis.com/replit/images/1588547351487_f17f0b104ccf45830db6df04d26537fe.png)