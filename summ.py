'''
    ye h ek module
'''
def summ(*arg: float):
    count = 0
    for i in *args:
        count += i
    return count

if __name__ == "__main__":
    print('run as main')
