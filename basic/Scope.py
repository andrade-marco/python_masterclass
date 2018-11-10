import os


# Inner function can access but not modify outer variables
# unless using nonlocal
def spam1():

    def spam2():

        def spam3():
            z = ' even'
            z += y
            return z

        y = ' more ' + x
        y += spam3()
        return y

    x = 'SPAM'
    x += spam2()
    return x


def list_directories(s):

    def dir_list(d):
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print('\t' * tab_stop + 'Directory ' + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print('\t' * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print('Directory listing of ' + s)
        dir_list(s)
    else:
        print(s + ' does not exist')


print(spam1())
list_directories('.')
