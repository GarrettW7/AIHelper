from groq import Groq
import os


client = Groq(api_key=os.environ.get('GROQ_API_KEY'))

def dataSummarized(message):

    chat_completion = client.chat.completions.create(
        #
        # Required parameters
        #
        messages=[
            # Set an optional system message. This sets the behavior of the
            # assistant and can be used to provide specific instructions for
            # how it should behave throughout the conversation.
            {
                "role": "system",
                # "content": "You give the most correct answer possible. Reguardless of the question, you will always give the most correct answer."
                # "content" : "You will make fun of anything that i say and then make a haiku to finish your thoughts."
                "content": "I want to collect my thoughts, and group them into categories. You will listen and then group and summarize the things that are written!"
            },
            # Set a user message for the assistant to respond to.
            {
                "role": "user",
                "content": f"{message}"
            }
        ],

        # The language model which will generate the completion.
        model="llama-3.3-70b-versatile",

        #
        # Optional parameters
        #

        # Controls randomness: lowering results in less random completions.
        # As the temperature approaches zero, the model will become deterministic
        # and repetitive.
        temperature=.9,

        # The maximum number of tokens to generate. Requests can use up to
        # 32,768 tokens shared between prompt and completion.
        max_completion_tokens=1024,

        # Controls diversity via nucleus sampling: 0.5 means half of all
        # likelihood-weighted options are considered.
        top_p=1,

        # A stop sequence is a predefined or user-specified text string that
        # signals an AI to stop generating content, ensuring its responses
        # remain focused and concise. Examples include punctuation marks and
        # markers like "[end]".
        stop=None,

        # If set, partial message deltas will be sent.
        stream=False,
    )

    # Print the completion returned by the LLM.
    return(chat_completion.choices[0].message.content)