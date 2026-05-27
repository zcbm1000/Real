def coverUnit(lenMm):
    unitDic = {}

    unitDic['cm'] = lenMm * .1
    unitDic['m'] = lenMm * .001
    unitDic['inch'] = lenMm * .03931
    unitDic['ft'] = lenMm * .003281

    return unitDic

def pringLength(lengths):
    for len in lengths.keys():
        print(f'{len}: {lengths[len]}{len}')
inputData = int(input(f'길이(mm)를 입력하세요.\n 입력:'))
resultData = coverUnit(inputData)
printLength = (resultData)