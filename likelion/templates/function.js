var A= prompt("첫번쨰 숫자를 입력해주세요");
var B= prompt("두번째 숫자를 입력해주세요");

function whichOne(a, b) {
    if(a>b){

        document.write(a+"가 더크군요 ")
    }
    else{
        document.write(b+"가 크군요");
    }

    return;
}