# Solution (No Peeking!)
![](https://www.youtube.com/watch?v=KobdLjIvoeE)

<details> <summary> 👀 Answer </summary>

```python
import os, time

while True:
  print("HIGH SCORE TABLE")
  print()
  name = input("INITIALS > ").upper()
  score = input("SCORE > ")
  print()

  f = open("high.score", "a+")
  f.write(f"{name} {score}\n")
  f.close()

  print("ADDED")
  time.sleep(1)
  os.system("clear")
```

</details>

- Join our [100 Days Community](https://replit.com/100-days-help)
- Want [live support?](https://replit.com/replit-101)