# 1.

li = []


def flatten(n):
    for i in n:
        if isinstance(i, list):  # Kontrol ediyor liste mi diye
            flatten(i)
        else:
            li.append(i)  # Eğer liste değilse boş olan li elemanına ekliyor


liste = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5, [4.5]]
flatten(liste)
print(li)

print("----------------------")

# 2.

list_2 = []


def reverse_list(liste):
    for i in liste:
        if isinstance(i, list):
            i.reverse()
            list_2.append(i)
        else:
            list_2.append(i)


list_1 = [[1, 2], [3, 4], [5, 6, 7]]
reverse_list(list_1)
print(list_2)
