from transitions.extensions import GraphMachine
from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
    def is_going_to_description(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'help'
        return False

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state1_reply(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'a' or text.lower() == 'b' or text.lower() == 'c' or text.lower() == 'd'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'next'
        return False

    def is_going_to_state2_reply(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'a' or text.lower() == 'b' or text.lower() == 'c' or text.lower() == 'd'
        return False

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'next'
        return False

    def is_going_to_state3_reply(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'a' or text.lower() == 'b' or text.lower() == 'c' or text.lower() == 'd'
        return False

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'next'
        return False

    def is_going_to_state4_reply(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'a' or text.lower() == 'b' or text.lower() == 'c' or text.lower() == 'd'
        return False

    def is_going_to_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'next'
        return False

    def is_going_to_state5_reply(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'a' or text.lower() == 'b' or text.lower() == 'c' or text.lower() == 'd'
        return False

    def is_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def is_going_to_state7(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'a' or text.lower() == 'b' or text.lower() == 'c'
        return False

    def is_going_to_state8(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'a' or text.lower() == 'b'
        return False

    def is_going_to_state9(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'a' or text.lower() == 'b' or text.lower() == 'c'
        return False

    def is_going_to_state10(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'a' or text.lower() == 'b'
        return False

    def is_going_to_state11(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'a' or text.lower() == 'b'
        return False


    def on_enter_description(self, event):
        print("I'm entering description!")

        sender_id = event['sender']['id']
        response = send_text_message(sender_id, "你累了嗎？底下有兩項輕鬆的心理小測驗喔～～")
        response = send_text_message(sender_id, "1.動物愛情心理測驗：每題皆為a/b/c/d四個選項，請選擇其中一個，答完一題可立即看到選項的解釋，輸入next會進行下一題。\n\n2.隱藏悲傷指數測驗：每題的選項為a/b或a/b/c，請選擇其中一個，並記下選項的得分，5題結束後將得分加總對照測驗結果。")
        response = send_text_message(sender_id, "現在請選擇輸入1或2來開始進行測驗吧！")
        self.go_back()

    def on_exit_description(self):
        print('Leaving description')

    def on_enter_state1(self, event):
        print("I'm entering state1!")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "1.假如世界末日來臨，你只能解救一種動物，你會救以下哪一種?\na. 兔\nb. 羊\nc. 鹿\nd. 馬")
        send_text_message(sender_id, "請輸入a/b/c/d其中一個選項")

    def on_exit_state1(self, event):
        print('Leaving state1')

    def on_enter_state1_reply(self, event):
        print("I'm entering state1_reply!")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "你在現實生活中會被哪一類人所吸引：\na. 兔——有分裂的人格，外表像冰而內心熾熱的人。\nb. 羊——重視順從而溫暖的人。\nc. 鹿——優雅及有禮貌的人。\nd. 馬——不受約束嚮往自由的人。")
        send_text_message(sender_id, "請輸入next進行下一題")

    def on_exit_state1_reply(self, event):
        print('Leaving state1_reply')

    def on_enter_state2(self, event):
        print("I'm entering state2!")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "2.在非洲旅行途中，你造訪了一個部落，部落首領堅持讓你選一種動物的頭骨帶回去當紀念品，你會選哪一種?\na. 猴\nb. 獅\nc. 蛇\nd. 長頸鹿")
        send_text_message(sender_id, "請輸入a/b/c/d其中一個選項")

    def on_exit_state2(self, event):
        print('Leaving state2')

    def on_enter_state2_reply(self, event):
        print("I'm entering state2_reply!")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "哪種求愛手段最容易使你覺得情不自禁：\na. 猴——有創造性，從不會讓你感到無趣。\nb. 獅——直來直往，直接地告訴你他愛你。\nc. 蛇——心情搖擺不定，忽冷忽熱，遊移不定。\nd. 長頸鹿——有耐性，對你永遠不放棄。")
        send_text_message(sender_id, "請輸入next進行下一題")

    def on_exit_state2_reply(self, event):
        print('Leaving state2_reply')

    def on_enter_state3(self, event):
        print("I'm entering state3!")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "3.你做錯事了，上天懲罰你變成人以外的動物，你想變成下面哪一種動物?\na. 狗\nb. 貓\nc. 馬\nd. 蛇")
        send_text_message(sender_id, "請輸入a/b/c/d其中一個選項")

    def on_exit_state3(self, event):
        print('Leaving state3')

    def on_enter_state3_reply(self, event):
        print("I'm entering state3_reply!")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "你想給愛人什麼樣的印象：\na. 狗——忠誠忠實，永不改變。\nb. 貓——有個性的。\nc. 馬——樂觀的。\nd. 蛇——可通融的。")
        send_text_message(sender_id, "請輸入next進行下一題")

    def on_exit_state3_reply(self, event):
        print('Leaving state3_reply')

    def on_enter_state4(self, event):
        print("I'm entering state4!")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "4.有一天，你碰上了一種會說人話的動物，你希望那是哪種動物?\na. 羊\nb. 馬\nc. 兔\nd. 鳥")
        send_text_message(sender_id, "請輸入a/b/c/d其中一個選項")

    def on_exit_state4(self, event):
        print('Leaving state4')

    def on_enter_state4_reply(self, event):
        print("I'm entering state4_reply!")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "你想跟你的愛人建立一個什麼樣的關係：\na. 羊——你倆不用多說話，用心溝通，對方自然知道你要什麼。\nb. 馬——你倆能談任何事情，沒有秘密。\nc. 兔——一種讓你一直能夠感受到溫暖與戀愛的關係。\nd. 鳥——你和愛人不只關心現在也關心將來，一種你能與之一起成長的長期關係。")
        send_text_message(sender_id, "請輸入next進行下一題")

    def on_exit_state4_reply(self, event):
        print('Leaving state4_reply')

    def on_enter_state5(self, event):
        print("I'm entering state5!")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "5.假如你有5分鐘的時間可以當一種動物，你會選擇當哪種動物?\na. 獅\nb. 貓\nc. 馬\nd. 鴿子")
        send_text_message(sender_id, "請輸入a/b/c/d其中一個選項")

    def on_exit_state5(self, event):
        print('Leaving state5')

    def on_enter_state5_reply(self, event):
        print("I'm entering state5_reply!")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "此刻你對愛情的看法：\na. 獅——你總是渴望愛情，能為愛情做任何事，但你不會輕易墜入情網。\nb. 貓——你非常以自我為中心，認為愛情對你是可以輕易得到和放棄的東西。\nc. 馬——你不想被固定的關係綁住，你只想處處調情。\nd. 鴿子——你認為愛情是二人互相的承諾。")
        send_text_message(sender_id, "這項測驗到此結束囉～\n\n接下來請輸入help依說明重新開始測驗吧！")
        self.go_back()

    def on_exit_state5_reply(self):
        print('Leaving state5_reply')

    def on_enter_state6(self, event):
        print("I'm entering state6!")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "1.和朋友在一起時，是否也覺得心裡空虛？\na.有過幾次，心情非常低落（2分）\nb.沒有，和朋友在一起很開心（1分）\nc.經常這樣，總是被心事困擾（3分）")
        send_text_message(sender_id, "請輸入a/b/c其中一個選項")


    def on_exit_state6(self, event):
        print('Leaving state6')

    def on_enter_state7(self, event):
        print("I'm entering state7!")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "2.心情不好的時候，你會？\na.快速宣洩悲傷的情緒（1分）\nb.悶在心裡，自己慢慢消化（3分）")
        send_text_message(sender_id, "請輸入a/b其中一個選項")

    def on_exit_state7(self, event):
        print('Leaving state7')

    def on_enter_state8(self, event):
        print("I'm entering state8!")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "3.在K歌的時候，你會嘗試唱不熟的歌嗎？\na.不會（3分）\nb.會（1分）\nc.看情況（2分）")
        send_text_message(sender_id, "請輸入a/b/c其中一個選項")

    def on_exit_state8(self, event):
        print('Leaving state8')

    def on_enter_state9(self, event):
        print("I'm entering state9!")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "4.假如，你能看到自己結婚那天或死亡那天，你會選？\na.結婚那天（1分）\nb.死亡那天（3分)")
        send_text_message(sender_id, "請輸入a/b其中一個選項")

    def on_exit_state9(self, event):
        print('Leaving state9')

    def on_enter_state10(self, event):
        print("I'm entering state10!")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "5.如果你被外星人抓走了，你會選擇死亡還是成為實驗體從而變強大？\na.選擇死亡（3分）\nb.成為實驗體（1分）")
        send_text_message(sender_id, "請輸入a/b其中一個選項")

    def on_exit_state10(self, event):
        print('Leaving state10')

    def on_enter_state11(self, event):
        print("I'm entering state11!")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "測驗結束，請把你的得分對照下面的結果喔～")
        send_text_message(sender_id, "5~8分：隱藏悲傷指數15%\n你人緣很好，就像是朋友中的開心果，有你在的地方總是充斥著歡樂。平時你樂觀、積極，很少會想到陰暗的一面，即使接近表里如一的你也難免在某些時候難以排解的情緒。")
        send_text_message(sender_id, "9~12分：隱藏悲傷指數40%\n你的個性比較開朗，也願與朋友嬉戲打鬧，所以這時候的你是歡樂的。只是一個人的時候或者在夜深人靜的時候，你內心會產生一種說不出的感覺，整個人提不起精神，內心憋著一口氣讓人感覺很難受。")
        send_text_message(sender_id, "13分以上：隱藏悲傷指數70%\n早已不是肆無忌憚的年紀，現在的你學會將心事埋在心底，並將痛苦自己消化、將憂傷掩藏；就算有時候情不自禁的消極、負能量爆棚，你都能將情緒收拾的很好。")
        send_text_message(sender_id, "還意猶未盡嗎？接下來請輸入help依說明重新開始測驗吧！")
        self.go_back()

    def on_exit_state11(self):
        print('Leaving state11')
