def advice(pain,mood):
    text=[]
    if pain>=7:
        text.append("近期疼痛较明显，建议关注身体状态。")
    else:
        text.append("疼痛记录处于较稳定范围。")
    if mood in ["低落","一般"]:
        text.append("建议保持规律运动和良好睡眠。")
    else:
        text.append("当前情绪状态积极，请继续保持。")
    return "\n\n".join(text)