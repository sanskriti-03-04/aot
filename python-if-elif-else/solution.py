def classify_number(x: int | float) -> str:
    
    if x < 0 :
        return "negative"
    elif x == 0 :
        return "zero"
    elif 0 < x <= 10 :
        return "small"
    elif x >10 :
        return "large"
