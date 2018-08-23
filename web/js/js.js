//Project Hata 用JS

function waitTextValueCng($this) {
    console.log($this.value);
    var viewArea = document.getElementById ('dataview');
    //console.log(viewArea.value);
    //ここで自動的にviewAreaの最初の行を差し替えるようにしてもよいかも（未実装）
    //document.getElementById("dataview").value = $this.value + viewArea.value;


}

function cpFileBtnOn($this) {
  // Copyボタン押されると呼び出される。csvFileNameTextの値をボタンの値に
    console.log($this.value);
    document.getElementById("csvFileNameText").value = $this.value;

    // *.csvをリスト化してプルダウンリストにしてもよいかも？（未実装）
}


$(
  // シーケンサーマトリクスクリックチェック用

  function(){
  var btn = $('button');
  var e = document.getElementById ('dataview');
  var stat = document.getElementById ('stat');
  var waitSec = document.getElementById ('WaitTime');

  //console.log(stat,waitSec);

  //e.value = 'hoge';
  btn.click(function(){
    var a = document.getElementsByClassName('btn');
    var name =  $(this).attr("name"); //name拾っているが使ってない
    //btn.removeClass('active');
    if ($(this).hasClass('active')) {
      $(this).removeClass('active');
    }else{
      $(this).addClass('active');
    }
    //e.value=a[0].outerHTML;
    //console.log(a);

    var s='';

    //var s2=String(waitSec.outerHTML);
    var s2=waitSec.value;
      console.log('Wait=',s2);

      //s=s+s2+'\n';
      s=s2+'\n';

      for(var i=0;i<(20*6);i++){
        if(!(i % 20)){
          if (i !=0 ){
            s=s.slice(0,-1) // 最後の , カット
            s=s+'\n';
          }
        }

        var s1=String(a[i].outerHTML);
        //var s1=String(a[i].);
        var result = s1.indexOf('active');
        console.log(s1,result);

        if(result>0){
          console.log('Hit');
          s=s+'1,';
        }else{
          s=s+'0,';
        }
        //console.log(a);
        console.log(i,s);
      }
    s=s.slice(0,-1) // 最後の , カット
    e.value=s;
  });
});
