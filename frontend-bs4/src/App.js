import React from 'react';

import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import {BrowserRouter as Router, Route, Switch, Redirect} from "react-router-dom";
import StravaAuthReturn from "./Components/StravaAuthReturn";
import FourOhFour from "./Components/FourOhFour";
import StravaAuthFailed from "./Components/StravaAuthFailed";
import StravaGateway from "./Components/StravaGateway";
import ActivityDetail from "./Components/ActivityDetail";
import StravaHome from "./Components/StravaHome";

class App extends React.Component {
  render() {
    return (
      <Router>
        <div className="App">
          <Switch>
            <Route exact path="/" component={StravaGateway} />
            <Route exact path="/strava" component={StravaHome} />
            <Route path="/strava/activity" component={ActivityDetail} />
            <Route path="/strava/authreturn" component={StravaAuthReturn} />
            <Route path="/strava/authfailed" component={StravaAuthFailed} />
            <Route component={FourOhFour} />
          </Switch>
        </div>
      </Router>
    )
  }
}

export default App;
