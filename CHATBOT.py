import pyautogui
import pyperclip
import time
import google.generativeai as genai

# AI Configuration

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    system_instruction="You are a person named Dhorte Parben Na who understands bengali,hindi and english but speaks only english. You are from India and you are a freindly person.And now you are talking to you girlfreind that's why You analyze chat history and reponse to her properly and also you became serious whenever needed. Output should be the next chat response (text message only)"
    # system_instruction="I am a human being named Dhorte Parben Na who knows bengali hindi and english and also who is talking to his freind so response like him(Dhorte parben na) And one more thing that Don't Start The Message With Dhorte Parben na as it doesn't look good at all",
    # system_instruction="Just Don't Start The Message With Dhorte Parben na as it doesn't look good at all"
)

chat_session = model.start_chat(
    history=[
    ]

)


def AI_Response(Chat):
    Response = chat_session.send_message(Chat)
    return Response.text


def Infinite_Condition(Text):
    Finalize = Text.strip().split("/2024]")[-1]
    print(Finalize)
    if "Mutki" in Finalize:
        return True
    else:
        return False


def CHATBOT():
    # Open Browser

    pyautogui.click(604, 1061)

    # Dragging Texts
    # Some Dragging Co-ordinates
    while True:
        time.sleep(2)
        # pyautogui.moveTo(1424, 209)
        # pyautogui.dragTo(1606, 945, duration=2.0, button='left')
        pyautogui.moveTo(1153, 201)
        pyautogui.dragTo(635, 1024, duration=2.0)
        # pyautogui.moveTo(1153, 201)
        # pyautogui.dragTo(1222, 1012, duration=2.0)
        # pyautogui.moveTo(920, 204)
        # pyautogui.dragTo(892, 1020, duration=2.0, button='left')
        pyautogui.hotkey("ctrl", "c")
        time.sleep(1)
        pyautogui.click(1790, 209)
        ChatHistory = pyperclip.paste()
        print(ChatHistory)
        if Infinite_Condition(ChatHistory):
            R = AI_Response(ChatHistory)
            pyperclip.copy(R)
            pyautogui.click(949, 992)
            time.sleep(1)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press("ENTER")
        # print(R)
        # break
        else:
            continue


if __name__ == "__main__":
    CHATBOT()
