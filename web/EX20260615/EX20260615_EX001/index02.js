<<<<<<< HEAD
// 제어문 - 조건문(if 문, switcd ~ case 문)
/*
if 문
if(조건식){
    실행문
    }
*/
let age = 20;
if (age >= 18){
    console.log('성인 입니다.')
}

/* 
if ~ else 문
*/
let isLogin = false;
if (isLogin) {
    console.log('로그인 상태입니다.')
} else{
    console.log('비 로그인 상태입니다.')
}

/*
if ~ else if ~ else if   → 다중 비교
*/
let score = 85;
if (score >= 90){
    console.log('A학점');
}
else if (score >= 80){
    console.log('B학점');
}
else if (score >= 70){
    console.log('C학점');
}
else if (score >= 60){
    console.log('D학점');
}
else {
    console.log('F학점')
}

// switch 문  → 콕! 찝어서 실행을 함.
let day = 3
switch(day){
    case 1:
        console.log('월요일')
        break; // break가 없을경우 day 를 1로 실행하면 break가 없는곳도 실행

    case 2:
        console.log('화요일')
=======
// 제어문 - 조건문(if문, switch ~ case문)
/*
if문
if (조건식) {
    실행문
}
*/
let age = 20;
if (age >= 18) {
    console.log('성인 입니다.')
}

/*
if ~ else문   -> 양자택일
*/
let isLogin = false;
if (isLogin) {
    console.log('로그인 되어 있어요.')
} else {
    console.log('로그인 되어 있지않아요.')
}

/*
if ~ else if ~ else if .......   -> 다중 비교
*/
let score = 85;
if (score >= 90) {
    console.log('A학점');

} else if (score >= 80) {
    console.log('B학점');

} else if (score >= 70) {
    console.log('C학점');

} else if (score >= 60) {
    console.log('D학점');

} else {
    console.log('F학점');
    
}

// switch문 --> 콕! 찝어서 실행
let day = 0;
switch(day) {

    case 1:
        console.log('월요일')
>>>>>>> 4c579c143ec73d274a4e1db75eff18a056e5a513
        break;

    case 3:
        console.log('수요일')
        break;

<<<<<<< HEAD
=======
    case 2:
        console.log('화요일')
        break;

>>>>>>> 4c579c143ec73d274a4e1db75eff18a056e5a513
    case 4:
        console.log('목요일')
        break;

    default:
<<<<<<< HEAD
        console.log('몰라요!')
        break;               
}

// 제어문 - 반복문(for문, while문)
// for 문  → 횟수에 의한 반복 실행
/*
파이썬에서는
for 변수 in 반복범위:
    실행문

자바스크립트에서는
for (초기식; 증감식){
    반복 실행문
}
*/
let sum = 0
for (let n =1; n < 11; n++){
    sum += n;
}
    console.log('sum:', sum);

for(i=10, j=0; i>0, j<10; i--,j++){
    console.log('i:', i);
    console.log('j:', j);
}

// while 문 → 조건에 의한 반복 실행
/*
파이썬에서는
while True:
    실행문

자바스크립트에서는
while(조건식){
실행문
}
*/
let k = 3;
while(k < 10){
    console.log('k:', k);
=======
        console.log('몰라요!!')
    
}

// 제어문 - 박복문(for문, while문)
// for문 -> 횟수에 의한 반복 실행
/*
1에서 부터 10까지의 정수의 합

for (초기식; 조건식; 증감식) {
    반복 실행문
}
*/

// let sum = 0;
// for (let n = 1; n < 11; n++) {  // 1부터 10까지 1씩 증가해야!
//     sum += n;
// }
// console.log('sum: ', sum);      // 55

// let sum = 0;
// let n = 1;
// for (; n < 11; n++) {
//     sum += n;
// }
// console.log('sum: ', sum);      // 55

for (let i=10, j=0; i > 0, j < 10; i--, j++) {
    console.log('i: ', i);
    console.log('j: ', j);
}

// for (let i=10, j=0; i > 0, j < 10; i--) {
//     console.log('i: ', i);
//     console.log('j: ', j);
// }

// for (let i=10, j=0; true; i--, j++) {
//     console.log('i: ', i);
//     console.log('j: ', j);
// }


// while문 -> 조건에 의한 반복 실행
/*
while (조건식) {
    실행문    
}
*/

let k = 3;
while (k < 10) {
    console.log('k: ', k);
>>>>>>> 4c579c143ec73d274a4e1db75eff18a056e5a513
    if (k >= 7) break;
    k++;
}

<<<<<<< HEAD
// do ~ while 문
let count = 5;
do{
    console.log('count:', count);
    count--;
}while(count > 0);

let pt = prompt('이름을 입력하세요:');
console.log('pt:', pt)

let pt = prompt('숫자를 입력하세요:');





=======
// do ~ while문
let count = 5;
do {
    console.log('count: ', count);      // 5
    count--;
} while(count > 10);

let pt = prompt("숫자 입력");
console.log('pt: ', typeof(Number(pt)));
>>>>>>> 4c579c143ec73d274a4e1db75eff18a056e5a513
