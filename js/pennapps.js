// pennappses go ['season', 'year', 'link']
var pennappses = [
  ['Spring', '2012', 'http://2012s.pennapps.com/'],
  ['Fall', '2011', 'http://2011f.pennapps.com/'],
  ['Spring', '2011', 'http://pennapps.com/spring2011/'],
  ['Fall', '2010', 'http://pennapps.com/2010'],
  ['Fall', '2009', 'http://pennapps.com/2009']
];
var html = "";
$.each(pennappses, function(index, pennapps) {
  html += "<div style='background-image: url(img/"+pennapps[0]+pennapps[1]+".png)' class='pennapps_container' data-link='"+pennapps[2]+"'";
  html += "<div class='pennapps' id='"+pennapps[0]+pennapps[1]+"'>";
  html += "<div class='left'>";
  html +=   "<span class='season'>"+pennapps[0]+"</span>";
  html +=   "<span class='year'>"+pennapps[1]+"</span>";
  html += "</div>";
  html += "<div class='right'></div>";
  html += "</div>";
  html += "</div>";
});
document.write(html);
$('.pennapps_container').on('click', function() {
  window.open($(this).data('link'),'_blank');
});
$('.pennapps_container').on('mouseenter touchstart', function() {
  // console.log($(this).attr('id'));
  $(this).css('background-image', "url(img/"+$(this).attr('id')+"_active.png)");
});
$('.pennapps_container').on('mouseout touchend', function() {
  $(this).css('background-image', "url(img/"+$(this).attr('id')+".png)");
});
