#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let n = 0; n < this.height; n++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
