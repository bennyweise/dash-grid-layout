/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import { Grid } from '../lib';

class App extends Component {

    constructor() {
        super();
        this.state = {
            value: ''
        };
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        return (
          <div>
              <h1>plotly-grid Demo</h1>

              <hr/>
              <h2>PlotlyGrid</h2>
              <Grid
                  // label="This is an example label"
                  // value={this.state.value}
                  // setProps={newProps => this.setState({value: newProps.value})}

              >
                  <div key="a">a</div>
                  <div key="b">d</div>
                  <div key="c">f</div>
              </Grid>
              <hr/>
          </div>
        );
    }
}

export default App;
