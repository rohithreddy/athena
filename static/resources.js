var spans = $(".sidenote")
var labels = $("label")
$.each(spans, function(index, value) {
  console.log(index + ": " + value);
  value.remove();
});
$.each(labels, function(index, value) {
  $(labels[index]).after(spans[index]);
});

// <label class="margin-toggle sidenote-number" for="sn-anything"><input class="margin-toggle" id="sn-anything" type="checkbox">
console.log(labels)
$("label").replaceWith("<label class='margin-toggle sidenote-number' for='sn-anything'><input class='margin-toggle' id='sn-anything' type='checkbox'>");

$(window).on('resize', function() {
  enquire.register("screen and (max-width: 760px)", {
    match : function() {
      $('#blog-p').insertBefore('.thefooter');
    },
    unmatch : function() {
      $("#blog-p").insertAfter("body > div.thearticle > article > h1:nth-child(1)");
    }
  });
});

$(".thearticle > article > p:nth-of-type(2)").html(function (i, html) {
  return html.replace(/(\w+\S+\s)/, '<span class="newthought">$1</span>')
});

var spans = $(".sidenote")
var labels = $("label")
$.each(spans, function(index, value) {
  console.log(index + ": " + value);
  value.remove();
});
$.each(labels, function(index, value) {
  $(labels[index]).after(spans[index]);
});
$("label").replaceWith("<label class='margin-toggle sidenote-number' for='sn-anything'><input class='margin-toggle' id='sn-anything' type='checkbox'>");
