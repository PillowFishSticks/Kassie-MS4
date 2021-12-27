
function openContent(evt, contentName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  if (document.getElementById(contentName)) {
      const element = document.getElementById(contentName).style.display = "block";
      evt.currentTarget.className += " active";
}
}

// Get the element with id="defaultOpen" and click on it
if (document.getElementById("defaultOpen")) {
  ﻿ const element = document.getElementById("defaultOpen").click();
  ﻿}