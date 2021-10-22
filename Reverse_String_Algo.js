var str = 'Hello';
function reverseString(str){
    var newstr = ''
    for (i = str.length - 1; i >= 0; i--){
        newstr += str[i];
    }
    return newstr;

}
console.log(reverseString(str));
