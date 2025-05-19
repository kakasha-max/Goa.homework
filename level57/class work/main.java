// მომხმარებლისგან მონაცემების მიღება
let firstName = prompt("შეიყვანე შენი სახელი:");
let lastName = prompt("შეიყვანე შენი გვარი:");
let age = prompt("შეიყვანე შენი ასაკი:");
let city = prompt("შეიყვანე საცხოვრებელი ადგილი:");
let profession = prompt("შეიყვანე შენი პროფესია:");

// წინადადების აგება
let sentence = "გამარჯობა, ჩემი სახელია " + firstName + ", ჩემი გვარია " + lastName + ", მე ვარ " + age + " წლის, ვცხოვრობ " + city + "-ში და ვარ " + profession + ".";

// შედეგის გამოტანა
console.log(sentence);
alert(sentence);