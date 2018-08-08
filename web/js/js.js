$(function(){
  var btn = $('button');
  btn.click(function(){
    //btn.removeClass('active');
    if ($(this).hasClass('active')) {
      $(this).removeClass('active');

    }else{
      $(this).addClass('active');      
    }
  });
});
