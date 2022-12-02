import React, {Component} from 'react';
import {DayPilot, DayPilotCalendar, DayPilotNavigator} from "@daypilot/daypilot-lite-react";
import Modal from "./Modal";
import axios from 'axios'; 

const styles = {
  wrap: {
    display: "flex"
  },
  left: {
    marginRight: "10px"
  },
  main: {
    flexGrow: "1"
  }
};



class Calendar extends Component {

  constructor(props) {
    super(props);
    this.calendarRef = React.createRef();
    this.state = {
      viewType: "WorkWeek",
      durationBarVisible: false,
      businessBeginsHour: 8,
          businessEndsHour: 20,

         
      heightSpec: "BusinessHours",
     
      activeItem: {
        title: "",
        duration: "",
        block: false
      },
       taskList: [],
    
    
    
    };
  }

   refreshList = () => {
    axios   //Axios to send and receive HTTP requests
      .get("http://localhost:8000/final")
      .then(res => this.setState({ taskList: res.data }))
      .catch(err => console.log(err));

  };

  toggle = () => {
    //add this after modal creation
    this.setState({ modal: !this.state.modal });
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

  get calendar() {
    return this.calendarRef.current.control;
  }

  componentDidUpdate() {
    /*this.refreshList();
    const item = this.activeItem;
    //DayPilot.Calendar.events.load("http://localhost:8000/api/tasks/");

    const startDate = DayPilot.Date.today();

    this.calendar.update({startDate, events: this.state.taskList});*/
    this.refreshList();
    this.loadEvents();

  }
  async loadEvents() {
    const start = this.calendar.visibleStart();
    const end = this.calendar.visibleEnd();
    const {data} = await DayPilot.Http.get(`http://localhost:8000/final`);
    this.calendar.update({events: data});
  }

  // rendertasks = () => {
    
  // }

  render() {
    return (
      <div> <h1>
        Hello, welcome to your week.
        </h1>
        <div style={styles.wrap}>
        <div style={styles.left}>
        </div>
        <div style={styles.main}>
          <DayPilotCalendar
            {...this.state}
            ref={this.calendarRef}
          />
        </div>
        <div style={styles.wrap}>
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
        </div>
      </div>
        </div>
      
      
      
    );
    
  }
}

export default Calendar;