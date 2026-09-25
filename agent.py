# Glow Studio AI Agent - by Jaudat
def ai_agent_reply(msg):
    msg = msg.lower()
    if "price" in msg or "qeemat" in msg:
        return "Zafarani Cream Rs.650 - Free Delivery. Order ke liye ORDER likhen"
    elif "order" in msg:
        return "Daraz Link: [Apna Link Lagao] WhatsApp: 03XX-XXXXXXX"
    else:
        return "Salam! Glow Studio me khush amdeed. Price likhen."

print(ai_agent_reply("price kya hai"))
