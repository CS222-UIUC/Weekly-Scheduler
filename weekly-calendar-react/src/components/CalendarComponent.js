import React, {Component} from 'react';
import {DayPilot, DayPilotCalendar} from "@daypilot/daypilot-lite-react";
//import "./CalendarStyles.css";
class Calendar extends Component {

  constructor(props) {
    super(props);
    this.state = {
      viewType: "Week",
      durationBarVisible: true,
      
    };
  }





  render() {
    const {...config} = this.state;
    return (
      <div>
        <DayPilotCalendar
          {...config}
          onTimeRangeSelected={args => {
            this.calendar.message("Selected range: " + args.start.toString("hh:mm tt") + " - " + args.end.toString("hh:mm tt"));
          }}
          ref={this.calendarRef}
        />
      </div>
    );
  }
}

export default Calendar;