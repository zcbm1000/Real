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

   

