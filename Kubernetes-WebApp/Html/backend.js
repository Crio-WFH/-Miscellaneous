function dark(){
            
            bgelement = document.getElementById("bg");
            bgelement.style.backgroundColor="#222222";
            bgelement.style.color="black";
            x=document.getElementById("output_box");
            x.style.backgroundColor="#222222";
            x.style.color="white";
            a=document.getElementById("a1");
            a.style.backgroundColor="#222222";
            a.style.color="white";
            b=document.getElementById("a2");
            b.style.backgroundColor="#222222";
            b.style.color="white";
            c=document.getElementById("a3");
            c.style.backgroundColor="#222222";
            c.style.color="white";
            d=document.getElementById("a4");
            d.style.backgroundColor="#222222";
            d.style.color="white";
            e=document.getElementById("a5");
            e.style.backgroundColor="#222222";
            e.style.color="white";
            f=document.getElementById("a6");
            f.style.backgroundColor="#222222";
            f.style.color="white";
            g=document.getElementById("a7");
            g.style.backgroundColor="#222222";
            g.style.color="white";
            i=document.getElementById("imglogo");
            i.style.display="none";
            
        }  
function white(){
            bgelement = document.getElementById("bg");
            bgelement.style.backgroundColor="white";
            bgelement.style.color="black";
            x=document.getElementById("output_box");
            x.style.backgroundColor="white";
            x.style.color="black";
            a=document.getElementById("a1");
            a.style.backgroundColor="white";
            a.style.color="black";
            a=document.getElementById("a2");
            a.style.backgroundColor="white";
            a.style.color="black";
            a=document.getElementById("a3");
            a.style.backgroundColor="white";
            a.style.color="black";
            a=document.getElementById("a4");
            a.style.backgroundColor="white";
            a.style.color="black";
            a=document.getElementById("a5");
            a.style.backgroundColor="white";
            a.style.color="black";
            a=document.getElementById("a6");
            a.style.backgroundColor="white";
            a.style.color="black";
            a=document.getElementById("a7");
            a.style.backgroundColor="white";
            a.style.color="black";
            i=document.getElementById("imglogo");
            i.style.display="inline-block";
        } 

function openForm2() {
  z=document.getElementById("output_box");
  z.style.height="30%";
    document.getElementById("myForm2").style.display = "block";
}

function closeForm2() {
  z=document.getElementById("output_box");
  z.style.height="45%";
    document.getElementById("myForm2").style.display = "none";
}

function openForm1() {
  z=document.getElementById("output_box");
  z.style.height="30%";
    document.getElementById("myForm1").style.display = "block";
  }

function closeForm1() {
  z=document.getElementById("output_box");
  z.style.height="45%";
    document.getElementById("myForm1").style.display = "none";
  }



  function openForm3() {
    z=document.getElementById("output_box");
    z.style.height="35%";
    document.getElementById("myForm3").style.display = "block";
  }

  function closeForm3() {
    z=document.getElementById("output_box");
  z.style.height="45%";
    document.getElementById("myForm3").style.display = "none";
  }

  function openForm4() {
    z=document.getElementById("output_box");
    z.style.height="35%";
    document.getElementById("myForm4").style.display = "block";
  }

  function closeForm4() {
    z=document.getElementById("output_box");
  z.style.height="45%";
    document.getElementById("myForm4").style.display = "none";
  }

  function openForm5() {
    z=document.getElementById("output_box");
    z.style.height="35%";
    document.getElementById("myForm5").style.display = "block";
  }

  function closeForm5() {
    z=document.getElementById("output_box");
    z.style.height="45%";
    document.getElementById("myForm5").style.display = "none";
  }
  function openForm6() {
    z=document.getElementById("output_box");
    z.style.height="30%";
    document.getElementById("myForm6").style.display = "block";
  }

  function closeForm6() {
    z=document.getElementById("output_box");
  z.style.height="45%";
    document.getElementById("myForm6").style.display = "none";
  }



  function openForm7() {
    z=document.getElementById("output_box");
  z.style.height="30%";
    document.getElementById("myForm7").style.display = "block";
  }

  function closeForm7() {
    z=document.getElementById("output_box");
  z.style.height="45%";
    document.getElementById("myForm7").style.display = "none";

  }
  function openForm8() {
    
    document.getElementById("myForm6").style.display = "block";
  }

  function closeForm8() {
    
    document.getElementById("myForm6").style.display = "none";
  }
// ==================================================================================================================


  
function launchPod() {

  var i = document.getElementById("pod_name").value;
  var j = document.getElementById("pod_image_name").value;

	console.log(i,j);
  var xhr = new XMLHttpRequest();
  xhr.open("GET", `http://192.168.56.101/cgi-bin/launchpod.py?x=${i}&y=${j}`,true);
  xhr.send();

  xhr.onload = function() {
      document.getElementById("output_id").innerHTML = xhr.responseText;
  }
}


function launchDeploy() {

  var k = document.getElementById("deployment_name").value;
  var l = document.getElementById("deployment_image_name").value;

  var xhr = new XMLHttpRequest();
  xhr.open("GET", `http://192.168.56.101/cgi-bin/launchdeploy.py?deployname= ${k}&dimage=${l}`, true);
  xhr.send();

  xhr.onload = function() {
      document.getElementById("output_id").innerHTML = xhr.responseText;
  }
}

function delAll() {
  decision = confirm("Are you sure, you want to 'Delete' all the resources.?");
  if(decision == true){
        var xhr = new XMLHttpRequest();
        xhr.open("GET","http://192.168.56.101/cgi-bin/delall.py",true);
        xhr.send();
        xhr.onload = function() {
          document.getElementById("output_id").innerHTML = xhr.responseText;
    }
  }
}

function delPod() {
  decision = confirm("Are you sure, you want to 'Delete' this pod.?");
  if(decision == true){
        var m = document.getElementById("delete_pod_name").value;
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://192.168.56.101/cgi-bin/delpod.py?del_podname=" + m, true);
        xhr.send();
        xhr.onload = function() {
          document.getElementById("output_id").innerHTML = xhr.response;
    }
  }
}

function delDeploy() {
  decision = confirm("Are you sure, you want to 'Delete' this deployment.?");
  if(decision == true){
      var n = document.getElementById("delete_deployment_name").value;
      var xhr = new XMLHttpRequest();
      xhr.open("GET", "http://192.168.56.101/cgi-bin/deldeploy.py?del_deployname=" + n, true);
      xhr.send();
      xhr.onload = function() {
        document.getElementById("output_id").innerHTML = xhr.response;
    }
  }
}

function scaleReplica() {
  decision = confirm("Are you sure, you want to create this much replicas.?");
  if(decision == true){
    var o = document.getElementById("scale_name").value;
    var p = document.getElementById("replicas").value;
    var xhr = new XMLHttpRequest();
    xhr.open("GET","http://192.168.56.101/cgi-bin/scalereplica.py?deploy_name= ${o}&replicas=${p}",true);
    xhr.send();

    xhr.onload = function() {
      document.getElementById("output_id").innerHTML = xhr.responseText;
  }
  }
  
}

function expose() {
  decision = confirm("Are you sure, you want to expose this deployment.?");
  if(decision == true){
  var q = document.getElementById("expose_name").value

  var xhr = new XMLHttpRequest();
  xhr.open("GET", "http://192.168.56.101/cgi-bin/expose.py?del_deployname=" + q, true);
  xhr.send();

  xhr.onload = function() {
      document.getElementById("output_id").innerHTML = xhr.responseText;
  }
}
}

function other() {
  
  var cmd = document.getElementById("cmd_name").value

  var xhr = new XMLHttpRequest();
  xhr.open("GET", "http://192.168.56.101/cgi-bin/kubernetes.py?x=" + cmd, true);
  xhr.send();

  xhr.onload = function() {
      document.getElementById("output_id").innerHTML = xhr.responseText;
  }
}
