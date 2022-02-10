def get_data(file):
    #
    with open(file, mode='r', encoding='utf8') as f:
        rest = f.readlines()
        data_li = []
    for i in range(1, len(rest)):
        tup = tuple(rest[i].strip().split(','))
        data_li.append(tup)
    return data_li
if __name__ == '__main__':
    print(get_data(r'F:\Users\admin\PycharmProjects\untitled\test\data\login.csv'))