
import './App.css';
//import Modal from './components/Modal';
import CalendarComponent from './components/CalendarComponent';
import { render } from 'react-dom';
import React, { Component } from "react";
import Modal from "./components/Modal";
import axios from 'axios'; 

class App extends Component {
 
  // add a constructor to take props
  constructor(props) {
    super(props);
     
    // add the props here
    this.state = {
     
      activeItem: {
        title: "",
        duration: "",
        block: false
      },
       taskList: []
    };
    
  }
 
  // Add componentDidMount()
  componentDidMount() {
    this.refreshList();
  }
 
  
  refreshList = () => {
    axios   //Axios to send and receive HTTP requests
      .get("http://localhost:8000/api/tasks/")
      .then(res => this.setState({ taskList: res.data }))
      .catch(err => console.log(err));
  };
 
  toggle = () => {
    //add this after modal creation
    this.setState({ modal: !this.state.modal });
  };
  handleSubmit = (item) => {
    this.toggle();
    alert("save" + JSON.stringify(item));
  };
 
  // Submit an item
  handleSubmit = (item) => {
    this.toggle();
    if (item.id) {
      // if old post to edit and submit
      axios
        .put(`http://localhost:8000/api/tasks/${item.id}/`, item)
        .then((res) => this.refreshList());
      return;
    }
    // if new post to submit
    axios
      .post("http://localhost:8000/api/tasks/", item)
      .then((res) => this.refreshList());
  };
 
  // Create item
  createItem = () => {
    const item = { title: "", duration: "",day: "", block: false };
    this.setState({ activeItem: item, modal: !this.state.modal });
  };
  // Start by visual effects to viewer
  render() {
    return (
      <main className="content">
        <CalendarComponent></CalendarComponent>
        <h1 className="text-success text-uppercase text-center my-4">
          Weekly Calendar
        </h1>
        <button onClick={this.createItem} className="btn btn-info">
        Add task
        </button>
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}
export default App;
