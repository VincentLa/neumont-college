counter_names = 0
def post_name(arg=''):
    global counter_names
    counter_names += 1
    print(arg)

post_name('hello')