//Neon Lights Text II by G.P.F. (gpf@beta-cc.de)
//visit http://www.beta-cc.de
//Visit http://www.dynamicdrive.com for this script 

var message="Play With Icons"
var neonbasecolor="gray"
var neontextcolor="yellow"
var neontextcolor2="#FFFFA8"
var flashspeed=100						// speed of flashing in milliseconds
var flashingletters=3						// number of letters flashing in neontextcolor
var flashingletters2=1						// number of letters flashing in neontextcolor2 (0 to disable)
var flashpause=0	
var now = new Date();
var dayNames = new Array("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday");
var monNames = new Array("January","February","March","April","May","June","July","August","September","October","November","December");					// the pause between flash-cycles in milliseconds

///No need to edit below this line/////

document.write('<font size="6">'+message+'</font>')
var n=0
if (document.all||document.getElementById){

//document.write('<font color="'+neonbasecolor+'" size="6">')

//for (m=0;m<message.length;m++)
//document.write('<span id="neonlight'+m+'">'+message.charAt(m)+'</span>')
//document.write('</font>')
}
else
document.write(message)

function crossref(number){
var crossobj=document.all? eval("document.all.neonlight"+number) : document.getElementById("neonlight"+number)
return crossobj
}

function neon(){

//Change all letters to base color
if (n==0){
for (m=0;m<message.length;m++)
crossref(m).style.color=neonbasecolor
}

//cycle through and change individual letters to neon color
crossref(n).style.color=neontextcolor

if (n>flashingletters-1) crossref(n-flashingletters).style.color=neontextcolor2 
if (n>(flashingletters+flashingletters2)-1) crossref(n-flashingletters-flashingletters2).style.color=neonbasecolor


if (n<message.length-1)
n++
else{
n=0
clearInterval(flashing)
setTimeout("beginneon()",flashpause)
return
}
}

function beginneon(){
if (document.all||document.getElementById)
flashing=setInterval("neon()",flashspeed)
}
beginneon()




