// 컨테이너 자료형
// 블로그번호 118
/*
1. 컨테이너 자료형이란?
컨테이너(Container) 자료형이란 여러 개의 데이터를 하나의 변수에 담아 관리할 수 있는 자료형을 말합니다.
즉, 하나의 값이 아닌 값들의 집합(묶음)을 표현할 수 있습니다.

JavaScript의 대표적인 컨테이너 자료형은 다음과 같습니다.
- 배열(Array): 순서가 있는 데이터의 집합(by index)
- 객체(Object): 이름(키)와 값(value)로 구성된 집합
*/

//배열(Array)
// 대괄호[]로 묶어 표현하며, 순서(index)를 기반으로 각 요소에 접근한다.
// 인덱스는 0부터 시작한다.

let fruits = ['사과', '바나나', '포도'];
console.log('fruits:', fruits);
console.log('fruits[0]:', fruits[0]);
console.log('fruits[1]:', fruits[1]);
console.log('fruits[2]:', fruits[2]);
for(let i = 0; i < fruits.length; i++){
    console.log(fruits[i]);
}

for (fruit of fruits){
    console.log(fruit);
}

// 마지막 값 구하기
let lastdata = fruits[fruits.length-1]
console.log(lastdata)

//객체(object)   → dic
let man = {
    'name' : '홍길동',
    'age'  : 20,
    'mail' : 'gildong@gmail.com',
    'nobby': ['축구', '농구', '배구'],
    'fun' : function(){
        console.log('멍');
    }
}

console.log('man:', man)
console.log('manName:', man['name'])
console.log('manNobby:', man['nobby'])
console.log('manNobby마지막데이터:', man['nobby'][man['nobby'].length -1])

man['fun']();

//함수(function)
/*1. function 함수이름(매개변수, ...){
    함수 실행 부
}
*/

function intro(){        //함수 선언부
    alert('안녕하세여');  // 함수 실행부
}
intro();                // 함수 호출부

//2. 함수 표현식(function expression)
/*
const 함수이름 = function(매개변수, ...){
    함수 실행부
}
*/
const intro1 = function(){
    alert('반갑습니다.');
}
intro1();

//화살표 함수 (arrow function)
/*
const 함수이름 = (매개변수, ...) =>{
    함수 실행 부
}
*/
const intro2 = () =>{
    alert('고맙습니다.');
}
intro2();

const add = (n1, n2) =>{
    return n1+n2;
}

let result = add(10, 20);
console.log('retult:', result);
