
			
			function div1()
			{					
                              				
				document.getElementById("sub").style.display=""; 
				document.getElementById("ver").style.display="none"; 
				document.getElementById("obj").style.display="none"; 
				document.getElementById("load1").style.display="none";
				document.getElementById("load2").style.display="none";
				
				

			}
			function div2()
			{				
				document.getElementById("sub").style.display="none";  
				document.getElementById("ver").style.display=""; 
				document.getElementById("obj").style.display="none";  

			}
			function div3()
			{				
				document.getElementById("sub").style.display="none"; 
				document.getElementById("ver").style.display="none"; 
				document.getElementById("obj").style.display=""; 
				
			}
			
			function disp_but1(a,b)
			{ 
				document.getElementById("img1").style.backgroundImage="url("+a+")";
				document.getElementById("img1").style.backgroundRepeat="no-repeat";
				document.getElementById("img1").value="";
				document.getElementById("img1").style.backgroundSize="cover"; 
				document.getElementById("sentence_sub").innerHTML=b;	
				//alert(document.getElementById("img1").value);
				document.getElementById("marq").style.display="none";
				document.getElementById("refresh").style.display=""; 
				document.getElementById("Audio").style.display=""; 
				document.getElementById("Translate").style.display="";
				document.getElementById("sub").style.display="none";
				document.getElementById("ver").style.display="";
				document.getElementById("Cart_subimg").innerHTML='Preferences:   '+"<img src='"+a+"' width='50' height='50'>";
				document.getElementById("Cart_subtitl").innerHTML=b;

				
							
				
						
			}
			
			
			
			function disp_but2(a,b)
			{ 	
				document.getElementById("img2").style.background="url('"+a+"')";
				document.getElementById("img2").style.backgroundRepeat="no-repeat";
				document.getElementById("img2").value="";
				document.getElementById("img2").style.backgroundSize="cover";
				document.getElementById("sentence_ver").innerHTML=b;
				document.getElementById("refresh").style.display=""; 
				document.getElementById("Audio").style.display=""; 
				document.getElementById("Translate").style.display="";
				document.getElementById("ver").style.display="none";
				document.getElementById("obj").style.display="";
				document.getElementById("Cart_verimg").innerHTML="<img src='"+a+"' width='50' height='50'>";
				document.getElementById("Cart_vertitl").innerHTML=b;
				
				
			}
						

			function disp_but3(a,b)
			{ 	
				document.getElementById("img3").style.background="url('"+a+"')";
				document.getElementById("img3").style.backgroundRepeat="no-repeat";
				document.getElementById("img3").value="";				
				document.getElementById("img3").style.backgroundSize="cover";
				document.getElementById("sentence_obj").innerHTML=b;
				document.getElementById("refresh").style.display=""; 
				document.getElementById("Audio").style.display=""; 
				document.getElementById("Translate").style.display="";
				document.getElementById("obj").style.display="none";
				//document.getElementById("sub").style.display="";
				document.getElementById("Cart_objimg").innerHTML="<img src='"+a+"' width='50' height='50'>";
				document.getElementById("Cart_objtitl").innerHTML=b;

				document.getElementById("new").style.display="";
				var New = confirm("Want to say anything more");
				
				if( New == true )
				{
					document.getElementById("new").style.display="none";
					document.getElementById("sub").style.display="";
				}
				else
				{
					alert("Thank you, your sentence has been generated");
									
				}
					

			}

			function ModifySub()
			{
								
				var title=prompt("Please enter title","");

				if (title!=null)
  				{
  					document.getElementById("sentence_sub").innerHTML=title;
					document.getElementById("Cart_subtitl").innerHTML=title;
				
  				}
			}

			function ModifyObj()
			{
								
				var title=prompt("Please enter title","");

				if (title!=null)
  				{
  					document.getElementById("sentence_obj").innerHTML=title;
					document.getElementById("Cart_objtitl").innerHTML=title;
				
  				}
			}

			function Question()
			{
				
				myWindow=window.open('','Question','width=600,height=400,top=300,left=600');
				myWindow.document.write("<html><body>");				
				myWindow.document.write("<br>");
				myWindow.document.write('<input type="radio" name="question" value="a" onclick="Quest1()"><img src="{{ STATIC_URL }}iconwrite/Can_I.png" width="40" height="40"/>Can</input><br>');
				myWindow.document.write('<input type="radio" name="question" value="a" onclick="Quest2()"><img src="{{ STATIC_URL }}iconwrite/Can_I.png" width="40" height="40"/>May</input><br>');
				myWindow.document.write('<input type="radio" name="question" value="a" onclick="Quest3()"><img src="{{ STATIC_URL }}iconwrite/Can_I.png" width="40" height="40"/>Did</input><br>');
				myWindow.document.write('<input type="radio" name="question" value="a" onclick="Quest4()"><img src="{{ STATIC_URL }}iconwrite/Can_I.png" width="40" height="40"/>Have</input><br>');
				myWindow.document.write("</body></html>");
				myWindow.focus();
				
				function Quest1()
				{
					myWindow.close();
					var a=document.getElementById("sentence_sub").innerHTML;
					document.getElementById("sentence_sub").innerHTML=a+"Can";
				}
				function Quest2()
				{
					myWindow.close();
					var a=document.getElementById("sentence_sub").innerHTML;
					document.getElementById("sentence_sub").innerHTML=a+"May";
				}
				function Quest3()
				{	myWindow.close();
					var a=document.getElementById("sentence_sub").innerHTML;
					document.getElementById("sentence_sub").innerHTML=a+"Did";
				}
				function Quest4()
				{	myWindow.close();
					var a=document.getElementById("sentence_sub").innerHTML;
					document.getElementById("sentence_sub").innerHTML=a+"Have";
				}


			}

			
			
			function reload()
			{
			
				document.location.reload();
				
			}
		
			function Audio()
			{
				
				var sub= document.getElementById("sentence_sub").innerHTML;
				var ver= document.getElementById("sentence_ver").innerHTML;
				var obj= document.getElementById("sentence_obj").innerHTML;

				//myWindow.document.getElementById('audio').href = "http://translate.google.com/translate_tts?tl=en&q=" + sub+" "+ ver +" "+ obj;
				
				myWindow=window.open('http://translate.google.com/translate_tts?tl=en&q=' + sub+' '+ ver +' '+ obj,'Sound','width=200,height=100,top=300,left=800');
				myWindow.focus();
				
			}

			function trans()
			{
				$.ajax({
					url: 'http://api.mymemory.translated.net/get',
					//type: 'POST',
					data: {q:"Hello World!",langpair:"en|it"},
        				beforeSend: function()
					{
              
					              				
                              		},
					success: function(data)
					{
						var abc = data;

        					alert(data.responseData.translatedText);
        

			     		},
        				complete: function()
					{
     
	
					}


					}); 
 
			}

			function chatDivSub(c,d,e)
			{	
				//alert(c);
				//A = document.getElementById("border").src;
				
				document.getElementById("chat_sub").innerHTML=c+':   '+"<img src='"+e+"' width='50' height='50'>"+d;
				document.getElementById("chatSub").style.display="none";
				document.getElementById("chatVer").style.display="";
				
				//document.getElementById("chat_sub").value=document.getElementById("border1").value;
			}
			
			function chatDivVer(d,e)
			{	
				
				document.getElementById("chat_ver").innerHTML="<img src='"+e+"' width='50' height='50'>"+d;
				document.getElementById("chatVer").style.display="none";
				document.getElementById("chatObj").style.display="";
				
			}

			function chatDivObj(d,e)
			{	
				
				document.getElementById("chat_obj").innerHTML="<img src='"+e+"' width='50' height='50'>"+d;
				document.getElementById("chatObj").style.display="none";
				document.getElementById("chatSub").style.display="";
				
			}			
	

			// jquery design interface
			$(window).load(function(){ 
				$("body").css({"background":"#FFFFCC"});
				$(".button1").css({"width": "150px","height":"150px","margin-top":"-230px","font-size": "35px","background-color": "#b29af8","margin-left":"-19px"});
				$(".button2").css({"width": "150px","height":"150px","margin-top":"-230px","font-size": "35px","background-color": "#b29af8","margin-left":"104px"});
				$(".button3").css({"width": "150px","height":"150px","margin-top":"-230px","font-size": "35px","background-color": "#b29af8","margin-left":"115px"});
				$("#content").css({"margin-left":"0%"}); 
			
		
				$('#loader').fadeOut(2000);	
				
				$("img").click(function() {
    				$(this).css('border', "solid 3px blue");  
  				});			
		
			}) 

						
			

