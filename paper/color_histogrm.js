window.onload = function(){

var canvas = document.createElement("canvas");
    canvas.width=68,
    canvas.height=68;


    document.body.appendChild(canvas);
    var ctx    = canvas.getContext("2d"),
    img    = document.getElementById("img");

    ctx.drawImage(img,0,0,68,68);

    var imgData = ctx.getImageData(0,0,68,68);

    for(var i = 0,len = imgData.data.length;i<len;i+=4){
      var data = imgData.data[i+2] ;
      if( data > 192 ){
        console.log( "blue ,", data   );
      }
    }
    //console.log(ctx.getImageData(0,0,68,68));


}
