/*
This time no story, no theory. The examples below show you how to write function accum:

Examples:
  accum("abcd") -> "A-Bb-Ccc-Dddd"
  accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
  accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
*/

function accum(str) {
  let letters = str.toLowerCase().split('');
  for(let i = 0; i < letters.length; i++){
    letters[i] = letters[i].toUpperCase() + letters[i].repeat(i);
  }
	return letters.join('-');
}