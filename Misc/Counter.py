from collections import Counter


class Test:
    def test_counter(self, my_string: str) -> dict:
        # my_counter = {}
        # for c in my_string:
        #     if c not in my_counter:
        #         my_counter[c] = 0
        #     my_counter[c] += 1

        # return my_counter

        my_counter = Counter(my_string)
        return my_counter


this_string = "mississippi"
sol = Test()
print(sol.test_counter(this_string))
