#!/usr/bin/nodejs

exports.esrever = function (list) {
  const rlist = [];
  if (!Array.isArray(list)) { return list; }
  for (let len = list.length - 1; len >= 0; len--) {
    rlist.push(list[len]);
  }
  return rlist;
};
