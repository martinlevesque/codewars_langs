
# when calling add(N) it returns the instance from the int class
# when calling add(N)(N), the call method make another class instance
# and add n
class add(int):
    def __call__(self, n):
        return add(self + n)


assert add(1) == 1
assert add(1)(2) == 3
assert add(1)(2)(3) == 6

