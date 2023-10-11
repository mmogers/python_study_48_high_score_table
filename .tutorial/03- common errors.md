# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*


## I/O operation error

👉 What is the problem here?
```python
f = open("savedFile.txt", "a")
whatText = input("> ")
f.write(f"{whatText}\n")
f.close()
whatText = input("> ")
f.write(f"{whatText}\n")
```

<details> <summary> 👀 Answer </summary>

The second input and write command are **after** the file has been closed instead of before.

```python
f = open("savedFile.txt", "a+")
whatText = input("> ")
f.write(f"{whatText}\n")
whatText = input("> ")
f.write(f"{whatText}\n")
f.close()
```


</details>