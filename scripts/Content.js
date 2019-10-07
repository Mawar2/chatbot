import * as React from 'react';
import { Socket } from './Socket';
import { Button } from './Button';


export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            chatMessages: []
        };
    }
    
    componentDidMount() {
        Socket.on('message received', (data) => {
            this.setState({
                'message_received': data['message']
            });
        })
    }

    render() {
        const styles = {
            container: {
              height: '100vh',
              display: 'flex',
              flexDirection: 'column',
            },
           chatContainer: {
              display: 'flex',
              flex: 1,
            },
            whosOnlineListContainer: {
              width: '800px',
              height: '1000px',
              flex: 'none',
              padding: 20,
              backgroundColor: '#2c303b',
              color: 'white',
            },
            chatListContainer: {
              padding: 20,
              width: '85%',
              display: 'flex',
              flexDirection: 'column',
            },
         }

        let chat_messages = this.state.message_received
        console.log(chat_messages)
        //console.log(chat_messages.keys)
        
        return (
            
            <div> 
                <h1>ChatBot!</h1>
                        <section style={styles.chatListContainer}>
                        <aside style={styles.whosOnlineListContainer}>
                        <Button />
                            <div> <text> {this.state.message_received} </text> </div>
                        </aside>
                        </section>
            </div>
    )
  }
}