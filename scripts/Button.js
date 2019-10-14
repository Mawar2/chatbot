import * as React from 'react';
import { Socket } from './Socket';
import { GoogleLogin } from 'react-google-login';

export class Button extends React.Component {
    constructor(props) {
    super(props);
    this.state = {message: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
      }
    
    handleChange(event) {
        this.setState({message: event.target.value});
    }
    handleSubmit(event) {
        event.preventDefault();
    
        // this is a local variable so we don't need to initialize in the constructor
        console.log('Sending message: ', this.state.message);
        Socket.emit('new message', {'message': this.state.message, 'user_data': this.state.signin});
        if (this.state.signin == true){
          Socket.emit('connect', {'connected_users': this.state.count});
        console.log('This confirms that a message was sent to server')
    }
  }
    
    componentDidMount() {
      Socket.on('google keys', (data) => {
        this.setState({
          'Google_id': data['GoogleID'],
          'secret': data['GoogleSecret']
        });
      });
    }

    render() {
      const responseGoogle = (response) => {
        this.setState({'signin': response, enabled: true, count: this.state.count++});
        console.log(response);
      };
        return (
          <form onSubmit={this.handleSubmit}>
            <GoogleLogin
                clientId="658977310896-knrl3gka66fldh83dao2rhgbblmd4un9.apps.googleusercontent.com"
                buttonText="Login"
                onSuccess={responseGoogle}
                onFailure={responseGoogle}
                cookiePolicy={'single_host_origin'}
            />
            <label>
              Chat:
              <input type="text" value={this.state.value} onChange={this.handleChange} />
            </label>
            <input type="submit" value="Submit" />
          </form>
        );
  }
}

