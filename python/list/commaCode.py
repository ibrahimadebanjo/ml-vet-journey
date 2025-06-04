spam = ['apples', 'bananas', 'tofu', 'cats']
def commaCode(spam):
    spam += spam[0] + spam[1] + spam[2] + spam[3]
    return spam

commaCode(spam)
print(spam)
# or
spam = ['apples', 'bananas', 'tofu', 'cats']
def func(spam):
    return spam
func(spam)
print(spam)

# deepseek correctio
def commaCode(items):
    if not items:
        return ''
    if len(items) == 1:
        return items[0]
    return ', '.join(items[:-1]) + ', and ' + items[-1]

# Example usage:
spam = ['apples', 'bananas', 'tofu', 'cats']
print(commaCode(spam))  # Output: "apples, bananans, tofu, and cats"