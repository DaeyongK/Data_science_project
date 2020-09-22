var stepTgl = 0
var stepTgl1 = 0

var acc = document.getElementsByClassName("accordion");
var panel = document.getElementsByClassName('panel');

for (var i = 0; i < acc.length; i++) {
    acc[i].onclick = function() {
        if (stepTgl != 1) {
            var setClasses = !this.classList.contains('active');
            setClass(acc, 'active', 'remove');
            setClass(panel, 'show', 'remove');

            if (setClasses) {
                this.classList.toggle("active");
                this.nextElementSibling.classList.toggle("show");
            }
        }
    }
}

function setClass(els, className, fnName) {
    if (stepTgl != 1) {
        for (var i = 0; i < els.length; i++) {
            els[i].classList[fnName](className);
        }
    }
}

var acc1 = document.getElementsByClassName("accordion1");
var panel1 = document.getElementsByClassName('panel1');

for (var i = 0; i < acc1.length; i++) {
    acc1[i].onclick = function() {
        if (stepTgl1 != 1) {
            var setClasses1 = !this.classList.contains('active');
            setClass1(acc1, 'active', 'remove');
            setClass1(panel1, 'show', 'remove');

            if (setClasses1) {
                this.classList.toggle("active");
                this.nextElementSibling.classList.toggle("show");
            }
        }
    }
}

function setClass1(els, className, fnName) {
    if (stepTgl1 != 1) {
        for (var i = 0; i < els.length; i++) {
            els[i].classList[fnName](className);
        }
    }
}

document.getElementById("step2").style.display = "none";
document.getElementById("step3").style.display = "none";
document.getElementById("step4").style.display = "none";


function toStep2() {
    var x = document.getElementById("step2");
    if (x.style.display === "none") {
        x.style.display = "";
    }
    document.querySelector('#btGrp1').innerHTML = 'Done!';
}

function toStep3() {
    var x = document.getElementById("step3");
    if (x.style.display === "none") {
        x.style.display = "";
        stepTgl = 1
    }
    document.querySelector('#btGrp2-1').innerHTML = 'Selected!';
    document.querySelector('#btGrp2-2').innerHTML = 'Selected!';
    document.querySelector('#btGrp2-3').innerHTML = 'Selected!';
}

function toStep4() {
    var x = document.getElementById("step4");
    if (x.style.display === "none") {
        x.style.display = "";
        "";
        stepTgl1 = 1
    }
    document.querySelector('#btGrp3-1').innerHTML = 'Selected!';
    document.querySelector('#btGrp3-2').innerHTML = 'Selected!';
    document.querySelector('#btGrp3-3').innerHTML = 'Selected!';
}

var viewportWidth = document.documentElement.clientWidth;


function alg1() {
    var x = document.getElementById("finalOutput");
    x.innerHTML = "<img src='https://i.imgur.com/DRfO8j5.jpeg' width = '300'>"
}

function alg2() {
    var x = document.getElementById("finalOutput");
    x.innerHTML = "<img src='https://i.imgur.com/JxIraTo.jpeg' width = '300'>"
}

function alg3() {
    var x = document.getElementById("finalOutput");
    x.innerHTML = "<img src='https://i.imgur.com/RnEtxIq.jpg' width = '300'>"
}
