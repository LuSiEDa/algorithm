def solution(price):
    if price >= 500000:
        return round(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return price * 95 // 100
    else:
        return price
