"""
Given two dataframes, implement the join/merge operation - inner, left/right_outer, full_outer.
"""

table1 = [{
    "id": 100,
    "name": "abc"
},
    {
        "id": 101,
        "name": "abcs"
    }
]
table2 = [
    {
        "id": 100,
        "name": "abc"
    },
    {
        "id": 103,
        "name": "xyx"
    }
]


def inner_join(table1, table2):
    result = []
    for ele in table1:
        if ele['id'] in table2:
            result.append(ele)
    return result


# print(inner_join(table1,table2))
"""
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
"""

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
def is_odd(n):
    if n%2 == 0:
        return False
    return True
result = lambda x: x%2 !=0
