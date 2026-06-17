<<<<<<< HEAD
// 호이스팅(Hoistiong) 현상
console.log(num);
var num = 10;

//--- 자바스크립트에서 읽을때 다음과 같이 읽어버림.

var num;
console.log(num);
var num = 10;


let name = 'gildong'
const PI= 3.14;      // 상수 선언 및 초기화


/*
var(x), let(o), const(o)
*/

// 연산자
// 산술 연산자
console.log(20+10);
console.log(20-10);
console.log(20*10);
console.log(20/10);
console.log(20%10);

// 대입 연산자, 복합 대입 연산자
num = 10;
num += 10;
num -= 10;
num *= 10;
num /= 10;
num %= 10;


// 비교 연산자
console.log(10>20);
console.log(10>=20);
console.log(10<20);
console.log(10<=20);
console.log(10==20);
console.log(10!=20);

let num1 = 10;
let num2 = '10';
console.log('num1 == num2:', num1 == num2 );      // 자바스크립트에서 형 변환을 해버림
console.log('num1 === num2:', num1 === num2 );    // 타입까지 비교함
console.log('num1 !== num2:', num1 !== num2 );    // 

// 논리 연산자   (and = &&)
console.log(true && true);
console.log(true && false);
console.log(false && false);

// 논리 연산자 (or = ||)
console.log(true || true);
console.log(true || false);
console.log(false || false);

// 부정 연산자 (not = !)
console.log(!true);
console.log(!false);
console.log(!!!!false);


// 증감 연산자
let myScore = 80;
console.log('myScore:', myScore);

// myScore
myScore++;
console.log('myScore:', myScore);

myScore--;
console.log('myScore:', myScore);

// 전위 증감 연산자
myScore = 80;
temp = --myScore;
console.log('temp:', temp);
console.log('myScore:', myScore);

// 삼항(조건식) 연산자
// status = 'success' if myScore > 80 else 'fail'
   let score = 85;
   let grade = score >= 90 ?'A' : 'B';
   // 스코어가 90을 넘으면 A 그렇지 않으면 B
   //(? 는 앞에 조건이 참이라면 : 은 앞에 조건이 거짓이라면)

   

=======
// 호이스팅(Hoisting) 현상
// console.log(num)
// var num = 10;

// -------------------------------

// var num;
// console.log(num)  // undefined
// var num = 10;

// -------- 2015년 구글 엔진니어들이 ES6(V8)
let name = 'gildong'
const PI = 3.14;        // 상수 선언 및 초기화

/*
var(X), let(O), const(O)
*/

// 연산자
// 산술연산자
console.log(10 + 20);       // 30
console.log(10 - 20);       // -10
console.log(10 * 20);       // 200
console.log(10 / 20);       // 0.5
console.log(10 % 20);       // 10

// 대입연산자, 복합대입연산자
num = 10;
num += 10; // num = num + 10
num -= 10; // num = num - 10
num *= 10; // num = num * 10
num /= 10; // num = num / 10
num %= 10; // num = num % 10

// 비교연산자
console.log(10 > 20);   // false
console.log(10 >= 20);   // false
console.log(10 < 20);   // true
console.log(10 <= 20);   // true
console.log(10 == 20);   // false
console.log(10 != 20);   // true

let num1 = 10;
let num2 = '10';
console.log('num1 == num2: ', num1 == num2);  // num1 == num2:  true
console.log('num1 === num2: ', num1 === num2); // num1 === num2:  false
console.log('num1 !== num2: ', num1 !== num2); // num1 !== num2:  true


// 논리연산자
// &&  --> and
console.log(true && true); // true
console.log(true && false); // false
console.log(false && true); // false
console.log(false && false); // false

// ||  --> or
console.log(true || true); // true
console.log(true || false); // true
console.log(false || true); // true
console.log(false || false); // false

// ! --> not
console.log(!true); // false
console.log(!false); // true
console.log(!!false); // false

// 증감 연산자
let myScore = 80;
console.log('myScore: ', myScore);  // 80

// myScore += 1;  
myScore++;       
console.log('myScore: ', myScore);  // 81

myScore--;       
console.log('myScore: ', myScore);  // 80

// 후위 증감연산자
var temp = myScore--;
console.log('temp: ', temp);  // 80
console.log('myScore: ', myScore);  // 79

// 전위 증감연산자
myScore = 80;
temp = --myScore;
console.log('temp: ', temp); // 79
console.log('myScore: ', myScore);  // 79

// 삼항(조건식) 연산자
// status = 'success' if myScore > 80 else 'fail'

let score = 85;
let grade = score >= 90 ? 'A' : 'B';
console.log('grade: ', grade);
>>>>>>> 4c579c143ec73d274a4e1db75eff18a056e5a513
