function getXMLHttp()
{
 var xmlHttp;
 try
 {
  xmlHttp = new XMLHttpRequest();
 }
 catch(e)
 {
  //Internet Explorer is different than the others
  try
  {
   xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
  }
  catch(e)
  {
   try
   {
    xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
   }
   catch(e)
   {
    alert("You have Old Browser! Please update to use AJAX call.")
    return false;
   }
 }
}
return xmlHttp;
}

function ajaxRequest()
{
 var xmlHttp = getXMLHttp();
 xmlHttp.onreadystatechange = function()
 {
 if(xmlHttp.readyState == 4)
 {
  handleResponse(xmlHttp.responseText);
 }
 }
xmlHttp.open("GET", "index.html", true);
xmlHttp.send(null);
}

function handleResponse(response)
{
document.getElementById('getAjaxResponse').innerHTML = response;
}