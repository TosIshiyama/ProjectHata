/*
  Project Hata 用JavaScript
*/

function dataSend(){
  // 書き換わった要素のデータを dataviewテキストボックスへcsv形式で展開する
  // ※保存は別の CGItoCSV.py で行う（※javascriptからはローカルファイルの保存ができないため）
  var btn = $('button');
  var e = document.getElementById ('dataview');
  var a = document.getElementsByClassName('btn');
  var stat = document.getElementById ('stat');
  var waitSec = document.getElementById ('WaitTime');
  var s='';

  //var s2=String(waitSec.outerHTML);
  var s2=waitSec.value;
    console.log('Wait=',s2);

    s=s2+'\n';

    for(var i=0;i<(20*6);i++){  // 20x6のマトリクス
      if(!(i % 20)){
        if (i !=0 ){
          s=s.slice(0,-1) // 最後の , カット
          s=s+'\n';
        }
      }

      var s1=String(a[i].outerHTML);  // 必要なHTMLを取り出し

      var result = s1.indexOf('active');  // activeかどうかをチェック
      console.log(s1,result);

      if(result>0){
        console.log('Hit'); //activeなら　1
        s=s+'1,';
      }else{
        s=s+'0,';
      }
      //console.log(a);
      console.log(i,s);
    }
  s=s.slice(0,-1) // 最後の , カット
  e.value=s;
}

function waitTextValueCng($this) {
    console.log($this.value);
    var viewArea = document.getElementById ('dataview');
    console.log(viewArea.value);
    //ここで自動的にviewAreaを書き換える。下の全体イベントドリブン内での処理と重複。いらないか？
    dataSend();
}


//全体のイベントドリブン
$(
  function(){   // HTMLを読み込み終わったら動作開始function

    // CSVリストが選択されたらValueをcsvFileNameTextテキストボックスへ
    var select = document.getElementById( 'listbox' );
    select.onchange = function()
    {
      // 選択されているoption要素を取得する
      var selectedItem = this.options[ this.selectedIndex ];
      document.getElementById("csvFileNameText").value = selectedItem.value;
      console.log( selectedItem.value );
    }

    var wt = document.getElementById( 'WaitTime' );
    wt.onchange = function()
    {
      // WaitTime が書き換わったら
      var wt_text = wt.value;
      console.log( "wt_text="+ wt_text );
      dataSend();

    }

    // 以下シーケンサーマトリクスクリックチェック用
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


      dataSend();

  });
});
