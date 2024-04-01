import re


word="1234"
reg=re.compile((r'[가-힣]'))

if reg.match(word):
    print("한글입니다")
else:
    print("한글이 아닙니다.")