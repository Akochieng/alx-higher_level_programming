#!/usr/bin/node

exports.callMeMoby = function (num, func) {
  while (num > 0) {
    func();
    num--;
  }
};
