class shadrunovbot(object):
    '''
    A docstring documenting this bot.
    '''

    def usage(self):
        return '''Your description of the bot'''

    def handle_message(self, message, bot_handler):
        def handle_message(self, message, bot_handler):
            # original_content = message['content']
            # original_sender = message['sender_email']
            # new_content = original_content.replace('@followup',
            #                                        'from %s:' % (original_sender,))

            bot_handler.send_reply(message, 'sssssssss')

handler_class = shadrunovbot
