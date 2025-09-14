# def snake_case_converter(my_string):
#     my_list = []
#     for char in my_string:
#         if char.isupper():
#             my_list.append('_'+char.lower())
#         else:
#             my_list.append(char)
#     result = ''.join(my_list)
#     result = result.strip('_')
#     return result


def snake_case_converter(my_string):
    my_list = ['_' + char.lower() if char.isupper() else char for char in my_string]

    return ''.join(my_list).strip('_')
def main():
    examples = [
    ["camelCase", "camel_case"],
    ["PascalCase", "pascal_case"],
    ["thisIsATest", "this_is_a_test"],
    ["AnotherExampleHere", "another_example_here"],
    ["yetAnotherOne", "yet_another_one"],
    ["MyVariableName", "my_variable_name"]
]
    for i, example in enumerate(examples):
       
        print(f"{i}:    camelOrpascalCase: {example[0]}, result: {example[1] ==  snake_case_converter(example[0])}")
        

main()