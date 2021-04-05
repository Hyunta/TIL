def solution(phone_book):
    phone_book.sort()
    for i,x in enumerate(phone_book):
        if any(x in y[:len(x)] for y in phone_book[i+1:i+10]): # i+10 부분이 완벽하지 못함, 혹시 11번째에 나오게 되면 제대로된 값 안나옴
            return False
            sys.exit(0)
    return True
