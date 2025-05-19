58 homevork----------
// მომხმარებელს შემოატანინეთ ცვლადი prompt-ის დახმარებით და ააწყვეთ წინადადება
let userName = prompt("შეიყვანე შენი სახელი");
console.log("სასიამოვნოა შენი გაცნობა, " + userName + "!");

// მომხმარებელს შემოატანინეთ 5 რიცხვი და გააკეთეთ მათემათიკური ოპერატორების გამოყენებით
let num1 = Number(prompt("შეიყვანე პირველი რიცხვი"));
let num2 = Number(prompt("შეიყვანე მეორე რიცხვი"));
let num3 = Number(prompt("შეიყვანე მესამე რიცხვი"));
let num4 = Number(prompt("შეიყვანე მეოთხე რიცხვი"));
let num5 = Number(prompt("შეიყვანე მეხუთე რიცხვი"));

console.log("ჯამი: " + (num1 + num2 + num3 + num4 + num5));
console.log("სხვაობა: " + (num1 - num2 - num3 - num4 - num5));
console.log("ნამრავლი: " + (num1 * num2 * num3 * num4 * num5));
console.log("გაყოფა: " + (num1 / num2));
console.log("ხარისხი: " + (num1 ** 2));
console.log("ნაშთი გაყოფისას: " + (num1 % num2));

// prompt-ის დახმარებით ააგეთ დიალოგი 2 მომხმარებელს შორის
let user1 = prompt("მომხმარებელი 1: რა გინდა თქვა?");
let user2 = prompt("მომხმარებელი 2: რას უპასუხებ?");
console.log("მომხმარებელი 1 ამბობს: " + user1);
console.log("მომხმარებელი 2 პასუხობს: " + user2);

// 5 მაგალითი ინკრემენტაციაზე
let a = 1;
a++;
console.log(a);

let b = 5;
b++;
console.log(b);

let c = 10;
c++;
console.log(c);

let d = -3;
d++;
console.log(d);

let e = 0;
e++;
console.log(e);

// 5 მაგალითი დეკრემენტაციაზე
let f = 10;
f--;
console.log(f);

let g = 0;
g--;
console.log(g);

let h = -5;
h--;
console.log(h);

let i = 100;
i--;
console.log(i);

let j = 1;
j--;
console.log(j);