alert('hello')
// 페이지 실행시 알람을 나타냄.

// 원시 타입
var num = 42;         // Number
var pi = 3.14;        // Number
var name = '홍길동';   // String
var name = "홍길동";   // String
var isStudent = true; // boolean
var nothing;          // Undefined



console.log('num:', num);
console.log('numType:', typeof(num));
console.log('pi:', pi);
console.log('piType', typeof(pi));
console.log('isStudent', typeof(isStudent));

// 참조 타입
var fruits = ['사과', '바나나', '포도'];
console.log('fruits:', fruits);
console.log('fruitsLength:', fruits.length);
console.log('fruitsType:', typeof(fruits));


// 파이썬에서는 딕셔너리, 자바스크립트에서는 오브젝트
var person = {
    'name' : '홍길동',
    'age'  : 20,
    'mail' : 'gildong@Gmail.com'
};
console.log('person:', person);
console.log('personType:', typeof(person));

// 함수
// 함수도 데이터기에 변수에 담아서 사용을한다.
var myFun = function(){
    console.log('myFun() CALLED!')
};

    console.log('myFun:', myFun);
    console.log('myFunType:', typeof(myFun));
    myFun() // 함수 호출 호출하면 'myFun() CALLED!' 가 호출된다.