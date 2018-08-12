$(function(){
  var btn = $('button');
  var e = document.getElementById ('dataview');
  e.value = 'hoge';
  btn.click(function(){
    var a = document.getElementsByClassName('btn');
    var id =  $(this).attr("name");
    //btn.removeClass('active');
    if ($(this).hasClass('active')) {
      $(this).removeClass('active');
    }else{
      $(this).addClass('active');
    }
    //e.value=a[0].outerHTML;
    //console.log(a);

    var s='';
//    for(var j=0;j<2;j++){
      for(var i=0;i<10;i++){
        var s1=String(a[i].outerHTML);
        //var s1=String(a[i].);
        var result = s1.indexOf('active');
        console.log(s1,result);

        if(result>0){
          console.log('Hit');
          s=s+'1';
        }else{
          s=s+'0';
        }
        //console.log(a);
        console.log(i,s);
      }
//      s=s+'\n';
//    }
    e.value=s;
  });
});
