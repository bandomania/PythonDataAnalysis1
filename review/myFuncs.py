# 사용자 정의 함수를 모듈로 저장합니다.
def BMI(hgt = 175, wgt = 65):
    '''
    This function returns BMI from height(cm) and weight(kg).
    '''
    return wgt / (hgt/100) ** 2
