
import './App.css';
//import Modal from './components/Modal';
import CalendarComponent from './components/CalendarComponent';
import { render } from 'react-dom';
import React, { Component } from "react";
import Modal from "./components/Modal";
import axios from 'axios'; 

class App extends Component {
 
  // add a constructor to take props
  
  // Start by visual effects to viewer
  render() {
    return (
      <main className="content">
        <CalendarComponent></CalendarComponent>
        
      
      </main>
    );
  }
}
export default App;
