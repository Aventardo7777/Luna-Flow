import pandas as pd
import plotly.express as px

def cycle_chart():
    data=pd.DataFrame({
        "周期":["1月","2月","3月","4月","5月"],
        "天数":[30,28,29,31,27]
    })
    return px.line(data,x="周期",y="天数",markers=True,
    title="历史周期变化趋势")