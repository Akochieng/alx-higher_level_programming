#!/usr/bin/node

exports.converter = function (base) {
  const myFunc = function (num) {
    let temp = 0;
    let str = '';
    if (num < base) {
      if (num > 9) {
        str += String.fromCharCode(num - 9 + 60); 
      } else {
        str += num;
        }
      return str;
    }
    temp = num % base;
    if (temp > 9) {
      str += String.fromCharCode(temp - 9 + 60);
    } else {
      str += temp;
    }
    return myFunc(parseInt(num / base)) + str;
  };
  return (function (num) {
    let str = myFunc(num);
    console.log(str);
  });
}
