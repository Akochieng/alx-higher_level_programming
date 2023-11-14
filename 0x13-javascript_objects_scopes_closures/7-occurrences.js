#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  if (!Array.isArray(list)) { return (0); }
  list.forEach(el => {
    if (el === searchElement) { count += 1; }
  });
  return count;
};
