def manual():
        with open('manual.html','w') as manual:
            html_file='''<!Manual>
                        <html>
                            <head>
                                <title>Manual</title>
                                <meta charset='UTF-8',name="viewport" content="width=device-width, initial-scale=1">
                                <link rel = "icon" href = "images/manual.png" type = "image/x-icon" rel="preload">
                                <style>
                                body
                                {
                                    background-image: url('images/manual.png');
                                    background-repeat: no-repeat;
                                    background-size: cover;
                                }
                                ::selection
                                {
                                    color: blue;
                                    background: green;
                                }
                                #myBtn
                                {
                                    display: none;
                                    position: fixed;  
                                    bottom: 20px;
                                    right: 30px;
                                    z-index: 99;
                                    font-size: 18px;
                                    border: none;
                                    outline: none;
                                    background-color: red;
                                    color: white;
                                    cursor: pointer;
                                    padding: 15px;
                                    border-radius: 4px;
                                }
                                #myBtn:hover
                                {
                                    background-color: #555;
                                }
                                div.image_opacity
                                {
                                    opacity: 0.1;
                                }
                                .image_opacity:hover
                                {
                                    opacity: 1;
                                }
                                /* Add a black background color to the top navigation */
                                .topnav
                                {
                                    background-color: #333;
                                    overflow: hidden;
                                }
                                /* Style the links inside the navigation bar */
                                .topnav a
                                {
                                    float: left;
                                    color: #f2f2f2;
                                    text-align: center;
                                    padding: 14px 16px;
                                    text-decoration: none;
                                    font-size: 17px;
                                }
                                /* Change the color of links on hover */
                                .topnav a:hover
                                {
                                    background-color: #ddd;
                                    color: black;
                                }
                                /* Add a color to the active/current link */
                                .topnav a.active
                                {
                                    background-color: #04AA6D;
                                    color: white;
                                }
                                #footer
                                {
                                    position: fixed;
                                    padding: 10px 10px 0px 10px;
                                    bottom: 0;
                                    width: 100%;
                                    /* Height of the footer*/ 
                                    height: 40px;
                                }
                                </style>
                                <div class="topnav">
                                    <a class="active" href="Home.html">Home</a>
                                    <a href="open_window(params)">News</a>
                                    <a href="Home.html#container reveal#text-container#textbox">Contact</a>
                                    <a href="#about">About</a>
                                </div>
                            </head>
                            <font face="Comic sans MS" color=pink>HELLO USER
                                <br>NAMASTE
                            </font>
                            <body>
                                <div id="google_translate_element" align='right' alt="cannot load google translate please check your network/data connection">
                                </div>
                                <script type="text/javascript">
                                function googleTranslateElementInit()
                                {
                                    new google.translate.TranslateElement(
                                    {pageLanguage: 'en', layout: google.translate.TranslateElement.InlineLayout.HORIZONTAL}, 'google_translate_element');
                                }
                                </script>
                                <script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit">
                                </script>
                                <h2>
                                    <font face="Comic sans MS" color=blue>
                                        Welcome
                                    </font>
                                    </h2>
                                    <div class="image_opacity">
                                        <a href="https://study.com/academy/lesson/the-purpose-content-structure-of-manuals.html">
                                            <img src="images/manual.png" alt="purpose" align='right'>
                                        </a>
                                    </div>
                                    <p>
                                        <font face="Comic sans MS" color=dark green>
                                            My name is Manoj Nayak &nbsp;(CLASS 12th ROLL NO.29).
                                            <br>This is my project(Note:This app only uses python tkinter for frame work) which contains 'Hospital/Clinic management,window for uploading a profile picture and a entertainment section which contains snake game' for now. Our software engineers are working to add more games and feature to the clinic interface and making more secure network.
                                            </br><br><!spacing in html &nbsp 1,&ensp 2,&emsp 3 space>
                                            <font face="Comic sans MS" color=green>Manual:-
                                                <br>&emsp;&emsp;&emsp;&emsp; medical:-
                                                </br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; From start click on medical for medical queries.
                                                <br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Then click on medical and then hospital.
                                                <br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Then for registering your details click on register button.
                                                <br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Then for appoinment click on appointment and add nesscary details.
                                                <br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Then for list of doctors click on particular button.
                                                <br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Then for services in hospital click the specific button.
                                                <br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Then for modification click on modify button and put patient id for verification.
                                                <br>&emsp;&emsp;&emsp;&emsp; profile:-
                                                <br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Click upload button.
                                                <br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; It's only for our reference to create your file and arrange our data
                                                <br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; and our doctor's busy schedule.
                                                <br>&emsp;&emsp;&emsp;&emsp; games:-
                                                <br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Click on entertainment button.
                                                <br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Then click games then select the particular game.
                                                <br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; or any other option in entertainment section (if any).
                                            </font>
                                            </br><br>
                                            <font face="Comic sans MS" color=red>Remember!!</font>
                                            </br>Whatever you enter is saved on our server including the button you press.
                                            <br>So be careful while adding data.
                                            <br>It's just for safety.
                                            <br>We are not going to release your details.So no need to <a href="https://economictimes.indiatimes.com/tech/internet/intelligence-bureau-wants-isps-to-log-all-customer-details/articleshow/7187899.cms?from=mdr">worry!</a>
                                            </br><br>
                                            <img src="images/animation.gif" alt='manual animation' align=right>
                                            For customer related queries:-
                                            <br>&emsp;&emsp;&emsp;&emsp; CONTACT :- 9920041290 
                                            <br>&emsp;&emsp;&emsp;&emsp; Manoj Nayak
                                            <br>&emsp;&emsp;&emsp;&emsp; Developer of this wonderful application.
                                            <br>&emsp;&emsp;&emsp;&emsp; If you want to support us for making our app better and work for you in a better way please contact on phone number mentioned above.
                                            </br><br>
                                            Jai Hind!
                                            <br>BHARAT MATA KI JAI!!
                                            </br><br>
                                            #MADE IN INDIA &#128516;&#128525;
                                            <br><a href="https://aatmanirbharbharat.mygov.in/" style='color:orange'>#AATMANIRBHAR BHARAT</a>
                                            </br><br>
                                            THANK YOU!!!!
                                        </font>
                                        </br>
                                        <font face="Conic sans MS Bold">
                                            <div id="footer">
                                                &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
                                                &#169;
                                                Copyright of Convergnite and Nayak industries
                                            </div>
                                        </font>
                                    </p>
                                    <button onclick="topFunction()" id="myBtn" title="Go to top">
                                         &uarr;
                                    </button>
                                <script>
                                    //Get the button
                                    var mybutton = document.getElementById("myBtn");
                                    // When the user scrolls down 20px from the top of the document, show the button
                                    window.onscroll = function() {scrollFunction()};
                                    function scrollFunction()
                                    {
                                        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20)
                                        {
                                            mybutton.style.display = "block";
                                        }
                                        else
                                        {
                                            mybutton.style.display = "none";
                                        }
                                    }
                                    // When the user clicks on the button, scroll to the top of the document
                                    function topFunction()
                                    {
                                        document.body.scrollTop = 0;
                                        document.documentElement.scrollTop = 0;
                                    }
                                </script>
                                                    <script>
                                                    //function open_window(params) {
                                                        
                                                    //win = window.open("", "Title", "toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=yes, width=780, height=200, top="+(screen.height-400)+", left="+(screen.width-840));
                                                    //win.document.body.innerHTML = "<html><title>hh</title></html>";}
                                </script>
                            </body>
                        </html>'''
            manual.write(html_file)
manual()
def Home():
        with open('Home.html','w') as home:
                Html_write='''<html>
                              <head>
                                <title>Home | Medical - convergnite</title>
                                <link rel="icon" href="images/home.png" type="image/x-icon" rel="preload">
                                <meta charset='UTF-8',name="viewport" content="width=device-width, initial-scale=1" lang="en">
                                <style>
                                @import url('https://fonts.googleapis.com/css2?family=Asap&display=swap');
                                *{
                                    margin: 0;
                                    padding: 0;
                                    box-sizing: border-box;
                                    font-family: "Asap", sans-serif;
                                  }
                                  body
                                  {
                                    background: #42455a;
                                  }
                                  section
                                  {
                                    min-height: 100vh;
                                    display: flex;
                                    justify-content: center;
                                    align-items: center;
                                  }
                                  section:nth-child(1)
                                  {
                                      color: #e0ffff;
                                  }
                                  section:nth-child(2)
                                  {
                                    color: #42455a;
                                    background: #e0ffff;
                                  } 
                                  section:nth-child(3)
                                  {
                                    color: #e0ffff;
                                  }
                                  section:nth-child(4)
                                  {
                                    color: #42455a;
                                    background: #e0ffff;
                                  }
                                  section:nth-child(5)
                                  {
                                    color:#e0ffff;
                                  }
                                  section .container
                                  {
                                    margin: 100px;
                                  }
                                  section h1
                                  {
                                    font-size: 3rem;
                                    font-style: italic;
                                    margin: 20px;
                                    align-content: center;
                                  }
                                  section h2
                                  {
                                    font-size: 40px;
                                    text-align: center;
                                    text-transform: uppercase;
                                  }
                                  section .text-container
                                  {
                                    display: flex;
                                  }
                                  section .text-container .text-box
                                  {
                                    margin: 20px;
                                    padding: 20px;
                                    background: #00c2cb;
                                  }
                                  section .text-container .text-box_contact_me
                                  {
                                    margin: 20px;
                                    padding: 20px;
                                    background: #ffffff00;
                                  }
                                  section .text-container .text-box h3
                                  {
                                    font-size: 30px;
                                    text-align: center;
                                    text-transform: uppercase;
                                    margin-bottom: 10px;
                                  }
                                  @media (max-width: 900px)
                                  {
                                    section h1{
                                    font-size: 2rem;
                                    text-align: center;
                                  }
                                  section .text-container
                                  {
                                    flex-direction: column;
                                  }
                                  }  
                                  .reveal
                                  {
                                    position: relative;
                                    transform: translateY(150px);
                                    opacity: 0;
                                    transition: 1s all ease;
                                  } 
                                  .reveal.active
                                  {
                                    transform: translateY(0);
                                    opacity: 1;
                                  }
                                  .button
                                  {
                                    background-color: #4CAF50; /* Green */
                                    border: none;
                                    color: white;
                                    padding: 20px;
                                    text-align: center;
                                    text-decoration: none;
                                    display: inline-block;
                                    font-size: 16px;
                                    margin: 4px 2px;
                                    cursor: pointer;
                                  }
                                  .button_sec1{border-radius: 8px;}.button_sec1:hover{box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);}
                                  .button_sec2{border-radius: 8px;}.button_sec2:hover{box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);}
                                  .button_sec3{border-radius: 8px;}.button_sec3:hover{box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);}
                                </style>
                              </head>
                              <body>
                                <section>
                                  <h1>Hi, Welcome to converginite medical
                                    <br> Please scroll down to see more &#8595;
                                    <img src="https://lh3.googleusercontent.com/BMKlwqY3oLUa-INaw0wLgFkuQ-_UHpnTzANUbTSnwx98BYfL4ItZY-N3LKyJ4trF7PnY043zF9S0CVQOaeWJ9EMGW9gvqnbfXRx_6veyjXbfkIbuuwHw=w350-rw-e365-v1" width="100" alt="phone">
                                  </h1>
                                </section>
                                <section>
                                  <div class="container reveal">
                                    <h2>About Application</h2>
                                    <div class="text-container">
                                      <img src="images/icon.png" width='100' alt='about Application'>
                                      <div class="text-box">
                                        <h3></h3>
                                        <p>You can use games,hospital and many more <br> use only for pc</p>
                                      </div>
                                      <button class="button button_sec1"><a href="manual made.html" onclick="location.href=this.href+'?file='+val;return false;" style='color:white; text-decoration: none;'>Information &rarr; </a></button>
                                    </div>
                                  </div>
                                </section>
                                <section>
                                  <div class="container reveal">
                                    <h2>Download</h2>
                                    <div class="text-container">
                                      <img href='#vfssf' src="myqr.svg" alt="image">
                                      <button class="button button_sec2"><a id="link" href="project.exe"></a>Download &rarr;</button>
                                    </div>
                                  </div>
                                </section>
                                <section>
                                  <div class="container reveal">
                                    <h2>About Company</h2>
                                    <div class="text-container">
                                      <div class="text-box">
                                        <h3>About me</h3>
                                        <p>
                                          I'm Manoj Nayak<br>Designer of this app<br>For more Information click the button for more Information <br>copyright of converginite.
                                        </p>
                                      </div>
                                      <button class="button button_sec3" > <a href="About.html" style="color: white; text-decoration: wavy;">About me &rarr;</a> </button>
                                    </div>
                                  </div>
                                </section>
                                <section>
                                  <div class="container reveal">
                                    <h2>review</h2>
                                    <div class="text-container">
                                      <div class="text-box_contact_me">
                                        <h3></h3>
                                      </div>
                                    </div>
                                  </div>
                                </section>
                                <script>
                                  var val="main"
                                  function reveal()
                                  {
                                    var reveals = document.querySelectorAll(".reveal");
                                    for (var i = 0; i < reveals.length; i++)
                                    {
                                      var windowHeight = window.innerHeight;
                                      var elementTop = reveals[i].getBoundingClientRect().top;
                                      var elementVisible = 150;
                                      if (elementTop < windowHeight - elementVisible)
                                      {
                                        reveals[i].classList.add("active");
                                      }
                                      else
                                      {
                                        reveals[i].classList.remove("active");
                                      }
                                    }
                                  }
                                  window.addEventListener("scroll", reveal);
                                </script>
                                <!file download>
                                <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js">
                                  $(document).ready(function (){
                                  $("#link").click(function (e){
                                    e.preventDefault();				
                                    window.location.href
                                      = "E:\MANOJ\dav\school apps\school\OneDrive - DAV PUBLIC SCHOOL NEW PANVEL\computer\project\project.exe";
                                    });
                                  });
                                </script>
                              </body>
                            </html>'''
            home.write(Html_write)
Home()
#recent.write(news_write)
#news()
debuging=True
