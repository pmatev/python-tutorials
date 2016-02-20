1. Write a function that takes 2 integers and returns the sum
```
    e.g. add(1, 2) # equals 3
         add(4, 5) # equals 9
```
2. Write a function that can add a list of numbers
```
    e.g. add([1, 2, 3, 4, 5]) # returns 15
```

3. Write a function that can add an abritrary amount of numbers as parameters (hint: lookup *args, **kwargs)
```
    e.g. add(1, 2, 3, 4, 5) # returns 15
```

4. Make a custom number object that can be used like this
```
    x = Number(1)
    x.value # returns 1
    x.add(1)
    x.value # returns 2
```

5. Extend your Number object to be able to be used like this:
```
    x = Number(1)
    y = Number(2)

    z = x + y
    z.value   # returns 3

    z += 1
    z.value  # returns 4
```

6. Extend your Number object to be able to do this:
```
    x = Number(1)
    print(x)  # returns '1'
```

7. Change your Number object to be able to do this:
```
    x = Number(1)
    y = x.add(1).add(1).add(1)
    y.value = 4
    x.value = 1
```

8. Extend your Number object to be able to do this:
```
    x = Number(1)
    y = x.add(1, 2, 3)
    y.value = 7
    x.value = 1
```

9. Create an EvenNumber object that can do this:
```
    x = EvenNumber(2)
    y = x.add(4).add(4)
    print(y) # 10

    x = EvenNumber(1) # raises Exception
```

10. Create a module called 'numbers' so that it can be used like this:
```
    import numbers

    x = numbers.Number(1)
    y = numbers.EvenNumber(2)
    ...

    or

    from numbers import Number, EvenNumber
```
