# merge_sort e merge do Course Trybe
# https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/290e715d-73e3-4b2d-a3c7-4fe113474070/section/73f2a1d5-7d77-440b-a9f2-3ea9750db228/day/346e18ae-25d8-47a5-bd59-0e4d9cd2a2d2/lesson/9b22b10c-1e8a-4f00-bab8-edac69573b6b


def merge_sort(array, start=0, end=None):
    if end is None:
        end = len(array)
    if (end - start) > 1:  # se não reduzi o suficiente, continua
        mid = (start + end) // 2  # encontrando o meio
        merge_sort(array, start, mid)  # dividindo as listas
        merge_sort(array, mid, end)
        merge(array, start, mid, end)  # unindo as listas


# função auxiliar que realiza a mistura dos dois arrays


def merge(lista, start, mid, end):
    left = lista[start:mid]
    right = lista[mid:end]
    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            lista[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            lista[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            lista[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            lista[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    first = list(first_string.lower())
    second = list(second_string.lower())
    merge_sort(first, 0, len(first))
    merge_sort(second, 0, len(second))
    if first == second:
        return True
    return False
