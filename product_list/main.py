def product_list(input_list):
    product_array = []
    for index in range(len(input_list)):
        product = 1
        for pointer in range(len(input_list)):
            if pointer == index:
                continue
            product *= input_list[pointer]
        # print('product:', [product])
        product_array.append(product)
    print('product_array', product_array)

    return product_array


assert product_list([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert product_list([2, 2, 2, 2]) == [8, 8, 8, 8]
assert product_list([10, 20]) == [20, 10]
assert product_list([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
assert product_list([10, 3, 5, 6, 2]) == [180, 600, 360, 300, 900]
