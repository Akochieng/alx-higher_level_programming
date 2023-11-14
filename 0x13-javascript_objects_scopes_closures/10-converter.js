#!/usr/bin/node

exports.converter = function (base) {
  const myFunc = function (num) {
    const temp;
    if (num < base) {
      if (num > 9) { console.log(String.fromCharCode(num - 9 + 60)); } else { console.log(num); }
      return;
    }
    temp = num % base;
    if (temp > 9) { console.log(String.fromCharCode(temp - 9 + 60)); } else { console.log(temp); }
    return (myFunc(parseInt(num / base)));
  };
  return myFunc;
}
