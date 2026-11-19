# Demo bug report

When the bill request has `people: 0`, the app crashes with `ZeroDivisionError` instead of returning a useful validation error.

Traceback (from running `python app.py`):

```text
Traceback (most recent call last):
  File "app.py", line 19, in <module>
    print(process_bill({"total": 120.0, "people": 0, "discount": 10.0}))
  File "app.py", line 8, in process_bill
    per_person = calculate_split(discounted_total, people)
  File "calculator.py", line 6, in calculate_split
    return round(total_amount / num_people, 2)
ZeroDivisionError: division by zero
```
