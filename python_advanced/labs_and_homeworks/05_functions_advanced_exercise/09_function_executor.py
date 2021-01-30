def func_executor(*args):
    results = []
    for function_name, numbers in args:
        final_res = function_name(*numbers)
        results.append(final_res)

    return results


