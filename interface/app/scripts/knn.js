var can = document.querySelector("#can"),
    ctx = can.getContext("2d"),
    canWidth = can.width,
    canHeight = can.height;

var trehold = 3;


function Node(x,y,type,color){
    this.color = color || "red";
    this.type = type || "circle";
    this.x     = x;
    this.y     = y;
}
Node.prototype.draw = function(){
    ctx.beginPath();
    if(this.type == "rectangle"){
      //console.log(this.type);
    }
    if(this.type == "circle"){
      ctx.arc(this.x,this.y,5,0, 2 * Math.PI , false);
    }
    else{
      ctx.rect(this.x,this.y,10,10);
    }
    ctx.fillStyle = this.color;
    ctx.fill();
}
 
var isNear = function(node1,node2,dist){
 
    var dx =  Math.abs(node1.x - node2.x),
        dy = Math.abs(node1.y - node2.y);
    
        return Math.sqrt( dx * dx + dy * dy) < dist ? 1 : 0;
}


var node_len = 20,
    nodes = [];

function initNodes(num,type,color){
  var curIdx = nodes.length - 1 > 0 ? nodes.length : 0;
  for(var i = 0;i<num ;i++){
      nodes.push( new Node(Math.random()*canWidth, Math.random()*canHeight, type,color)); 
      nodes[curIdx + i].draw();
  } 
}

function drawResult(node,dist){
    ctx.beginPath();
    ctx.arc(node.x,node.y,dist,0, 2 * Math.PI , false);
    ctx.strokeStyle = "#fff";
    ctx.stroke();

}
function init(){

    //generate some random point
    initNodes(50,"circle","yellow");
    initNodes(80,"rectangle","blue");
    initNodes(50,"circle","orange");

    //init the testgin point
    initNodes(1,"circle","red");
    var redNode = nodes.pop();
    //start testing
    var circle_num = 0,
        rectangle_num = 0,
        flag = false;
    for(var dist = 1;dist < canWidth;dist+=2){
        if(!flag){
          for(var i =0 ;i < nodes.length ; i++){
              var item = nodes[i];
              if(isNear(item,redNode,dist)){
                  if(item.type == "circle"){
                      circle_num++;
                      if(circle_num == 3 ){
                        //show result;
                        drawResult(redNode,dist); 
                        console.log("circle");
                        flag = true;
                        break;
                      }
                  }
                  else{
                      rectangle_num++; 
                      if(rectangle_num == 3 ){
                        //show result;
                        drawResult(redNode,dist); 
                        console.log("rectangle");
                        flag = true;
                        break;
                      }
                  }
                  nodes.splice(i,1);
              } 
          }
        }
    }
}
init();


