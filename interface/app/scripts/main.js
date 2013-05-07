require.config({
  shim: {
    /*jscrop: {
      deps:['jquery']
    }*/    
  },

  paths: {
    hm: 'vendor/hm',
    esprima: 'vendor/esprima',
    jquery: 'vendor/jquery.min',
    jscrop:'../components/jcrop/js/jquery.Jcrop'
  }
});
 
require(['jquery','jscrop'], function($,JsCrop) {
  //drag an image first
  var area = $(".drag"),
      fileInput = $("#chooseFile");
  
  fileInput.on("change",function(e){
    var file = fileInput[0].files[0],
        reader = new FileReader();

        reader.onload = function(event){ 
          var image = new Image();
          image.src = event.target.result;
          $('.image').html('').append($(image));
          area.css("height",'0px');
          $(image).Jcrop({
            onSelect:function updateCoords(c)
            {
              $('#x').val(c.x);
              $('#y').val(c.y);
              $('#w').val(c.w);
              $('#h').val(c.h);
           }
          });

        }//end of reader onload
        reader.readAsDataURL(file)
  });

  area.on("dragover",function(){
    console.log("over");
    return false;
  });
  area.on("dragend",function(){
    console.log("end"); 
    return false;
  });
  area.on("drop",function(e){
    console.log("drop",e.originalEvent.dataTransfer.files);
    var file = e.originalEvent.dataTransfer.files[0],
        reader = new FileReader();
    /*
    reader.onload = function(event){ 
      var image = new Image()
      image.src = event.target.result;
      document.body.appendChild(image);
      area.css("height",'0px');
      $(image).Jcrop({
        onSelect:function updateCoords(c)
        {
          $('#x').val(c.x);
          $('#y').val(c.y);
          $('#w').val(c.w);
          $('#h').val(c.h);
        };
      });

      $("#sendForm").on("submit",function(e){
        e.preventDefault();

        var formData = new FormData();
        formData.append("x",$('#x').val(c.x))
        
        xhr.open("POST","127.0.0.1:8888/upload");
        xhr.onload = function(){
          console.log(xhr.status) 
        }

        xhr.send(formData);
        return false;
      })

    }

    reader.readAsDataURL(file)
    */  


    e.preventDefault();
    return false;
  });



});
