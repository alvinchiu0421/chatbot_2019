import os

from bottle import route, run, request, abort, static_file

from fsm import TocMachine

VERIFY_TOKEN = "2104365879"
PORT = os.environ.get('PORT', 5050)

machine = TocMachine(
    states=[
        'user',
        'description',
        'state1',
        'state1_reply',
        'state2',
        'state2_reply',
        'state3',
        'state3_reply',
        'state4',
        'state4_reply',
        'state5',
        'state5_reply',
        'state6',
        'state7',
        'state8',
        'state9',
        'state10',
        'state11'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'description',
            'conditions': 'is_going_to_description'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },

        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state1_reply',
            'conditions': 'is_going_to_state1_reply'
        },
        {
            'trigger': 'advance',
            'source': 'state1_reply',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state2_reply',
            'conditions': 'is_going_to_state2_reply'
        },
        {
            'trigger': 'advance',
            'source': 'state2_reply',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state3_reply',
            'conditions': 'is_going_to_state3_reply'
        },
        {
            'trigger': 'advance',
            'source': 'state3_reply',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state4_reply',
            'conditions': 'is_going_to_state4_reply'
        },
        {
            'trigger': 'advance',
            'source': 'state4_reply',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state5_reply',
            'conditions': 'is_going_to_state5_reply'
        },
        {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state7',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'advance',
            'source': 'state7',
            'dest': 'state8',
            'conditions': 'is_going_to_state8'
        },
        {
            'trigger': 'advance',
            'source': 'state8',
            'dest': 'state9',
            'conditions': 'is_going_to_state9'
        },
        {
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'state10',
            'conditions': 'is_going_to_state10'
        },
        {
            'trigger': 'advance',
            'source': 'state10',
            'dest': 'state11',
            'conditions': 'is_going_to_state11'
        },


        {
            'trigger': 'go_back',
            'source': [
                'description',
                'state5_reply',
                'state11'
            ],
            'dest': 'user'
        },

    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
