var stepTgl = 0;

var acc = document.getElementsByClassName("accordion");
console.log(acc)
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

var viewportWidth = document.documentElement.clientWidth;
