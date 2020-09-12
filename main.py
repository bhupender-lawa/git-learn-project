from operations import summ

def addition():
    numbers = tuple(map(int, input('Enter no.s to summ: ').split()))
    return print(f'the summ is = {summ(numbers)}')

if __name__ == "__main__":
    addition()
    input("Press enter to exit:")