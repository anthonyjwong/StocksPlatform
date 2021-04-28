import React from "react";
import "semantic-ui-css/semantic.min.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import "./App.css";
import Home from "./components/Home/index";
import Login from "./components/Login/index";
import Signup from "./components/Signup/index";
import Dashboard from "./components/Dashboard/index";
import Project from "./components/Project/index";
import StockSearch from "./components/StockSearch/index";
import Settings from "./components/Settings/index";

import ApiHandler from './api'

/* Central app file which holds our app router allowing us to switch between files */
class App extends React.PureComponent {
  constructor(props) {
    super(props);

    this.state = {};
  }

  _updateGlobalState(key, value) {
    return this.setState({
      [key]: value,
    });
  }

  _getGlobalState(key) {
    return this.state[key];
  }

  render() {
    return (
      <div className="App">
        <Router>
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/signup" component={Signup} />
            <Route
              path="/login"
              component={(props) => (
                <Login
                  {...props}
                  setUser={(user) => {
                    this._updateGlobalState("user", user)
                    ApiHandler.setToken(this.state.user.accessKey)
                  }}
                />
              )}
            />
            <Route path="/dashboard/home" component={Dashboard} />
            <Route path="/dashboard/projects" component={Project} />
            <Route path="/dashboard/stock-search" component={StockSearch} />
            <Route path="/dashboard/settings" component={Settings} />
            {/* <Route path='/dashboard/my-profile' component={Profile} /> */}
          </Switch>
        </Router>
      </div>
    );
  }
}

export default App;
