def check_len(obj):
    if hasattr(obj,'__len__'):
        print(len(obj))
    else:
        print('sorry....')

check_len()