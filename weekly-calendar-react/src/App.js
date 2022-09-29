
import './App.css';
import TestComponent from './components/TestComponet';
import CalendarComponent from './components/CalendarComponent';


function App() {
  return (
    <div className="App">
      <CalendarComponent></CalendarComponent>
      <TestComponent displaytext = "app test"/>
      <button type="submit">
        Test Button</button>
    </div>
  );
}

export default App;
