import re


def human_and(item_list):
    if len(item_list) == 0:
        return ''

    if len(item_list) == 1:
        return ' '.join(item_list)

    if len(item_list) == 2:
        return ' and '.join(item_list)

    return ', '.join(item_list[:-1]) + ' and ' + item_list[-1]


def clean_medication_name(name):
    try:
        return re.search('[a-zA-Z-_ ]+', name).group()
    except:
        return name


if __name__ == '__main__':
    print(human_and([]))
    print(human_and(['1']))
    print(human_and(['1', '2']))
    print(human_and(['1', '2', '3']))
    print(human_and(['1', '2', '3', '4']))
