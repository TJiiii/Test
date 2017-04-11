# 귀찮았기에 적당히 받는 장소

README 는 나중에 추가하도록 하자.

YYMMDD-ABCDEFG(출생년도 : 생년월일)

[뒷 7자리 차례대로 설명]
 
A : 남녀 성별구분(남자 : 1, 3, 여자 : 2, 4) 3과 4는 2000년 이후 출생자를 뜻함
B ~  E : 출생신고를 기록한 지역의 고유번호
    B : 출생신고지 광역시 or 도 단위 번호(서울 0, 부산, 1, 경남 9 ....)
    C : 시, 군 단위 번호
    D : 읍, 면, 동 단위 번호
    E : 통, 반, 리 단위 번호
F : 같은 날 같은 성씨로 출생신고를 등록한 순서가 됩니다.(F != 0)
G : 체크번호(검증번호) 이 숫자로 맞는 주민등록번호인지 확인이 가능합니다.
 
 
 
[정상적인 주민등록번호인지 확인 알고리즘]
 
예를 들어 640713-******* 이 주민번호를 예로 들어보죠
우선 주민등록번호 마지막자리수만 제외하고, 
각각의 자리수마다 다음과 같은 수를 곱하여 전체를 더한다.
6 4 0 7 1 3 1 0 1 8 4 3 
x x x x x x x x x x x x 
2 3 4 5 6 7 8 9 2 3 4 5 
-----------------------
+ + + + + + + + + + + +
즉, (6*2)+(4*3)+(0*4)+(7*5)+(1*6)+(3*7)+(1*8)+(0*9)+(1*2)
+(8*3)+(4*4)+(3*5) = 151
그러면 151 이란 수가 나온다. 이 151을 매직키인 11로 나누어 나머지만 취한다.
151 / 11 = 몫: 13 <-- 버림
나머지: 8
마지막 단계로 매직키인 11에서 나머지 8을 빼면 3이란 수가 나오
는데, 이숫자가 주민등록번호 마지막 자리의 숫자와 일치하면 대한민국 국민이다.
11 - 8 = 3 --> 정상적인 주민등록번호임
