
//document.getElementById("edit_left").addEventListener("onchange", render)
//document.addEventListener("click", render)

function render_title() {
  document.getElementById("rendered_title").innerHTML = document.getElementById("id_title").value;
}

function render_content() {
  document.getElementById("rendered_content").innerHTML = document.getElementById("id_content").value;
}

function auto_complete(evt) {

  ele = evt.currentTarget;
  pos = ele.selectionStart;
  val = ele.value;
  last = val.lastIndexOf("<",pos-1);

  //define what tags should be autocompleted
  tags = ["a", "body", "button", "caption", "cite", "del", "div", "em", "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "iframe", "label", "li", "nav", "ol", "p", "section", "small", "span", "strong", "style", "sub", "sup", "table", "td", "textarea", "th", "title", "tr", "ul", "var"]

  if (evt.key == ">") {
    tag = val.substring(last+1,pos-1);
    if (tags.includes(tag)) {
      ins = "</" + tag + ">";
      evt.currentTarget.value = val.substring(0,pos) + ins + val.substring(pos);
      evt.currentTarget.selectionEnd = pos;
    }

  }
}


function script() {
  document.getElementById("id_title").addEventListener("keyup", render_title);
  document.getElementById("id_content").addEventListener("keyup", render_content);
  document.getElementById("id_content").addEventListener("keyup", auto_complete);
}
