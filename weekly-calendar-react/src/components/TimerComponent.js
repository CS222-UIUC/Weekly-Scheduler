import React, {Component} from 'react';



class timer extends Component {
  handleClick = () => {
    
    var duration = 60 * 6;
    var timer = duration, minutes, seconds;
    var timealert = false;
    
    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
       seconds = parseInt(timer % 60, 10);
        

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        var display = document.getElementById("time");
        display.style.color = 'green';

        display.textContent = minutes + ":" + seconds;
        
        if(minutes <= 4) {
          
          display.style.color = 'blue';
          if(timealert === false) {
            alert("Time for your study break");
            timealert = true;
            
          }
          
          display.textContent = minutes + ":" + seconds + " Take five minutes to relax, you've earned it!";
        }

        if (--timer < 0) {
            timer = duration;
        }


    }, 1000);
    
  };


  render() {
    return (
        <div id = "button"> 
        <button onClick={this.handleClick} style = {{
          color: 'blue',
        }}> Click me to begin your study session!</button>
        

       



        <div id = "timer">Your study timer: <span id="time">6:00</span></div>
        </div>
        


    )
    ;
  }
}

export default timer;