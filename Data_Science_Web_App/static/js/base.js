
$(document).ready(function () {
  $('.navbar-light .dmenu').hover(function () {
    $(this).find('.sm-menu').first().stop(true, true).slideDown(150);
  }, function () {
    $(this).find('.sm-menu').first().stop(true, true).slideUp(105)
  });
});

function filterFunction() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("button");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "block";
    } else {
      a[i].style.display = "none";
    }
    if (filter == "") {
      a[i].style.display = "block";
    }
  }
}

function filterFunctionNav() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInputNav");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdownNav");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "block";
    } else {
      a[i].style.display = "none";
    }
    if (filter == "") {
      a[i].style.display = "none";
    }
  }
}
