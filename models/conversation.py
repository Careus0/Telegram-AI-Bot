from config import constants

class ConversationManager:
    def __init__(self):
        self.conversation_context = {}

    def get_context(self, user_id: int) -> list:
        return self.conversation_context.get(user_id, [])

    def update_context(self, user_id: int, user_message: str, bot_response: str) -> None:
        context_messages = self.get_context(user_id)
        context_messages.extend([
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": bot_response}
        ])
        self.conversation_context[user_id] = context_messages[-constants.MAX_CONTEXT_LENGTH:] 